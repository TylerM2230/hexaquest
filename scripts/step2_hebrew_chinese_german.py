#!/usr/bin/env python3
"""
Step 2 Datasets for Hebrew, Chinese, German
"""

HEBREW_STEP2 = {
    "sealName": "Luach HaShanah Calendar Seal",
    "timekeeper": {
        "name": "Eli",
        "role": "Jerusalem Market Timekeeper",
        "avatar": "📅",
        "prompt": "Shalom! Set calendar dates for seasons, holidays, and milestones across Israel."
    },
    "cards": [
        {"id": "heb_m1", "type": "month", "monthNum": 1, "glyph": "יָנוּאָר", "phonetic": "yánuar ['januaʁ]", "gloss": "January • 31 יום", "speakText": "ינואר", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-yanuar.ogg", "whisper": "January in the civil Israeli calendar. Written with initial Yod (י)."},
        {"id": "heb_m2", "type": "month", "monthNum": 2, "glyph": "פֶבְּרוּאָר", "phonetic": "fébruar ['febʁuaʁ]", "gloss": "February • 28/29 יום", "speakText": "פברואר", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-februar.ogg", "whisper": "Starts with hard Pei [f/p]."},
        {"id": "heb_m3", "type": "month", "monthNum": 3, "glyph": "מֶרְץ", "phonetic": "merts [meʁts]", "gloss": "March • 31 יום", "speakText": "מרץ", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-merts.ogg", "whisper": "Ends with final Tzadi Sofit (ץ)."},
        {"id": "heb_m4", "type": "month", "monthNum": 4, "glyph": "אַפְּרִיל", "phonetic": "apríl [ʔap'ʁil]", "gloss": "April • 30 יום", "speakText": "אפריל", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-april.ogg", "whisper": "Alef carries the 'ah' pataḥ vowel."},
        {"id": "heb_m5", "type": "month", "monthNum": 5, "glyph": "מַאי", "phonetic": "may [maj]", "gloss": "May • 31 יום", "speakText": "מאי", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-may.ogg", "whisper": "Two letters: Mem + Yod (מַאי)."},
        {"id": "heb_m6", "type": "month", "monthNum": 6, "glyph": "יוּנִי", "phonetic": "yúni ['juni]", "gloss": "June • 30 יום", "speakText": "יוני", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-yuni.ogg", "whisper": "June. Clear 'yu-ni'."},
        {"id": "heb_m7", "type": "month", "monthNum": 7, "glyph": "יוּלִי", "phonetic": "yúli ['juli]", "gloss": "July • 31 יום", "speakText": "יולי", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-yuli.ogg", "whisper": "July. Lamed (ל) replaces Nun (נ) in Juni."},
        {"id": "heb_m8", "type": "month", "monthNum": 8, "glyph": "אוֹגוּסְט", "phonetic": "ógust ['ʔoɡust]", "gloss": "August • 31 יום", "speakText": "אוגוסט", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-ogust.ogg", "whisper": "Starts with Alef + Vav (אוֹ = 'O')."},
        {"id": "heb_m9", "type": "month", "monthNum": 9, "glyph": "סֶפְטֶמְבֶּר", "phonetic": "septémber [sep'tembeʁ]", "gloss": "September • 30 יום", "speakText": "ספטמבר", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-september.ogg", "whisper": "Begins with Samekh (ס)."},
        {"id": "heb_m10", "type": "month", "monthNum": 10, "glyph": "אוֹקְטוֹבֶּר", "phonetic": "október [ok'tobeʁ]", "gloss": "October • 31 יום", "speakText": "אוקטובר", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-oktober.ogg", "whisper": "Contains Qof (ק) and Tet (ט)."},
        {"id": "heb_m11", "type": "month", "monthNum": 11, "glyph": "נוֹבֶמְבֶּר", "phonetic": "novémber [no'vembeʁ]", "gloss": "November • 30 יום", "speakText": "נובמבר", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-november.ogg", "whisper": "Begins with Nun (נ)."},
        {"id": "heb_m12", "type": "month", "monthNum": 12, "glyph": "דֶּצֶמְבֶּר", "phonetic": "detsémber [de'tsembeʁ]", "gloss": "December • 31 יום", "speakText": "דצמבר", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-detsember.ogg", "whisper": "Begins with Dalet (ד) and Tzadi (צ)."},
        {"id": "heb_n11", "type": "date_num", "num": 11, "glyph": "11 — אַחַת-עֶשְׂרֵה", "phonetic": "achat-esré [ʔaˌχat esˈʁe]", "gloss": "Number 11", "speakText": "אחת עשרה", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-achat_esre.ogg", "whisper": "Feminine teen used for dates: achát + esré = 11."},
        {"id": "heb_n12", "type": "date_num", "num": 12, "glyph": "12 — שְׁתֵּים-עֶשְׂרֵה", "phonetic": "shtem-esré [ʃtem esˈʁe]", "gloss": "Number 12", "speakText": "שתים עשרה", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-shtem_esre.ogg", "whisper": "Twelve. Note 'shtem' replaces 'shtayim'."},
        {"id": "heb_n15", "type": "date_num", "num": 15, "glyph": "15 — חֲמֵשׁ-עֶשְׂרֵה", "phonetic": "chamesh-esré [χaˌmeʃ esˈʁe]", "gloss": "Number 15", "speakText": "חמש עשרה", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-chamesh_esre.ogg", "whisper": "Fifteen: 'בְּ-15 בְּמַאי' = on the 15th of May."},
        {"id": "heb_n20", "type": "date_num", "num": 20, "glyph": "20 — עֶשְׂרִים", "phonetic": "esrím [ʔesˈʁim]", "gloss": "Number 20", "speakText": "עשרים", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-esrim.ogg", "whisper": "Formed as the plural form of 10 ('éser' + '-im' = 'esrím'!)."},
        {"id": "heb_n21", "type": "date_num", "num": 21, "glyph": "21 — עֶשְׂרִים וְאַחַת", "phonetic": "esrím ve'achát", "gloss": "Number 21", "speakText": "עשרים ואחת", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-esrim_veachat.ogg", "whisper": "20 + 'and' (וְ) + 1 = esrím ve'achát."},
        {"id": "heb_n30", "type": "date_num", "num": 30, "glyph": "30 — שְׁלוֹשִׁים", "phonetic": "shloshím [ʃloˈʃim]", "gloss": "Number 30", "speakText": "שלושים", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-shloshim.ogg", "whisper": "Formed as the plural of 3 ('shalosh' + '-im' = 30!)."},
        {"id": "heb_n31", "type": "date_num", "num": 31, "glyph": "31 — שְׁלוֹשִׁים וְאַחַת", "phonetic": "shloshím ve'achát", "gloss": "Number 31", "speakText": "שלושים ואחת", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-shloshim_veachat.ogg", "whisper": "Thirty-one. Final day of long months."}
    ],
    "earGym": [
        {
            "prompt": "Listen to the teen number. Is it 13 (shlosh-esré) or 30 (shloshím)?",
            "speakAudio": "שלוש עשרה",
            "options": ["13 (shlosh-esré)", "30 (shloshím)", "3 (shalosh)"],
            "correct": 0,
            "explain": "The suffix '-esré' marks the teens (13), while '-im' marks the tens (30)."
        },
        {
            "prompt": "Listen to the date phrase. What date was spoken?",
            "speakAudio": "באחד במאי",
            "options": ["On May 1st ('b'-echad b'-May')", "On May 15th", "On June 1st"],
            "correct": 0,
            "explain": "Hebrew uses the prefix 'בְּ-' (b'- = in/on) before both the day and month: בְּ-1 בְּמַאי."
        }
    ],
    "sundial": [
        {
            "quest": "Spring May Day",
            "clue": "Eli: 'Set the Jerusalem calendar to May 1 (בְּ-1 בְּמַאי)!'",
            "targetMonthIdx": 4,
            "targetDay": 1,
            "displayMonth": "מַאי",
            "explain": "May 1st in Jerusalem."
        },
        {
            "quest": "Mid-Month Festival",
            "clue": "Eli: 'Mark the 15th of Nisan / April (בְּ-15 בְּאַפְּרִיל)!'",
            "targetMonthIdx": 3,
            "targetDay": 15,
            "displayMonth": "אַפְּרִיל",
            "explain": "15th of April / Nisan."
        },
        {
            "quest": "Autumn Gathering",
            "clue": "Eli: 'Mark October 20 (בְּ-20 בְּאוֹקְטוֹבֶּר)!'",
            "targetMonthIdx": 9,
            "targetDay": 20,
            "displayMonth": "אוֹקְטוֹבֶּר",
            "explain": "October 20th in Hebrew."
        }
    ],
    "scribe": [
        {"clue": "Assemble the month of January in Hebrew:", "tiles": ["י", "נ", "ו", "א", "ר", "מ"], "answer": "ינואר", "gloss": "יָנוּאָר (January)"},
        {"clue": "Assemble the month of March (ends in Tzadi Sofit):", "tiles": ["מ", "ר", "ץ", "נ", "ש"], "answer": "מרץ", "gloss": "מֶרְץ (March)"},
        {"clue": "Assemble the number 20 (plural of 10):", "tiles": ["ע", "ש", "ר", "י", "ם"], "answer": "עשרים", "gloss": "עֶשְׂרִים (20)"}
    ],
    "quiz": [
        {
            "q": "Which prefix letter in Hebrew means 'on' or 'in' when stating dates (e.g. 'on May 1st')?",
            "options": [
                "The preposition prefix בְּ- (b'-) — e.g. בְּ-1 בְּמַאי",
                "The prefix לְ- (l'-)",
                "The prefix מִ- (m'-)"
            ],
            "correct": 0,
            "explain": "The prefix בְּ- (bet with shva) attaches to dates: בְּ-15 בְּיָנוּאָר (on January 15th)."
        },
        {
            "q": "How are tens like 20 (עֶשְׂרִים) and 30 (שְׁלוֹשִׁים) grammatically formed from 10 and 3?",
            "options": [
                "By adding the masculine plural suffix '-im' (ים-) to the base root!",
                "With unrelated new roots",
                "By doubling the first letter"
            ],
            "correct": 0,
            "explain": "éser (10) $\to$ esrím (20); shalósh (3) $\to$ shloshím (30)."
        },
        {
            "q": "Which gender of numbers is traditionally used for dates and abstract counting in Hebrew?",
            "options": [
                "Feminine numbers (achát, shtáyim... achat-esré, esrím ve'achát)",
                "Masculine numbers exclusively",
                "Dual numbers only"
            ],
            "correct": 0,
            "explain": "Dates and counting default to the feminine forms."
        },
        {
            "q": "What is the Hebrew name for the month of March, ending with final Tzadi ץ?",
            "options": ["מֶרְץ (merts)", "מַאי (may)", "אַפְּרִיל (apríl)"],
            "correct": 0,
            "explain": "March is מֶרְץ (merts), ending with final Tzadi (ץ)."
        },
        {
            "q": "How is 21 formed in Hebrew ('twenty and one')?",
            "options": [
                "עֶשְׂרִים וְאַחַת (esrím ve'achát) using the conjunction וְ- (and)",
                "אַחַת עֶשְׂרִים without 'and'",
                "עֶשְׂרֵה אֶחָד"
            ],
            "correct": 0,
            "explain": "Tens connect to units with the prefix conjunction וְ- (ve- = and): עֶשְׂרִים וְאַחַת."
        }
    ]
}

CHINESE_STEP2 = {
    "sealName": "Jade Lunar Calendar Seal",
    "timekeeper": {
        "name": "Master Lao",
        "role": "Sanctuary Astronomer & Teahouse Elder",
        "avatar": "🌕",
        "prompt": "Nǐ hǎo! Track celestial festivals and solar dates using the transparent Chinese calendar."
    },
    "cards": [
        {"id": "zh_m1", "type": "month", "monthNum": 1, "glyph": "一月", "phonetic": "yīyuè (1st tone + 4th tone)", "gloss": "January • Month 1", "speakText": "一月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-yīyuè.ogg", "whisper": "Months in Chinese are completely regular: simply Number 1–12 + 月 (yuè = moon/month)!"},
        {"id": "zh_m2", "type": "month", "monthNum": 2, "glyph": "二月", "phonetic": "èryuè (4th tone + 4th tone)", "gloss": "February • Month 2", "speakText": "二月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-èryuè.ogg", "whisper": "Use 二 (èr), not 两 (liǎng), for months!"},
        {"id": "zh_m3", "type": "month", "monthNum": 3, "glyph": "三月", "phonetic": "sānyuè (1st tone + 4th tone)", "gloss": "March • Month 3", "speakText": "三月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-sānyuè.ogg", "whisper": "Three + Month = March."},
        {"id": "zh_m4", "type": "month", "monthNum": 4, "glyph": "四月", "phonetic": "sìyuè (4th tone + 4th tone)", "gloss": "April • Month 4", "speakText": "四月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-sìyuè.ogg", "whisper": "Four + Month = April."},
        {"id": "zh_m5", "type": "month", "monthNum": 5, "glyph": "五月", "phonetic": "wǔyuè (3rd tone + 4th tone)", "gloss": "May • Month 5", "speakText": "五月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-wǔyuè.ogg", "whisper": "Five + Month = May. Dragon Boat Festival is 五月五号 (5th day of 5th lunar month)."},
        {"id": "zh_m6", "type": "month", "monthNum": 6, "glyph": "六月", "phonetic": "liùyuè (4th tone + 4th tone)", "gloss": "June • Month 6", "speakText": "六月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-liùyuè.ogg", "whisper": "Six + Month = June."},
        {"id": "zh_m7", "type": "month", "monthNum": 7, "glyph": "七月", "phonetic": "qīyuè (1st tone + 4th tone)", "gloss": "July • Month 7", "speakText": "七月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-qīyuè.ogg", "whisper": "Seven + Month = July."},
        {"id": "zh_m8", "type": "month", "monthNum": 8, "glyph": "八月", "phonetic": "bāyuè (1st tone + 4th tone)", "gloss": "August • Month 8", "speakText": "八月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-bāyuè.ogg", "whisper": "Eight + Month = August. Mid-Autumn Moon Festival is 八月十五号!"},
        {"id": "zh_m9", "type": "month", "monthNum": 9, "glyph": "九月", "phonetic": "jiǔyuè (3rd tone + 4th tone)", "gloss": "September • Month 9", "speakText": "九月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-jiǔyuè.ogg", "whisper": "Nine + Month = September."},
        {"id": "zh_m10", "type": "month", "monthNum": 10, "glyph": "十月", "phonetic": "shíyuè (2nd tone + 4th tone)", "gloss": "October • Month 10", "speakText": "十月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-shíyuè.ogg", "whisper": "Ten + Month = October. China's National Day is 十月一日."},
        {"id": "zh_m11", "type": "month", "monthNum": 11, "glyph": "十一月", "phonetic": "shíyīyuè", "gloss": "November • Month 11", "speakText": "十一月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-shíyīyuè.ogg", "whisper": "11 (十一) + Month = November."},
        {"id": "zh_m12", "type": "month", "monthNum": 12, "glyph": "十二月", "phonetic": "shí'èryuè", "gloss": "December • Month 12", "speakText": "十二月", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-shíèryuè.ogg", "whisper": "12 (十二) + Month = December."},
        {"id": "zh_n11", "type": "date_num", "num": 11, "glyph": "11 — 十一", "phonetic": "shíyī", "gloss": "Number 11", "speakText": "十一", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-shíyī.ogg", "whisper": "10 (十) + 1 (一) = 十一 (11)."},
        {"id": "zh_n15", "type": "date_num", "num": 15, "glyph": "15 — 十五 (十五号)", "phonetic": "shíwǔ", "gloss": "Number 15", "speakText": "十五", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-shíwǔ.ogg", "whisper": "10 + 5 = 15. In dates, attach 号 (hào) for spoken or 日 (rì) for written."},
        {"id": "zh_n20", "type": "date_num", "num": 20, "glyph": "20 — 二十", "phonetic": "èrshí", "gloss": "Number 20", "speakText": "二十", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-èrshí.ogg", "whisper": "2 × 10 = 二十 (20)."},
        {"id": "zh_n21", "type": "date_num", "num": 21, "glyph": "21 — 二十一", "phonetic": "èrshíyī", "gloss": "Number 21", "speakText": "二十一", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-èrshíyī.ogg", "whisper": "2 × 10 + 1 = 二十一 (21)."},
        {"id": "zh_n30", "type": "date_num", "num": 30, "glyph": "30 — 三十", "phonetic": "sānshí", "gloss": "Number 30", "speakText": "三十", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-sānshí.ogg", "whisper": "3 × 10 = 三十 (30)."},
        {"id": "zh_n31", "type": "date_num", "num": 31, "glyph": "31 — 三十一", "phonetic": "sānshíyī", "gloss": "Number 31", "speakText": "三十一", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Zh-sānshíyī.ogg", "whisper": "3 × 10 + 1 = 三十一 (31)."}
    ],
    "earGym": [
        {
            "prompt": "Listen to the festival date. Which historic celebration was spoken?",
            "speakAudio": "八月十五号",
            "options": ["August 15 (八月十五号 — Mid-Autumn Festival)", "August 5 (八月五号)", "July 15 (七月十五号)"],
            "correct": 0,
            "explain": "'八月十五号' is the full-moon Mid-Autumn Festival."
        },
        {
            "prompt": "Listen to the month name. Is it April (4) or October (10)?",
            "speakAudio": "十月",
            "options": ["October (十月 — shíyuè, 2nd tone)", "April (四月 — sìyuè, 4th tone)", "July (七月 — qīyuè)"],
            "correct": 0,
            "explain": "'十月' (shíyuè) has the rising 2nd tone, meaning October (10th month)."
        },
        {
            "prompt": "Listen to the question. What does Master Lao ask?",
            "speakAudio": "今天几月几号",
            "options": ["What is today's date? (Jīntiān jǐ yuè jǐ hào?)", "What time is it?", "How many months? (几月)"],
            "correct": 0,
            "explain": "'几月几号' (jǐ yuè jǐ hào) is the natural idiom to ask 'which month, which day?'"
        }
    ],
    "sundial": [
        {
            "quest": "Mid-Autumn Moon Festival (中秋节)",
            "clue": "Master Lao: 'Set the moon calendar to August 15 (八月十五号)!'",
            "targetMonthIdx": 7,
            "targetDay": 15,
            "displayMonth": "八月",
            "explain": "八月十五号 is the night of the round full moon and mooncakes."
        },
        {
            "quest": "New Year's Day (元旦)",
            "clue": "Master Lao: 'Mark January 1 (一月一日)!'",
            "targetMonthIdx": 0,
            "targetDay": 1,
            "displayMonth": "一月",
            "explain": "一月一日 is the first day of the new calendar year."
        },
        {
            "quest": "National Day (国庆节)",
            "clue": "Master Lao: 'Mark October 1 (十月一日)!'",
            "targetMonthIdx": 9,
            "targetDay": 1,
            "displayMonth": "十月",
            "explain": "十月一日 commemorates National Day."
        }
    ],
    "scribe": [
        {"clue": "Assemble the month of January in characters:", "tiles": ["一", "月", "二", "十"], "answer": "一月", "gloss": "一月 (January)"},
        {"clue": "Assemble the month of August:", "tiles": ["八", "月", "日", "号"], "answer": "八月", "gloss": "八月 (August)"},
        {"clue": "Assemble the date number 15 + day marker (号):", "tiles": ["十", "五", "号", "月", "年"], "answer": "十五号", "gloss": "十五号 (15th day)"}
    ],
    "quiz": [
        {
            "q": "What is the standard order for expressing full dates in Chinese?",
            "options": [
                "Year $\\to$ Month $\\to$ Day (年 $\\to$ 月 $\\to$ 日/号), going from largest to smallest unit!",
                "Day $\\to$ Month $\\to$ Year",
                "Month $\\to$ Day $\\to$ Year"
            ],
            "correct": 0,
            "explain": "Chinese date logic strictly proceeds from largest to smallest (Year, Month, Day)."
        },
        {
            "q": "How do you form the names of all 12 calendar months in Mandarin?",
            "options": [
                "Simply take digits 1–12 and add '月' (yuè): 一月, 二月, 三月... 十二月!",
                "Each month has a completely unique mythological name",
                "By adding '天' (tiān)"
            ],
            "correct": 0,
            "explain": "Months are 100% regular in Chinese: 1–12 followed by 月 (yuè)."
        },
        {
            "q": "In casual spoken Chinese, which word is preferred for 'day of the month': '号' (hào) or '日' (rì)?",
            "options": [
                "号 (hào) is preferred in speech; 日 (rì) is more formal and written",
                "日 is only for weekends",
                "They are never used with numbers"
            ],
            "correct": 0,
            "explain": "Spoken Chinese almost always says '几月几号' (jǐ yuè jǐ hào)."
        },
        {
            "q": "Which character for 'two' is used when naming the month of February?",
            "options": ["二 (èr — 二月)", "两 (liǎng)", "双 (shuāng)"],
            "correct": 0,
            "explain": "二 (èr) is used for months (二月) and dates (二号)."
        },
        {
            "q": "How do you ask 'What is today's date?' in Mandarin?",
            "options": [
                "今天几月几号? (Jīntiān jǐ yuè jǐ hào?)",
                "你在哪里? (Nǐ zài nǎlǐ?)",
                "你叫什么名字? (Nǐ jiào shénme míngzì?)"
            ],
            "correct": 0,
            "explain": "'今天几月几号?' literally asks 'Today which month which day?'"
        }
    ]
}

GERMAN_STEP2 = {
    "sealName": "Kaiserwald Eichenkalender Seal",
    "timekeeper": {
        "name": "Bäcker Hans",
        "role": "Berlin Master Baker & Almanac Keeper",
        "avatar": "📅",
        "prompt": "Guten Tag! Mark the seasonal baker holidays and festival dates on the German calendar."
    },
    "cards": [
        {"id": "de_m1", "type": "month", "monthNum": 1, "glyph": "Januar", "phonetic": "[ˈjanu̯aːɐ̯]", "gloss": "January • 31 Tage", "speakText": "Januar", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Januar.ogg", "whisper": "Initial 'J' is pronounced like English 'Y': [ˈjanu̯aːɐ̯]."},
        {"id": "de_m2", "type": "month", "monthNum": 2, "glyph": "Februar", "phonetic": "[ˈfeːbʁuaːɐ̯]", "gloss": "February • 28/29 Tage", "speakText": "Februar", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Februar.ogg", "whisper": "Initial 'F' with long 'e'."},
        {"id": "de_m3", "type": "month", "monthNum": 3, "glyph": "März", "phonetic": "[mɛʁts]", "gloss": "March • 31 Tage", "speakText": "März", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-März.ogg", "whisper": "Features the Umlaut 'ä' and crisp 'z' [ts]."},
        {"id": "de_m4", "type": "month", "monthNum": 4, "glyph": "April", "phonetic": "[aˈpʁɪl]", "gloss": "April • 30 Tage", "speakText": "April", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-April.ogg", "whisper": "'April, April, der weiß nicht, was er will!' (famous weather proverb)."},
        {"id": "de_m5", "type": "month", "monthNum": 5, "glyph": "Mai", "phonetic": "[maɪ]", "gloss": "May • 31 Tage", "speakText": "Mai", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Mai.ogg", "whisper": "'ai' sounds like 'eye' [aɪ]. Month of Maibaum festivals."},
        {"id": "de_m6", "type": "month", "monthNum": 6, "glyph": "Juni", "phonetic": "[ˈjuːni]", "gloss": "June • 30 Tage", "speakText": "Juni", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Juni.ogg", "whisper": "To prevent confusion with 'Juli' on the radio or phone, Germans often say 'Juno'!"},
        {"id": "de_m7", "type": "month", "monthNum": 7, "glyph": "Juli", "phonetic": "[ˈjuːli]", "gloss": "July • 31 Tage", "speakText": "Juli", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Juli.ogg", "whisper": "On the radio or phone, often spoken as 'Julei' to distinguish from Juni!"},
        {"id": "de_m8", "type": "month", "monthNum": 8, "glyph": "August", "phonetic": "[aʊ̯ˈɡʊst]", "gloss": "August • 31 Tage", "speakText": "August", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-August.ogg", "whisper": "Stress on the second syllable: au-GUST."},
        {"id": "de_m9", "type": "month", "monthNum": 9, "glyph": "September", "phonetic": "[zɛpˈtɛmbɐ]", "gloss": "September • 30 Tage", "speakText": "September", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-September.ogg", "whisper": "Initial 'S' is voiced buzzing [z]. Month of Oktoberfest kick-off!"},
        {"id": "de_m10", "type": "month", "monthNum": 10, "glyph": "Oktober", "phonetic": "[ɔkˈtoːbɐ]", "gloss": "October • 31 Tage", "speakText": "Oktober", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Oktober.ogg", "whisper": "German Unity Day (Tag der Deutschen Einheit) is celebrated am 3. Oktober."},
        {"id": "de_m11", "type": "month", "monthNum": 11, "glyph": "November", "phonetic": "[noˈvɛmbɐ]", "gloss": "November • 30 Tage", "speakText": "November", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-November.ogg", "whisper": "Features 'v' pronounced [v] in this Latin loanword."},
        {"id": "de_m12", "type": "month", "monthNum": 12, "glyph": "Dezember", "phonetic": "[deˈtsɛmbɐ]", "gloss": "December • 31 Tage", "speakText": "Dezember", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-Dezember.ogg", "whisper": "'Z' is crisp [ts]. Month of Weihnachtsmarkt and St. Nikolaus."},
        {"id": "de_n11", "type": "date_num", "num": 11, "glyph": "11 — elf", "phonetic": "[ɛlf]", "gloss": "Number 11", "speakText": "elf", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-elf.ogg", "whisper": "Short Germanic root 'elf'."},
        {"id": "de_n12", "type": "date_num", "num": 12, "glyph": "12 — zwölf", "phonetic": "[tsvœlf]", "gloss": "Number 12", "speakText": "zwölf", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-zwölf.ogg", "whisper": "Z=[ts], W=[v], plus Umlaut 'ö' [œ]!"},
        {"id": "de_n13", "type": "date_num", "num": 13, "glyph": "13 — dreizehn", "phonetic": "[ˈdʁaɪ̯tseːn]", "gloss": "Number 13", "speakText": "dreizehn", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-dreizehn.ogg", "whisper": "drei + zehn = dreizehn (13)."},
        {"id": "de_n20", "type": "date_num", "num": 20, "glyph": "20 — zwanzig", "phonetic": "[ˈtsvantsɪç]", "gloss": "Number 20", "speakText": "zwanzig", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-zwanzig.ogg", "whisper": "Ends in '-ig', pronounced like a soft palate hiss [ɪç] in standard German."},
        {"id": "de_n21", "type": "date_num", "num": 21, "glyph": "21 — einundzwanzig", "phonetic": "[ˈaɪ̯n.ʊnt.tsvantsɪç]", "gloss": "Number 21", "speakText": "einundzwanzig", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-einundzwanzig.ogg", "whisper": "The famous German 'ones-before-tens' rule: ONE-AND-TWENTY (ein-und-zwanzig)!"},
        {"id": "de_n30", "type": "date_num", "num": 30, "glyph": "30 — dreißig", "phonetic": "[ˈdʁaɪ̯sɪç]", "gloss": "Number 30", "speakText": "dreißig", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-dreißig.ogg", "whisper": "Notice it uses 'ß' (dreißig), unlike zwanzig or vierzig which use 'z'!"},
        {"id": "de_n31", "type": "date_num", "num": 31, "glyph": "31 — einunddreißig", "phonetic": "[ˈaɪ̯n.ʊnt.dʁaɪ̯sɪç]", "gloss": "Number 31", "speakText": "einunddreißig", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-einunddreißig.ogg", "whisper": "One-and-thirty (31)."}
    ],
    "earGym": [
        {
            "prompt": "Listen to the national holiday date. Which German historic day was spoken?",
            "speakAudio": "am dritten Oktober",
            "options": ["October 3rd (am dritten Oktober — Unity Day)", "October 13th (am dreizehnten)", "November 3rd"],
            "correct": 0,
            "explain": "'am dritten Oktober' is the Day of German Unity (Tag der Deutschen Einheit)."
        },
        {
            "prompt": "Listen closely. Is the number 13 (dreizehn) or 30 (dreißig)?",
            "speakAudio": "dreizehn",
            "options": ["13 (dreizehn — ends in -zehn)", "30 (dreißig — ends in -ßig)", "3 (drei)"],
            "correct": 0,
            "explain": "'dreizehn' ends with '-zehn' (10), while 'dreißig' ends in '-ßig'."
        },
        {
            "prompt": "Listen to the summer month. Is it Juni or Juli?",
            "speakAudio": "Juni",
            "options": ["June (Juni — ends in -ni)", "July (Juli — ends in -li)", "January (Januar)"],
            "correct": 0,
            "explain": "'Juni' ends with 'n', while 'Juli' ends with 'l'."
        }
    ],
    "sundial": [
        {
            "quest": "Tag der Deutschen Einheit (German Unity Day)",
            "clue": "Hans: 'Set the Berlin calendar to October 3 (am 3. Oktober)!'",
            "targetMonthIdx": 9,
            "targetDay": 3,
            "displayMonth": "Oktober",
            "explain": "Am 3. Oktober commemorates the reunification of Germany in 1990."
        },
        {
            "quest": "Neujahr (New Year's Day)",
            "clue": "Hans: 'Mark the first of January (am 1. Januar)!'",
            "targetMonthIdx": 0,
            "targetDay": 1,
            "displayMonth": "Januar",
            "explain": "Am ersten Januar begins the new year."
        },
        {
            "quest": "Heiligabend (Christmas Eve)",
            "clue": "Hans: 'Mark December 24 (am 24. Dezember)!'",
            "targetMonthIdx": 11,
            "targetDay": 24,
            "displayMonth": "Dezember",
            "explain": "Am vierundzwanzigsten Dezember is Christmas Eve in Germany."
        }
    ],
    "scribe": [
        {"clue": "Assemble the month of March (with the Umlaut!):", "tiles": ["M", "Ä", "R", "Z", "S", "T"], "answer": "MÄRZ", "gloss": "März (March)"},
        {"clue": "Assemble the month of October:", "tiles": ["O", "K", "T", "O", "B", "E", "R"], "answer": "OKTOBER", "gloss": "Oktober (October)"},
        {"clue": "Assemble the number 20:", "tiles": ["Z", "W", "A", "N", "Z", "I", "G"], "answer": "ZWANZIG", "gloss": "zwanzig (20)"}
    ],
    "quiz": [
        {
            "q": "How are compound numbers like 21 formed in German?",
            "options": [
                "Units before tens connected by 'und': einundzwanzig (literally 'one-and-twenty')!",
                "Tens before units: zwanzigeins",
                "Using separate words with hyphens"
            ],
            "correct": 0,
            "explain": "German uses the 'units-and-tens' structure for all numbers 21–99 (einundzwanzig, zweiundzwanzig)."
        },
        {
            "q": "Which preposition and case ending are used when stating dates in German (e.g. 'on the 3rd of October')?",
            "options": [
                "The dative contraction 'am' (= an dem) + ordinal suffix '-ten': am dritten Oktober!",
                "The preposition 'in' + nominative",
                "No preposition is used"
            ],
            "correct": 0,
            "explain": "'am' (an dem) triggers the dative case on the ordinal number: am ersten, am dritten, am zwanzigsten."
        },
        {
            "q": "Why do German speakers sometimes say 'Juno' and 'Julei' on telephone or radio broadcasts?",
            "options": [
                "To clearly distinguish 'Juni' (June) and 'Juli' (July), which sound dangerously similar over audio!",
                "Because they are archaic dialect words",
                "It is a legal requirement"
            ],
            "correct": 0,
            "explain": "Juni and Juli differ by only one consonant, so 'Juno' and 'Julei' eliminate ambiguity."
        },
        {
            "q": "How does the spelling of 'dreißig' (30) differ from 'zwanzig' (20) and 'vierzig' (40)?",
            "options": [
                "dreißig uses the Eszett 'ß', while other tens end in '-zig' with a 'z'!",
                "dreißig is spelled with double 's'",
                "There is no difference"
            ],
            "correct": 0,
            "explain": "dreißig is unique among the tens in keeping '-ßig' instead of '-zig'."
        },
        {
            "q": "How is the letter 'J' pronounced in the German months 'Januar', 'Juni', and 'Juli'?",
            "options": [
                "Like an English 'Y' [j] as in 'yes' ([ˈjanu̯aːɐ̯], [ˈjuːni])",
                "Like an English 'J' [dʒ]",
                "Like a French 'J' [ʒ]"
            ],
            "correct": 0,
            "explain": "German 'J' is always pronounced like an English 'Y' [j]."
        }
    ]
}

print("HEBREW_STEP2, CHINESE_STEP2, GERMAN_STEP2 defined.")

