#!/usr/bin/env python3
"""
Inject Step 2 data and functionality into hexaquest_cozy_pixel_language_sanctuary.html
"""
import json
import re

with open("scripts/step2_data.json", "r", encoding="utf-8") as f:
    step2_data = json.load(f)

with open("hexaquest_cozy_pixel_language_sanctuary.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the header to add the Step Switcher group
step_switcher_html = '''        <!-- Step 1 & Step 2 Journey Switcher Group -->
        <div class="flex items-center gap-1.5 bg-[var(--bg-deep)] p-1 rounded border-2 border-[var(--border-pixel)]" id="stepSelectorGroup">
          <button onclick="switchStep(1)" id="stepBtn-1" class="pixel-btn px-2.5 py-1 text-xs pixel-btn-amber" title="Step 1: Alphabets, Runes & Numbers 0–10">
            <span>◈ Step 1: 0–10</span>
          </button>
          <button onclick="switchStep(2)" id="stepBtn-2" class="pixel-btn px-2.5 py-1 text-xs" title="Step 2: Dates, Months & Numbers 11–31">
            <span>📅 Step 2: Dates</span>
          </button>
        </div>
'''

if 'id="stepSelectorGroup"' not in html:
    # Insert right before Level & XP Bar
    target = '<!-- Cozy Player Level, XP Bar & Badges -->'
    html = html.replace(target, step_switcher_html + '\n        ' + target)

# Update seal badge title & text in header
html = html.replace('title="Step 1 Sanctuary Seals Earned">0/6 SEALS</span>', 'title="Sanctuary Seals Earned Across Steps 1 & 2" id="hudBadges">0/12 SEALS</span>')

# Update realm banner to include stepContextBadge
if 'id="stepContextBadge"' not in html:
    old_audio_badge = '<span id="audioSourceBadge"'
    new_audio_badge = '<span id="stepContextBadge" class="px-2 py-0.5 rounded bg-[var(--bg-deep)] border border-[var(--accent-amber)] text-[10px] text-[var(--accent-amber)] font-pixel-ui">STEP 1: 0–10</span>\n        <span id="audioSourceBadge"'
    html = html.replace(old_audio_badge, new_audio_badge)

# Replace the static tabs with dynamic arenaTabsContainer
tabs_old_pattern = re.compile(r'<!-- 5-Tab Pedagogical Practice Arena Navigation -->\s*<div class="w-full grid grid-cols-5 gap-1.5 sm:gap-2 mb-5" role="tablist">.*?</div>', re.DOTALL)
tabs_new = '<!-- 5-Tab Pedagogical Practice Arena Navigation (Dynamic per Step) -->\n    <div class="w-full grid grid-cols-5 gap-1.5 sm:gap-2 mb-5" role="tablist" id="arenaTabsContainer"></div>'
html = tabs_old_pattern.sub(tabs_new, html)

# In Chronology steps, update step 2 status to ACTIVE ARENA
html = html.replace('"STEP 2 BLUEPRINT"', '"ACTIVE ARENA"')

# Inject Step 2 JSON dictionary at beginning of script
step2_json_str = json.dumps(step2_data, ensure_ascii=False)
injection_marker = 'const LANGUAGES = {'
replacement_marker = f'const STEP2_DATA = {step2_json_str};\n\n    const LANGUAGES = {{'
html = html.replace(injection_marker, replacement_marker)

# After LANGUAGES dictionary definition, loop and assign step2
attach_code = '''
    // Attach Step 2 datasets to each language realm
    Object.keys(STEP2_DATA).forEach(langId => {
      if (LANGUAGES[langId]) {
        LANGUAGES[langId].step2 = STEP2_DATA[langId];
      }
    });
'''
state_marker = 'const state = {'
html = html.replace(state_marker, attach_code + '\n    ' + state_marker)

# Update state object
old_state = '''    const state = {
      currentLang: "waray",
      activeTab: "cards", // 'cards' | 'ear_gym' | 'market' | 'scribe' | 'guardian'
      cardFilter: "all",  // 'all' | 'rune' | 'number'
      cardIndex: 0,
      whisperOpen: false,
      keepWhisperPinned: false,

      // Ear Gym state
      earIndex: 0,
      earSelected: null,

      // Market state
      marketIndex: 0,
      marketUserCount: 0,
      marketCompleted: false,

      // Scribe state
      scribeIndex: 0,
      scribeBuffer: [],
      scribeSuccess: false,

      // Owl Guardian exam state
      quizIndex: 0,
      quizSelected: null,
      quizCompletedByLang: {},'''

new_state = '''    const state = {
      currentStep: 1,     // 1: Runes & 0–10 | 2: Dates & Months 11–31
      currentLang: "waray",
      activeTab: "cards", // 'cards' | 'ear_gym' | 'market' | 'sundial' | 'scribe' | 'guardian'
      cardFilter: "all",  // 'all' | 'rune' | 'number' | 'month' | 'date_num'
      cardIndex: 0,
      whisperOpen: false,
      keepWhisperPinned: false,

      // Ear Gym state
      earIndex: 0,
      earSelected: null,

      // Market state (Step 1)
      marketIndex: 0,
      marketUserCount: 0,
      marketCompleted: false,

      // Sundial state (Step 2)
      sundialIndex: 0,
      sundialMonthIdx: 0,
      sundialDay: 1,
      sundialCompleted: false,

      // Scribe state
      scribeIndex: 0,
      scribeBuffer: [],
      scribeSuccess: false,

      // Owl Guardian exam state
      quizIndex: 0,
      quizSelected: null,
      quizCompletedByLang: {},'''

html = html.replace(old_state, new_state)

with open("hexaquest_cozy_pixel_language_sanctuary.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Injected step2 data, state, and HTML markup successfully!")

