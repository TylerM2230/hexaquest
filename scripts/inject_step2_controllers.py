#!/usr/bin/env python3
"""
Update UI controller functions for Step 2 in hexaquest_cozy_pixel_language_sanctuary.html
"""
import re

with open("hexaquest_cozy_pixel_language_sanctuary.html", "r", encoding="utf-8") as f:
    html = f.read()

# Helper function to get active step data
helper_func = '''
    function getActiveStepData() {
      const langObj = LANGUAGES[state.currentLang];
      if (state.currentStep === 2 && langObj.step2) {
        return {
          stepNum: 2,
          sealName: langObj.step2.sealName,
          timekeeper: langObj.step2.timekeeper,
          cards: langObj.step2.cards,
          earGym: langObj.step2.earGym,
          sundial: langObj.step2.sundial,
          scribe: langObj.step2.scribe,
          quiz: langObj.step2.quiz
        };
      }
      return {
        stepNum: 1,
        sealName: langObj.sealName,
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
      state.scribeIndex = 0;
      state.scribeBuffer = [];
      state.scribeSuccess = false;
      state.quizIndex = 0;
      state.quizSelected = null;
      state.activeTab = "cards";

      const btn1 = document.getElementById("stepBtn-1");
      const btn2 = document.getElementById("stepBtn-2");
      if (btn1 && btn2) {
        btn1.classList.toggle("pixel-btn-amber", stepNum === 1);
        btn2.classList.toggle("pixel-btn-amber", stepNum === 2);
      }
      const badge = document.getElementById("stepContextBadge");
      if (badge) badge.textContent = stepNum === 1 ? "STEP 1: 0–10" : "STEP 2: DATES";

      playChime("step");
      renderTabs();
      renderStage();
      updateHud();
      setFooterStatus(stepNum === 1 ? "Switched to Step 1 Sanctuary: Runes & Numbers 0–10." : "✨ Switched to Step 2 Arena: Dates, Months & Numbers 11–31!");
    }

    function renderTabs() {
      const container = document.getElementById("arenaTabsContainer");
      if (!container) return;
      const s = state.currentStep;
      const tabs = s === 1 ? [
        { id: "cards", label: "1A. Cards", title: "1A. Single-Item Flashcard Study" },
        { id: "ear_gym", label: "1B. Ear Gym", title: "1B. Auditory Minimal Pairs & Tone Gym" },
        { id: "market", label: "1C. Market", title: "1C. Cozy Merchant Quantity Sprints" },
        { id: "scribe", label: "1D. Scribe", title: "1D. Active Orthography & Tile Scribe" },
        { id: "guardian", label: "1E. Owl Exam", title: "1E. Owl Guardian Sanctuary Seal Exam" }
      ] : [
        { id: "cards", label: "2A. Calendar", title: "2A. Months & Dates 11–31 Cards" },
        { id: "ear_gym", label: "2B. Ear Gym", title: "2B. Calendar Acoustic Discrimination" },
        { id: "sundial", label: "2C. Sundial", title: "2C. Timekeeper Sundial Date Construction" },
        { id: "scribe", label: "2D. Scribe", title: "2D. Active Calendar Orthography" },
        { id: "guardian", label: "2E. Owl Exam", title: "2E. Step 2 Sanctuary Seal Exam" }
      ];

      // Auto-correct activeTab if switching between market and sundial
      if (s === 1 && state.activeTab === "sundial") state.activeTab = "market";
      if (s === 2 && state.activeTab === "market") state.activeTab = "sundial";

      container.innerHTML = tabs.map(t => `
        <button onclick="switchTab('${t.id}')" id="tab-${t.id}" class="pixel-btn py-2 px-1 text-[11px] sm:text-xs ${state.activeTab === t.id ? 'pixel-btn-active-tab' : ''}" title="${t.title}">
          <span>${t.label}</span>
        </button>
      `).join("");
    }
'''

# Insert helper_func right before updateHud
html = html.replace('function updateHud() {', helper_func + '\n    function updateHud() {')

# Update updateHud() seals counter
old_hud_badges = 'const sealsEarned = Object.keys(state.quizCompletedByLang).length;\n      document.getElementById("hudBadges").textContent = `${sealsEarned}/6 SEALS`;'
new_hud_badges = 'const sealsEarned = Object.keys(state.quizCompletedByLang).filter(k => state.quizCompletedByLang[k]).length;\n      document.getElementById("hudBadges").textContent = `${sealsEarned}/12 SEALS`;'
html = html.replace(old_hud_badges, new_hud_badges)

# In switchTab, handle sundial
old_switch_tab = '''    function switchTab(tabId) {
      state.activeTab = tabId;
      playChime("step");
      ["cards", "ear_gym", "market", "scribe", "guardian"].forEach(t => {
        const btn = document.getElementById(`tab-${t}`);
        if (btn) btn.classList.toggle("pixel-btn-active-tab", t === tabId);
      });
      renderStage();
    }'''

new_switch_tab = '''    function switchTab(tabId) {
      state.activeTab = tabId;
      playChime("step");
      ["cards", "ear_gym", "market", "sundial", "scribe", "guardian"].forEach(t => {
        const btn = document.getElementById(`tab-${t}`);
        if (btn) btn.classList.toggle("pixel-btn-active-tab", t === tabId);
      });
      renderStage();
    }'''
html = html.replace(old_switch_tab, new_switch_tab)

# Update renderStage() to check for sundial
old_render_stage = '''      if (state.activeTab === "cards") {
        renderCardsStage(stage, langObj);
      } else if (state.activeTab === "ear_gym") {
        renderEarGymStage(stage, langObj);
      } else if (state.activeTab === "market") {
        renderMarketStage(stage, langObj);
      } else if (state.activeTab === "scribe") {
        renderScribeStage(stage, langObj);
      } else if (state.activeTab === "guardian") {
        renderGuardianStage(stage, langObj);
      }'''

new_render_stage = '''      if (state.activeTab === "cards") {
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
      }'''
html = html.replace(old_render_stage, new_render_stage)

# Update renderCardsStage to support Step 1 & Step 2 cards and filters
old_render_cards_deck = '''    function renderCardsStage(stage, langObj) {
      const filteredDeck = langObj.cards.filter(c => {
        if (state.cardFilter === "rune") return c.type === "rune";
        if (state.cardFilter === "number") return c.type === "number";
        return true;
      });'''

new_render_cards_deck = '''    function renderCardsStage(stage, langObj) {
      const stepData = getActiveStepData();
      const filteredDeck = stepData.cards.filter(c => {
        if (state.cardFilter === "rune") return c.type === "rune";
        if (state.cardFilter === "number") return c.type === "number";
        if (state.cardFilter === "month") return c.type === "month";
        if (state.cardFilter === "date_num") return c.type === "date_num";
        return true;
      });'''
html = html.replace(old_render_cards_deck, new_render_cards_deck)

# Update the card filter buttons in renderCardsStage
old_filter_html = '''            <div class="flex items-center gap-1.5 text-xs">
              <button onclick="setCardFilter('all')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'all' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">All (${langObj.cards.length})</button>
              <button onclick="setCardFilter('rune')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'rune' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">Runes</button>
              <button onclick="setCardFilter('number')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'number' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">Numbers (0–10)</button>
            </div>'''

new_filter_html = '''            <div class="flex items-center gap-1.5 text-xs flex-wrap">
              <button onclick="setCardFilter('all')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'all' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">All (${stepData.cards.length})</button>
              ${state.currentStep === 1 ? `
                <button onclick="setCardFilter('rune')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'rune' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">Runes</button>
                <button onclick="setCardFilter('number')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'number' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">Numbers 0–10</button>
              ` : `
                <button onclick="setCardFilter('month')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'month' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">Months (1–12)</button>
                <button onclick="setCardFilter('date_num')" class="pixel-btn px-2 py-0.5 text-[10px] ${state.cardFilter === 'date_num' ? 'border-[var(--accent-amber)] text-[var(--accent-amber)]' : ''}">Dates 11–31</button>
              `}
            </div>'''
html = html.replace(old_filter_html, new_filter_html)

# Update Ear Gym stage to use getActiveStepData()
html = html.replace('const list = langObj.earGym;', 'const stepData = getActiveStepData();\n      const list = stepData.earGym;')
html = html.replace('const item = langObj.earGym[state.earIndex];', 'const stepData = getActiveStepData();\n      const item = stepData.earGym[state.earIndex];')

# Update Scribe stage to use getActiveStepData()
html = html.replace('const list = langObj.scribe;', 'const stepData = getActiveStepData();\n      const list = stepData.scribe;')
html = html.replace('const item = langObj.scribe[state.scribeIndex];', 'const stepData = getActiveStepData();\n      const item = stepData.scribe[state.scribeIndex];')

# Add renderSundialStage and adjust sundial controllers
sundial_renderers = '''
    /* -------------------------------------------------------------------------
       7C-2. 2C. SUNDIAL DESK (APPLIED CALENDAR DATE CONSTRUCTION)
       ------------------------------------------------------------------------- */
    function renderSundialStage(stage, langObj) {
      const stepData = getActiveStepData();
      const list = stepData.sundial;
      if (!list || state.sundialIndex >= list.length) {
        stage.innerHTML = `
          <div class="pixel-box p-6 sm:p-8 text-center card-animate space-y-4">
            <span class="text-3xl">${stepData.timekeeper ? stepData.timekeeper.avatar : '📅'}</span>
            <h3 class="font-pixel-title text-base text-[var(--accent-amber)]">${stepData.timekeeper ? stepData.timekeeper.name : 'Timekeeper'}'s Almanac Complete!</h3>
            <p class="text-xs sm:text-sm text-[var(--text-muted)] max-w-md mx-auto">
              You calibrated calendar dates and festival markers across the ${langObj.name} realm!
            </p>
            <div class="flex flex-wrap items-center justify-center gap-3 pt-2">
              <button onclick="state.sundialIndex = 0; state.sundialCompleted = false; renderStage();" class="pixel-btn px-4 py-2 text-xs">↻ Replay Sundial</button>
              <button onclick="switchTab('scribe')" class="pixel-btn pixel-btn-amber px-4 py-2 text-xs">Go to Scribe Desk ▶</button>
            </div>
          </div>
        `;
        return;
      }

      const item = list[state.sundialIndex];
      const monthCards = stepData.cards.filter(c => c.type === "month");
      const currentMonthCard = monthCards[state.sundialMonthIdx] || monthCards[0];

      stage.innerHTML = `
        <div class="pixel-box p-6 sm:p-8 card-animate space-y-5">
          <!-- Timekeeper Header -->
          <div class="flex items-center justify-between border-b border-[var(--border-pixel)] pb-3">
            <div class="flex items-center gap-3">
              <div class="text-2xl">${stepData.timekeeper ? stepData.timekeeper.avatar : '📅'}</div>
              <div>
                <div class="font-pixel-ui text-xs text-[var(--accent-amber)]">${stepData.timekeeper ? stepData.timekeeper.name : 'Timekeeper'}</div>
                <div class="text-[11px] text-[var(--text-muted)]">${stepData.timekeeper ? stepData.timekeeper.role : 'Calendar Master'}</div>
              </div>
            </div>
            <span class="font-pixel-ui text-xs text-[var(--accent-sage)]">QUEST ${state.sundialIndex + 1}/${list.length}</span>
          </div>

          <!-- Quest Prompt -->
          <div class="pixel-box-whisper p-4 space-y-1">
            <div class="font-pixel-ui text-[11px] text-[var(--accent-amber)]">${item.quest}</div>
            <div class="text-sm sm:text-base font-semibold text-[var(--text-main)] italic">
              "${item.clue}"
            </div>
          </div>

          <!-- Interactive Sundial Dials -->
          <div class="p-5 rounded bg-[var(--bg-deep)] border-2 border-[var(--border-pixel)] text-center space-y-4">
            <div class="text-xs text-[var(--text-muted)]">Align Month and Day on the Sanctuary Parchment:</div>
            
            <!-- Big Date Parchment Display -->
            <div class="p-4 rounded bg-[var(--bg-surface)] border border-[var(--border-pixel)] flex flex-col items-center justify-center gap-1">
              <div dir="${langObj.rtl ? 'rtl' : 'ltr'}" class="font-pixel-title text-base sm:text-lg text-[var(--accent-amber)] font-body">
                ${currentMonthCard ? currentMonthCard.glyph : ''}
              </div>
              <div class="font-pixel-tall text-3xl sm:text-4xl text-[var(--text-main)]">
                Day ${state.sundialDay}
              </div>
              <div class="text-xs text-[var(--text-muted)] font-pixel-ui">
                [${currentMonthCard ? currentMonthCard.phonetic : ''}]
              </div>
            </div>

            <!-- Dials -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              <!-- Month Dial -->
              <div class="flex items-center justify-between gap-2 p-2 rounded bg-[var(--bg-surface)] border border-[var(--border-pixel)]">
                <button onclick="adjustSundialMonth(-1)" class="pixel-btn px-3 py-1.5 text-xs">◀</button>
                <div dir="${langObj.rtl ? 'rtl' : 'ltr'}" class="text-xs font-pixel-ui text-[var(--text-main)] truncate max-w-[130px] font-body">${currentMonthCard ? currentMonthCard.glyph : ''}</div>
                <button onclick="adjustSundialMonth(1)" class="pixel-btn px-3 py-1.5 text-xs">▶</button>
              </div>
              <!-- Day Dial -->
              <div class="flex items-center justify-between gap-2 p-2 rounded bg-[var(--bg-surface)] border border-[var(--border-pixel)]">
                <button onclick="adjustSundialDay(-1)" class="pixel-btn px-3 py-1.5 text-xs">◀</button>
                <div class="text-sm font-pixel-tall text-[var(--accent-amber)] font-bold">Day ${state.sundialDay}</div>
                <button onclick="adjustSundialDay(1)" class="pixel-btn px-3 py-1.5 text-xs">▶</button>
              </div>
            </div>
          </div>

          <!-- Submit / Feedback -->
          ${!state.sundialCompleted ? `
            <div class="text-center pt-2">
              <button onclick="checkSundialDate()" class="pixel-btn pixel-btn-amber px-6 py-2.5 text-xs">
                Confirm Date on Calendar ★
              </button>
            </div>
          ` : `
            <div class="pixel-box-whisper p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 card-animate">
              <div class="text-xs sm:text-sm">
                <strong class="font-pixel-ui text-[var(--accent-sage)]">✨ Calendar Aligned!</strong>
                <span class="text-[var(--text-main)] ml-1">${item.explain}</span>
              </div>
              <button onclick="nextSundialQuest()" class="pixel-btn pixel-btn-amber px-4 py-2 text-xs whitespace-nowrap">
                Next Calendar Quest ▶
              </button>
            </div>
          `}
        </div>
      `;
    }

    function adjustSundialMonth(delta) {
      playChime("step");
      const stepData = getActiveStepData();
      const monthCards = stepData.cards.filter(c => c.type === "month");
      state.sundialMonthIdx = (state.sundialMonthIdx + delta + monthCards.length) % monthCards.length;
      renderStage();
    }

    function adjustSundialDay(delta) {
      playChime("step");
      state.sundialDay = Math.max(1, Math.min(31, state.sundialDay + delta));
      renderStage();
    }

    function checkSundialDate() {
      const stepData = getActiveStepData();
      const item = stepData.sundial[state.sundialIndex];
      if (state.sundialMonthIdx === item.targetMonthIdx && state.sundialDay === item.targetDay) {
        playChime("correct");
        awardXp(25, `Aligned calendar for ${item.quest}`);
        state.sundialCompleted = true;
      } else {
        playChime("retry");
        setFooterStatus(`🌿 Not quite aligned! Looking for ${item.displayMonth} Day ${item.targetDay}.`);
        logMistake("Sundial", `${LANGUAGES[state.currentLang].name}: ${item.quest} (Target: ${item.displayMonth} ${item.targetDay})`);
      }
      renderStage();
    }

    function nextSundialQuest() {
      state.sundialIndex += 1;
      state.sundialCompleted = false;
      playChime("step");
      renderStage();
    }
'''

# Insert sundial_renderers before Scribe stage
html = html.replace('/* -------------------------------------------------------------------------\n       7D. 1D. SCRIBE\'S DESK', sundial_renderers + '\n\n    /* -------------------------------------------------------------------------\n       7D. 1D. SCRIBE\'S DESK')

# Update Guardian Exam stage to use getActiveStepData() and sealKey
old_guardian_stage_head = '''    function renderGuardianStage(stage, langObj) {
      const quizList = langObj.quiz;
      const isFinished = state.quizIndex >= quizList.length;

      if (isFinished) {
        const sealAlreadyEarned = !!state.quizCompletedByLang[langObj.id];
        if (!sealAlreadyEarned) {
          state.quizCompletedByLang[langObj.id] = true;
          awardXp(50, `Unlocked ${langObj.sealName}!`);
          renderLanguageBar();
          playChime("xp");
        }'''

new_guardian_stage_head = '''    function renderGuardianStage(stage, langObj) {
      const stepData = getActiveStepData();
      const quizList = stepData.quiz;
      const isFinished = state.quizIndex >= quizList.length;

      if (isFinished) {
        const sealKey = `${langObj.id}:step${state.currentStep}`;
        const sealAlreadyEarned = !!state.quizCompletedByLang[sealKey];
        if (!sealAlreadyEarned) {
          state.quizCompletedByLang[sealKey] = true;
          awardXp(50, `Unlocked ${stepData.sealName}!`);
          saveProgress();
          renderLanguageBar();
          updateHud();
          playChime("xp");
        }'''
html = html.replace(old_guardian_stage_head, new_guardian_stage_head)

# In guardian exam completed template, update text to stepData.sealName and step number
html = html.replace('${langObj.sealName} Unlocked!', '${stepData.sealName} Unlocked!')
html = html.replace('<span class="font-pixel-ui text-xs text-[var(--accent-sage)]">STEP 1 REALM MASTERED</span>', '<span class="font-pixel-ui text-xs text-[var(--accent-sage)]">STEP ${state.currentStep} REALM MASTERED</span>')

# Update answerGuardianQuestion to use stepData
old_ans_guardian = '''    function answerGuardianQuestion(selectedIndex) {
      if (state.quizSelected !== null) return;
      const langObj = LANGUAGES[state.currentLang];
      const item = langObj.quiz[state.quizIndex];
      state.quizSelected = selectedIndex;'''

new_ans_guardian = '''    function answerGuardianQuestion(selectedIndex) {
      if (state.quizSelected !== null) return;
      const langObj = LANGUAGES[state.currentLang];
      const stepData = getActiveStepData();
      const item = stepData.quiz[state.quizIndex];
      state.quizSelected = selectedIndex;'''
html = html.replace(old_ans_guardian, new_ans_guardian)

# Update window.onload to call renderTabs()
old_onload = '''    window.onload = function () {
      loadSavedProgress();
      document.getElementById("themeIcon").textContent = state.theme === "twilight" ? "🌙" : "☀️";
      document.getElementById("themeLabel").textContent = state.theme === "twilight" ? "Twilight" : "Parchment";
      renderLanguageBar();
      updateHud();
      renderStage();
      initParticles();
      animateSanctuaryBg();
    };'''

new_onload = '''    window.onload = function () {
      loadSavedProgress();
      document.getElementById("themeIcon").textContent = state.theme === "twilight" ? "🌙" : "☀️";
      document.getElementById("themeLabel").textContent = state.theme === "twilight" ? "Twilight" : "Parchment";
      renderTabs();
      renderLanguageBar();
      updateHud();
      renderStage();
      initParticles();
      animateSanctuaryBg();
    };'''
html = html.replace(old_onload, new_onload)

# In selectLanguage, call renderTabs()
old_select_lang = '''      renderLanguageBar();
      renderStage();
    }'''

new_select_lang = '''      renderLanguageBar();
      renderTabs();
      renderStage();
    }'''
html = html.replace(old_select_lang, new_select_lang)

with open("hexaquest_cozy_pixel_language_sanctuary.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Controller functions updated successfully!")

