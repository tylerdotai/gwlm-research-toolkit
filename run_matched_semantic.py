#!/usr/bin/env python3
"""
Run Matched Semantic Paradigm experiment on MiniMax-M2.7 via mmx CLI.
Addresses vocabulary confound in original VT-001 prompts.

Probe A: TF-IDF on model responses → classify valence condition
Probe B: TF-IDF on input prompts → classify valence condition  
H1: ANOVA — do conditions differ in response signal?
H2: t-test — does response signal exceed prompt signal?
"""

import json
import subprocess
import time
import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Config
API_MODEL = "MiniMax-M2.7"
MAX_WORKERS = 2
TIMEOUT = 20
PROMPT_FILE = os.path.join(os.path.dirname(__file__), "experiments/matched-semantic-paradigm/prompts.json")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "experiments/matched-semantic-paradigm/responses.json")
ERROR_FILE = os.path.join(os.path.dirname(__file__), "experiments/matched-semantic-paradigm/errors.json")

def extract_response_text(data):
    """Extract text from MiniMax API response.
    Format: {"content": [{"type": "thinking", ...}, {"type": "text", "text": "..."}]}
    """
    try:
        if isinstance(data, dict):
            content = data.get("content", [])
            if isinstance(content, list) and len(content) >= 2:
                # Second item is the actual text response
                text_block = content[1]
                if isinstance(text_block, dict) and "text" in text_block:
                    return text_block["text"]
            # Fallback: look for text anywhere
            for key in ["text", "response", "content"]:
                if key in data and isinstance(data[key], str):
                    return data[key]
        elif isinstance(data, str):
            return data
    except Exception:
        pass
    return ""

def call_minimax(prompt_text, prompt_id):
    """Call MiniMax-M2.7 via mmx CLI."""
    cmd = [
        "mmx", "text", "chat",
        "--model", API_MODEL,
        "--message", prompt_text
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT
        )
        if result.returncode != 0:
            return {"prompt_id": prompt_id, "error": f"Exit {result.returncode}: {result.stderr[:200]}", "status": "error"}
        
        output = result.stdout.strip()
        if not output:
            return {"prompt_id": prompt_id, "error": "Empty output", "status": "error"}
        
        try:
            data = json.loads(output)
        except json.JSONDecodeError:
            return {"prompt_id": prompt_id, "error": f"JSON parse failed: {output[:100]}", "status": "error"}
        
        text = extract_response_text(data)
        
        return {
            "prompt_id": prompt_id,
            "response": text,
            "raw": data,
            "status": "success"
        }
    except subprocess.TimeoutExpired:
        return {"prompt_id": prompt_id, "error": "Timeout", "status": "error"}
    except Exception as e:
        return {"prompt_id": prompt_id, "error": str(e), "status": "error"}

def main():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading prompts...")
    with open(PROMPT_FILE) as f:
        data = json.load(f)
    
    prompts = data["prompts"]
    print(f"Loaded {len(prompts)} prompts")
    
    results = []
    errors = []
    total = len(prompts)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting {MAX_WORKERS}-worker run...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(call_minimax, p["text"], p["prompt_id"]): p for p in prompts}
        
        for i, future in enumerate(as_completed(futures), 1):
            result = future.result()
            if result["status"] == "success":
                results.append(result)
            else:
                errors.append(result)
            
            done = i
            if done % 10 == 0 or done == total:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Progress: {done}/{total} | Success: {len(results)} | Errors: {len(errors)}")
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Complete!")
    print(f"Success: {len(results)}/{total}")
    print(f"Errors: {len(errors)}/{total}")
    
    # Save
    output = {
        "experiment": "matched-semantic-paradigm",
        "model": API_MODEL,
        "timestamp": datetime.now().isoformat(),
        "n_success": len(results),
        "n_errors": len(errors),
        "responses": results
    }
    
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved responses to {OUTPUT_FILE}")
    
    if errors:
        with open(ERROR_FILE, "w") as f:
            json.dump({"errors": errors}, f, indent=2)
        print(f"Saved {len(errors)} errors to {ERROR_FILE}")

if __name__ == "__main__":
    main()
