#!/usr/bin/env python3
"""
Step 2 Datasets for French, Latin, Hebrew, Chinese, German
"""

FRENCH_STEP2 = {
    "sealName": "Lumière Solaire Calendar Seal",
    "timekeeper": {
        "name": "Madame Claudine",
        "role": "Parisian Almanac Keeper",
        "avatar": "📅",
        "prompt": "Bonjour ! Set dates on the Paris calendar for national celebrations and seasonal solstices."
    },
    "cards": [
        {"id": "fr_m1", "type": "month", "monthNum": 1, "glyph": "janvier", "phonetic": "[ʒɑ̃.vje]", "gloss": "January • 31 jours", "speakText": "janvier", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-janvier.ogg", "whisper": "Months are NOT capitalized in French: 'en janvier' (in January)."},
        {"id": "fr_m2", "type": "month", "monthNum": 2, "glyph": "février", "phonetic": "[fe.vʁi.je]", "gloss": "February • 28/29 jours", "speakText": "février", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-février.ogg", "whisper": "Notice the acute accent on 'é': [fe.vʁi.je]."},
        {"id": "fr_m3", "type": "month", "monthNum": 3, "glyph": "mars", "phonetic": "[maʁs]", "gloss": "March • 31 jours", "speakText": "mars", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-mars.ogg", "whisper": "Final 's' is clearly pronounced: [maʁs]."},
        {"id": "fr_m4", "type": "month", "monthNum": 4, "glyph": "avril", "phonetic": "[a.vʁil]", "gloss": "April • 30 jours", "speakText": "avril", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-avril.ogg", "whisper": "Features the 'Poisson d'avril' (April Fools tradition)."},
        {"id": "fr_m5", "type": "month", "monthNum": 5, "glyph": "mai", "phonetic": "[mɛ]", "gloss": "May • 31 jours", "speakText": "mai", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-mai.ogg", "whisper": "Pronounced with open 'ai' [mɛ], rhyming with 'café lait'."},
        {"id": "fr_m6", "type": "month", "monthNum": 6, "glyph": "juin", "phonetic": "[ʒwɛ̃]", "gloss": "June • 30 jours", "speakText": "juin", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-juin.ogg", "whisper": "Features nasal vowel [ɛ̃]: [ʒwɛ̃]."},
        {"id": "fr_m7", "type": "month", "monthNum": 7, "glyph": "juillet", "phonetic": "[ʒɥi.jɛ]", "gloss": "July • 31 jours", "speakText": "juillet", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-juillet.ogg", "whisper": "'ill' makes the palatal glide [j]: zhoo-ee-yay. Month of Bastille Day (14 juillet)."},
        {"id": "fr_m8", "type": "month", "monthNum": 8, "glyph": "août", "phonetic": "[u] / [ut]", "gloss": "August • 31 jours", "speakText": "août", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-août.ogg", "whisper": "Surprise: spelled with 4 letters but pronounced simply [u] or [ut]!"},
        {"id": "fr_m9", "type": "month", "monthNum": 9, "glyph": "septembre", "phonetic": "[sɛp.tɑ̃bʁ]", "gloss": "September • 30 jours", "speakText": "septembre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-septembre.ogg", "whisper": "Contains the nasal vowel 'em' [ɑ̃]."},
        {"id": "fr_m10", "type": "month", "monthNum": 10, "glyph": "octobre", "phonetic": "[ɔk.tɔbʁ]", "gloss": "October • 31 jours", "speakText": "octobre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-octobre.ogg", "whisper": "Crisp [k] and uvular [ʁ]."},
        {"id": "fr_m11", "type": "month", "monthNum": 11, "glyph": "novembre", "phonetic": "[nɔ.vɑ̃bʁ]", "gloss": "November • 30 jours", "speakText": "novembre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-novembre.ogg", "whisper": "Nasal 'em' [ɑ̃]."},
        {"id": "fr_m12", "type": "month", "monthNum": 12, "glyph": "décembre", "phonetic": "[de.sɑ̃bʁ]", "gloss": "December • 31 jours", "speakText": "décembre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-décembre.ogg", "whisper": "Acute 'é' gives bright [e]."},
        {"id": "fr_n11", "type": "date_num", "num": 11, "glyph": "11 — onze", "phonetic": "[ɔ̃z]", "gloss": "Number 11", "speakText": "onze", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-onze.ogg", "whisper": "No liaison or elision with 'onze': 'le onze mai' (never 'l'onze')!"},
        {"id": "fr_n12", "type": "date_num", "num": 12, "glyph": "12 — douze", "phonetic": "[duz]", "gloss": "Number 12", "speakText": "douze", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-douze.ogg", "whisper": "'ou' makes the [u] sound."},
        {"id": "fr_n14", "type": "date_num", "num": 14, "glyph": "14 — quatorze", "phonetic": "[ka.tɔʁz]", "gloss": "Number 14", "speakText": "quatorze", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-quatorze.ogg", "whisper": "The famous date: 'le quatorze juillet' (Fête nationale)."},
        {"id": "fr_n20", "type": "date_num", "num": 20, "glyph": "20 — vingt", "phonetic": "[vɛ̃]", "gloss": "Number 20", "speakText": "vingt", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-vingt.ogg", "whisper": "The final 'gt' is silent standalone ([vɛ̃]), but links as [t] in 21–29!"},
        {"id": "fr_n21", "type": "date_num", "num": 21, "glyph": "21 — vingt et un", "phonetic": "[vɛ̃.t‿e.œ̃]", "gloss": "Number 21", "speakText": "vingt et un", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-vingt_et_un.ogg", "whisper": "Uses the linker 'et': vingt ET un (21). All others use hyphens (vingt-deux)."},
        {"id": "fr_n30", "type": "date_num", "num": 30, "glyph": "30 — trente", "phonetic": "[tʁɑ̃t]", "gloss": "Number 30", "speakText": "trente", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-trente.ogg", "whisper": "Nasal 'en' [ɑ̃]."},
        {"id": "fr_n31", "type": "date_num", "num": 31, "glyph": "31 — trente et un", "phonetic": "[tʁɑ̃.t‿e.œ̃]", "gloss": "Number 31", "speakText": "trente et un", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-trente_et_un.ogg", "whisper": "Like 21, uses 'et': trente et un (31)."}
    ],
    "earGym": [
        {
            "prompt": "Listen to the date. Which French national holiday is mentioned?",
            "speakAudio": "le quatorze juillet",
            "options": ["July 14 (le 14 juillet — Bastille Day)", "June 14 (le 14 juin)", "July 4 (le 4 juillet)"],
            "correct": 0,
            "explain": "'le quatorze juillet' is France's National Day (Bastille Day)."
        },
        {
            "prompt": "Listen to the month. Which one is spoken?",
            "speakAudio": "août",
            "options": ["August (août — pronounced [u] or [ut])", "April (avril)", "May (mai)"],
            "correct": 0,
            "explain": "'août' is pronounced simply [u] or [ut]!"
        },
        {
            "prompt": "Listen to the date. Is it the first of May or second?",
            "speakAudio": "le premier mai",
            "options": ["May 1st (le premier mai)", "May 2nd (le deux mai)", "May 10th (le dix mai)"],
            "correct": 0,
            "explain": "French uses 'premier' ONLY for the 1st day of the month; all other days use regular cardinal numbers!"
        }
    ],
    "sundial": [
        {
            "quest": "Fête Nationale (Bastille Day)",
            "clue": "Madame Claudine: 'Set the Paris calendar to July 14 (le 14 juillet)!'",
            "targetMonthIdx": 6,
            "targetDay": 14,
            "displayMonth": "juillet",
            "explain": "Le 14 juillet commemorates the storming of the Bastille."
        },
        {
            "quest": "Jour de l'An (New Year)",
            "clue": "Madame Claudine: 'Mark the first of January (le premier janvier)!'",
            "targetMonthIdx": 0,
            "targetDay": 1,
            "displayMonth": "janvier",
            "explain": "The 1st of the month always uses 'le premier'."
        },
        {
            "quest": "Fête de la Musique (Summer Solstice)",
            "clue": "Madame Claudine: 'Mark June 21 (le 21 juin) for the music festival!'",
            "targetMonthIdx": 5,
            "targetDay": 21,
            "displayMonth": "juin",
            "explain": "Le 21 juin fills the streets of France with live music."
        }
    ],
    "scribe": [
        {"clue": "Assemble the month of February:", "tiles": ["F", "É", "V", "R", "I", "E", "R"], "answer": "FÉVRIER", "gloss": "février (February)"},
        {"clue": "Assemble the tricky 4-letter month of August:", "tiles": ["A", "O", "Û", "T", "E", "S"], "answer": "AOÛT", "gloss": "août (August)"},
        {"clue": "Assemble the number 20:", "tiles": ["V", "I", "N", "G", "T", "E"], "answer": "VINGT", "gloss": "vingt (20)"}
    ],
    "quiz": [
        {
            "q": "How is the 1st day of the month phrased in French compared to the remaining days?",
            "options": [
                "Only the 1st uses the ordinal 'le premier' (e.g. le premier mai); all other days use cardinal numbers (le deux mai, le trois mai)!",
                "All days use ordinals (le premier, le deuxième, le troisième)",
                "No articles are used"
            ],
            "correct": 0,
            "explain": "French uniquely reserves 'premier' for day 1, using regular cardinal digits for 2–31."
        },
        {
            "q": "Are month names capitalized in standard French sentences?",
            "options": [
                "No, months are written in lowercase (e.g. en janvier, le 14 juillet)",
                "Yes, always capitalized like in English",
                "Only during leap years"
            ],
            "correct": 0,
            "explain": "In French, days of the week and months of the year are not capitalized."
        },
        {
            "q": "How is the month name 'août' (August) pronounced?",
            "options": [
                "[u] or [ut] — a short, clean sound",
                "[a-o-u-t] pronouncing every letter",
                "[aw-oot]"
            ],
            "correct": 0,
            "explain": "'août' is pronounced simply as [u] or [ut]."
        },
        {
            "q": "How do you form 21 ('vingt et un') versus 22 ('vingt-deux')?",
            "options": [
                "21 uses the linker 'et' (vingt et un); 22–29 use hyphens (vingt-deux, vingt-trois)",
                "Both use 'et'",
                "Both use hyphens without 'et'"
            ],
            "correct": 0,
            "explain": "Numbers ending in 1 (21, 31, 41...) take 'et un', while others use hyphens."
        },
        {
            "q": "Which preposition expresses 'in' a given month (e.g. 'in July')?",
            "options": ["en (en juillet)", "à", "dans le"],
            "correct": 0,
            "explain": "'en' is the standard temporal preposition for months: en janvier, en juillet."
        }
    ]
}

LATIN_STEP2 = {
    "sealName": "Fasti Romani Calendar Seal",
    "timekeeper": {
        "name": "Marcus",
        "role": "Forum Romanum Pontifex & Timekeeper",
        "avatar": "🏛️",
        "prompt": "Salvē! Inscribe the Kalends, Nones, and Ides onto the ancient Roman Fastī stone."
    },
    "cards": [
        {"id": "lat_m1", "type": "month", "monthNum": 1, "glyph": "Iānuārius", "phonetic": "[jaː.nuˈaː.rɪ.ʊs]", "gloss": "January • Month of Janus", "speakText": "Ianuarius", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Ianuarius.ogg", "whisper": "Named for Janus, two-faced god of beginnings and doorways looking to past & future."},
        {"id": "lat_m2", "type": "month", "monthNum": 2, "glyph": "Februārius", "phonetic": "[fɛ.bruˈaː.rɪ.ʊs]", "gloss": "February • Month of Purification", "speakText": "Februarius", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Februarius.ogg", "whisper": "From 'februa' (instruments of ritual purification)."},
        {"id": "lat_m3", "type": "month", "monthNum": 3, "glyph": "Martius", "phonetic": "[ˈmar.tɪ.ʊs]", "gloss": "March • Month of Mars", "speakText": "Martius", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Martius.ogg", "whisper": "Originally month 1 of the earliest Roman calendar! Named for Mars, god of war & agriculture."},
        {"id": "lat_m4", "type": "month", "monthNum": 4, "glyph": "Aprīlis", "phonetic": "[aˈpriː.lɪs]", "gloss": "April • 'The Opening'", "speakText": "Aprilis", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Aprilis.ogg", "whisper": "From 'aperīre' (to open, as spring blossoms open)."},
        {"id": "lat_m5", "type": "month", "monthNum": 5, "glyph": "Maius", "phonetic": "[ˈma.jʊs]", "gloss": "May • Month of Maia", "speakText": "Maius", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Maius.ogg", "whisper": "Named for the goddess Maia, mother of Mercury."},
        {"id": "lat_m6", "type": "month", "monthNum": 6, "glyph": "Iūnius", "phonetic": "[ˈjuː.nɪ.ʊs]", "gloss": "June • Month of Juno", "speakText": "Iunius", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Iunius.ogg", "whisper": "Named for Juno, queen of the gods and protector of marriage."},
        {"id": "lat_m7", "type": "month", "monthNum": 7, "glyph": "Iūlius", "phonetic": "[ˈjuː.lɪ.ʊs]", "gloss": "July • Julius Caesar", "speakText": "Iulius", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Iulius.ogg", "whisper": "Originally 'Quīntīlis' (5th month); renamed in honor of Julius Caesar after his calendar reform!"},
        {"id": "lat_m8", "type": "month", "monthNum": 8, "glyph": "Augustus", "phonetic": "[au̯ˈɡʊs.tʊs]", "gloss": "August • Emperor Augustus", "speakText": "Augustus", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-Augustus.ogg", "whisper": "Originally 'Sextīlis' (6th month); renamed for Rome's first emperor Augustus."},
        {"id": "lat_m9", "type": "month", "monthNum": 9, "glyph": "September", "phonetic": "[sɛpˈtɛm.bɛr]", "gloss": "September • 7th Roman Month", "speakText": "September", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-September.ogg", "whisper": "From 'septem' (7)! Preserves its ancient place when March was Month 1."},
        {"id": "lat_m10", "type": "month", "monthNum": 10, "glyph": "Octōber", "phonetic": "[ɔkˈtoː.bɛr]", "gloss": "October • 8th Roman Month", "speakText": "October", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-October.ogg", "whisper": "From 'octō' (8)."},
        {"id": "lat_m11", "type": "month", "monthNum": 11, "glyph": "November", "phonetic": "[nɔˈwɛm.bɛr]", "gloss": "November • 9th Roman Month", "speakText": "November", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-November.ogg", "whisper": "From 'novem' (9)."},
        {"id": "lat_m12", "type": "month", "monthNum": 12, "glyph": "December", "phonetic": "[dɛˈkɛm.bɛr]", "gloss": "December • 10th Roman Month", "speakText": "December", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-December.ogg", "whisper": "From 'decem' (10)."},
        {"id": "lat_n11", "type": "date_num", "num": 11, "glyph": "XI — ūndecim", "phonetic": "[ˈuːn.dɛ.kɪm]", "gloss": "Number 11", "speakText": "undecim", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-undecim.ogg", "whisper": "ūnus + decem = ūndecim (11)."},
        {"id": "lat_n12", "type": "date_num", "num": 12, "glyph": "XII — duodecim", "phonetic": "[dʊˈɔ.dɛ.kɪm]", "gloss": "Number 12", "speakText": "duodecim", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-duodecim.ogg", "whisper": "duo + decem = duodecim (12)."},
        {"id": "lat_n15", "type": "date_num", "num": 15, "glyph": "XV — quīndecim", "phonetic": "[ˈkwiːn.dɛ.kɪm]", "gloss": "Number 15", "speakText": "quindecim", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-quindecim.ogg", "whisper": "quīnque + decem = quīndecim. Day of the Ides in March, May, July, October!"},
        {"id": "lat_n18", "type": "date_num", "num": 18, "glyph": "XVIII — duodēvīgintī", "phonetic": "[dʊ.ɔ.deː.wiːˈɡɪn.tiː]", "gloss": "Number 18", "speakText": "duodeviginti", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-duodeviginti.ogg", "whisper": "Notice Roman subtraction: 'two from twenty'!"},
        {"id": "lat_n19", "type": "date_num", "num": 19, "glyph": "XIX — ūndēvīgintī", "phonetic": "[uːn.deː.wiːˈɡɪn.tiː]", "gloss": "Number 19", "speakText": "undeviginti", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-undeviginti.ogg", "whisper": "'one from twenty' = 19."},
        {"id": "lat_n20", "type": "date_num", "num": 20, "glyph": "XX — vīgintī", "phonetic": "[wiːˈɡɪn.tiː]", "gloss": "Number 20", "speakText": "viginti", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-viginti.ogg", "whisper": "Remember 'v' sounds like [w]: [wiːˈɡɪn.tiː]."},
        {"id": "lat_n31", "type": "date_num", "num": 31, "glyph": "XXXI — trīgintā ūnus", "phonetic": "[triːˈɡɪn.taː ˈuː.nʊs]", "gloss": "Number 31", "speakText": "triginta unus", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/La-cls-triginta_unus.ogg", "whisper": "Thirty-one. Final day in Roman full months."}
    ],
    "earGym": [
        {
            "prompt": "Listen to the famous Roman date. Which historic day was spoken?",
            "speakAudio": "Idus Martiae",
            "options": ["March 15 (Īdūs Martiae — Ides of March)", "March 1 (Kalendae Martiae)", "May 15 (Idus Maiae)"],
            "correct": 0,
            "explain": "'Īdūs Martiae' is the 15th of March, famous in Shakespeare and Roman history."
        },
        {
            "prompt": "Listen to the Roman month. Which month is it?",
            "speakAudio": "Ianuarius",
            "options": ["January (Iānuārius)", "June (Iūnius)", "July (Iūlius)"],
            "correct": 0,
            "explain": "'Iānuārius' begins with consonantal 'I' [j] sounding like 'Y': [jaː.nuˈaː.rɪ.ʊs]."
        },
        {
            "prompt": "Listen to the subtractive Latin number. Is it 18 or 19?",
            "speakAudio": "duodeviginti",
            "options": ["18 (duodēvīgintī — 2 from 20)", "19 (ūndēvīgintī — 1 from 20)", "20 (vīgintī)"],
            "correct": 0,
            "explain": "'duodēvīgintī' means literally 'two-from-twenty' (18)."
        }
    ],
    "sundial": [
        {
            "quest": "The Ides of March",
            "clue": "Marcus: 'Mark the Ides of March (Īdūs Martiae — March 15) on the Fastī!'",
            "targetMonthIdx": 2,
            "targetDay": 15,
            "displayMonth": "Martius",
            "explain": "The Ides fell on the 15th in March, May, July, and October."
        },
        {
            "quest": "The Kalends of January",
            "clue": "Marcus: 'Mark Kalendae Iānuāriae (January 1) for the new Roman consuls!'",
            "targetMonthIdx": 0,
            "targetDay": 1,
            "displayMonth": "Iānuārius",
            "explain": "Kalendae (the 1st of every month) is the root of our modern word 'calendar'!"
        },
        {
            "quest": "Festival of Ceres",
            "clue": "Marcus: 'Mark April 19 (Certāmen Cereris — Aprīlis 19)!'",
            "targetMonthIdx": 3,
            "targetDay": 19,
            "displayMonth": "Aprīlis",
            "explain": "April 19 marked the Cereālia festival in ancient Rome."
        }
    ],
    "scribe": [
        {"clue": "Assemble the month of March:", "tiles": ["M", "A", "R", "T", "I", "U", "S"], "answer": "MARTIUS", "gloss": "Martius (March)"},
        {"clue": "Assemble the sacred first day of the Roman month (Kalends):", "tiles": ["K", "A", "L", "E", "N", "D", "A", "E"], "answer": "KALENDAE", "gloss": "Kalendae (Kalends)"},
        {"clue": "Assemble the number 20 (Roman spelling):", "tiles": ["V", "I", "G", "I", "N", "T", "I"], "answer": "VIGINTI", "gloss": "vīgintī (20)"}
    ],
    "quiz": [
        {
            "q": "What were the three pivotal landmark days in the ancient Roman calendar?",
            "options": [
                "Kalendae (1st of month), Nōnae (5th or 7th), and Īdūs (13th or 15th)",
                "Beginning, Middle, and End",
                "Morning, Noon, and Night"
            ],
            "correct": 0,
            "explain": "Romans reckoned days backwards from the Kalends, Nones, and Ides."
        },
        {
            "q": "Why were July and August originally called Quīntīlis and Sextīlis?",
            "options": [
                "Because they were the 5th (quīntus) and 6th (sextus) months in the original 10-month calendar of Romulus!",
                "They were named after constellations",
                "It was purely arbitrary"
            ],
            "correct": 0,
            "explain": "When the year started in March, July was month 5 and August was month 6."
        },
        {
            "q": "How did Romans express the numbers 18 and 19?",
            "options": [
                "Subtractively from 20: duodēvīgintī (2 from 20 = 18) and ūndēvīgintī (1 from 20 = 19)!",
                "Additively: decem et octō",
                "With single Greek loanwords"
            ],
            "correct": 0,
            "explain": "Romans favored subtractive counting before tens (duodēvīgintī = 18)."
        },
        {
            "q": "Which Roman month was named for the two-faced god of gateways and beginnings?",
            "options": ["Iānuārius (Janus)", "Martius (Mars)", "Maius (Maia)"],
            "correct": 0,
            "explain": "Janus had two faces looking forward into the new year and back into the past."
        },
        {
            "q": "On which day did the Ides (Īdūs) fall in March, May, July, and October?",
            "options": ["The 15th day of the month", "The 13th day", "The 1st day"],
            "correct": 0,
            "explain": "In the four long months (March, May, July, October), the Ides fell on the 15th (13th in others)."
        }
    ]
}

print("FRENCH_STEP2 and LATIN_STEP2 defined.")

