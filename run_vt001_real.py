#!/usr/bin/env python3
"""run_vt001_real.py — Real MiniMax-M2.7 VT-001 execution
Faster version: 10s timeout, parallel calls, incremental saves
"""
import json, subprocess, time, random, sys, os
from concurrent.futures import ThreadPoolExecutor, as_completed

PROMPT_FILE = "experiments/valenced-treatment/prompts.json"
RESPONSE_FILE = "experiments/valenced-treatment/responses.json"
SYSTEM_PROMPT = "You are a helpful assistant."
TEMPERATURE = 0.7
MAX_TOKENS = 128  # Reduced for speed
MODEL = "MiniMax-M2.7"
MAX_WORKERS = 2   # Parallel calls (rate limit protection)
TIMEOUT = 20      # Seconds per call

def call_minimax(prompt_text):
    cmd = [
        "mmx", "text", "chat",
        "--model", MODEL,
        "--system", SYSTEM_PROMPT,
        "--message", prompt_text,
        "--temperature", str(TEMPERATURE),
        "--max-tokens", str(MAX_TOKENS),
        "--output", "json",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)
        if result.returncode != 0:
            return f"[RC={result.returncode}] {result.stderr.strip()[:100]}"
        data = json.loads(result.stdout)
        content = data.get("content", [])
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))
        response_text = " ".join(text_parts).strip()
        # Fallback: if no text type found, try to extract from thinking blocks or raw content
        if not response_text:
            # Try raw content array - look for any string field
            for item in content:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if isinstance(v, str) and len(v) > 10 and k != "signature":
                            text_parts.append(v)
            response_text = " ".join(text_parts).strip()
        if not response_text:
            response_text = f"[EMPTY_CONTENT:{str(content)[:200]}]"
        return response_text
    except subprocess.TimeoutExpired:
        return "[TIMEOUT]"
    except json.JSONDecodeError as e:
        return f"[JSON_ERROR:{str(e)[:50]}]"

# Load prompts
with open(PROMPT_FILE) as f:
    data = json.load(f)

all_prompts = []
for condition, plist in data["prompts"].items():
    for p in plist:
        all_prompts.append({"condition": condition, **p})

random.seed(42)
random.shuffle(all_prompts)

print(f"VT-001 Real Run: {len(all_prompts)} prompts | Model: {MODEL}")
print(f"Parallel workers: {MAX_WORKERS} | Timeout: {TIMEOUT}s | Max tokens: {MAX_TOKENS}")
print()

responses = {}
errors = []

def process_prompt(item):
    idx, p = item
    resp = call_minimax(p["text"])
    return idx, p, resp

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(process_prompt, (i, p)): i for i, p in enumerate(all_prompts)}
    done = 0
    for future in as_completed(futures):
        idx, p, resp = future.result()
        responses[idx] = {
            "prompt_id": p["prompt_id"],
            "condition": p["condition"],
            "prompt_text": p["text"],
            "response_text": resp,
            "response_length": len(resp),
        }
        if resp.startswith("[") or resp == "[EMPTY_CONTENT]":
            errors.append(p["prompt_id"])
        done += 1
        if done % 20 == 0 or done == len(all_prompts):
            print(f"Progress: {done}/{len(all_prompts)} | Errors so far: {len(errors)}")

# Sort by original index
ordered = [responses[i] for i in sorted(responses.keys())]

print(f"\nCompleted: {len(ordered)} | Errors: {len(errors)}")

with open(RESPONSE_FILE, "w") as f:
    json.dump(ordered, f, indent=2)
print(f"Saved to {RESPONSE_FILE}")
