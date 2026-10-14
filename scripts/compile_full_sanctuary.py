#!/usr/bin/env python3
"""
Compiler script to inject Step 2 into hexaquest_cozy_pixel_language_sanctuary.html
"""

import json
from step2_waray import WARAY_STEP2
from step2_french_latin import FRENCH_STEP2, LATIN_STEP2
from step2_hebrew_chinese_german import HEBREW_STEP2, CHINESE_STEP2, GERMAN_STEP2

STEP2_DICT = {
    "waray": WARAY_STEP2,
    "french": FRENCH_STEP2,
    "latin": LATIN_STEP2,
    "hebrew": HEBREW_STEP2,
    "chinese": CHINESE_STEP2,
    "german": GERMAN_STEP2
}

def main():
    print("Step 2 data loaded for all 6 languages.")
    with open("scripts/step2_data.json", "w", encoding="utf-8") as f:
        json.dump(STEP2_DICT, f, ensure_ascii=False, indent=2)
    print("Saved to scripts/step2_data.json")

if __name__ == "__main__":
    main()

