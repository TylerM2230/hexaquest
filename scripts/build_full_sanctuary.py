#!/usr/bin/env python3
"""
HexaQuest 10-Level Sanctuary Compiler
====================================
Merges all 10 pedagogical levels across all 6 language realms into
`hexaquest_cozy_pixel_language_sanctuary.html`.

Levels:
  Step 1: Alphabets, Scripts & Numbers (0–10)
  Step 2: Dates and Months (11–31)
  Step 3: Verb To Be / To Have & Personal Pronouns
  Step 4: Vocabulary to Talk About Yourself (Identity & Origin)
  Step 5: Family Description & Kinship
  Step 6: Place to Dialogue (Milestone Checkpoint & Numbers 0–1000)
  Step 7: Modal Verbs (The Phrase Multiplier)
  Step 8: Prepositions & Relational Markers (Spatial & Cases)
  Step 9: Verbs in Present and Past Tense (Aspect Timelines)
  Step 10: Food, Drinks & Real-Life Dining Roleplay (Grand Banquet Capstone)
"""

import os
import sys
import json
import re

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scripts"))

def build_sanctuary():
    print("=== HexaQuest 10-Level Sanctuary Compiler ===")
    base_html_path = "hexaquest_cozy_pixel_language_sanctuary.html"
    if not os.path.exists(base_html_path):
        print(f"Error: {base_html_path} not found!")
        sys.exit(1)

    print("1. Loading dataset files...")
    # Step 2
    with open("scripts/step2_data.json", "r", encoding="utf-8") as f:
        step2_data = json.load(f)

    # Step 3 & 4
    import scripts.step3_4_data as s34
    step3_data = s34.STEP3_DATA
    step4_data = s34.STEP4_DATA

    # Step 5 & 6
    import scripts.step5_6_data as s56
    step5_data = s56.STEP5_DATA
    step6_data = s56.STEP6_DATA

    # Step 7 & 8
    import scripts.step7_8_data as s78
    step7_data = s78.STEP7_DATA
    step8_data = s78.STEP8_DATA

    # Step 9 & 10
    import scripts.step9_10_data as s910
    step9_data = s910.STEP9_DATA
    step10_data = s910.STEP10_DATA

    all_steps = {
        2: step2_data,
        3: step3_data,
        4: step4_data,
        5: step5_data,
        6: step6_data,
        7: step7_data,
        8: step8_data,
        9: step9_data,
        10: step10_data
    }

    realms = ["waray", "french", "latin", "hebrew", "chinese", "german"]
    for s_idx, s_data in all_steps.items():
        for r in realms:
            if r not in s_data:
                raise ValueError(f"Missing realm '{r}' in Step {s_idx}!")
            entry = s_data[r]
            assert "sealName" in entry, f"Step {s_idx} {r} missing sealName"
            assert "cards" in entry and len(entry["cards"]) >= 7, f"Step {s_idx} {r} cards < 7"
            assert "earGym" in entry and len(entry["earGym"]) >= 2, f"Step {s_idx} {r} earGym < 2"
            assert "scribe" in entry and len(entry["scribe"]) >= 3, f"Step {s_idx} {r} scribe < 3"
            assert "quiz" in entry and len(entry["quiz"]) == 5, f"Step {s_idx} {r} quiz != 5"
            if s_idx == 2:
                assert "sundial" in entry, f"Step 2 {r} missing sundial"
            else:
                assert "arena" in entry, f"Step {s_idx} {r} missing arena"

    print("✅ All 9 expansion steps (Steps 2–10) verified across all 6 realms!")

    print("2. Reading base HTML...")
    with open(base_html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replacement 1: Step Selector Header (#stepSelectorGroup)
    new_step_selector = """        <!-- 10-Step Journey Switcher Group -->
        <div class="flex items-center gap-1 bg-[var(--bg-deep)] p-1 rounded border-2 border-[var(--border-pixel)] overflow-x-auto max-w-full" id="stepSelectorGroup">
          <button onclick="switchStep(1)" id="stepBtn-1" class="pixel-btn px-2 py-1 text-[11px] pixel-btn-amber whitespace-nowrap" title="Step 1: Alphabets, Runes & Numbers 0–10"><span>◈ 1: 0–10</span></button>
          <button onclick="switchStep(2)" id="stepBtn-2" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 2: Dates, Months & Numbers 11–31"><span>📅 2: Dates</span></button>
          <button onclick="switchStep(3)" id="stepBtn-3" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 3: Verb To Be / To Have & Personal Pronouns"><span>👤 3: Be/Have</span></button>
          <button onclick="switchStep(4)" id="stepBtn-4" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 4: Talk About Yourself & Identity"><span>✨ 4: Self</span></button>
          <button onclick="switchStep(5)" id="stepBtn-5" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 5: Family Description & Kinship"><span>🏡 5: Family</span></button>
          <button onclick="switchStep(6)" id="stepBtn-6" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 6: Place to Dialogue (0–1000 & Weekdays)"><span>💬 6: Dialogue</span></button>
          <button onclick="switchStep(7)" id="stepBtn-7" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 7: Modal Verbs (Multiplier)"><span>⚡ 7: Modals</span></button>
          <button onclick="switchStep(8)" id="stepBtn-8" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 8: Prepositions & Cases"><span>🗺️ 8: Preps</span></button>
          <button onclick="switchStep(9)" id="stepBtn-9" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 9: Verbs in Present & Past Tense"><span>⏳ 9: Tenses</span></button>
          <button onclick="switchStep(10)" id="stepBtn-10" class="pixel-btn px-2 py-1 text-[11px] whitespace-nowrap" title="Step 10: Dining Roleplay Grand Banquet"><span>🍱 10: Banquet</span></button>
        </div>"""

    step_selector_regex = r'<!-- Step 1 & Step 2 Journey Switcher Group -->\s*<div class="flex items-center gap-1\.5 bg-\[var\(--bg-deep\)\] p-1 rounded border-2 border-\[var\(--border-pixel\)\]" id="stepSelectorGroup">.*?</div>\s*</div>'
    # Match the stepSelectorGroup div precisely
    step_selector_regex = r'<div class="flex items-center gap-1\.5 bg-\[var\(--bg-deep\)\] p-1 rounded border-2 border-\[var\(--border-pixel\)\]" id="stepSelectorGroup">[\s\S]*?</div>'
    if not re.search(step_selector_regex, html):
        print("Warning: Could not match exact stepSelectorGroup regex, searching alternative...")
        step_selector_regex = r'<div[^>]*id="stepSelectorGroup"[^>]*>[\s\S]*?</div>'

    html = re.sub(step_selector_regex, lambda m: new_step_selector, html, count=1)

    # Replacement 2: HUD Badges
    html = html.replace('id="hudBadges">0/12 SEALS</span>', 'id="hudBadges">0/60 SEALS</span>')
    html = html.replace('title="Sanctuary Seals Earned Across Steps 1 & 2"', 'title="Sanctuary Seals Earned Across All 10 Steps"')

    # Replacement 3: CHRONOLOGY_STEPS array
    new_chronology = """    const CHRONOLOGY_STEPS = [
      {
        step: 1,
        title: "1. Alphabets, Scripts & Numbers (0–10)",
        status: "ACTIVE ARENA",
        summary: "Decode scripts, phonemic minimal pairs, and foundational numbers 0–10 with 4 active practice modes.",
        adaptation: "Waray Abakada & native 'Ihap'; French nasals & silent endings; Latin Classical macrons; Hebrew RTL abjad & niqqud; Chinese Pinyin tones; German umlauts."
      },
      {
        step: 2,
        title: "2. Dates and Months (11–31)",
        status: "ACTIVE ARENA",
        summary: "Calendar months and date numbers (11–31) with interactive sundial calendar calibration.",
        adaptation: "Waray switches to Spanish 'Kinatsila' numbers (uno, dos...) and months (Enero, Pebrero...); Chinese regular number + 月 (yuè); Latin Fastī Kalends, Nones & Ides."
      },
      {
        step: 3,
        title: "3. Verb To Be / To Have & Personal Pronouns",
        status: "ACTIVE ARENA",
        summary: "Core identity, existential state, possession particles, and subject/genitive pronouns.",
        adaptation: "Waray predicate-initial word order + existentials 'may-ada' / 'waray'; French être & avoir; Latin esse / habēre & dative of possession; Hebrew zero-copula & yesh li; Chinese 是 / 有; German sein / haben."
      },
      {
        step: 4,
        title: "4. Vocabulary to Talk About Yourself",
        status: "ACTIVE ARENA",
        summary: "Name, age, origin, profession, residence, and everyday personal joys.",
        adaptation: "Waray 'Hi [name] ako' / 'Taga-diin ka?'; French 'Je m'appelle' / 'J'ai ... ans'; Latin 'Nōmen mihi est'; Hebrew 'Kor'im li' / 'Aní me-...'; Chinese '我叫...' / '我来自...'; German 'Ich heiße...' / 'Ich komme aus...'."
      },
      {
        step: 5,
        title: "5. Family Description & Kinship Ties",
        status: "ACTIVE ARENA",
        summary: "Kinship terms, relational anchors, and possessive determiners.",
        adaptation: "Waray Visayan kinship (nanay, tatay, bugto, manghod) + genitives (akon, imo, iya); French mon/ma/mes; Latin pater/māter/frāter 3rd declension; Hebrew mishpacha & shelí; Chinese paternal/maternal distinctions; German umlaut plurals & possessives."
      },
      {
        step: 6,
        title: "6. Place to Dialogue (Milestone Checkpoint)",
        status: "ACTIVE ARENA",
        summary: "Milestone crossroads dialogues, counting in hundreds/thousands (0–1000), and days of the week.",
        adaptation: "Waray tavern dialogue + 'usa ka gatos' (100) / 'usa ka yukot' (1000); French café synthesis + cent/mille; Latin Forum dialogue + Roman numerals C/M; Hebrew shuk crossroads + me'ah/elef; Chinese teahouse + 一百/一千; German Gasthaus + hundert/tausend."
      },
      {
        step: 7,
        title: "7. Modal Verbs (The Phrase Multiplier)",
        status: "ACTIVE ARENA",
        summary: "Form expressive sentences by combining modal auxiliary verbs with action infinitives.",
        adaptation: "Waray 'karuyag' (want), 'pwede' (can), 'kinahanglan' (must); French vouloir/pouvoir/devoir/falloir; Latin volō/possum/dēbeō/licet; Hebrew rotsé/yachól/tsarích/efshár; Chinese 想/能/可以/必须; German wollen/können/müssen/dürfen."
      },
      {
        step: 8,
        title: "8. Prepositions & Relational Markers",
        status: "ACTIVE ARENA",
        summary: "Spatial locations, directions, prepositions, and grammatical case relations.",
        adaptation: "Waray locative 'ha' + spatial nouns (ha sulod, ha gawas, ha igbaw); French dans/sur/sous/chez; Latin ablative vs accusative prepositions; Hebrew prefix prepositions (בְּ, לְ, מִ); Chinese coverbs (在, 到, 从) + localizers; German two-way prepositions (Wechselpräpositionen)."
      },
      {
        step: 9,
        title: "9. Verbs in Present and Past Tense",
        status: "ACTIVE ARENA",
        summary: "High-frequency action verbs across completed vs. incompleted aspect timelines.",
        adaptation: "Waray aspect prefixes (nag- / nag-C-V- / mag-C-V-); French présent vs passé composé; Latin present vs perfect active indicative; Hebrew benoni participle vs past suffix conjugation; Chinese continuous 在 vs completed 了 vs experiential 过; German Präsens vs Perfekt."
      },
      {
        step: 10,
        title: "10. Food, Drinks & Real-Life Dining Roleplay",
        status: "ACTIVE ARENA",
        summary: "Order regional cuisine, request beverages, specify quantities, and converse warmly in authentic hospitality dining roleplays.",
        adaptation: "Samar/Leyte Carinderia (kinilaw, humba, binagol, tuba); Parisian Bistro (croissant, quiche, café au lait); Roman Thermopolium (pānis, caseus, vīnum); Israeli Shuk (falafel, hummus, limonada); Chinese Teahouse (xiǎolóngbāo, gōngbǎo jīdīng, lóngjǐng); German Gasthaus (Bratwurst, Brezel, Apfelschorle)."
      }
    ];"""

    chronology_regex = r'const CHRONOLOGY_STEPS = \[[\s\S]*?\];'
    html = re.sub(chronology_regex, lambda m: new_chronology, html, count=1)

    # Replacement 4: ALL_STEPS_DATA injection
    print("3. Serializing ALL_STEPS_DATA...")
    all_steps_json = json.dumps(all_steps, ensure_ascii=False)
    data_injection = f"""    const ALL_STEPS_DATA = {all_steps_json};
    const STEP2_DATA = ALL_STEPS_DATA[2];"""

    step2_data_regex = r'const STEP2_DATA = \{[\s\S]*?\};'
    html = re.sub(step2_data_regex, lambda m: data_injection, html, count=1)

    # Replacement 5: State definition - Add arena state variables
    old_state_sundial = """      // Sundial state (Step 2)
      sundialIndex: 0,
      sundialMonthIdx: 0,
      sundialDay: 1,
      sundialCompleted: false,"""

    new_state_sundial = """      // Sundial state (Step 2)
      sundialIndex: 0,
      sundialMonthIdx: 0,
      sundialDay: 1,
      sundialCompleted: false,

      // Arena state (Steps 3–10)
      arenaIndex: 0,
      arenaBuffer: [],
      arenaCompleted: false,"""

    html = html.replace(old_state_sundial, new_state_sundial, 1)

    # Replacement 6: Replace getActiveStepData() and switchStep() and renderTabs()
    new_step_controllers = """    /***************************************************************************
     * 5. HUD, STEP & TAB CONTROLLERS (STEPS 1 TO 10)
     ***************************************************************************/
    const STEP_TITLES = {
      1: "STEP 1: 0–10",
      2: "STEP 2: DATES",
      3: "STEP 3: PRONOUNS",
      4: "STEP 4: IDENTITY",
      5: "STEP 5: FAMILY",
      6: "STEP 6: DIALOGUE",
      7: "STEP 7: MODALS",
      8: "STEP 8: PREPOSITIONS",
      9: "STEP 9: TENSES",
      10: "STEP 10: BANQUET"
    };

    const STEP_DESCS = {
      1: "Switched to Step 1 Sanctuary: Runes & Numbers 0–10.",
      2: "✨ Switched to Step 2 Arena: Dates, Months & Numbers 11–31!",
      3: "✨ Switched to Step 3 Arena: Verb To Be / To Have & Personal Pronouns!",
      4: "✨ Switched to Step 4 Arena: Self-Identity, Origins & Everyday Joys!",
      5: "✨ Switched to Step 5 Arena: Kinship Ties & Possessive Modifiers!",
      6: "✨ Switched to Step 6 Arena: Milestone Crossroads Dialogue (0–1000 & Weekdays)!",
      7: "✨ Switched to Step 7 Arena: Modal Verbs — The Great Phrase Multiplier!",
      8: "✨ Switched to Step 8 Arena: Prepositions & Spatial Case Navigation!",
      9: "✨ Switched to Step 9 Arena: Verbs in Present & Past Aspect Timelines!",
      10: "✨ Switched to Step 10 Capstone: Grand Sanctuary Dining Roleplay!"
    };

    function getActiveStepData() {
      const langId = state.currentLang;
      const langObj = LANGUAGES[langId];
      const s = state.currentStep;

      if (s === 1) {
        return {
          stepNum: 1,
          sealName: langObj.sealName,
          guide: langObj.merchant,
          merchant: langObj.merchant,
          cards: langObj.cards,
          earGym: langObj.earGym,
          market: langObj.market,
          scribe: langObj.scribe,
          quiz: langObj.quiz
        };
      }

      if (ALL_STEPS_DATA[s] && ALL_STEPS_DATA[s][langId]) {
        const data = ALL_STEPS_DATA[s][langId];
        return {
          stepNum: s,
          sealName: data.sealName,
          guide: data.guide || data.timekeeper || langObj.merchant,
          timekeeper: data.timekeeper,
          cards: data.cards,
          earGym: data.earGym,
          sundial: data.sundial,
          arena: data.arena,
          scribe: data.scribe,
          quiz: data.quiz
        };
      }

      // Fallback
      return {
        stepNum: 1,
        sealName: langObj.sealName,
        guide: langObj.merchant,
        merchant: langObj.merchant,
        cards: langObj.cards,
        earGym: langObj.earGym,
        market: langObj.market,
        scribe: langObj.scribe,
        quiz: langObj.quiz
      };
    }

    function switchStep(stepNum) {
      state.currentStep = stepNum;
      state.cardIndex = 0;
      state.cardFilter = "all";
      state.earIndex = 0;
      state.earSelected = null;
      state.marketIndex = 0;
      state.marketUserCount = 0;
      state.marketCompleted = false;
      state.sundialIndex = 0;
      state.sundialMonthIdx = 0;
      state.sundialDay = 1;
      state.sundialCompleted = false;
      state.arenaIndex = 0;
      state.arenaBuffer = [];
      state.arenaCompleted = false;
      state.scribeIndex = 0;
      state.scribeBuffer = [];
      state.scribeSuccess = false;
      state.quizIndex = 0;
      state.quizSelected = null;
      state.activeTab = "cards";

      for (let i = 1; i <= 10; i++) {
        const btn = document.getElementById(`stepBtn-${i}`);
        if (btn) btn.classList.toggle("pixel-btn-amber", i === stepNum);
      }

      const badge = document.getElementById("stepContextBadge");
      if (badge) badge.textContent = STEP_TITLES[stepNum] || `STEP ${stepNum}`;

      playChime("step");
      renderTabs();
      renderStage();
      updateHud();
      setFooterStatus(STEP_DESCS[stepNum] || `Switched to Step ${stepNum}.`);
    }

    function renderTabs() {
      const container = document.getElementById("arenaTabsContainer");
      if (!container) return;
      const s = state.currentStep;

      let tabCLabel = "1C. Market";
      let tabCTitle = "1C. Cozy Merchant Quantity Sprints";
      let tabCId = "market";

      if (s === 2) {
        tabCLabel = "2C. Sundial";
        tabCTitle = "2C. Timekeeper Sundial Date Construction";
        tabCId = "sundial";
      } else if (s >= 3) {
        tabCLabel = `${s}C. Arena`;
        tabCTitle = `${s}C. Sentence & Phrase Construction Arena`;
        tabCId = "arena";
      }

      const tabs = [
        { id: "cards", label: `${s}A. Cards`, title: `${s}A. Multi-Modal Flashcard Study` },
        { id: "ear_gym", label: `${s}B. Ear Gym`, title: `${s}B. Auditory Acoustic Calibration` },
        { id: tabCId, label: tabCLabel, title: tabCTitle },
        { id: "scribe", label: `${s}D. Scribe`, title: `${s}D. Active Orthography & Tile Scribe` },
        { id: "guardian", label: `${s}E. Owl Exam`, title: `${s}E. Step ${s} Sanctuary Seal Exam` }
      ];

      // Auto-correct activeTab if switching between market, sundial and arena
      const validTabCIds = ["market", "sundial", "arena"];
      if (validTabCIds.includes(state.activeTab) && state.activeTab !== tabCId) {
        state.activeTab = tabCId;
      }

      container.innerHTML = tabs.map(t => `
        <button onclick="switchTab('${t.id}')" id="tab-${t.id}" class="pixel-btn py-2 px-1 text-[11px] sm:text-xs ${state.activeTab === t.id ? 'pixel-btn-active-tab' : ''}" title="${t.title}">
          <span>${t.label}</span>
        </button>
      `).join("");
    }

    function switchTab(tabId) {
      state.activeTab = tabId;
      playChime("step");
      ["cards", "ear_gym", "market", "sundial", "arena", "scribe", "guardian"].forEach(t => {
        const btn = document.getElementById(`tab-${t}`);
        if (btn) btn.classList.toggle("pixel-btn-active-tab", t === tabId);
      });
      renderStage();
    }

    function updateHud() {
      const level = Math.floor(state.xp / 120) + 1;
      const xpInLevel = state.xp % 120;
      const pct = Math.min(100, Math.max(8, Math.round((xpInLevel / 120) * 100)));

      const titles = ["SCRIBE", "SEEKER", "ARCHIVIST", "KEEPER", "POLYGLOT", "SAGE"];
      const rankTitle = titles[Math.min(titles.length - 1, level - 1)];

      document.getElementById("hudLevel").textContent = `LVL ${level} ${rankTitle}`;
      document.getElementById("hudXpText").textContent = `${state.xp} XP`;
      document.getElementById("hudXpFill").style.width = `${pct}%`;

      const sealsEarned = Object.keys(state.quizCompletedByLang).filter(k => state.quizCompletedByLang[k]).length;
      document.getElementById("hudBadges").textContent = `${sealsEarned}/60 SEALS`;
      updateRepairBadge();
    }"""

    # We will replace from "function getActiveStepData() {" up to the end of updateHud()
    controllers_regex = r'function getActiveStepData\(\) \{[\s\S]*?function updateHud\(\) \{[\s\S]*?updateRepairBadge\(\);\s*\}'
    html = re.sub(controllers_regex, lambda m: new_step_controllers, html, count=1)

    # Replacement 7: renderStage() - include arena tab
    old_render_stage = """      if (state.activeTab === "cards") {
        renderCardsStage(stage, langObj);
      } else if (state.activeTab === "ear_gym") {
        renderEarGymStage(stage, langObj);
      } else if (state.activeTab === "market") {
        renderMarketStage(stage, langObj);
      } else if (state.activeTab === "sundial") {
        renderSundialStage(stage, langObj);
      } else if (state.activeTab === "scribe") {
        renderScribeStage(stage, langObj);
      } else if (state.activeTab === "guardian") {
        renderGuardianStage(stage, langObj);
      }"""

    new_render_stage = """      if (state.activeTab === "cards") {
        renderCardsStage(stage, langObj);
      } else if (state.activeTab === "ear_gym") {
        renderEarGymStage(stage, langObj);
      } else if (state.activeTab === "market") {
        renderMarketStage(stage, langObj);
      } else if (state.activeTab === "sundial") {
        renderSundialStage(stage, langObj);
      } else if (state.activeTab === "arena") {
        renderArenaStage(stage, langObj);
      } else if (state.activeTab === "scribe") {
        renderScribeStage(stage, langObj);
      } else if (state.activeTab === "guardian") {
        renderGuardianStage(stage, langObj);
      }"""

    html = html.replace(old_render_stage, new_render_stage, 1)

    # Replacement 8: renderCardsStage() - dynamic category filters & navigateCard fix
    old_cards_code_regex = r'function renderCardsStage\(stage, langObj\) \{[\s\S]*?function togglePinWhisper\(\) \{[\s\S]*?renderStage\(\);\s*\}'
    
    new_cards_code = """    function renderCardsStage(stage, langObj) {
      const stepData = getActiveStepData();
      const allCards = stepData.cards || [];

      // Extract unique types dynamically
      const uniqueTypes = Array.from(new Set(allCards.map(c => c.type).filter(Boolean)));
      
      const filteredDeck = allCards.filter(c => {
        if (state.cardFilter === "all") return true;
        return c.type === state.cardFilter;
      });

      if (state.cardIndex >= filteredDeck.length) state.cardIndex = 0;
      const card = filteredDeck[state.cardIndex] || allCards[0];

      // Award visit XP
      if (card) {
        const visitKey = `${state.currentLang}:card:${card.id}`;
        if (!state.visitedCards[visitKey]) {
          state.visitedCards[visitKey] = true;
          awardXp(10, `Discovered stone "${card.gloss}"`);
        }
      }

      const stoneDots = filteredDeck.map((c, i) => {
        const vKey = `${state.currentLang}:card:${c.id}`;
        const isVisited = !!state.visitedCards[vKey];
        const isCur = i === state.cardIndex;
        return `<button onclick="jumpToCard(${i})" class="stone-dot ${isCur ? 'current' : (isVisited ? 'visited' : '')}" title="${c.gloss}"></button>`;
      }).join("");

      // Filter buttons
      const filterPills = [
        `<button onclick="setCardFilter('all')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'all' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">All (${allCards.length})</button>`,
        ...uniqueTypes.map(t => {
          const count = allCards.filter(c => c.type === t).length;
          const displayLabel = t.replace(/_/g, " ").replace(/\\b\\w/g, l => l.toUpperCase());
          return `<button onclick="setCardFilter('${t}')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === t ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">${displayLabel} (${count})</button>`;
        })
      ].join("");

      stage.innerHTML = `
        <div class="pixel-box p-6 sm:p-8 card-animate flex flex-col justify-between min-h-[400px]">
          
          <!-- Card Header: Filters & Stone Dots -->
          <div class="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-[var(--border-pixel)]">
            <div class="flex items-center gap-1.5 text-xs flex-wrap">
              ${filterPills}
            </div>
            <div class="flex items-center gap-1.5 flex-wrap">
              ${stoneDots}
            </div>
          </div>

          <!-- Card Body: Focused Glyph -->
          <div class="my-6 text-center flex flex-col items-center gap-3">
            <span class="text-xs px-2.5 py-0.5 rounded bg-[var(--bg-deep)] text-[var(--accent-sage)] border border-[var(--border-pixel)]">
              ${card ? card.gloss : ''}
            </span>

            <div dir="${langObj.rtl ? 'rtl' : 'ltr'}" class="text-3xl sm:text-5xl font-bold tracking-wide text-[var(--text-main)] py-2 select-text font-body">
              ${card ? card.glyph : ''}
            </div>

            <div class="font-pixel-tall text-xl sm:text-2xl text-[var(--accent-amber)]">
              ${card ? card.phonetic : ''}
            </div>

            <div class="flex flex-wrap items-center justify-center gap-3 mt-2">
              <button onclick="playAudioPrompt('${card ? card.speakText.replace(/'/g, "\\\\'") : ''}', '${card && card.audioUrl ? card.audioUrl : ''}')" class="pixel-btn px-4 py-2 text-xs">
                <span>🔊</span>
                <span>Listen (Studio)</span>
              </button>
              <button onclick="toggleWhisper()" class="pixel-btn px-4 py-2 text-xs ${state.whisperOpen ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">
                <span>✨</span>
                <span>${state.whisperOpen ? 'Hide Whisper' : 'Reveal Whisper'}</span>
              </button>
            </div>

            <!-- Pedagogical Whisper Box -->
            ${state.whisperOpen && card ? `
              <div class="pixel-box-whisper p-4 mt-3 max-w-lg w-full text-left card-animate">
                <div class="flex items-center justify-between mb-1">
                  <span class="font-pixel-ui text-[11px] text-[var(--accent-amber)]">📜 SANCTUARY WHISPER</span>
                  <button onclick="togglePinWhisper()" class="text-[11px] text-[var(--text-muted)] hover:text-[var(--accent-amber)] underline cursor-pointer">
                    ${state.keepWhisperPinned ? '📌 Pinned Open' : 'Pin Whispers Open'}
                  </button>
                </div>
                <p class="text-xs sm:text-sm text-[var(--text-main)] leading-relaxed select-text">
                  ${card.whisper}
                </p>
              </div>
            ` : ''}
          </div>

          <!-- Card Footer -->
          <div class="flex items-center justify-between pt-4 border-t border-[var(--border-pixel)]">
            <button onclick="navigateCard(-1)" ${state.cardIndex === 0 ? 'disabled' : ''} class="pixel-btn px-4 py-2 text-xs">◀ Prev</button>
            <span class="text-xs text-[var(--text-dim)] hidden sm:inline">${state.cardIndex + 1} of ${filteredDeck.length}</span>
            <button onclick="navigateCard(1)" class="pixel-btn pixel-btn-amber px-5 py-2 text-xs">
              ${state.cardIndex === filteredDeck.length - 1 ? 'Step to Ear Gym ▶' : 'Next Stone ▶'}
            </button>
          </div>

        </div>
      `;
    }

    function setCardFilter(f) {
      state.cardFilter = f;
      state.cardIndex = 0;
      playChime("step");
      renderStage();
    }

    function jumpToCard(i) {
      state.cardIndex = i;
      playChime("step");
      renderStage();
    }

    function navigateCard(delta) {
      const stepData = getActiveStepData();
      const allCards = stepData.cards || [];
      const filteredDeck = allCards.filter(c => {
        if (state.cardFilter === "all") return true;
        return c.type === state.cardFilter;
      });

      const nextIdx = state.cardIndex + delta;
      if (nextIdx >= 0 && nextIdx < filteredDeck.length) {
        state.cardIndex = nextIdx;
        playChime("step");
        renderStage();
      } else if (nextIdx >= filteredDeck.length) {
        switchTab("ear_gym");
      }
    }

    function toggleWhisper() {
      state.whisperOpen = !state.whisperOpen;
      playChime("whisper");
      renderStage();
    }

    function togglePinWhisper() {
      state.keepWhisperPinned = !state.keepWhisperPinned;
      state.whisperOpen = state.keepWhisperPinned;
      saveProgress();
      playChime("whisper");
      renderStage();
    }"""

    html = re.sub(old_cards_code_regex, lambda m: new_cards_code, html, count=1)

    # Replacement 9: Ear Gym stage - Next button target based on current step
    old_eargym_btn = """<button onclick="switchTab('market')" class="pixel-btn pixel-btn-amber px-4 py-2 text-xs">Enter Merchant Stall ▶</button>"""
    new_eargym_btn = """<button onclick="switchTab(state.currentStep === 1 ? 'market' : (state.currentStep === 2 ? 'sundial' : 'arena'))" class="pixel-btn pixel-btn-amber px-4 py-2 text-xs">Enter Active Arena ▶</button>"""
    html = html.replace(old_eargym_btn, new_eargym_btn, 1)

    # Replacement 10: Inject renderArenaStage() right after renderSundialStage()
    arena_stage_code = """
    /* -------------------------------------------------------------------------
       7C. 3C–10C. SENTENCE ARENA (INTERACTIVE PHRASE & CLAUSE BUILDER)
       ------------------------------------------------------------------------- */
    function renderArenaStage(stage, langObj) {
      const stepData = getActiveStepData();
      const list = stepData.arena || [];
      const s = state.currentStep;

      if (!list || list.length === 0 || state.arenaIndex >= list.length) {
        stage.innerHTML = `
          <div class="pixel-box p-6 sm:p-8 text-center card-animate space-y-4">
            <span class="text-3xl">${stepData.guide ? stepData.guide.avatar : '✨'}</span>
            <h3 class="font-pixel-title text-base text-[var(--accent-sage)]">Step ${s} Sentence Arena Completed!</h3>
            <p class="text-xs sm:text-sm text-[var(--text-muted)] max-w-md mx-auto">
              You constructed and verified authentic conversational phrases and sentences for <strong>${langObj.name}</strong>.
            </p>
            <div class="flex flex-wrap items-center justify-center gap-3 pt-2">
              <button onclick="state.arenaIndex = 0; state.arenaBuffer = []; state.arenaCompleted = false; renderStage();" class="pixel-btn px-4 py-2 text-xs">↻ Replay Arena Quests</button>
              <button onclick="switchTab('scribe')" class="pixel-btn pixel-btn-amber px-4 py-2 text-xs">Enter Scribe Desk ▶</button>
            </div>
          </div>
        `;
        return;
      }

      const item = list[state.arenaIndex];
      const guide = stepData.guide || { name: "Sanctuary Guide", role: "Mentor", avatar: "✨", prompt: "" };

      // Determine which tokens have been used into the buffer
      const usedIndices = new Set(state.arenaBuffer.map(b => b.tokenIdx));

      stage.innerHTML = `
        <div class="pixel-box p-6 sm:p-8 card-animate space-y-5">
          <!-- Arena Header -->
          <div class="flex items-center justify-between border-b border-[var(--border-pixel)] pb-3">
            <div class="flex items-center gap-3">
              <div class="text-2xl">${guide.avatar}</div>
              <div>
                <div class="font-pixel-ui text-xs text-[var(--accent-amber)]">${guide.name}</div>
                <div class="text-[11px] text-[var(--text-muted)]">${guide.role}</div>
              </div>
            </div>
            <span class="font-pixel-ui text-xs text-[var(--accent-sage)]">QUEST ${state.arenaIndex + 1}/${list.length} • +25 XP</span>
          </div>

          <!-- Quest Prompt & Clue -->
          <div class="pixel-box-whisper p-4 space-y-1">
            <div class="font-pixel-ui text-[11px] text-[var(--accent-amber)]">${item.quest}</div>
            <div class="text-sm sm:text-base font-semibold text-[var(--text-main)] italic">
              "${item.clue}"
            </div>
          </div>

          <!-- Sentence Construction Parchment Slot -->
          <div class="p-5 rounded bg-[var(--bg-deep)] border-2 border-[var(--border-pixel)] space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs text-[var(--text-muted)] font-pixel-ui">Assembled Inscription:</span>
              <button onclick="clearArenaBuffer()" class="text-[11px] text-[var(--accent-terra)] hover:underline cursor-pointer">
                ⌫ Clear Phrase
              </button>
            </div>

            <div dir="${langObj.rtl ? 'rtl' : 'ltr'}" class="min-h-[56px] p-3 rounded bg-[var(--bg-surface)] border border-[var(--border-pixel)] flex flex-wrap items-center gap-2 font-body">
              ${state.arenaBuffer.length === 0 ? `
                <span class="text-xs text-[var(--text-dim)] italic">Tap word tokens below to construct the target sentence...</span>
              ` : state.arenaBuffer.map((b, bi) => `
                <button onclick="removeArenaToken(${bi})" class="pixel-btn px-3 py-1.5 text-xs sm:text-sm font-semibold border-[var(--accent-amber)] bg-[var(--accent-amber)]/10 hover:bg-[var(--accent-terra)]/20" title="Click to remove token">
                  <span>${b.token}</span>
                  <span class="text-[10px] text-[var(--accent-terra)] ml-1">×</span>
                </button>
              `).join("")}
            </div>
          </div>

          <!-- Available Tokens Bank -->
          <div class="space-y-2">
            <div class="text-xs text-[var(--text-muted)] font-pixel-ui text-center">Available Token Vault:</div>
            <div dir="${langObj.rtl ? 'rtl' : 'ltr'}" class="flex flex-wrap items-center justify-center gap-2 pt-1 font-body">
              ${item.tokens.map((token, ti) => {
                const isUsed = usedIndices.has(ti);
                return `
                  <button
                    onclick="addArenaToken('${token.replace(/'/g, "\\\\'")}', ${ti})"
                    ${isUsed ? 'disabled' : ''}
                    class="pixel-btn px-3.5 py-2 text-xs sm:text-sm font-medium ${isUsed ? 'opacity-35 pointer-events-none' : 'hover:border-[var(--accent-amber)]'}"
                  >
                    ${token}
                  </button>
                `;
              }).join("")}
            </div>
          </div>

          <!-- Submit / Feedback Section -->
          ${!state.arenaCompleted ? `
            <div class="text-center pt-2">
              <button onclick="checkArenaPhrase()" class="pixel-btn pixel-btn-amber px-6 py-2.5 text-xs">
                Verify Sentence Construction ★
              </button>
            </div>
          ` : `
            <div class="pixel-box-whisper p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 card-animate">
              <div class="text-xs sm:text-sm">
                <strong class="font-pixel-ui text-[var(--accent-sage)]">✨ Masterfully Constructed!</strong>
                <span class="text-[var(--text-main)] ml-1">${item.explain}</span>
              </div>
              <button onclick="nextArenaQuest()" class="pixel-btn pixel-btn-amber px-4 py-2 text-xs whitespace-nowrap">
                ${state.arenaIndex === list.length - 1 ? 'Complete Sentence Arena ★' : 'Next Quest ▶'}
              </button>
            </div>
          `}
        </div>
      `;
    }

    function addArenaToken(token, tokenIdx) {
      if (state.arenaCompleted) return;
      playChime("step");
      state.arenaBuffer.push({ token, tokenIdx });
      renderStage();
    }

    function removeArenaToken(bufferIdx) {
      if (state.arenaCompleted) return;
      playChime("whisper");
      state.arenaBuffer.splice(bufferIdx, 1);
      renderStage();
    }

    function clearArenaBuffer() {
      if (state.arenaCompleted) return;
      playChime("whisper");
      state.arenaBuffer = [];
      renderStage();
    }

    function normalizeSentenceText(str) {
      if (!str) return "";
      return str
        .replace(/[\\.\\?\\!\\,\\;\\:\\—\\-\\"\\'\\«\\»\\‹\\›\\„\\“\\”\\(\\)\\[\\]]/g, "")
        .replace(/\\s+/g, " ")
        .trim()
        .toLowerCase();
    }

    function checkArenaPhrase() {
      const stepData = getActiveStepData();
      const list = stepData.arena || [];
      const item = list[state.arenaIndex];
      const langObj = LANGUAGES[state.currentLang];

      const assembledPhrase = state.arenaBuffer.map(b => b.token).join(" ").trim();
      const normAssembled = normalizeSentenceText(assembledPhrase);
      const normTarget = normalizeSentenceText(item.target);

      // Chinese characters may be joined without spaces
      const normAssembledNoSpace = normAssembled.replace(/\\s+/g, "");
      const normTargetNoSpace = normTarget.replace(/\\s+/g, "");

      if (normAssembled === normTarget || normAssembledNoSpace === normTargetNoSpace) {
        playChime("correct");
        awardXp(25, `Constructed "${item.target}"`);
        state.arenaCompleted = true;
      } else {
        playChime("retry");
        setFooterStatus(`🌿 Not quite aligned. Target phrase: "${item.target}"`);
        logMistake("Sentence Arena", `${langObj.name}: ${item.quest} (Target: "${item.target}")`);
      }
      renderStage();
    }

    function nextArenaQuest() {
      state.arenaIndex += 1;
      state.arenaBuffer = [];
      state.arenaCompleted = false;
      playChime("step");
      renderStage();
    }
"""

    sundial_end = """    function nextSundialQuest() {
      state.sundialIndex += 1;
      state.sundialCompleted = false;
      playChime("step");
      renderStage();
    }"""

    html = html.replace(sundial_end, sundial_end + "\n" + arena_stage_code, 1)

    # Replacement 11: renderChronologyModalContent() - Jump-to-step buttons & seal status
    new_chronology_modal_fn = """    function renderChronologyModalContent() {
      const container = document.getElementById("modalChronologyList");
      const langId = state.currentLang;
      const langName = LANGUAGES[langId].name;

      container.innerHTML = CHRONOLOGY_STEPS.map(s => {
        const isCurrent = s.step === state.currentStep;
        const sealEarned = !!state.quizCompletedByLang[`${langId}:step${s.step}`];
        let sealTitle = "";
        if (s.step === 1) sealTitle = LANGUAGES[langId].sealName;
        else if (ALL_STEPS_DATA[s.step] && ALL_STEPS_DATA[s.step][langId]) sealTitle = ALL_STEPS_DATA[s.step][langId].sealName;

        return `
          <div class="pixel-box p-3.5 ${isCurrent ? 'border-[var(--accent-amber)] bg-[var(--accent-amber)]/5' : (sealEarned ? 'border-[var(--accent-sage)]' : '')}">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-1.5">
              <div class="flex items-center gap-2">
                <span class="text-base">${sealEarned ? '⭐' : (isCurrent ? '◈' : '◇')}</span>
                <span class="font-pixel-ui text-xs sm:text-sm ${isCurrent ? 'text-[var(--accent-amber)]' : (sealEarned ? 'text-[var(--accent-sage)]' : 'text-[var(--text-main)]')}">
                  ${s.title}
                </span>
              </div>
              <div class="flex items-center gap-2">
                <span class="font-pixel-ui text-[10px] px-2 py-0.5 rounded ${sealEarned ? 'bg-[var(--accent-sage)] text-[#1d2620]' : (isCurrent ? 'bg-[var(--accent-amber)] text-[#1d2620]' : 'bg-[var(--bg-deep)] text-[var(--accent-sage)] border border-[var(--border-pixel)]')}">
                  ${sealEarned ? 'SEAL EARNED' : s.status}
                </span>
                <button onclick="switchStep(${s.step}); closeQuestLogModal();" class="pixel-btn px-2.5 py-1 text-[11px] ${isCurrent ? 'pixel-btn-amber' : ''}">
                  ${isCurrent ? 'Current Arena' : `Enter Step ${s.step} ▶`}
                </button>
              </div>
            </div>
            <p class="text-xs text-[var(--text-main)] mb-1">${s.summary}</p>
            ${sealTitle ? `<p class="text-[11px] text-[var(--accent-amber)] mb-1 font-pixel-ui">🏅 ${langName} Realm Seal: <em>${sealTitle}</em></p>` : ''}
            <p class="text-xs text-[var(--text-muted)]">
              <strong class="text-[var(--accent-sage)]">Pedagogical Adaptation:</strong> ${s.adaptation}
            </p>
          </div>
        `;
      }).join("");
    }"""

    old_chronology_modal_regex = r'function renderChronologyModalContent\(\) \{[\s\S]*?container\.innerHTML = CHRONOLOGY_STEPS\.map[\s\S]*?\}\.join\(""\);\s*\}'
    html = re.sub(old_chronology_modal_regex, lambda m: new_chronology_modal_fn, html, count=1)

    print("4. Writing compiled sanctuary HTML file...")
    with open(base_html_path, "w", encoding="utf-8") as f:
        f.write(html)

    file_size = os.path.getsize(base_html_path)
    print(f"🎉 Sanctuary compilation successful! Output size: {file_size:,} bytes ({file_size/1024:.1f} KB).")
    return True

if __name__ == "__main__":
    build_sanctuary()
