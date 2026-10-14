#!/usr/bin/env python3
"""
Generate the complete HTML app incorporating Step 1 and Step 2
"""
import json

with open("scripts/step2_data.json", "r", encoding="utf-8") as f:
    step2_data = json.load(f)

# Read the current html file
with open("hexaquest_cozy_pixel_language_sanctuary.html", "r", encoding="utf-8") as f:
    content = f.read()

# Verify json is valid and readable
print(f"Step 2 data loaded with keys: {list(step2_data.keys())}")

