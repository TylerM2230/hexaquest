#!/usr/bin/env python3
"""
HexaQuest Step 5 & Step 6 Comprehensive Pedagogical Dataset
===========================================================
Defines complete, linguistically validated datasets for:
- STEP 5: Family Description & Kinship Terms (with possessive modifiers)
- STEP 6: Place to Dialogue (Milestone Checkpoint: Synthesizing Steps 1–5,
          Counting 0–1000, Days of the Week, and Full Authentic Dialogues)

Across all 6 HexaQuest Language Realms:
1. Waray-Waray (Austronesian / Visayan)
2. French (Romance)
3. Latin (Classical Italic)
4. Hebrew (Semitic)
5. Mandarin Chinese (Sinitic)
6. German (West Germanic)
"""

# ==============================================================================
# STEP 5: FAMILY DESCRIPTION (KINSHIP TERMS & POSSESSIVE MODIFIERS)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WARAY-WARAY — STEP 5: BANAY SANGKAY KINSHIP REALM
# ------------------------------------------------------------------------------

WARAY_STEP5 = {
    "sealName": "Banay Sangkay Kinship Knot Seal",
    "guide": {
        "name": "Manang Elena",
        "role": "Village Matriarch & Family Weaver",
        "avatar": "👵",
        "prompt": "Malipayon nga pag-abot ha amon panimalay! In Leyte and Samar, family (pamilya or banay) is the sacred center of life. Discover our kinship terms from nanay and tatay to bugto, magurang, and manghod, paired with possessive genitives akon/nakon, imo/nimo, and iya/niya."
    },
    "cards": [
        {
            "id": "war5_c1",
            "type": "kinship",
            "glyph": "nanay / iroy",
            "phonetic": "[na.ˈnaj] / [ʔi.ˈɾɔj]",
            "gloss": "mother • maternal anchor",
            "speakText": "nanay, iroy",
            "audioUrl": "",
            "whisper": "'Nanay' is the widespread everyday Visayan term for mother; 'iroy' is the poetic, classical Samar-Leyte term celebrated in the regional anthem 'Iroy nga Tuna' (Motherland)."
        },
        {
            "id": "war5_c2",
            "type": "kinship",
            "glyph": "tatay / amay",
            "phonetic": "[ta.ˈtaj] / [ʔa.ˈmaj]",
            "gloss": "father • paternal anchor",
            "speakText": "tatay, amay",
            "audioUrl": "",
            "whisper": "'Tatay' is the familiar term for father; 'amay' is the classical Waray word preserved in religious liturgy ('Amay Namon' = Our Father) and formal literature."
        },
        {
            "id": "war5_c3",
            "type": "kinship",
            "glyph": "bugto",
            "phonetic": "[bʊɡ.ˈtɔʔ]",
            "gloss": "sibling • brother or sister",
            "speakText": "bugto",
            "audioUrl": "",
            "whisper": "Waray kinship is gender-neutral by default! 'Bugto' means sibling of any gender. To specify, add 'nga lalaki' (brother) or 'nga babaye' (sister)."
        },
        {
            "id": "war5_c4",
            "type": "kinship",
            "glyph": "magurang",
            "phonetic": "[ma.ɡʊ.ˈɾaŋ]",
            "gloss": "older sibling / elder",
            "speakText": "magurang",
            "audioUrl": "",
            "whisper": "From root 'gurang' (old/mature). Respect for birth order is paramount: the older sibling carries family responsibility and is addressed with respect as Manong/Manoy or Manang."
        },
        {
            "id": "war5_c5",
            "type": "kinship",
            "glyph": "manghod",
            "phonetic": "[maŋ.ˈhɔd]",
            "gloss": "younger sibling",
            "speakText": "manghod",
            "audioUrl": "",
            "whisper": "Younger brother or younger sister. Eldest siblings take care of the 'manghod' in the tight-knit Visayan household."
        },
        {
            "id": "war5_c6",
            "type": "kinship",
            "glyph": "apohan (lolo / lola)",
            "phonetic": "[ʔa.pɔ.ˈhan]",
            "gloss": "grandparent • ancestor",
            "speakText": "apohan, lolo, lola",
            "audioUrl": "",
            "whisper": "'Apohan' encompasses grandparents generally; familiarly, 'lolo' (grandfather) and 'lola' (grandmother) are universal across Philippine households."
        },
        {
            "id": "war5_c7",
            "type": "kinship",
            "glyph": "anak",
            "phonetic": "[ʔa.ˈnak]",
            "gloss": "child • son or daughter",
            "speakText": "anak",
            "audioUrl": "",
            "whisper": "'Anak' means offspring or child. Parents affectionately say 'an akon anak' (my child). Gender is distinguished as 'anak nga lalaki' (son) and 'anak nga babaye' (daughter)."
        },
        {
            "id": "war5_c8",
            "type": "kinship",
            "glyph": "asawa",
            "phonetic": "[ʔa.ˈsa.wa]",
            "gloss": "spouse • husband or wife",
            "speakText": "asawa",
            "audioUrl": "",
            "whisper": "'Asawa' applies equally to husband and wife. An affectionate Visayan synonym is 'kabuak han kasingkasing' (half of one's heart)."
        },
        {
            "id": "war5_c9",
            "type": "possessive",
            "glyph": "akon / nakon",
            "phonetic": "[ʔa.ˈkɔn] / [na.ˈkɔn]",
            "gloss": "my / mine (preposed vs. enclitic)",
            "speakText": "akon, nakon",
            "audioUrl": "",
            "whisper": "Two ways to say 'my': preposed with topic marker 'an akon nanay' (my mother), or postposed as an enclitic genitive 'an nanay nakon'!"
        },
        {
            "id": "war5_c10",
            "type": "possessive",
            "glyph": "imo / iya (nimo / niya)",
            "phonetic": "[ʔi.ˈmɔ] / [ʔi.ˈja]",
            "gloss": "your / his / her",
            "speakText": "imo, iya, nimo, niya",
            "audioUrl": "",
            "whisper": "Preposed: 'an imo tatay' (your father), 'an iya bugto' (his/her sibling). Postposed: 'an tatay nimo', 'an bugto niya'."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the family phrase. Who is being referred to?",
            "speakAudio": "an akon nanay",
            "options": ["My mother ('an akon nanay')", "My older sister", "My daughter"],
            "correct": 0,
            "explain": "'Akon' (my) + 'nanay' (mother) denotes 'my mother'."
        },
        {
            "prompt": "Listen to the kinship distinction. Is this the older or younger sibling?",
            "speakAudio": "an magurang nakon",
            "options": ["My older sibling ('an magurang nakon')", "My younger sibling ('manghod')", "My grandchild"],
            "correct": 0,
            "explain": "'Magurang' specifically denotes the older sibling in Visayan birth order."
        },
        {
            "prompt": "Listen to the possessive modifier. Whose spouse is spoken of?",
            "speakAudio": "an iya asawa",
            "options": ["His/Her spouse ('an iya asawa')", "My spouse ('akon asawa')", "Your spouse ('imo asawa')"],
            "correct": 0,
            "explain": "'Iya' is the 3rd person singular genitive/possessive pronoun (his/her)."
        },
        {
            "prompt": "Listen to the affectionate address. What relationship is 'manghod'?",
            "speakAudio": "an akon manghod",
            "options": ["My younger sibling", "My grandmother", "My uncle"],
            "correct": 0,
            "explain": "'Manghod' is the younger sibling in Waray-Waray family life."
        }
    ],
    "arena": [
        {
            "quest": "Introduce Your Mother: 'This is my mother'",
            "clue": "Manang Elena: 'Use the demonstrative Ini, focus marker an, and preposed akon nanay!'",
            "target": "Ini an akon nanay",
            "tokens": ["Ini", "an", "akon", "nanay", "tatay", "hiya"],
            "explain": "'Ini' (this) + 'an' (focal case marker) + 'akon' (my) + 'nanay' (mother)."
        },
        {
            "quest": "Describe Sibling Rank: 'He is my older sibling'",
            "clue": "Manang Elena: 'Put the kinship title first, enclitic nakon, then pronoun hiya!'",
            "target": "Magurang nakon hiya",
            "tokens": ["Magurang", "nakon", "hiya", "manghod", "ikaw", "akon"],
            "explain": "'Magurang' (older sibling) + 'nakon' (my) + 'hiya' (he/she)."
        },
        {
            "quest": "Inquire About Family: 'Where is your father?'",
            "clue": "Manang Elena: 'Combine locative interrogative Hain, marker an, and imo tatay!'",
            "target": "Hain an imo tatay",
            "tokens": ["Hain", "an", "imo", "tatay", "diin", "nakon"],
            "explain": "'Hain' (where is [specific entity]) + 'an imo tatay' (your father)."
        },
        {
            "quest": "Affirm Conjugal Bond: 'My spouse is kind'",
            "clue": "Manang Elena: 'Predicate-initial: Buotan an akon asawa!'",
            "target": "Buotan an akon asawa",
            "tokens": ["Buotan", "an", "akon", "asawa", "waray", "hiya"],
            "explain": "'Buotan' (kind/good-natured) + 'an akon asawa' (my spouse)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the Waray word for MOTHER (NANAY):",
            "tiles": ["N", "A", "N", "A", "Y", "O", "T"],
            "answer": "NANAY",
            "gloss": "nanay (mother)"
        },
        {
            "clue": "Spell the Waray gender-neutral term for SIBLING (BUGTO):",
            "tiles": ["B", "U", "G", "T", "O", "A", "R"],
            "answer": "BUGTO",
            "gloss": "bugto (sibling)"
        },
        {
            "clue": "Spell the preposed 1st person possessive MY (AKON):",
            "tiles": ["A", "K", "O", "N", "I", "M"],
            "answer": "AKON",
            "gloss": "akon (my / mine)"
        }
    ],
    "quiz": [
        {
            "q": "What is the crucial cultural distinction between 'magurang' and 'manghod' in Visayan kinship?",
            "options": [
                "'Magurang' denotes an older sibling who commands respect and responsibility; 'manghod' denotes a younger sibling!",
                "'Magurang' is strictly for cousins while 'manghod' is for aunts",
                "'Magurang' means male sibling and 'manghod' means female sibling"
            ],
            "correct": 0,
            "explain": "Waray kinship strictly encodes relative age (birth order) rather than gender: magurang (older) vs. manghod (younger)."
        },
        {
            "q": "How do preposed 'akon' and enclitic 'nakon' differ syntactically when saying 'my father'?",
            "options": [
                "'Akon' precedes the noun with a case marker ('an akon tatay'); 'nakon' follows the noun directly ('an tatay nakon')!",
                "'Akon' is only for food items while 'nakon' is for people",
                "There is no difference and both must be used together in every phrase"
            ],
            "correct": 0,
            "explain": "Visayan genitives have preposed emphatic forms (akon, imo, iya) and postposed enclitic forms (nakon, nimo, niya)."
        },
        {
            "q": "What is the classical, poetic Waray term for 'mother' immortalized in regional heritage?",
            "options": [
                "iroy (as in 'Iroy nga Tuna' — Motherland)",
                "nanay",
                "manang"
            ],
            "correct": 0,
            "explain": "'Iroy' is the deep poetic Waray-Waray term for mother, while 'nanay' is common informal speech."
        },
        {
            "q": "Are basic Waray kinship terms like 'bugto' (sibling) and 'anak' (child) inherently gendered?",
            "options": [
                "No, they are inherently gender-neutral; gender is optionally added with 'nga lalaki' (male) or 'nga babaye' (female)!",
                "Yes, 'bugto' is masculine and 'anak' is feminine",
                "Yes, Waray requires grammatical masculine and feminine noun endings"
            ],
            "correct": 0,
            "explain": "Austronesian languages typically lack grammatical gender; kinship roots like bugto, anak, and asawa apply to all genders."
        },
        {
            "q": "Which respectful honorific titles are traditionally used for elder brothers and elder sisters in Samar and Leyte?",
            "options": [
                "Manong / Manoy for elder brothers, and Manang for elder sisters!",
                "Lolo and Lola",
                "Tiyo and Tiya"
            ],
            "correct": 0,
            "explain": "Manong/Manoy and Manang are ubiquitous Visayan honorifics demonstrating filial respect for elder siblings."
        }
    ]
}

# ------------------------------------------------------------------------------
# 2. FRENCH — STEP 5: LUMIÈRE FAMILIALE KINSHIP REALM
# ------------------------------------------------------------------------------

FRENCH_STEP5 = {
    "sealName": "L'Arbre Généalogique de France Seal",
    "guide": {
        "name": "Madame Claudine",
        "role": "Parisian Genealogist & Family Archivist",
        "avatar": "⚜️",
        "prompt": "Bienvenue dans notre cercle de famille ! In French, kinship is intertwined with the melody of possessives: mon, ma, mes; son, sa, ses. Remember: possessive determiners agree with the gender of the noun possessed, not the possessor!"
    },
    "cards": [
        {
            "id": "fr5_c1",
            "type": "kinship",
            "glyph": "mère (la mère)",
            "phonetic": "[mɛʁ]",
            "gloss": "mother • feminine",
            "speakText": "mère",
            "audioUrl": "",
            "whisper": "Spelled with a grave accent (è): 'la mère'. Affectionately called 'maman' [ma.mɑ̃]."
        },
        {
            "id": "fr5_c2",
            "type": "kinship",
            "glyph": "père (le père)",
            "phonetic": "[pɛʁ]",
            "gloss": "father • masculine",
            "speakText": "père",
            "audioUrl": "",
            "whisper": "Grave accent on 'è': 'le père'. Familiarly called 'papa'."
        },
        {
            "id": "fr5_c3",
            "type": "kinship",
            "glyph": "frère (le frère)",
            "phonetic": "[fʁɛʁ]",
            "gloss": "brother • masculine",
            "speakText": "frère",
            "audioUrl": "",
            "whisper": "'Le frère'. Notice the uvular [ʁ] sound surrounding the vowel: [fʁɛʁ]."
        },
        {
            "id": "fr5_c4",
            "type": "kinship",
            "glyph": "sœur (la sœur)",
            "phonetic": "[sœʁ]",
            "gloss": "sister • feminine",
            "speakText": "sœur",
            "audioUrl": "",
            "whisper": "Features the French ligature 'œ' (e dans l'o): [sœʁ]. Always spelled with 'œu'!"
        },
        {
            "id": "fr5_c5",
            "type": "kinship",
            "glyph": "fils / fille",
            "phonetic": "[fis] / [fij]",
            "gloss": "son / daughter",
            "speakText": "fils, fille",
            "audioUrl": "",
            "whisper": "Pronunciation surprise: in 'fils' (son), the 'l' is silent and 's' is pronounced [fis]! In 'fille' (daughter), 'ill' sounds like the glide 'y' [fij]."
        },
        {
            "id": "fr5_c6",
            "type": "kinship",
            "glyph": "grand-père / grand-mère",
            "phonetic": "[ɡʁɑ̃.pɛʁ] / [ɡʁɑ̃.mɛʁ]",
            "gloss": "grandfather / grandmother",
            "speakText": "grand-père, grand-mère",
            "audioUrl": "",
            "whisper": "Notice that 'grand-mère' historically retains the masculine form 'grand' without an 'e'! Familiarly 'papi' and 'mamie'."
        },
        {
            "id": "fr5_c7",
            "type": "kinship",
            "glyph": "mari / femme",
            "phonetic": "[ma.ʁi] / [fam]",
            "gloss": "husband / wife",
            "speakText": "mari, femme",
            "audioUrl": "",
            "whisper": "'Le mari' (husband) and 'la femme' (wife / woman). Pronunciation note: 'femme' is spelled with 'e' but pronounced [fam]!"
        },
        {
            "id": "fr5_c8",
            "type": "kinship",
            "glyph": "oncle / tante",
            "phonetic": "[ɔ̃kl] / [tɑ̃t]",
            "gloss": "uncle / aunt",
            "speakText": "oncle, tante",
            "audioUrl": "",
            "whisper": "Both feature distinctive nasal vowels: 'oncle' has [ɔ̃], while 'tante' has [ɑ̃]."
        },
        {
            "id": "fr5_c9",
            "type": "possessive",
            "glyph": "mon / ma / mes",
            "phonetic": "[mɔ̃] / [ma] / [me]",
            "gloss": "my (masc. / fem. / plural)",
            "speakText": "mon, ma, mes",
            "audioUrl": "",
            "whisper": "'Mon père' (masc.), 'ma mère' (fem.), 'mes parents' (pl.). Crucial rule: before a feminine noun starting with a vowel, use 'mon' (e.g. 'mon amie') to avoid vowel clash!"
        },
        {
            "id": "fr5_c10",
            "type": "possessive",
            "glyph": "son / sa / ses",
            "phonetic": "[sɔ̃] / [sa] / [se]",
            "gloss": "his / her / its (masc. / fem. / plural)",
            "speakText": "son, sa, ses",
            "audioUrl": "",
            "whisper": "In French, possessives agree with the GENDER OF THE NOUN POSSESSED, not the possessor: 'son père' = his father OR her father; 'sa mère' = his mother OR her mother!"
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the introduction. Who is Madame Claudine presenting?",
            "speakAudio": "Voici mon père et ma mère",
            "options": ["My father and my mother", "My brother and my sister", "My uncle and my aunt"],
            "correct": 0,
            "explain": "'Mon père' (masc. my father) + 'ma mère' (fem. my mother)."
        },
        {
            "prompt": "Listen to the pronunciation of 'fils'. Which family member is it?",
            "speakAudio": "C'est mon fils",
            "options": ["My son ('fils' pronounced [fis])", "My daughter ('fille')", "My sister ('sœur')"],
            "correct": 0,
            "explain": "'Fils' is pronounced [fis] with a silent 'l' and audible 's', meaning 'son'."
        },
        {
            "prompt": "Listen to the possessive agreement: 'sa sœur'. Who does this refer to?",
            "speakAudio": "Il aime sa sœur",
            "options": ["His sister ('sa' agrees with feminine 'sœur')", "His brother ('son frère')", "His father ('son père')"],
            "correct": 0,
            "explain": "'Sa' is used because 'sœur' is feminine, regardless of whether the possessor is male or female."
        },
        {
            "prompt": "Listen to the phonetic liaison: 'mon amie'. Why is 'mon' used with a female friend?",
            "speakAudio": "mon amie",
            "options": ["To prevent hiatus/vowel clash (*ma amie)", "Because amie is masculine", "It is an irregular slang form"],
            "correct": 0,
            "explain": "French replaces 'ma/ta/sa' with 'mon/ton/son' before feminine words beginning with a vowel."
        }
    ],
    "arena": [
        {
            "quest": "Present Your Family: 'This is my mother'",
            "clue": "Madame Claudine: 'Use C'est, feminine possessive ma, and mère!'",
            "target": "C'est ma mère",
            "tokens": ["C'est", "ma", "mère", "mon", "père", "sont"],
            "explain": "'C'est' (this is) + 'ma' (fem. possessive) + 'mère' (mother)."
        },
        {
            "quest": "Describe Sibling's Child: 'My brother has a daughter'",
            "clue": "Madame Claudine: 'Subject mon frère, verb a, object une fille!'",
            "target": "Mon frère a une fille",
            "tokens": ["Mon", "frère", "a", "une", "fille", "ma", "est"],
            "explain": "'Mon frère' (my brother) + 'a' (has) + 'une fille' (a daughter)."
        },
        {
            "quest": "State Kindness: 'His sister is kind'",
            "clue": "Madame Claudine: 'Subject Sa sœur, verb est, feminine adjective gentille!'",
            "target": "Sa sœur est gentille",
            "tokens": ["Sa", "sœur", "est", "gentille", "Son", "gentil"],
            "explain": "'Sa sœur' (his/her sister) + 'est' (is) + 'gentille' (fem. kind)."
        },
        {
            "quest": "Introduce Grandparents: 'These are my grandparents'",
            "clue": "Madame Claudine: 'Plural demonstrative Ce sont, plural mes, and grands-parents!'",
            "target": "Ce sont mes grands-parents",
            "tokens": ["Ce", "sont", "mes", "grands-parents", "C'est", "mon"],
            "explain": "'Ce sont' (these are) + 'mes' (plural my) + 'grands-parents'."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the French word for FATHER (PÈRE):",
            "tiles": ["P", "È", "R", "E", "M", "S"],
            "answer": "PÈRE",
            "gloss": "père (father)"
        },
        {
            "clue": "Spell the French word for SISTER with ligature (SŒUR):",
            "tiles": ["S", "Œ", "U", "R", "F", "E"],
            "answer": "SŒUR",
            "gloss": "sœur (sister)"
        },
        {
            "clue": "Spell the French word for BROTHER (FRÈRE):",
            "tiles": ["F", "R", "È", "R", "E", "O", "T"],
            "answer": "FRÈRE",
            "gloss": "frère (brother)"
        }
    ],
    "quiz": [
        {
            "q": "In French, what determines whether you say 'son père' or 'sa mère'?",
            "options": [
                "The grammatical gender of the noun possessed (père is masc., mère is fem.), regardless of whether the owner is a man or a woman!",
                "The gender of the person who owns them (men say son, women say sa)",
                "Whether the owner is currently present in the room"
            ],
            "correct": 0,
            "explain": "Unlike English (his/her), French possessives agree exclusively with the possessed noun: son père (his/her father), sa mère (his/her mother)."
        },
        {
            "q": "Why do French speakers say 'mon amie' (my female friend) instead of '*ma amie'?",
            "options": [
                "For euphony: 'mon' prevents an awkward vowel clash (hiatus) before vowel-initial feminine nouns!",
                "Because 'amie' becomes grammatically masculine in the presence of possessives",
                "Because 'ma' is strictly reserved for family members"
            ],
            "correct": 0,
            "explain": "Mon, ton, son replace ma, ta, sa before feminine nouns starting with a vowel or mute h."
        },
        {
            "q": "How is the French word 'fils' (son) uniquely pronounced?",
            "options": [
                "[fis] — the 'l' is completely silent, and the final 's' is pronounced!",
                "[fil] — the 's' is silent and 'l' is pronounced",
                "[filz] — both 'l' and 's' are fully pronounced"
            ],
            "correct": 0,
            "explain": "'Fils' is famous for its irregular pronunciation: [fis], completely omitting the 'l'."
        },
        {
            "q": "What special typographical letter is required when spelling the French word for sister ('sœur')?",
            "options": [
                "The ligature 'œ' (e dans l'o / o-e ligature)!",
                "The circumflex 'ô'",
                "The cedilla 'ç'"
            ],
            "correct": 0,
            "explain": "'Sœur' and 'cœur' are written with the unified ligature 'œ'."
        },
        {
            "q": "What is the plural form of the possessive determiner 'my' in French ('mes')?",
            "options": [
                "mes (used for both masculine and feminine plural nouns: mes frères, mes sœurs)!",
                "mons",
                "mas"
            ],
            "correct": 0,
            "explain": "'Mes' is the universal plural form of 'mon/ma': mes parents, mes enfants."
        }
    ]
}

# ------------------------------------------------------------------------------
# 3. LATIN — STEP 5: FĀMA FAMILIAQUE KINSHIP REALM
# ------------------------------------------------------------------------------

LATIN_STEP5 = {
    "sealName": "Stemma Domūs Romanae Kinship Seal",
    "guide": {
        "name": "Marcus",
        "role": "Roman Paterfamilias & Genealogist",
        "avatar": "🏛️",
        "prompt": "Salvēte in domō nostrā! In ancient Rome, the familia was the foundation of the Republic under the guidance of the paterfamiliās. Learn our classical kinship terms from pater and māter to frāter and soror, inflected with possessive adjectives meus, tuus, and suus."
    },
    "cards": [
        {
            "id": "lat5_c1",
            "type": "kinship",
            "glyph": "māter (mātris, f.)",
            "phonetic": "[ˈmaː.tɛr]",
            "gloss": "mother • 3rd declension feminine",
            "speakText": "mater",
            "audioUrl": "",
            "whisper": "Third declension consonant stem: māter, mātris, mātrī, mātrem, mātre. Macron marks the long 'ā'."
        },
        {
            "id": "lat5_c2",
            "type": "kinship",
            "glyph": "pater (patris, m.)",
            "phonetic": "[ˈpa.tɛr]",
            "gloss": "father • 3rd declension masculine",
            "speakText": "pater",
            "audioUrl": "",
            "whisper": "Genitive 'patris'. Head of the household was the 'paterfamiliās', possessing legal authority ('patria potestās')."
        },
        {
            "id": "lat5_c3",
            "type": "kinship",
            "glyph": "frāter (frātris, m.)",
            "phonetic": "[ˈfraː.tɛr]",
            "gloss": "brother • 3rd declension masculine",
            "speakText": "frater",
            "audioUrl": "",
            "whisper": "Third declension stem: frāter, frātris. Root of English 'fraternity' and 'fraternal'."
        },
        {
            "id": "lat5_c4",
            "type": "kinship",
            "glyph": "soror (sorōris, f.)",
            "phonetic": "[ˈsɔ.rɔr]",
            "gloss": "sister • 3rd declension feminine",
            "speakText": "soror",
            "audioUrl": "",
            "whisper": "Genitive 'sorōris'. Root of English 'sorority' and 'sororal'."
        },
        {
            "id": "lat5_c5",
            "type": "kinship",
            "glyph": "fīlius / fīlia",
            "phonetic": "[ˈfiː.lɪ.ʊs] / [ˈfiː.lɪ.a]",
            "gloss": "son / daughter",
            "speakText": "filius, filia",
            "audioUrl": "",
            "whisper": "Fīlius is 2nd declension masculine; fīlia is 1st declension feminine (dative/ablative plural 'fīliābus' to avoid clash with fīliīs!). Special vocative: 'mī fīlī' (my son!)."
        },
        {
            "id": "lat5_c6",
            "type": "kinship",
            "glyph": "avus / avia",
            "phonetic": "[ˈa.wʊs] / [ˈa.wɪ.a]",
            "gloss": "grandfather / grandmother",
            "speakText": "avus, avia",
            "audioUrl": "",
            "whisper": "Remember classical pronunciation: 'v' sounds like [w]: [ˈa.wʊs]. Ancestors generally are 'māiōrēs' (the greater ones)."
        },
        {
            "id": "lat5_c7",
            "type": "kinship",
            "glyph": "marītus / uxor",
            "phonetic": "[maˈriː.tʊs] / [ˈʊk.sɔr]",
            "gloss": "husband / wife",
            "speakText": "maritus, uxor",
            "audioUrl": "",
            "whisper": "'Marītus' (husband) and 'uxor' (gen. uxōris, wife). Root of English 'marital' and 'uxorious'."
        },
        {
            "id": "lat5_c8",
            "type": "possessive",
            "glyph": "meus, mea, meum",
            "phonetic": "[ˈmɛ.ʊs], [ˈmɛ.a], [ˈmɛ.ʊm]",
            "gloss": "my / mine (1st/2nd decl. adj.)",
            "speakText": "meus, mea, meum",
            "audioUrl": "",
            "whisper": "Agrees with the noun in gender, number, and case: 'pater meus' (masc. nom.), 'māter mea' (fem. nom.), 'frātrem meum' (acc.). Irregular vocative masculine: 'mī'!"
        },
        {
            "id": "lat5_c9",
            "type": "possessive",
            "glyph": "tuus, tua, tuum",
            "phonetic": "[ˈtʊ.ʊs], [ˈtʊ.a], [ˈtʊ.ʊm]",
            "gloss": "your / yours (singular possessor)",
            "speakText": "tuus, tua, tuum",
            "audioUrl": "",
            "whisper": "Declines like bonus: 'soror tua' (your sister), 'fīlius tuus' (your son)."
        },
        {
            "id": "lat5_c10",
            "type": "possessive",
            "glyph": "suus, sua, suum",
            "phonetic": "[ˈsʊ.ʊs], [ˈsʊ.a], [ˈsʊ.ʊm]",
            "gloss": "his own / her own / their own (reflexive)",
            "speakText": "suus, sua, suum",
            "audioUrl": "",
            "whisper": "Reflexive possessive: refers back to the subject of the sentence! 'Marcus suam sorōrem amat' = Marcus loves HIS OWN sister (versus 'eius' = someone else's sister)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the Latin statement. Where is the speaker's father?",
            "speakAudio": "Pater meus in horto est",
            "options": ["In the garden ('in hortō')", "In the forum ('in Forō')", "At home ('domī')"],
            "correct": 0,
            "explain": "'Pater meus' (my father) + 'in hortō est' (is in the garden)."
        },
        {
            "prompt": "Listen to the kinship pair. Who is mentioned in the phrase?",
            "speakAudio": "Mater et filia",
            "options": ["Mother and daughter ('Māter et fīlia')", "Father and son ('Pater et fīlius')", "Brother and sister ('Frāter et soror')"],
            "correct": 0,
            "explain": "'Māter' is mother and 'fīlia' is daughter."
        },
        {
            "prompt": "Listen to the affectionate vocative call. What does Marcus say?",
            "speakAudio": "Mi fili",
            "options": ["My son! ('Mī fīlī' — irregular vocative)", "My brother!", "My father!"],
            "correct": 0,
            "explain": "'Mī fīlī' is the classic Roman affectionate vocative for 'my son!'."
        },
        {
            "prompt": "Listen to the reflexive sentence. Whom does the subject love?",
            "speakAudio": "Suam sororem amat",
            "options": ["His/Her own sister ('suam sorōrem')", "Your sister ('tuam sorōrem')", "My sister ('meam sorōrem')"],
            "correct": 0,
            "explain": "'Suam' is the accusative singular feminine reflexive possessive (his/her own)."
        }
    ],
    "arena": [
        {
            "quest": "Assemble: 'This is my mother' (Haec est māter mea)",
            "clue": "Marcus: 'Feminine demonstrative Haec, copula est, and māter mea!'",
            "target": "Haec est māter mea",
            "tokens": ["Haec", "est", "māter", "mea", "Hic", "meus"],
            "explain": "'Haec' (fem. this) + 'est' (is) + 'māter mea' (my mother in nom. fem.)."
        },
        {
            "quest": "Assemble: 'My brother has a son' (Frāter meus fīlium habet)",
            "clue": "Marcus: 'Subject Frāter meus, accusative object fīlium, verb habet!'",
            "target": "Frāter meus fīlium habet",
            "tokens": ["Frāter", "meus", "fīlium", "habet", "fīlius", "est"],
            "explain": "'Frāter meus' (nom.) + 'fīlium' (acc. masc. son) + 'habet' (has)."
        },
        {
            "quest": "Assemble: 'Your father is in Rome' (Pater tuus Rōmae est)",
            "clue": "Marcus: 'Subject Pater tuus, locative Rōmae, and verb est!'",
            "target": "Pater tuus Rōmae est",
            "tokens": ["Pater", "tuus", "Rōmae", "est", "tua", "Rōmam"],
            "explain": "'Pater tuus' (nom.) + 'Rōmae' (locative: in Rome) + 'est' (is)."
        },
        {
            "quest": "Assemble: 'He loves his own family' (Familiam suam amat)",
            "clue": "Marcus: 'Accusative object familiam suam, transitive verb amat!'",
            "target": "Familiam suam amat",
            "tokens": ["Familiam", "suam", "amat", "meam", "habet"],
            "explain": "'Familiam suam' (acc. fem. his own family) + 'amat' (loves)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the Latin word for MOTHER (MĀTER):",
            "tiles": ["M", "Ā", "T", "E", "R", "P", "S"],
            "answer": "MĀTER",
            "gloss": "māter (mother)"
        },
        {
            "clue": "Spell the Latin word for FATHER (PATER):",
            "tiles": ["P", "A", "T", "E", "R", "M", "N"],
            "answer": "PATER",
            "gloss": "pater (father)"
        },
        {
            "clue": "Spell the Latin word for BROTHER (FRĀTER):",
            "tiles": ["F", "R", "Ā", "T", "E", "R", "O"],
            "answer": "FRĀTER",
            "gloss": "frāter (brother)"
        }
    ],
    "quiz": [
        {
            "q": "What is the critical distinction between reflexive 'suus, sua, suum' and genitive 'eius' in Latin?",
            "options": [
                "'Suus' refers back to the subject of the sentence ('his/her own'), while 'eius' refers to an external third person!",
                "'Suus' is for inanimate objects only",
                "'Eius' is strictly plural while 'suus' is singular"
            ],
            "correct": 0,
            "explain": "Latin rigorously distinguishes reflexive possession (suus = the subject's own) from non-reflexive (eius = of another)."
        },
        {
            "q": "What is the irregular vocative singular masculine of 'meus fīlius' (my son)?",
            "options": [
                "mī fīlī (contracted forms of both meus and fīlius)!",
                "mee fīlie",
                "meus fīlius"
            ],
            "correct": 0,
            "explain": "'Meus' has the irregular vocative 'mī', and 2nd declension nouns in '-ius' end in '-ī': 'mī fīlī!'."
        },
        {
            "q": "To which Latin declension do the core kinship nouns 'pater', 'māter', 'frāter', and 'soror' belong?",
            "options": [
                "The 3rd declension (consonant stems with genitive in -is)!",
                "The 1st declension in -a",
                "The 2nd declension in -us"
            ],
            "correct": 0,
            "explain": "Pater (patris), māter (mātris), frāter (frātris), soror (sorōris) are all 3rd declension consonant stems."
        },
        {
            "q": "How does the possessive adjective 'meus, mea, meum' agree with its noun in Latin?",
            "options": [
                "In gender, number, and case with the noun it modifies (e.g. pater meus, māter mea, frātrem meum)!",
                "It always remains masculine singular 'meus'",
                "It agrees with the person who is listening"
            ],
            "correct": 0,
            "explain": "Possessive adjectives in Latin function like 1st/2nd declension adjectives, fully inflecting for case, number, and gender."
        },
        {
            "q": "What legal power did the Roman 'paterfamiliās' hold over his household?",
            "options": [
                "Patria potestās — sovereign paternal legal authority over children, property, and the domestic sphere!",
                "Consular command of legions",
                "Pontifical oversight of public temples"
            ],
            "correct": 0,
            "explain": "'Patria potestās' was the defining legal institution of Roman familial life."
        }
    ]
}

# ------------------------------------------------------------------------------
# 4. HEBREW — STEP 5: MISHPACHA CHAYEINU KINSHIP REALM
# ------------------------------------------------------------------------------

HEBREW_STEP5 = {
    "sealName": "Mishpacha Chayeinu Kinship Seal",
    "guide": {
        "name": "Eli",
        "role": "Jerusalem Patriarch & Family Chronicler",
        "avatar": "🍇",
        "prompt": "Shalom uv'racha! In Hebrew heritage, mishpacha (family) is our sanctuary. Discover our kinship terms from ába and íma to ach, achót, ben, and bat, joined with possessives shelí, sheló, and sheláh."
    },
    "cards": [
        {
            "id": "heb5_c1",
            "type": "kinship",
            "glyph": "אִמָּא (אימא)",
            "phonetic": "íma [ˈʔi.ma]",
            "gloss": "mother / mom • feminine",
            "speakText": "אימא",
            "audioUrl": "",
            "whisper": "From Aramaic 'imma' with emphatic alef. Used universally in Modern Hebrew for both 'mother' and 'mom'. Plural: imahót (אִמָּהוֹת)."
        },
        {
            "id": "heb5_c2",
            "type": "kinship",
            "glyph": "אַבָּא",
            "phonetic": "ába [ˈʔa.ba]",
            "gloss": "father / dad • masculine",
            "speakText": "אבא",
            "audioUrl": "",
            "whisper": "From Aramaic 'abba'. Plural is masculine with feminine-looking ending: avót (אָבוֹת = fathers / forefathers)."
        },
        {
            "id": "heb5_c3",
            "type": "kinship",
            "glyph": "אָח",
            "phonetic": "ach [ʔaχ]",
            "gloss": "brother • masculine",
            "speakText": "אח",
            "audioUrl": "",
            "whisper": "Brother. Plural: achím (אַחִים). Also means 'male nurse' in modern clinical Hebrew!"
        },
        {
            "id": "heb5_c4",
            "type": "kinship",
            "glyph": "אָחוֹת",
            "phonetic": "achót [ʔaˈχot]",
            "gloss": "sister • feminine",
            "speakText": "אחות",
            "audioUrl": "",
            "whisper": "Sister. Irregular plural: achayót (אֲחָיוֹת). Also means 'female nurse'!"
        },
        {
            "id": "heb5_c5",
            "type": "kinship",
            "glyph": "בֵּן / בַּת",
            "phonetic": "ben [ben] / bat [bat]",
            "gloss": "son / daughter",
            "speakText": "בן, בת",
            "audioUrl": "",
            "whisper": "Plural of ben is baním (בָּנִים); plural of bat is banót (בָּנוֹת). Also used for ages: 'ben esrim' (20 years old, m.)."
        },
        {
            "id": "heb5_c6",
            "type": "kinship",
            "glyph": "סַבָּא / סָבְתָא",
            "phonetic": "sába [ˈsa.ba] / sávta [ˈsav.ta]",
            "gloss": "grandfather / grandmother",
            "speakText": "סבא, סבתא",
            "audioUrl": "",
            "whisper": "Aramaic loan roots. Deeply affectionate terms used by Israeli grandchildren everywhere."
        },
        {
            "id": "heb5_c7",
            "type": "kinship",
            "glyph": "בַּעַל / אִשָּׁה",
            "phonetic": "bá'al [ˈba.ʕal] / ishá [ʔiˈʃa]",
            "gloss": "husband / wife",
            "speakText": "בעל, אישה",
            "audioUrl": "",
            "whisper": "'Ishá' also means 'woman'. A widespread modern alternative for husband is 'ishí' (אִישִׁי = my man/husband)."
        },
        {
            "id": "heb5_c8",
            "type": "kinship",
            "glyph": "דּוֹד / דּוֹדָה",
            "phonetic": "dod [dod] / dodah [doˈda]",
            "gloss": "uncle / aunt",
            "speakText": "דוד, דודה",
            "audioUrl": "",
            "whisper": "In biblical Hebrew, 'dod' also meant 'beloved' (as in Song of Songs: 'Ani l'dodi v'dodi li')."
        },
        {
            "id": "heb5_c9",
            "type": "possessive",
            "glyph": "שֶׁלִּי",
            "phonetic": "shelí [ʃeˈli]",
            "gloss": "my / mine (possessive pronoun)",
            "speakText": "שלי",
            "audioUrl": "",
            "whisper": "Composed of particle 'she-' (that/which) + preposition 'l-' (to) + 1st person suffix: 'of me'. Follows the noun: 'ha-ába shelí' (my father)."
        },
        {
            "id": "heb5_c10",
            "type": "possessive",
            "glyph": "שֶׁלּוֹ / שֶׁלָּהּ",
            "phonetic": "sheló [ʃeˈlo] / sheláh [ʃeˈla]",
            "gloss": "his / her (possessives)",
            "speakText": "שלו, שלה",
            "audioUrl": "",
            "whisper": "'Sheló' (his) and 'sheláh' (her/hers). Notice dagesh in heh in formal sheláh. Agrees with possessor: ha-bayit sheló (his house), ha-bayit sheláh (her house)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the family phrase. Who is being identified?",
            "speakAudio": "זאת אימא שלי",
            "options": ["This is my mother ('zot íma shelí')", "This is my sister", "This is his mother"],
            "correct": 0,
            "explain": "'זאת' (f. this is) + 'אימא שלי' (my mother)."
        },
        {
            "prompt": "Listen to the sibling expression. Who is in the speaker's family?",
            "speakAudio": "יש לי אח ואחות",
            "options": ["I have a brother and a sister", "I have two brothers", "I have a mother and father"],
            "correct": 0,
            "explain": "'יש לי' (I have) + 'אח' (brother) + 'ואחות' (and a sister)."
        },
        {
            "prompt": "Listen to the possessive modifier: 'sheló'. Whose daughter is mentioned?",
            "speakAudio": "הבת שלו לומדת",
            "options": ["His daughter ('ha-bat sheló')", "My daughter ('ha-bat shelí')", "Her daughter ('ha-bat sheláh')"],
            "correct": 0,
            "explain": "'שלו' (sheló) signifies 'his'."
        },
        {
            "prompt": "Listen to the loving elder term. Who is 'sávta'?",
            "speakAudio": "סבתא שלי",
            "options": ["My grandmother ('sávta shelí')", "My aunt ('dodah')", "My grandfather ('sába')"],
            "correct": 0,
            "explain": "'סָבְתָא' (sávta) is grandmother."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'This is my father' (זה אבא שלי)",
            "clue": "Eli: 'Masculine demonstrative זה, noun אבא, and possessive שלי!'",
            "target": "זה אבא שלי",
            "tokens": ["זה", "אבא", "שלי", "זאת", "אימא"],
            "explain": "'זה' (m. this) + 'אבא' (father) + 'שלי' (my)."
        },
        {
            "quest": "Build: 'I have a brother' (יש לי אח)",
            "clue": "Eli: 'Existential possessive יש לי followed by אח!'",
            "target": "יש לי אח",
            "tokens": ["יש", "לי", "אח", "אחות", "אין"],
            "explain": "'יש לי' (I have / there is to me) + 'אח' (brother)."
        },
        {
            "quest": "Build: 'This is his sister' (זאת אחות שלו)",
            "clue": "Eli: 'Feminine demonstrative זאת, noun אחות, and possessive שלו!'",
            "target": "זאת אחות שלו",
            "tokens": ["זאת", "אחות", "שלו", "שלה", "זה"],
            "explain": "'זאת' (f. this) + 'אחות' (sister) + 'שלו' (his)."
        },
        {
            "quest": "Build: 'Where is your mother?' (איפה אמא שלך)",
            "clue": "Eli: 'Interrogative איפה followed by אמא שלך!'",
            "target": "איפה אמא שלך",
            "tokens": ["איפה", "אמא", "שלך", "שלי", "מי"],
            "explain": "'איפה' (where) + 'אמא שלך' (your mother)."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the Hebrew word for MOTHER (ÍMA -> אימא):",
            "tiles": ["א", "י", "מ", "א", "ב", "ת"],
            "answer": "אימא",
            "gloss": "אִמָּא (mother)"
        },
        {
            "clue": "Assemble the Hebrew word for FATHER (ÁBA -> אבא):",
            "tiles": ["א", "ב", "א", "ם", "ר"],
            "answer": "אבא",
            "gloss": "אַבָּא (father)"
        },
        {
            "clue": "Assemble the possessive pronoun MY / MINE (SHELÍ -> שלי):",
            "tiles": ["ש", "ל", "י", "ה", "ו"],
            "answer": "שלי",
            "gloss": "שֶׁלִּי (my / mine)"
        }
    ],
    "quiz": [
        {
            "q": "What syntactic rule applies when using possessive 'shel' (שֶׁל) with a definite noun in Hebrew?",
            "options": [
                "The noun must take the definite article prefix 'ha-' (e.g. 'ha-ába shelí' = literally 'the-father of-me')!",
                "The word 'shel' must precede the noun",
                "The definite article is forbidden with family words"
            ],
            "correct": 0,
            "explain": "When possessed by 'shel', the modified noun is syntactically definite and takes the prefix 'ha-': ha-bayit shelí, ha-achót sheló."
        },
        {
            "q": "From which sister Semitic language did Modern Hebrew adopt the everyday terms 'ába' (אַבָּא) and 'íma' (אִמָּא)?",
            "options": [
                "Aramaic (where final alef was the definite postpositive article)!",
                "Arabic",
                "Phoenician"
            ],
            "correct": 0,
            "explain": "Ába and íma originated in Judeo-Aramaic and became universal in Talmudic and Modern Hebrew."
        },
        {
            "q": "What is the irregular plural form of 'achót' (אָחוֹת — sister) in Hebrew?",
            "options": [
                "achayót (אֲחָיוֹת)",
                "achótím",
                "achótót"
            ],
            "correct": 0,
            "explain": "Sister (achót) undergoes an irregular vowel shift to achayót in the plural."
        },
        {
            "q": "How do you distinguish 'his' from 'her' when using the possessive base 'shel'?",
            "options": [
                "sheló (שֶׁלּוֹ) = his; sheláh (שֶׁלָּהּ) = her!",
                "shelí = his; sheló = her",
                "shelkhá = his; shelákh = her"
            ],
            "correct": 0,
            "explain": "Sheló carries the 3rd person masculine singular suffix (-o), while sheláh carries the 3rd feminine singular suffix (-ah)."
        },
        {
            "q": "What is the Hebrew cultural concept of 'mishpacha' (מִשְׁפָּחָה)?",
            "options": [
                "The extended family network, fostering profound solidarity, weekly Shabbat reunions, and mutual lifelong care!",
                "A formal legal contract only",
                "A school classroom"
            ],
            "correct": 0,
            "explain": "'Mishpacha' represents the deep familial anchor of Jewish and Israeli cultural life."
        }
    ]
}

# ------------------------------------------------------------------------------
# 5. CHINESE — STEP 5: JADE LINEAGE KINSHIP REALM
# ------------------------------------------------------------------------------

CHINESE_STEP5 = {
    "sealName": "Jade Family Lineage Seal (玉堂家和之印)",
    "guide": {
        "name": "Master Lao",
        "role": "Teahouse Patriarch & Lineage Elder",
        "avatar": "🍵",
        "prompt": "Nǐ hǎo! In Chinese culture, family (家庭 jiātíng) and ancestral harmony are paramount. Master the precise hierarchical terms: 爸爸, 妈妈, 哥哥, 弟弟, 姐姐, 妹妹, joined with the possessive particle 的 (de)—and notice how '的' is warmly omitted for immediate family!"
    },
    "cards": [
        {
            "id": "zh5_c1",
            "type": "kinship",
            "glyph": "爸爸 (bàba)",
            "phonetic": "bàba [pa˥˩.pa]",
            "gloss": "father / dad • 4th tone + neutral",
            "speakText": "爸爸",
            "audioUrl": "",
            "whisper": "Features 父 (father radical) on top and 巴 (phonetic) below. Reduplicated characters in kinship take a neutral tone on the second syllable: bàba."
        },
        {
            "id": "zh5_c2",
            "type": "kinship",
            "glyph": "妈妈 (māma)",
            "phonetic": "māma [ma˥.ma]",
            "gloss": "mother / mom • 1st tone + neutral",
            "speakText": "妈妈",
            "audioUrl": "",
            "whisper": "Features 女 (female radical) on the left and 马 (mǎ, horse phonetic) on the right: high level 1st tone followed by neutral tone: māma."
        },
        {
            "id": "zh5_c3",
            "type": "kinship",
            "glyph": "哥哥 / 弟弟",
            "phonetic": "gēge [kɤ˥.kɤ] / dìdi [ti˥˩.ti]",
            "gloss": "elder brother / younger brother",
            "speakText": "哥哥, 弟弟",
            "audioUrl": "",
            "whisper": "Chinese has NO generic word for 'brother' in everyday speech! You must specify seniority: 哥哥 (gēge = elder) or 弟弟 (dìdi = younger)."
        },
        {
            "id": "zh5_c4",
            "type": "kinship",
            "glyph": "姐姐 / 妹妹",
            "phonetic": "jiějie [tɕjɛ˨˩˦.tɕjɛ] / mèimei [meɪ̯˥˩.meɪ̯]",
            "gloss": "elder sister / younger sister",
            "speakText": "姐姐, 妹妹",
            "audioUrl": "",
            "whisper": "Both contain the 女 (woman) radical. Seniority is always explicit: 姐姐 (jiějie, 3rd tone = elder) vs 妹妹 (mèimei, 4th tone = younger)."
        },
        {
            "id": "zh5_c5",
            "type": "kinship",
            "glyph": "爷爷 / 奶奶",
            "phonetic": "yéye [jɛ˧˥.jɛ] / nǎinai [naɪ̯˨˩˦.naɪ̯]",
            "gloss": "paternal grandfather / grandmother",
            "speakText": "爷爷, 奶奶",
            "audioUrl": "",
            "whisper": "Specifically father's father (爷爷) and father's mother (奶奶). Paternal grandparents are traditionally the household lineage anchors."
        },
        {
            "id": "zh5_c6",
            "type": "kinship",
            "glyph": "外公 / 外婆",
            "phonetic": "wàigōng [waɪ̯˥˩.kʊŋ˥] / wàipó [waɪ̯˥˩.pʰwɔ˧˥]",
            "gloss": "maternal grandfather / grandmother",
            "speakText": "外公, 外婆",
            "audioUrl": "",
            "whisper": "Notice the prefix '外' (wài = outside/maternal): mother's father is 外公 (wàigōng), mother's mother is 外婆 (wàipó) or 姥爷/姥姥 in northern China."
        },
        {
            "id": "zh5_c7",
            "type": "kinship",
            "glyph": "儿子 / 女儿",
            "phonetic": "érzi [aɚ̯˧˥.tsz̩] / nǚ'ér [ny˨˩˦.ʔaɚ̯˧˥]",
            "gloss": "son / daughter",
            "speakText": "儿子, 女儿",
            "audioUrl": "",
            "whisper": "儿子 (érzi = son) and 女儿 (nǚ'ér = daughter). When giving birth, people affectionately announce '生了儿子' or '生了女儿'."
        },
        {
            "id": "zh5_c8",
            "type": "possessive",
            "glyph": "的 (de)",
            "phonetic": "de [tɤ]",
            "gloss": "possessive particle ('s / of)",
            "speakText": "的",
            "audioUrl": "",
            "whisper": "Neutral tone particle: 我的 (wǒ de = my), 你的 (nǐ de = your), 他的 (tā de = his). Syntactic bonus: with close family, '的' is colloquially dropped: 我爸爸 (wǒ bàba)!"
        },
        {
            "id": "zh5_c9",
            "type": "kinship",
            "glyph": "家人 / 家庭",
            "phonetic": "jiārén [tɕja˥.ʐən˧˥] / jiātíng [tɕja˥.tʰiŋ˧˥]",
            "gloss": "family members / household",
            "speakText": "家人, 家庭",
            "audioUrl": "",
            "whisper": "家 (home/family) + 人 (people) = family members. 家 (home) + 庭 (courtyard) = the institution of family."
        },
        {
            "id": "zh5_c10",
            "type": "possessive",
            "glyph": "我的 / 他的 (她的)",
            "phonetic": "wǒ de / tā de",
            "gloss": "my / his (her)",
            "speakText": "我的, 他的, 她的",
            "audioUrl": "",
            "whisper": "Pronoun + 的 forms possessive pronouns: 我的 (my/mine), 他的 (his), 她的 (hers). All spoken 'tā de' sound identical in speech!"
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the family introduction. Who is being presented?",
            "speakAudio": "这是我的妈妈",
            "options": ["This is my mother ('Zhè shì wǒ de māma')", "This is my older sister", "This is his mother"],
            "correct": 0,
            "explain": "'这' (this) + '是' (is) + '我的妈妈' (my mother)."
        },
        {
            "prompt": "Listen to the sibling distinction: '哥哥' vs '弟弟'. What is the difference?",
            "speakAudio": "哥哥和弟弟",
            "options": ["Elder brother and younger brother", "Elder sister and younger sister", "Father and son"],
            "correct": 0,
            "explain": "'哥哥' (gēge) is older brother and '弟弟' (dìdi) is younger brother."
        },
        {
            "prompt": "Listen to the intimate phrasing: '我爸爸'. Why is '的' omitted?",
            "speakAudio": "我爸爸在家",
            "options": ["In close family relationships, '的' can be naturally dropped", "It is a grammatical mistake", "Only words starting with 'b' drop '的'"],
            "correct": 0,
            "explain": "Close personal relations (family, close friends) allow natural omission of possessive '的': 我爸爸, 我妈妈."
        },
        {
            "prompt": "Listen to the grandparent term: '外公'. Which grandfather is this?",
            "speakAudio": "外公",
            "options": ["Maternal grandfather (mother's father)", "Paternal grandfather (father's father)", "Great-grandfather"],
            "correct": 0,
            "explain": "'外公' (wàigōng) designates maternal grandfather, while '爷爷' (yéye) is paternal."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'This is my father' (这是我爸爸)",
            "clue": "Master Lao: 'Assemble 这, 是, 我, and 爸爸!'",
            "target": "这是我爸爸",
            "tokens": ["这", "是", "我", "爸爸", "妈妈", "有"],
            "explain": "'这' (this) + '是' (is) + '我' (my) + '爸爸' (father)."
        },
        {
            "quest": "Build: 'I have an older brother' (我有一个哥哥)",
            "clue": "Master Lao: 'Subject 我, verb 有, measure phrase 一个, noun 哥哥!'",
            "target": "我有一个哥哥",
            "tokens": ["我", "有", "一个", "哥哥", "弟弟", "是"],
            "explain": "'我' + '有' (have) + '一个' (one [classifier]) + '哥哥' (older brother)."
        },
        {
            "quest": "Build: 'Her younger sister is very pretty' (她的妹妹很漂亮)",
            "clue": "Master Lao: 'Subject 她的妹妹, adverb 很, adjective 漂亮!'",
            "target": "她的妹妹很漂亮",
            "tokens": ["她的", "妹妹", "很", "漂亮", "是", "哥哥"],
            "explain": "'她的妹妹' (her younger sister) + '很' + '漂亮' (pretty, zero copula)."
        },
        {
            "quest": "Build: 'How many people in your family?' (你家有几口人)",
            "clue": "Master Lao: 'Classic idiom: 你家 + 有 + 几口人!'",
            "target": "你家有几口人",
            "tokens": ["你家", "有", "几口人", "我家", "几个", "是"],
            "explain": "'你家' (your home) + '有' (has) + '几口人' (how many members [classifier 口])."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the Chinese word for FATHER (BÀBA -> 爸爸):",
            "tiles": ["爸", "爸", "妈", "哥"],
            "answer": "爸爸",
            "gloss": "爸爸 (bàba = father)"
        },
        {
            "clue": "Assemble the Chinese word for MOTHER (MĀMA -> 妈妈):",
            "tiles": ["妈", "妈", "爸", "姐"],
            "answer": "妈妈",
            "gloss": "妈妈 (māma = mother)"
        },
        {
            "clue": "Assemble the Chinese word for ELDER BROTHER (GĒGE -> 哥哥):",
            "tiles": ["哥", "哥", "弟", "妹"],
            "answer": "哥哥",
            "gloss": "哥哥 (gēge = elder brother)"
        }
    ],
    "quiz": [
        {
            "q": "Why does standard Mandarin Chinese not have a single generic word for 'brother' or 'sister'?",
            "options": [
                "Chinese kinship strictly distinguishes seniority: elder brother (哥哥), younger brother (弟弟), elder sister (姐姐), younger sister (妹妹)!",
                "Ancient emperors forbade generic words",
                "Siblings are only counted by numbers 1, 2, 3"
            ],
            "correct": 0,
            "explain": "Confucian familial ethics place great emphasis on generational and birth seniority, requiring distinct words for older vs younger siblings."
        },
        {
            "q": "How do Chinese speakers distinguish maternal grandparents from paternal grandparents?",
            "options": [
                "Paternal are 爷爷 (yéye) & 奶奶 (nǎinai); maternal use the prefix 外 (outside): 外公 (wàigōng) & 外婆 (wàipó)!",
                "They use the same words with different tones",
                "Only maternal grandparents are given names"
            ],
            "correct": 0,
            "explain": "Traditionally, patrilineal lineage distinguishes the father's side from the mother's side (外 = outer)."
        },
        {
            "q": "Which measure word / classifier is traditionally used when counting family members (e.g. 'How many people in your family?')?",
            "options": [
                "口 (kǒu — literally 'mouths' to feed: 几口人)!",
                "个 (gè)",
                "只 (zhī)"
            ],
            "correct": 0,
            "explain": "'口' (kǒu = mouth) is the evocative classifier for family members: '我家有五口人' (My family has 5 people/mouths)."
        },
        {
            "q": "When can the possessive particle '的' (de) be naturally omitted in spoken Chinese?",
            "options": [
                "When expressing close personal relationships, such as immediate family members ('我爸爸', '我妈妈')!",
                "Never; '的' is strictly mandatory in all sentences",
                "Only after the pronoun '他'"
            ],
            "correct": 0,
            "explain": "Intimate kinship allows dropping '的': 我爸爸 (my dad) sounds warmer than the formal 我的爸爸."
        },
        {
            "q": "Which semantic radical is shared across female kinship characters like 妈, 姐, 妹, 奶, and 婆?",
            "options": [
                "女 (nǚ — the woman/female radical)!",
                "父 (fù — father)",
                "口 (kǒu — mouth)"
            ],
            "correct": 0,
            "explain": "The 女 radical visually encodes female family members in Chinese orthography."
        }
    ]
}

# ------------------------------------------------------------------------------
# 6. GERMAN — STEP 5: SCHWARZWALD FAMILIEN-WAPPEN KINSHIP REALM
# ------------------------------------------------------------------------------

GERMAN_STEP5 = {
    "sealName": "Schwarzwald Familien-Wappen Seal",
    "guide": {
        "name": "Herr Schmidt",
        "role": "Black Forest Genealogist & Woodcarver",
        "avatar": "🕰️",
        "prompt": "Grüß Gott! In Germany, family (die Familie) gathers around the warm hearth. Learn our kinship nouns from Mutter and Vater to Bruder, Schwester, Sohn, and Tochter, and master possessive inflection: mein, meine; sein, seine; ihr, ihre."
    },
    "cards": [
        {
            "id": "de5_c1",
            "type": "kinship",
            "glyph": "Mutter (die Mutter)",
            "phonetic": "[ˈmʊ.tɐ]",
            "gloss": "mother • feminine (pl. Mütter)",
            "speakText": "Mutter",
            "audioUrl": "",
            "whisper": "Feminine noun: 'die Mutter'. Notice the plural forms with an umlaut: 'die Mütter' [ˈmʏ.tɐ]! Affectionately 'Mutti' or 'Mama'."
        },
        {
            "id": "de5_c2",
            "type": "kinship",
            "glyph": "Vater (der Vater)",
            "phonetic": "[ˈfaː.tɐ]",
            "gloss": "father • masculine (pl. Väter)",
            "speakText": "Vater",
            "audioUrl": "",
            "whisper": "'V' sounds like [f]: [ˈfaː.tɐ]. Plural takes umlaut: 'die Väter' [ˈfɛː.tɐ]. Familiarly 'Vati' or 'Papa'."
        },
        {
            "id": "de5_c3",
            "type": "kinship",
            "glyph": "Bruder (der Bruder)",
            "phonetic": "[ˈbʁuː.dɐ]",
            "gloss": "brother • masculine (pl. Brüder)",
            "speakText": "Bruder",
            "audioUrl": "",
            "whisper": "Masculine: 'der Bruder'. Plural triggers umlaut fronting from [uː] to [yː]: 'die Brüder' [ˈbʁyː.dɐ]."
        },
        {
            "id": "de5_c4",
            "type": "kinship",
            "glyph": "Schwester (die Schwester)",
            "phonetic": "[ˈʃvɛs.tɐ]",
            "gloss": "sister • feminine (pl. Schwestern)",
            "speakText": "Schwester",
            "audioUrl": "",
            "whisper": "Feminine: 'die Schwester'. Initial 'Sch' makes [ʃ]. Plural adds '-n': 'die Schwestern'."
        },
        {
            "id": "de5_c5",
            "type": "kinship",
            "glyph": "Sohn / Tochter",
            "phonetic": "[zoːn] / [ˈtɔχ.tɐ]",
            "gloss": "son / daughter",
            "speakText": "Sohn, Tochter",
            "audioUrl": "",
            "whisper": "'Der Sohn' (pl. Söhne [ˈzøː.nə]) and 'die Tochter' (pl. Töchter [ˈtœç.tɐ]). Both form plurals via umlaut mutation!"
        },
        {
            "id": "de5_c6",
            "type": "kinship",
            "glyph": "Großvater / Großmutter",
            "phonetic": "[ˈɡʁoːsˌfaː.tɐ] / [ˈɡʁoːsˌmʊ.tɐ]",
            "gloss": "grandfather / grandmother",
            "speakText": "Großvater, Großmutter",
            "audioUrl": "",
            "whisper": "Compound words with 'Groß-' (great/grand). In daily life, almost everyone says 'Opa' (grandpa) and 'Oma' (grandma)!"
        },
        {
            "id": "de5_c7",
            "type": "kinship",
            "glyph": "Mann / Frau",
            "phonetic": "[man] / [fʁaʊ̯]",
            "gloss": "husband / wife (or man / woman)",
            "speakText": "Mann, Frau",
            "audioUrl": "",
            "whisper": "'Mein Mann' = my husband; 'meine Frau' = my wife. Formal terms: 'Ehemann' and 'Ehefrau'."
        },
        {
            "id": "de5_c8",
            "type": "kinship",
            "glyph": "Onkel / Tante",
            "phonetic": "[ˈɔŋ.kl̩] / [ˈtan.tə]",
            "gloss": "uncle / aunt",
            "speakText": "Onkel, Tante",
            "audioUrl": "",
            "whisper": "'Der Onkel' (pl. die Onkel) and 'die Tante' (pl. die Tanten). Together with cousins: 'die Verwandten' (relatives)."
        },
        {
            "id": "de5_c9",
            "type": "possessive",
            "glyph": "mein / meine",
            "phonetic": "[maɪ̯n] / [ˈmaɪ̯.nə]",
            "gloss": "my (masc./neut. vs. fem./plural)",
            "speakText": "mein, meine",
            "audioUrl": "",
            "whisper": "Inflects like 'ein': 'mein Vater' (masc. nom.), 'meine Mutter' (fem. nom.), 'meine Eltern' (plural). In the accusative masculine: 'meinen Bruder'!"
        },
        {
            "id": "de5_c10",
            "type": "possessive",
            "glyph": "sein / seine & ihr / ihre",
            "phonetic": "[zaɪ̯n] / [iːɐ̯]",
            "gloss": "his & her (possessives)",
            "speakText": "sein, seine, ihr, ihre",
            "audioUrl": "",
            "whisper": "'Sein/seine' = his; 'ihr/ihre' = her. They add '-e' before feminine and plural nouns: 'seine Schwester' (his sister), 'ihr Bruder' (her brother)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the family introduction. Who is Herr Schmidt introducing?",
            "speakAudio": "Das ist meine Mutter",
            "options": ["This is my mother ('meine Mutter')", "This is my sister", "This is my grandmother"],
            "correct": 0,
            "explain": "'Das ist' (this is) + 'meine Mutter' (fem. my mother)."
        },
        {
            "prompt": "Listen to the plural umlaut. How does 'Bruder' change in the plural?",
            "speakAudio": "zwei Brüder",
            "options": ["The vowel fronted to umlaut [yː] ('zwei Brüder')", "It added -en without vowel change", "It remained identical"],
            "correct": 0,
            "explain": "The plural of 'Bruder' is 'Brüder' with umlaut ü [yː]."
        },
        {
            "prompt": "Listen to the accusative case inflection. Why is 'einen' used?",
            "speakAudio": "Ich habe einen Bruder",
            "options": ["Because 'Bruder' is the masculine direct object (accusative takes -en)!", "Because Bruder is feminine", "It is optional slang"],
            "correct": 0,
            "explain": "Transitive 'haben' requires the accusative: masculine 'ein/mein' becomes 'einen/meinen'."
        },
        {
            "prompt": "Listen to the affectionate elder terms. Who are 'Oma und Opa'?",
            "speakAudio": "Oma und Opa",
            "options": ["Grandma and Grandpa ('Oma und Opa')", "Mom and Dad", "Aunt and Uncle"],
            "correct": 0,
            "explain": "'Oma' is grandma and 'Opa' is grandpa."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'This is my father' (Das ist mein Vater)",
            "clue": "Herr Schmidt: 'Demonstrative Das ist, masculine mein, and Vater!'",
            "target": "Das ist mein Vater",
            "tokens": ["Das", "ist", "mein", "Vater", "meine", "Mutter"],
            "explain": "'Das ist' (this is) + 'mein' (masc. nom.) + 'Vater' (father)."
        },
        {
            "quest": "Build: 'I have a sister' (Ich habe eine Schwester)",
            "clue": "Herr Schmidt: 'Subject Ich, verb habe, feminine accusative eine Schwester!'",
            "target": "Ich habe eine Schwester",
            "tokens": ["Ich", "habe", "eine", "Schwester", "einen", "Bruder"],
            "explain": "'Ich habe' + 'eine Schwester' (accusative feminine takes -e)."
        },
        {
            "quest": "Build: 'His brother is friendly' (Sein Bruder ist freundlich)",
            "clue": "Herr Schmidt: 'Possessive Sein, Bruder, copula ist, adjective freundlich!'",
            "target": "Sein Bruder ist freundlich",
            "tokens": ["Sein", "Bruder", "ist", "freundlich", "Seine", "hat"],
            "explain": "'Sein Bruder' (his brother) + 'ist' (is) + 'freundlich' (friendly)."
        },
        {
            "quest": "Build: 'Where are your parents?' (Wo sind deine Eltern)",
            "clue": "Herr Schmidt: 'Interrogative Wo, plural verb sind, plural deine Eltern!'",
            "target": "Wo sind deine Eltern",
            "tokens": ["Wo", "sind", "deine", "Eltern", "ist", "mein"],
            "explain": "'Wo' (where) + 'sind' (are) + 'deine Eltern' (your parents [pl.])."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the German word for MOTHER (MUTTER):",
            "tiles": ["M", "U", "T", "T", "E", "R", "V"],
            "answer": "MUTTER",
            "gloss": "Mutter (mother)"
        },
        {
            "clue": "Spell the German word for FATHER (VATER):",
            "tiles": ["V", "A", "T", "E", "R", "M", "N"],
            "answer": "VATER",
            "gloss": "Vater (father)"
        },
        {
            "clue": "Spell the German word for BROTHER (BRUDER):",
            "tiles": ["B", "R", "U", "D", "E", "R", "S"],
            "answer": "BRUDER",
            "gloss": "Bruder (brother)"
        }
    ],
    "quiz": [
        {
            "q": "When does the possessive determiner 'mein' take the ending '-e' (meine) in German?",
            "options": [
                "Before feminine singular nouns (die Mutter $\\to$ meine Mutter) and all plural nouns (die Eltern $\\to$ meine Eltern)!",
                "Only before masculine nouns",
                "Only when speaking to elders"
            ],
            "correct": 0,
            "explain": "'Mein' takes '-e' in the nominative for feminine (meine Schwester) and plural (meine Brüder)."
        },
        {
            "q": "How does 'mein Bruder' change in the sentence 'Ich habe _____ Bruder' (I have a brother)?",
            "options": [
                "meinen Bruder (masculine direct objects take the accusative ending -en)!",
                "meine Bruder",
                "meinem Bruder"
            ],
            "correct": 0,
            "explain": "The direct object of 'haben' takes the accusative: masculine singular adds '-en' (meinen Bruder)."
        },
        {
            "q": "What common morphological process creates the plural forms of Vater (Väter), Mutter (Mütter), and Bruder (Brüder)?",
            "options": [
                "Umlaut vowel mutation (fronting of the back vowel a, u $\\to$ ä, ü)!",
                "Adding the suffix -s",
                "Doubling the consonant"
            ],
            "correct": 0,
            "explain": "German kinship nouns frequently mark plural exclusively or primarily through umlaut: Vater $\to$ Väter, Mutter $\to$ Mütter, Bruder $\to$ Brüder."
        },
        {
            "q": "What is the collective German noun for all of one's brothers and sisters combined?",
            "options": [
                "die Geschwister (plural noun: 'Ich habe keine Geschwister' = I have no siblings)!",
                "die Brüderschaft",
                "die Verwandten"
            ],
            "correct": 0,
            "explain": "'Geschwister' is the standard German collective term for siblings."
        },
        {
            "q": "In German, what do 'mein Mann' and 'meine Frau' mean in everyday conversation?",
            "options": [
                "My husband and my wife (as well as literally my man and my woman)!",
                "My boss and my colleague",
                "My son and my daughter"
            ],
            "correct": 0,
            "explain": "'Mann' and 'Frau' are the universal standard terms for husband and wife when combined with possessive determiners."
        }
    ]
}

# ==============================================================================
# STEP 6: PLACE TO DIALOGUE (MILESTONE CHECKPOINT & SYNTHESIS)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. WARAY-WARAY — STEP 6: PUROK MILESTONE DIALOGUE REALM
# ------------------------------------------------------------------------------

WARAY_STEP6 = {
    "sealName": "Purok Milestone Dialogue Seal",
    "guide": {
        "name": "Lolo Pedring",
        "role": "Master Storyteller & Coastal Navigator",
        "avatar": "⛵",
        "prompt": "Maupay nga adlaw! Welcome to our seaside balay-taberna milestone. Here we weave together everything learned across Steps 1 to 5: greetings, identity, family bonds, the days of the week (Lunes to Domingo), and counting into the hundreds and thousands ('gatos' and 'yukot')!"
    },
    "cards": [
        {
            "id": "war6_c1",
            "type": "number",
            "glyph": "100 — usa ka gatos",
            "phonetic": "[ʔu.ˈsa ka ˈɡa.tɔs]",
            "gloss": "one hundred • 100",
            "speakText": "usa ka gatos",
            "audioUrl": "",
            "whisper": "Native Waray base: 'gatos' = hundred. The numeral connects to the base with the ligature 'ka': 'usa ka gatos' (100), 'duha ka gatos' (200)."
        },
        {
            "id": "war6_c2",
            "type": "number",
            "glyph": "200 — duha ka gatos",
            "phonetic": "[dʊ.ˈha ka ˈɡa.tɔs]",
            "gloss": "two hundred • 200",
            "speakText": "duha ka gatos",
            "audioUrl": "",
            "whisper": "Two hundreds: 'duha' (2) + 'ka' + 'gatos' (100). In market money, speakers also use Kinatsila 'dos syentos'."
        },
        {
            "id": "war6_c3",
            "type": "number",
            "glyph": "500 — lima ka gatos",
            "phonetic": "[li.ˈma ka ˈɡa.tɔs]",
            "gloss": "five hundred • 500",
            "speakText": "lima ka gatos",
            "audioUrl": "",
            "whisper": "'Lima' (5) + 'ka' + 'gatos' (100). Or Spanish loan 'kinyentos pisos' for bills."
        },
        {
            "id": "war6_c4",
            "type": "number",
            "glyph": "1,000 — usa ka yukot",
            "phonetic": "[ʔu.ˈsa ka ˈju.kɔt]",
            "gloss": "one thousand • 1,000",
            "speakText": "usa ka yukot",
            "audioUrl": "",
            "whisper": "Ancient Austronesian root: 'yukot' represents 1,000 (also 'mil' in Spanish loans). 'Usa ka yukot nga salamat' = a thousand thanks!"
        },
        {
            "id": "war6_c5",
            "type": "weekday",
            "glyph": "Lunes & Martes",
            "phonetic": "[ˈlu.nɛs] / [ˈmaɾ.tɛs]",
            "gloss": "Monday & Tuesday",
            "speakText": "Lunes, Martes",
            "audioUrl": "",
            "whisper": "Days of the week are nativized Spanish loans. To say 'on Monday', use temporal marker 'hit': 'hit Lunes'."
        },
        {
            "id": "war6_c6",
            "type": "weekday",
            "glyph": "Miyerkules & Huwebes",
            "phonetic": "[mɪ.ˈjɛɾ.kʊ.lɛs] / [hʊ.ˈwɛ.bɛs]",
            "gloss": "Wednesday & Thursday",
            "speakText": "Miyerkules, Huwebes",
            "audioUrl": "",
            "whisper": "Spelled phonetically in modern Waray orthography: 'Miyerkules' (Wednesday) and 'Huwebes' (Thursday)."
        },
        {
            "id": "war6_c7",
            "type": "weekday",
            "glyph": "Biyernes, Sabado, Domingo",
            "phonetic": "[bɪ.ˈjɛɾ.nɛs], [ˈsa.ba.dɔ], [dɔ.ˈmiŋ.ɡɔ]",
            "gloss": "Friday, Saturday, Sunday",
            "speakText": "Biyernes, Sabado, Domingo",
            "audioUrl": "",
            "whisper": "Friday through Sunday: market days and family celebrations across Eastern Visayas."
        },
        {
            "id": "war6_c8",
            "type": "dialogue",
            "glyph": "Pira ini ngatanan?",
            "phonetic": "[ˈpi.ɾa ʔi.ˈni ŋa.ta.ˈnan]",
            "gloss": "How much is all of this?",
            "speakText": "Pira ini ngatanan",
            "audioUrl": "",
            "whisper": "Essential milestone market phrase: 'Pira' (how much/many) + 'ini' (this) + 'ngatanan' (all/everything)."
        },
        {
            "id": "war6_c9",
            "type": "dialogue",
            "glyph": "Maupay nga pag-abot!",
            "phonetic": "[ma.ʔʊ.ˈpaj ŋa paɡ.ˈʔa.bɔt]",
            "gloss": "Welcome! (Pleasant arrival)",
            "speakText": "Maupay nga pag-abot",
            "audioUrl": "",
            "whisper": "The traditional Visayan greeting of warm hospitality to arriving travelers."
        },
        {
            "id": "war6_c10",
            "type": "dialogue",
            "glyph": "Magkikita kita hit...",
            "phonetic": "[maɡ.ki.ˈki.ta ˈki.ta hɪt]",
            "gloss": "We will meet on... [weekday]",
            "speakText": "Magkikita kita hit",
            "audioUrl": "",
            "whisper": "Reduplicated future aspect verb: 'magkikita' (will see each other) + 'kita' (we inclusive) + 'hit' + [day]."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the market price. How much does it cost?",
            "speakAudio": "lima ka gatos ka pisos",
            "options": ["500 pesos ('lima ka gatos')", "50 pesos", "100 pesos"],
            "correct": 0,
            "explain": "'Lima' (5) + 'ka gatos' (hundred) = 500 pesos."
        },
        {
            "prompt": "Listen to the rendezvous day. On which day will they meet?",
            "speakAudio": "Magkikita kita hit Biyernes",
            "options": ["On Friday ('hit Biyernes')", "On Thursday ('Huwebes')", "On Saturday ('Sabado')"],
            "correct": 0,
            "explain": "'Biyernes' is Friday; 'hit Biyernes' means on Friday."
        },
        {
            "prompt": "Listen to the large numeral: 'usa ka yukot'. What number is it?",
            "speakAudio": "usa ka yukot",
            "options": ["1,000 (one thousand)", "100 (one hundred)", "10,000 (ten thousand)"],
            "correct": 0,
            "explain": "'Yukot' is the ancient Waray numerical root for 1,000."
        },
        {
            "prompt": "Listen to the hospitality phrase. What is being expressed?",
            "speakAudio": "Maupay nga pag-abot ha amon bungto",
            "options": ["Welcome to our town ('Maupay nga pag-abot')", "Goodbye my friend", "Good morning elders"],
            "correct": 0,
            "explain": "'Maupay nga pag-abot' literally translates to 'pleasant arrival' (Welcome)."
        }
    ],
    "arena": [
        {
            "quest": "Tavern Transaction: 'This costs one hundred pesos'",
            "clue": "Lolo Pedring: 'Assemble Usa ka gatos ka pisos ini!'",
            "target": "Usa ka gatos ka pisos ini",
            "tokens": ["Usa", "ka", "gatos", "pisos", "ini", "yukot", "duha"],
            "explain": "'Usa ka gatos' (100) + ligature 'ka' + 'pisos' (pesos) + 'ini' (this)."
        },
        {
            "quest": "Milestone Rendezvous: 'We will meet on Monday'",
            "clue": "Lolo Pedring: 'Future verb Magkikita, pronoun kita, temporal hit Lunes!'",
            "target": "Magkikita kita hit Lunes",
            "tokens": ["Magkikita", "kita", "hit", "Lunes", "Martes", "ako"],
            "explain": "'Magkikita' (will meet) + 'kita' (we inc.) + 'hit Lunes' (on Monday)."
        },
        {
            "quest": "Sanctuary Milestone: 'A thousand thanks to you'",
            "clue": "Lolo Pedring: 'Usa ka yukot nga salamat ha imo!'",
            "target": "Usa ka yukot nga salamat ha imo",
            "tokens": ["Usa", "ka", "yukot", "nga", "salamat", "ha", "imo", "gatos"],
            "explain": "'Usa ka yukot' (1,000) + linker 'nga' + 'salamat' (thanks) + 'ha imo' (to you)."
        },
        {
            "quest": "Market Inquiry: 'How much is all of this?'",
            "clue": "Lolo Pedring: 'Pira + ini + ngatanan!'",
            "target": "Pira ini ngatanan",
            "tokens": ["Pira", "ini", "ngatanan", "hain", "salamat"],
            "explain": "'Pira' (how much) + 'ini' (this) + 'ngatanan' (everything)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the native Waray number for ONE HUNDRED (GATOS):",
            "tiles": ["G", "A", "T", "O", "S", "Y", "U"],
            "answer": "GATOS",
            "gloss": "gatos (hundred)"
        },
        {
            "clue": "Spell the ancient Waray word for ONE THOUSAND (YUKOT):",
            "tiles": ["Y", "U", "K", "O", "T", "G", "A"],
            "answer": "YUKOT",
            "gloss": "yukot (thousand)"
        },
        {
            "clue": "Spell the weekday FRIDAY in Waray (BIYERNES):",
            "tiles": ["B", "I", "Y", "E", "R", "N", "E", "S"],
            "answer": "BIYERNES",
            "gloss": "Biyernes (Friday)"
        }
    ],
    "quiz": [
        {
            "q": "What grammatical ligature links numerals like 'usa' and 'duha' to the counting base 'gatos' (hundred)?",
            "options": [
                "The ligature 'ka' (e.g. 'usa ka gatos', 'duha ka gatos')!",
                "The preposition 'ha'",
                "The marker 'hin'"
            ],
            "correct": 0,
            "explain": "The ligature 'ka' links numerals to units and nouns throughout Visayan grammar."
        },
        {
            "q": "Which temporal marker precedes days of the week when scheduling an event (e.g. 'on Monday')?",
            "options": [
                "hit (e.g. 'hit Lunes' = on Monday)!",
                "ha",
                "kan"
            ],
            "correct": 0,
            "explain": "'Hit' marks indefinite oblique/temporal phrases such as days of the week."
        },
        {
            "q": "What is the native Austronesian Waray word for 'thousand' ('1,000')?",
            "options": [
                "yukot (usa ka yukot = 1,000)!",
                "gatos",
                "mil"
            ],
            "correct": 0,
            "explain": "'Yukot' is the indigenous Waray-Waray term for one thousand."
        },
        {
            "q": "How do you form the future aspect of the verb 'kita' (to see / meet) for mutual appointments?",
            "options": [
                "Magkikita (by prefixing mag- and reduplicating the first CV syllable 'ki-')!",
                "Kumita",
                "Nakakita"
            ],
            "correct": 0,
            "explain": "Contemplated/future aspect in Waray uses CV reduplication with the actor focus prefix: mag-ki-kita."
        },
        {
            "q": "How do you ask 'How much is all of this?' at a traditional market in Samar or Leyte?",
            "options": [
                "Pira ini ngatanan?",
                "Hain ka makadto?",
                "Hin-o ito?"
            ],
            "correct": 0,
            "explain": "'Pira ini ngatanan?' is the standard conversational inquiry for total prices."
        }
    ]
}

# ------------------------------------------------------------------------------
# 2. FRENCH — STEP 6: GRAND CARREFOUR DE PARIS MILESTONE REALM
# ------------------------------------------------------------------------------

FRENCH_STEP6 = {
    "sealName": "Grand Carrefour des Lumières Seal",
    "guide": {
        "name": "Madame Claudine",
        "role": "Auberge Host & Parisian Salonniere",
        "avatar": "☕",
        "prompt": "Bienvenue au Grand Carrefour de Paris ! Here at Step 6, we synthesize our entire journey: greeting travelers, sharing origins and family stories, planning meetings across the days of the week (lundi à dimanche), and counting from cent to mille in authentic bistro dialogue."
    },
    "cards": [
        {
            "id": "fr6_c1",
            "type": "number",
            "glyph": "100 — cent",
            "phonetic": "[sɑ̃]",
            "gloss": "one hundred • 100",
            "speakText": "cent",
            "audioUrl": "",
            "whisper": "Pronounced with nasal vowel [ɑ̃]: 'cent'. The final 't' is silent unless liaison occurs before a vowel."
        },
        {
            "id": "fr6_c2",
            "type": "number",
            "glyph": "200 — deux cents",
            "phonetic": "[dø sɑ̃]",
            "gloss": "two hundred • 200",
            "speakText": "deux cents",
            "audioUrl": "",
            "whisper": "Orthography rule: 'cent' takes an 's' when multiplied and terminating ('deux cents'), but loses it if followed by another number ('deux cent cinq')!"
        },
        {
            "id": "fr6_c3",
            "type": "number",
            "glyph": "500 — cinq cents",
            "phonetic": "[sɛ̃k sɑ̃]",
            "gloss": "five hundred • 500",
            "speakText": "cinq cents",
            "audioUrl": "",
            "whisper": "'Cinq' [sɛ̃k] + 'cents' [sɑ̃]. Common denomination in currency and distances."
        },
        {
            "id": "fr6_c4",
            "type": "number",
            "glyph": "1,000 — mille",
            "phonetic": "[mil]",
            "gloss": "one thousand • 1,000",
            "speakText": "mille",
            "audioUrl": "",
            "whisper": "Golden rule: 'mille' is 100% INVARIABLE! It NEVER takes an 's': deux mille (2,000), dix mille (10,000). Pronounced [mil] with clear 'l'."
        },
        {
            "id": "fr6_c5",
            "type": "weekday",
            "glyph": "lundi & mardi",
            "phonetic": "[lœ̃.di] / [maʁ.di]",
            "gloss": "Monday & Tuesday",
            "speakText": "lundi, mardi",
            "audioUrl": "",
            "whisper": "Days of the week are NOT capitalized in French! Lundi (day of the Moon), mardi (day of Mars)."
        },
        {
            "id": "fr6_c6",
            "type": "weekday",
            "glyph": "mercredi & jeudi",
            "phonetic": "[mɛʁ.kʁə.di] / [ʒø.di]",
            "gloss": "Wednesday & Thursday",
            "speakText": "mercredi, jeudi",
            "audioUrl": "",
            "whisper": "Mercredi (day of Mercury) and jeudi (day of Jupiter). For single events, do not use prepositions: 'Je viens mercredi'."
        },
        {
            "id": "fr6_c7",
            "type": "weekday",
            "glyph": "vendredi, samedi, dimanche",
            "phonetic": "[vɑ̃.dʁə.di], [sam.di], [di.mɑ̃ʃ]",
            "gloss": "Friday, Saturday, Sunday",
            "speakText": "vendredi, samedi, dimanche",
            "audioUrl": "",
            "whisper": "Vendredi (Venus), samedi (Sabbath), dimanche (Lord's day). 'Le dimanche' means 'on Sundays' (habitual)!"
        },
        {
            "id": "fr6_c8",
            "type": "dialogue",
            "glyph": "Combien coûte... ?",
            "phonetic": "[kɔ̃.bjɛ̃ kut]",
            "gloss": "How much does ... cost?",
            "speakText": "Combien coûte",
            "audioUrl": "",
            "whisper": "'Combien' (how much/many) + 'coûte' (costs). Essential for bistros, boutiques, and bakeries."
        },
        {
            "id": "fr6_c9",
            "type": "dialogue",
            "glyph": "Mille mercis !",
            "phonetic": "[mil mɛʁ.si]",
            "gloss": "A thousand thanks!",
            "speakText": "Mille mercis",
            "audioUrl": "",
            "whisper": "The classic, elegant French expression of deep gratitude: 'Mille mercis pour tout !'"
        },
        {
            "id": "fr6_c10",
            "type": "dialogue",
            "glyph": "À lundi prochain !",
            "phonetic": "[a lœ̃.di pʁɔ.ʃɛ̃]",
            "gloss": "See you next Monday!",
            "speakText": "À lundi prochain",
            "audioUrl": "",
            "whisper": "'À' + day of the week means 'See you on [day]': 'À demain' (see you tomorrow), 'À vendredi' (see you Friday)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the price. How many euros does it cost?",
            "speakAudio": "cinq cents euros",
            "options": ["500 euros ('cinq cents')", "50 euros", "100 euros"],
            "correct": 0,
            "explain": "'Cinq cents' is 500."
        },
        {
            "prompt": "Listen to the rendezvous time. On which day is the meeting?",
            "speakAudio": "Rendez-vous mercredi à dix heures",
            "options": ["Wednesday ('mercredi')", "Tuesday ('mardi')", "Thursday ('jeudi')"],
            "correct": 0,
            "explain": "'Mercredi' is Wednesday in French."
        },
        {
            "prompt": "Listen to the expression of gratitude. What did Madame Claudine say?",
            "speakAudio": "Mille mercis mon ami",
            "options": ["A thousand thanks, my friend ('Mille mercis')", "One hundred apologies", "See you on Monday"],
            "correct": 0,
            "explain": "'Mille mercis' expresses 'a thousand thanks'."
        },
        {
            "prompt": "Listen to the date question. What is being asked?",
            "speakAudio": "Quel jour sommes-nous aujourd'hui",
            "options": ["What day of the week is it today?", "What time is it?", "How much does this cost?"],
            "correct": 0,
            "explain": "'Quel jour sommes-nous ?' asks what day of the week it is."
        }
    ],
    "arena": [
        {
            "quest": "Tavern Rendezvous: 'We meet on Monday'",
            "clue": "Madame Claudine: 'Reflexive verb Nous nous retrouvons followed by lundi!'",
            "target": "Nous nous retrouvons lundi",
            "tokens": ["Nous", "nous", "retrouvons", "lundi", "mardi", "le"],
            "explain": "Single specific days take no preposition in French: 'lundi'."
        },
        {
            "quest": "Price Inquiry: 'That costs two hundred euros'",
            "clue": "Madame Claudine: 'Cela coûte deux cents euros!'",
            "target": "Cela coûte deux cents euros",
            "tokens": ["Cela", "coûte", "deux", "cents", "euros", "cent", "mille"],
            "explain": "'deux cents' takes terminal plural -s; 'euros' takes -s."
        },
        {
            "quest": "Crossroads Hospitality: 'A thousand thanks my friend'",
            "clue": "Madame Claudine: 'Invariable Mille, plural mercis, mon ami!'",
            "target": "Mille mercis mon ami",
            "tokens": ["Mille", "mercis", "mon", "ami", "cent", "ma"],
            "explain": "'Mille' never takes -s; 'mercis' is plural; 'mon ami' = my friend."
        },
        {
            "quest": "Appointment Setting: 'See you Friday at the café'",
            "clue": "Madame Claudine: 'Preposition À, weekday vendredi, au café!'",
            "target": "À vendredi au café",
            "tokens": ["À", "vendredi", "au", "café", "le", "dans"],
            "explain": "'À' + day means 'See you on [day]'; 'au café' = at the café."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the French number for ONE HUNDRED (CENT):",
            "tiles": ["C", "E", "N", "T", "S", "M"],
            "answer": "CENT",
            "gloss": "cent (hundred)"
        },
        {
            "clue": "Spell the invariable French number for ONE THOUSAND (MILLE):",
            "tiles": ["M", "I", "L", "L", "E", "C", "T"],
            "answer": "MILLE",
            "gloss": "mille (thousand)"
        },
        {
            "clue": "Spell the French weekday WEDNESDAY (MERCREDI):",
            "tiles": ["M", "E", "R", "C", "R", "E", "D", "I"],
            "answer": "MERCREDI",
            "gloss": "mercredi (Wednesday)"
        }
    ],
    "quiz": [
        {
            "q": "When does the French number 'cent' take a final plural '-s'?",
            "options": [
                "When it is multiplied AND ends the whole number (e.g. 'deux cents' = 200, but 'deux cent cinq' = 205)!",
                "Always, whenever it is plural",
                "Never; numbers in French never take -s"
            ],
            "correct": 0,
            "explain": "'Cent' and 'vingt' take an -s only when multiplied and not followed by another cardinal number."
        },
        {
            "q": "Does the numeral 'mille' (1,000) ever take a plural '-s' in French?",
            "options": [
                "No, 'mille' is strictly invariable (deux mille, trois mille, dix mille)!",
                "Yes, it takes -s above 2,000",
                "Only in informal slang"
            ],
            "correct": 0,
            "explain": "'Mille' is entirely invariable in French orthography."
        },
        {
            "q": "What is the semantic difference between saying 'lundi' and 'le lundi'?",
            "options": [
                "'Lundi' refers to this coming Monday; 'le lundi' means every Monday (habitual action)!",
                "'Le lundi' is formal while 'lundi' is disrespectful",
                "They are completely interchangeable"
            ],
            "correct": 0,
            "explain": "Using the definite article with a day of the week indicates a recurring, habitual event: le lundi = on Mondays."
        },
        {
            "q": "Are the names of the days of the week capitalized in French sentences?",
            "options": [
                "No, days of the week and months are written in lowercase (lundi, mardi, janvier)!",
                "Yes, always capitalized like in English",
                "Only on weekends (samedi, dimanche)"
            ],
            "correct": 0,
            "explain": "French does not capitalize days of the week, months, or language names."
        },
        {
            "q": "How do you say 'See you on Thursday!' in natural French?",
            "options": [
                "À jeudi !",
                "Sur jeudi !",
                "Pour jeudi !"
            ],
            "correct": 0,
            "explain": "The preposition 'à' is universally paired with time words for future rendezvous: À bientôt, À demain, À jeudi."
        }
    ]
}

# ------------------------------------------------------------------------------
# 3. LATIN — STEP 6: FORUM ROMĀNUM COLLOQUIUM REALM
# ------------------------------------------------------------------------------

LATIN_STEP6 = {
    "sealName": "Forum Romanum Colloquium Seal",
    "guide": {
        "name": "Marcus",
        "role": "Forum Tribune & Taberna Keeper",
        "avatar": "🏛️",
        "prompt": "Salvēte ad Forum Romānum! Stand at the golden milestone (Mīliārium Aureum) where all imperial roads converge. At this 6th milestone, synthesize greetings, family lineage, the planetary days of the week (diēs Lūnae to diēs Sōlis), and count sesterces up to mīlle!"
    },
    "cards": [
        {
            "id": "lat6_c1",
            "type": "number",
            "glyph": "100 — centum [C]",
            "phonetic": "[ˈkɛn.tʊm]",
            "gloss": "one hundred • 100 (Roman C)",
            "speakText": "centum",
            "audioUrl": "",
            "whisper": "Indeclinable numeral: 'centum hominēs' (100 people). Roman numeral C (from initial letter of centum)."
        },
        {
            "id": "lat6_c2",
            "type": "number",
            "glyph": "200 — ducentī, -ae, -a",
            "phonetic": "[dʊˈkɛn.tiː]",
            "gloss": "two hundred • 200 (CC)",
            "speakText": "ducenti",
            "audioUrl": "",
            "whisper": "Declinable 1st/2nd declension plural adjective: duo + centum = ducentī (m), ducentae (f), ducenta (n)."
        },
        {
            "id": "lat6_c3",
            "type": "number",
            "glyph": "500 — quīngentī, -ae, -a [D]",
            "phonetic": "[kwiːŋˈɡɛn.tiː]",
            "gloss": "five hundred • 500 (Roman D)",
            "speakText": "quingenti",
            "audioUrl": "",
            "whisper": "From quīnque + centum. Roman numeral D represents 500."
        },
        {
            "id": "lat6_c4",
            "type": "number",
            "glyph": "1,000 — mīlle [M]",
            "phonetic": "[ˈmiːl.lɛ]",
            "gloss": "one thousand • 1,000 (Roman M)",
            "speakText": "mille",
            "audioUrl": "",
            "whisper": "Singular 'mīlle' is an indeclinable adjective ('mīlle passūs' = 1,000 paces, a Roman mile). Plural 'mīlia' is a 3rd declension neuter noun taking a genitive: 'duo mīlia passuum'!"
        },
        {
            "id": "lat6_c5",
            "type": "weekday",
            "glyph": "diēs Lūnae & diēs Martis",
            "phonetic": "[ˈdɪ.eːs ˈluː.nae̯] / [ˈmar.tɪs]",
            "gloss": "Monday & Tuesday",
            "speakText": "dies Lunae, dies Martis",
            "audioUrl": "",
            "whisper": "Planetary week: diēs (day, 5th decl.) + genitive of deity: Lūna (Moon) and Mars (god of war)."
        },
        {
            "id": "lat6_c6",
            "type": "weekday",
            "glyph": "diēs Mercuriī & diēs Iovis",
            "phonetic": "[mɛrˈkʊ.rɪ.iː] / [ˈjɔ.wɪs]",
            "gloss": "Wednesday & Thursday",
            "speakText": "dies Mercurii, dies Iovis",
            "audioUrl": "",
            "whisper": "Mercury's day (commerce and travelers) and Jupiter's day (king of the gods, genitive Iovis)."
        },
        {
            "id": "lat6_c7",
            "type": "weekday",
            "glyph": "diēs Veneris, Sāturnī, Sōlis",
            "phonetic": "[ˈwɛ.nɛ.rɪs], [saːˈtʊr.niː], [ˈsoː.lɪs]",
            "gloss": "Friday, Saturday, Sunday",
            "speakText": "dies Veneris, dies Saturni, dies Solis",
            "audioUrl": "",
            "whisper": "Venus (goddess of love), Saturn (god of agriculture), and Sol (the radiant Sun)."
        },
        {
            "id": "lat6_c8",
            "type": "dialogue",
            "glyph": "Quantī cōnstat?",
            "phonetic": "[ˈkwan.tiː ˈkoːn.stat]",
            "gloss": "How much does it cost?",
            "speakText": "Quanti constat",
            "audioUrl": "",
            "whisper": "'Quantī' is the genitive of price: 'At what price does it stand / cost?'"
        },
        {
            "id": "lat6_c9",
            "type": "dialogue",
            "glyph": "Mīlle grātiās tibi agō!",
            "phonetic": "[ˈmiːl.lɛ ˈɡraː.tɪ.aːs ˈtɪ.bɪ ˈa.ɡoː]",
            "gloss": "I give you a thousand thanks!",
            "speakText": "Mille gratias tibi ago",
            "audioUrl": "",
            "whisper": "The grand Roman expression of heartfelt gratitude: 'Mīlle grātiās tibi agō!'"
        },
        {
            "id": "lat6_c10",
            "type": "dialogue",
            "glyph": "Quō vadis, viātor?",
            "phonetic": "[kwoː ˈwa.dɪs wi.ˈaː.tɔr]",
            "gloss": "Where are you going, traveler?",
            "speakText": "Quo vadis, viator",
            "audioUrl": "",
            "whisper": "'Quō' indicates motion towards a destination ('whither'); 'vadis' from vadere (to go/walk); 'viātor' = traveler."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the forum transaction. How much was paid in denarii?",
            "speakAudio": "centum denariis constat",
            "options": ["100 denarii ('centum')", "50 denarii", "1,000 denarii ('mīlle')"],
            "correct": 0,
            "explain": "'Centum' is the Roman numeral 100."
        },
        {
            "prompt": "Listen to the meeting day in the Forum. Which weekday is spoken?",
            "speakAudio": "Die Martis in Forum conveniemus",
            "options": ["On Tuesday ('diē Martis')", "On Monday ('diē Lūnae')", "On Wednesday ('diē Mercuriī')"],
            "correct": 0,
            "explain": "'Diē Martis' is the ablative of time: on Tuesday (Mars's day)."
        },
        {
            "prompt": "Listen to the Roman measurement: 'mīlle passūs'. What distance is this?",
            "speakAudio": "mille passus",
            "options": ["A Roman mile ('a thousand paces')", "A stadium", "Ten cubits"],
            "correct": 0,
            "explain": "'Mīlle passūs' (a thousand double-steps) is the historical Roman mile (ca. 1,480 meters)."
        },
        {
            "prompt": "Listen to the mythological weekday. Which deity presides over 'diēs Iovis'?",
            "speakAudio": "dies Iovis",
            "options": ["Jupiter / Jove (Thursday)", "Mars (Tuesday)", "Saturn (Saturday)"],
            "correct": 0,
            "explain": "'Iovis' is the genitive of Iuppiter: Jove's day (Thursday)."
        }
    ],
    "arena": [
        {
            "quest": "Forum Meeting: 'We meet in the Forum on Monday'",
            "clue": "Marcus: 'Conveniēmus in Forō diē Lūnae!'",
            "target": "Conveniēmus in Forō diē Lūnae",
            "tokens": ["Conveniēmus", "in", "Forō", "diē", "Lūnae", "Martis", "ad"],
            "explain": "Ablative of time: 'diē Lūnae' (on Monday); 'in Forō' = in the Forum."
        },
        {
            "quest": "Price in the Taberna: 'It costs five hundred sesterces'",
            "clue": "Marcus: 'Ablative of price Quīngentīs sestertiīs cōnstat!'",
            "target": "Quīngentīs sestertiīs cōnstat",
            "tokens": ["Quīngentīs", "sestertiīs", "cōnstat", "centum", "mīlle"],
            "explain": "'Quīngentīs sestertiīs' (ablative of price) + 'cōnstat' (costs)."
        },
        {
            "quest": "Milestone Gratitude: 'I give you a thousand thanks'",
            "clue": "Marcus: 'Accusative plural Mīlle grātiās, dative tibi agō!'",
            "target": "Mīlle grātiās tibi agō",
            "tokens": ["Mīlle", "grātiās", "tibi", "agō", "centum", "mihi"],
            "explain": "'Mīlle grātiās' (a thousand thanks) + 'tibi agō' (I render to you)."
        },
        {
            "quest": "Traveler Inquiry: 'Where are you going traveler?'",
            "clue": "Marcus: 'Quō vadis viātor!'",
            "target": "Quō vadis viātor",
            "tokens": ["Quō", "vadis", "viātor", "ubi", "amīcus"],
            "explain": "'Quō' (whither) + 'vadis' (are you going) + 'viātor' (vocative traveler)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the Latin numeral word for ONE HUNDRED (CENTUM):",
            "tiles": ["C", "E", "N", "T", "U", "M", "S"],
            "answer": "CENTUM",
            "gloss": "centum (hundred)"
        },
        {
            "clue": "Spell the Latin word for ONE THOUSAND (MĪLLE):",
            "tiles": ["M", "Ī", "L", "L", "E", "C", "T"],
            "answer": "MĪLLE",
            "gloss": "mīlle (thousand)"
        },
        {
            "clue": "Spell the genitive of Mercury in WEDNESDAY (MERCURIĪ):",
            "tiles": ["M", "E", "R", "C", "U", "R", "I", "Ī"],
            "answer": "MERCURIĪ",
            "gloss": "Mercuriī (Mercury's [day])"
        }
    ],
    "quiz": [
        {
            "q": "What is the crucial syntactic difference between singular 'mīlle' and plural 'mīlia' in Latin?",
            "options": [
                "Singular 'mīlle' is an indeclinable adjective ('mīlle mīlitēs'); plural 'mīlia' is a neuter 3rd declension noun that takes a genitive ('duo mīlia mīlitum')!",
                "'Mīlle' is a verb while 'mīlia' is a preposition",
                "Both decline as 1st declension feminine nouns"
            ],
            "correct": 0,
            "explain": "Classical Latin treats mīlle as an indeclinable adjective in the singular, but plural mīlia as a neuter noun requiring a partitive genitive."
        },
        {
            "q": "What Roman grammatical case expresses 'time when' (e.g. 'on Monday' $\to$ 'diē Lūnae')?",
            "options": [
                "The Ablative case without a preposition (Ablative of Time When: diē Lūnae)!",
                "The Accusative of duration",
                "The Dative of possession"
            ],
            "correct": 0,
            "explain": "Time when is regularly expressed by the ablative case without a preposition in classical Latin."
        },
        {
            "q": "After which planetary celestial deities are the Roman days of the week named?",
            "options": [
                "The Sun, Moon, Mars, Mercury, Jupiter, Venus, and Saturn!",
                "The Olympian muses",
                "Roman emperors starting with Augustus"
            ],
            "correct": 0,
            "explain": "The Hellenistic and Roman 7-day planetary week honored the seven classical celestial wanderers."
        },
        {
            "q": "What was the 'Mīliārium Aureum' (Golden Milestone) erected by Augustus in the Roman Forum?",
            "options": [
                "The central monument from which all major Roman roads and road distances were measured across the Empire!",
                "A temple for storing gold bullion",
                "A boundary marker for foreign merchants"
            ],
            "correct": 0,
            "explain": "The Golden Milestone stood at the heart of Rome as the zero-point of the imperial road network ('All roads lead to Rome')."
        },
        {
            "q": "How does 'centum' decline in Latin compared to 'ducentī' and 'quīngentī'?",
            "options": [
                "'Centum' is completely indeclinable; 'ducentī' and 'quīngentī' decline like plural adjectives in -ī, -ae, -a!",
                "All of them decline as 3rd declension nouns",
                "None of them decline at all"
            ],
            "correct": 0,
            "explain": "Centum never changes form, but the hundreds (ducentī, trecentī, quīngentī...) decline as standard 1st/2nd declension plurals."
        }
    ]
}

# ------------------------------------------------------------------------------
# 4. HEBREW — STEP 6: SHA'AR YAFO MILESTONE DIALOGUE REALM
# ------------------------------------------------------------------------------

HEBREW_STEP6 = {
    "sealName": "Tzomet Yerushalayim Milestone Seal",
    "guide": {
        "name": "Eli",
        "role": "Mahane Yehuda Host & Storyteller",
        "avatar": "🍷",
        "prompt": "Shalom uv'ruchim ha-ba'im! Welcome to our Jerusalem crossroads milestone. Here we bring together everything from Steps 1 to 5: greeting friends, family origins, the seven days of the week (yom rishón through yom shabát), and counting shekels from me'áh (100) to élef (1,000)!"
    },
    "cards": [
        {
            "id": "heb6_c1",
            "type": "number",
            "glyph": "100 — מֵאָה",
            "phonetic": "me'áh [meˈʔa]",
            "gloss": "one hundred • 100",
            "speakText": "מאה",
            "audioUrl": "",
            "whisper": "Feminine noun: 'me'áh'. Hundreds plural is 'me'ót' (מֵאוֹת): shlosh me'ót (300), arba me'ót (400)."
        },
        {
            "id": "heb6_c2",
            "type": "number",
            "glyph": "200 — מָאתַיִם",
            "phonetic": "matáyim [maˈtajim]",
            "gloss": "two hundred • 200",
            "speakText": "מאתיים",
            "audioUrl": "",
            "whisper": "Ancient Semitic dual form with suffix '-áyim': 'matáyim' (two hundreds). Spelled מָאתַיִם."
        },
        {
            "id": "heb6_c3",
            "type": "number",
            "glyph": "500 — חֲמֵשׁ מֵאוֹת",
            "phonetic": "chamesh me'ót [χaˈmeʃ meˈʔot]",
            "gloss": "five hundred • 500",
            "speakText": "חמש מאות",
            "audioUrl": "",
            "whisper": "Construct pairing: feminine numeral 'chamesh' (5) + plural 'me'ót' (hundreds) = 500."
        },
        {
            "id": "heb6_c4",
            "type": "number",
            "glyph": "1,000 — אֶלֶף",
            "phonetic": "élef [ˈʔe.lef]",
            "gloss": "one thousand • 1,000",
            "speakText": "אלף",
            "audioUrl": "",
            "whisper": "Masculine noun: 'élef'. Plural: alafím (אֲלָפִים). Dual 2,000 is 'álpayim' (אַלְפַּיִם). 'Élef todót' = a thousand thanks!"
        },
        {
            "id": "heb6_c5",
            "type": "weekday",
            "glyph": "יוֹם רִאשׁוֹן וְשֵׁנִי",
            "phonetic": "yom rishón [jom ʁiˈʃon] / yom shení",
            "gloss": "Sunday & Monday (Days 1 & 2)",
            "speakText": "יום ראשון, יום שני",
            "audioUrl": "",
            "whisper": "Hebrew week begins on Sunday ('yom rishón' = first day). Monday is 'yom shení' (second day). Workweek runs Sunday through Thursday!"
        },
        {
            "id": "heb6_c6",
            "type": "weekday",
            "glyph": "יוֹם שְׁלִישִׁי וּרְבִיעִי",
            "phonetic": "yom shlishí [ʃliˈʃi] / yom revi'í [ʁviˈʕi]",
            "gloss": "Tuesday & Wednesday (Days 3 & 4)",
            "speakText": "יום שלישי, יום רביעי",
            "audioUrl": "",
            "whisper": "Third day (Tuesday) and fourth day (Wednesday). To say 'on Tuesday', prefix בְּ-: 'b'-yom shlishí'."
        },
        {
            "id": "heb6_c7",
            "type": "weekday",
            "glyph": "יוֹם חֲמִישִׁי, שִׁשִּׁי, שַׁבָּת",
            "phonetic": "chamishí, shishí, shabát",
            "gloss": "Thursday, Friday, Saturday",
            "speakText": "יום חמישי, יום שישי, שבת",
            "audioUrl": "",
            "whisper": "Fifth day (Thursday), sixth day (Friday eve), and the climax of the week: 'yom shabát' (the holy Sabbath rest)."
        },
        {
            "id": "heb6_c8",
            "type": "dialogue",
            "glyph": "כַּמָּה זֶה עוֹלֶה?",
            "phonetic": "kámah zeh olēh? [ˈka.ma ze ʔoˈle]",
            "gloss": "How much does this cost?",
            "speakText": "כמה זה עולה",
            "audioUrl": "",
            "whisper": "'Kámah' (how much) + 'zeh' (this) + 'olēh' (costs / goes up). The universal market inquiry in Israel."
        },
        {
            "id": "heb6_c9",
            "type": "dialogue",
            "glyph": "תּוֹדָה רַבָּה!",
            "phonetic": "todáh rabáh! [toˈda ʁaˈba]",
            "gloss": "Thank you very much!",
            "speakText": "תודה רבה",
            "audioUrl": "",
            "whisper": "'Todáh' (thanks) + feminine adjective 'rabáh' (great/much). Hearty response: 'b'vakashá' (you are welcome)."
        },
        {
            "id": "heb6_c10",
            "type": "dialogue",
            "glyph": "נִפְגַּשׁ בְּיוֹם...",
            "phonetic": "nipagēsh b'-yom... [nip'ɡeʃ beˈjom]",
            "gloss": "We will meet on... [weekday]",
            "speakText": "נפגש ביום",
            "audioUrl": "",
            "whisper": "Future 1st-person plural verb: 'nipagēsh' (we shall meet) + 'b'-yom' + [day name]."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the price. How many shekels is the item?",
            "speakAudio": "מאתיים שקל",
            "options": ["200 shekels ('matáyim')", "100 shekels ('me'áh')", "500 shekels ('chamesh me'ót')"],
            "correct": 0,
            "explain": "'מאתיים' (matáyim) is the dual form for 200."
        },
        {
            "prompt": "Listen to the rendezvous day. On which day will they meet?",
            "speakAudio": "נפגש ביום שלישי",
            "options": ["On Tuesday ('yom shlishí' — 3rd day)", "On Sunday ('yom rishón')", "On Wednesday ('yom revi'í')"],
            "correct": 0,
            "explain": "'יום שלישי' (yom shlishí) is Tuesday (the 3rd day)."
        },
        {
            "prompt": "Listen to the thousand count: 'élef'. What number was spoken?",
            "speakAudio": "אלף שקל",
            "options": ["1,000 ('élef')", "100 ('me'áh')", "10,000 ('aséret alafím')"],
            "correct": 0,
            "explain": "'אלף' (élef) is 1,000."
        },
        {
            "prompt": "Listen to the classic Friday afternoon greeting. What is wished?",
            "speakAudio": "שבת שלום ומבורך",
            "options": ["Peaceful and blessed Sabbath ('Shabát Shalóm')", "Happy New Year", "Good morning"],
            "correct": 0,
            "explain": "'Shabát Shalóm' is the traditional Sabbath greeting."
        }
    ],
    "arena": [
        {
            "quest": "Appointment at the Market: 'We will meet on Sunday'",
            "clue": "Eli: 'Future nipagēsh + prepositional phrase b'-yom rishón!'",
            "target": "נפגש ביום ראשון",
            "tokens": ["נפגש", "ביום", "ראשון", "שני", "שלום"],
            "explain": "'נפגש' (we will meet) + 'ביום ראשון' (on Sunday - 1st day)."
        },
        {
            "quest": "Transaction at Mahane Yehuda: 'This costs two hundred shekels'",
            "clue": "Eli: 'Assemble Zeh oleh matayim shekel!'",
            "target": "זה עולה מאתיים שקל",
            "tokens": ["זה", "עולה", "מאתיים", "שקל", "מאה", "אלף"],
            "explain": "'זה עולה' (this costs) + 'מאתיים' (200) + 'שקל' (shekels)."
        },
        {
            "quest": "Jerusalem Milestone: 'A thousand thanks my friend'",
            "clue": "Eli: 'Elef todot chaver sheli!'",
            "target": "אלף תודות חבר שלי",
            "tokens": ["אלף", "תודות", "חבר", "שלי", "מאה", "שלום"],
            "explain": "'אלף תודות' (a thousand thanks) + 'חבר שלי' (my friend)."
        },
        {
            "quest": "Price Inquiry: 'How much does this cost?'",
            "clue": "Eli: 'Kamah zeh oleh!'",
            "target": "כמה זה עולה",
            "tokens": ["כמה", "זה", "עולה", "איפה", "תודה"],
            "explain": "'כמה' (how much) + 'זה' (this) + 'עולה' (costs)."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the Hebrew word for ONE HUNDRED (ME'ÁH -> מאה):",
            "tiles": ["מ", "א", "ה", "ל", "ף"],
            "answer": "מאה",
            "gloss": "מֵאָה (hundred)"
        },
        {
            "clue": "Assemble the Hebrew word for ONE THOUSAND (ÉLEF -> אלף):",
            "tiles": ["א", "ל", "ף", "מ", "ה"],
            "answer": "אלף",
            "gloss": "אֶלֶף (thousand)"
        },
        {
            "clue": "Assemble the Hebrew word for FIRST DAY / SUNDAY (RISHÓN -> ראשון):",
            "tiles": ["ר", "א", "ש", "ו", "ן", "י", "ם"],
            "answer": "ראשון",
            "gloss": "רִאשׁוֹן (first / Sunday)"
        }
    ],
    "quiz": [
        {
            "q": "On which day does the traditional and commercial week begin in Israel?",
            "options": [
                "Sunday ('yom rishón' — literally the First Day)!",
                "Monday ('yom shení')",
                "Saturday ('yom shabát')"
            ],
            "correct": 0,
            "explain": "The Hebrew week strictly numbers days starting from Sunday (Day 1) through Friday (Day 6), culminating in Shabbat."
        },
        {
            "q": "What morphological suffix produces 'matáyim' (200) and 'álpayim' (2,000) in Hebrew?",
            "options": [
                "The ancient Semitic dual suffix '-áyim' (-ַיִם)!",
                "The plural suffix '-im'",
                "The feminine suffix '-ot'"
            ],
            "correct": 0,
            "explain": "Hebrew preserves the dual suffix -áyim for paired body parts, time periods (yomáyim, shnatáyim), and hundreds/thousands."
        },
        {
            "q": "Which prefix preposition attaches to weekday names to mean 'on [day]' (e.g. 'on Monday')?",
            "options": [
                "The inseparable prefix בְּ- (b'-) — e.g. 'b'-yom shení' (ביום שני)!",
                "The prefix לְ- (l'-)",
                "The preposition 'im' (עם)"
            ],
            "correct": 0,
            "explain": "The preposition בְּ- (in/on) attaches directly to yom: בְּיוֹם רִאשׁוֹן (on Sunday)."
        },
        {
            "q": "What is the plural form of 'me'áh' (100) used when counting 300–900 in Hebrew?",
            "options": [
                "me'ót (מֵאוֹת) — e.g. shlosh me'ót (300), chamesh me'ót (500)!",
                "me'im",
                "alafim"
            ],
            "correct": 0,
            "explain": "Me'áh takes the feminine plural suffix -ót: me'ót."
        },
        {
            "q": "What is the standard response when someone tells you 'todáh rabáh' (thank you very much)?",
            "options": [
                "b'vakashá (בְּבַקָּשָׁה — you're welcome / please)!",
                "shalom",
                "ken"
            ],
            "correct": 0,
            "explain": "'B'vakashá' is the polite formula for 'you are welcome' or 'please'."
        }
    ]
}

# ------------------------------------------------------------------------------
# 5. CHINESE — STEP 6: JADE TEAHOUSE MILESTONE DIALOGUE REALM
# ------------------------------------------------------------------------------

CHINESE_STEP6 = {
    "sealName": "Jade Pavilion Cháguǎn Milestone Seal",
    "guide": {
        "name": "Master Lao",
        "role": "Grand Teahouse Host & Philosopher",
        "avatar": "🍵",
        "prompt": "Huānyíng línmen! Welcome to the Jade Pavilion Teahouse milestone. Here we harmonize all foundations from Steps 1–5: greetings, identities, family ties, the days of the week (星期一 to 星期天), and counting into the hundreds and thousands (一百 to 一千) in natural tea conversations."
    },
    "cards": [
        {
            "id": "zh6_c1",
            "type": "number",
            "glyph": "100 — 一百 (yībǎi)",
            "phonetic": "yībǎi [i˥.paɪ̯˨˩˦]",
            "gloss": "one hundred • 100",
            "speakText": "一百",
            "audioUrl": "",
            "whisper": "一 (yī, 1st tone) + 百 (bǎi, 3rd tone). When counting internally, zero gaps require 零: 一百零五 (105)."
        },
        {
            "id": "zh6_c2",
            "type": "number",
            "glyph": "200 — 两百 (liǎngbǎi)",
            "phonetic": "liǎngbǎi [ljaŋ˨˩˦.paɪ̯˨˩˦]",
            "gloss": "two hundred • 200",
            "speakText": "两百",
            "audioUrl": "",
            "whisper": "两 (liǎng) is preferred over 二 (èr) before hundreds: 两百块 (200 kuai/yuan). 二百 is also understood."
        },
        {
            "id": "zh6_c3",
            "type": "number",
            "glyph": "500 — 五百 (wǔbǎi)",
            "phonetic": "wǔbǎi [u˨˩˦.paɪ̯˨˩˦]",
            "gloss": "five hundred • 500",
            "speakText": "五百",
            "audioUrl": "",
            "whisper": "五 (wǔ, 3rd tone) + 百 (bǎi, 3rd tone). Notice tone sandhi: the first 3rd tone changes to a rising 2nd tone: [wú-bǎi]!"
        },
        {
            "id": "zh6_c4",
            "type": "number",
            "glyph": "1,000 — 一千 (yīqiān)",
            "phonetic": "yīqiān [i˥.tɕʰjɛn˥]",
            "gloss": "one thousand • 1,000",
            "speakText": "一千",
            "audioUrl": "",
            "whisper": "一 (yī) + 千 (qiān, 1st tone). Ten thousand introduces the distinct Chinese base 万 (wàn)!"
        },
        {
            "id": "zh6_c5",
            "type": "weekday",
            "glyph": "星期一 & 星期二",
            "phonetic": "xīngqīyī / xīngqī'èr",
            "gloss": "Monday & Tuesday (Week 1 & 2)",
            "speakText": "星期一, 星期二",
            "audioUrl": "",
            "whisper": "Chinese days of the week are wonderfully logical: 星期 (xīngqī = week) + numbers 1 through 6!"
        },
        {
            "id": "zh6_c6",
            "type": "weekday",
            "glyph": "星期三 & 星期四",
            "phonetic": "xīngqīsān / xīngqīsì",
            "gloss": "Wednesday & Thursday",
            "speakText": "星期三, 星期四",
            "audioUrl": "",
            "whisper": "Wednesday (3) and Thursday (4). Synonyms for week: 周 (zhōu) as in 周三, and 礼拜 (lǐbài)."
        },
        {
            "id": "zh6_c7",
            "type": "weekday",
            "glyph": "星期五, 星期六, 星期天",
            "phonetic": "xīngqīwǔ, xīngqīliù, xīngqītiān",
            "gloss": "Friday, Saturday, Sunday",
            "speakText": "星期五, 星期六, 星期天",
            "audioUrl": "",
            "whisper": "Sunday breaks the number pattern! It uses 天 (tiān = sky/day) or formal 日 (rì = sun): 星期天 / 星期日 (never *星期七)!"
        },
        {
            "id": "zh6_c8",
            "type": "dialogue",
            "glyph": "多少钱？ (duōshao qián?)",
            "phonetic": "duōshao qián? [twɔ˥.ʂaʊ̯ tɕʰjɛn˧˥]",
            "gloss": "How much money / how much is it?",
            "speakText": "多少钱",
            "audioUrl": "",
            "whisper": "多 (many) + 少 (few) = how much/many; 钱 (qián) = money. Standard question across all Chinese markets."
        },
        {
            "id": "zh6_c9",
            "type": "dialogue",
            "glyph": "请进，请喝茶！",
            "phonetic": "qǐng jìn, qǐng hē chá! [tɕʰiŋ˨˩˦ tɕin˥˩, tɕʰiŋ˨˩˦ xɤ˥ tʂʰa˧˥]",
            "gloss": "Please enter, please drink tea!",
            "speakText": "请进, 请喝茶",
            "audioUrl": "",
            "whisper": "The timeless formula of Chinese teahouse and domestic hospitality."
        },
        {
            "id": "zh6_c10",
            "type": "dialogue",
            "glyph": "我们星期一见！",
            "phonetic": "wǒmen xīngqīyī jiàn!",
            "gloss": "We will meet on Monday!",
            "speakText": "我们星期一见",
            "audioUrl": "",
            "whisper": "Word order rule: time words always precede the verb! '我们' (we) + '星期一' (Monday) + '见' (meet/see)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the tea price. How much does the pot cost?",
            "speakAudio": "五百块",
            "options": ["500 yuan ('wǔbǎi kuài')", "50 yuan", "100 yuan"],
            "correct": 0,
            "explain": "'五百块' (wǔbǎi kuài) is 500 yuan."
        },
        {
            "prompt": "Listen to the appointment day. On which weekday will they meet?",
            "speakAudio": "我们星期三见",
            "options": ["Wednesday ('xīngqīsān')", "Tuesday ('xīngqī'èr')", "Thursday ('xīngqīsì')"],
            "correct": 0,
            "explain": "'星期三' (xīngqīsān) is Wednesday (week-3)."
        },
        {
            "prompt": "Listen to the numeral: 'yīqiān'. What number was spoken?",
            "speakAudio": "一千",
            "options": ["1,000 (one thousand)", "100 (one hundred)", "10,000 (ten thousand)"],
            "correct": 0,
            "explain": "'一千' (yīqiān) is 1,000."
        },
        {
            "prompt": "Listen to the weekend day. Which day is 'xīngqītiān'?",
            "speakAudio": "星期天",
            "options": ["Sunday ('星期天')", "Saturday ('星期六')", "Friday ('星期五')"],
            "correct": 0,
            "explain": "'星期天' (xīngqītiān) is Sunday."
        }
    ],
    "arena": [
        {
            "quest": "Teahouse Appointment: 'We meet on Monday' (我们星期一见)",
            "clue": "Master Lao: 'Subject 我们, time 星期一, verb 见!'",
            "target": "我们星期一见",
            "tokens": ["我们", "星期一", "见", "星期二", "去", "有"],
            "explain": "Time expressions precede the verb: '我们' + '星期一' + '见'."
        },
        {
            "quest": "Price Inquiry: 'How much money is this tea?' (这杯茶多少钱)",
            "clue": "Master Lao: 'Subject 这杯茶 followed by 多少钱!'",
            "target": "这杯茶多少钱",
            "tokens": ["这杯茶", "多少钱", "一百", "两百", "很"],
            "explain": "'这杯茶' (this cup of tea) + '多少钱' (how much money)."
        },
        {
            "quest": "Teahouse Bill: 'Altogether two hundred yuan' (一共两百块)",
            "clue": "Master Lao: 'Adverb 一共, numeral 两百, currency kuài!'",
            "target": "一共两百块",
            "tokens": ["一共", "两百", "块", "五百", "钱", "是"],
            "explain": "'一共' (in total) + '两百块' (200 kuài)."
        },
        {
            "quest": "Milestone Greeting: 'Please come in and drink tea' (请进请喝茶)",
            "clue": "Master Lao: 'Polite hospitality formulas: 请进 + 请喝茶!'",
            "target": "请进请喝茶",
            "tokens": ["请进", "请喝茶", "谢谢", "再见", "我们"],
            "explain": "'请进' (please enter) + '请喝茶' (please drink tea)."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the Chinese character for HUNDRED (BǍI -> 百):",
            "tiles": ["百", "千", "十", "万"],
            "answer": "百",
            "gloss": "百 (bǎi = hundred)"
        },
        {
            "clue": "Assemble the Chinese character for THOUSAND (QIĀN -> 千):",
            "tiles": ["千", "百", "十", "元"],
            "answer": "千",
            "gloss": "千 (qiān = thousand)"
        },
        {
            "clue": "Assemble the weekday compound MONDAY in Chinese (XĪNGQĪYĪ -> 星期一):",
            "tiles": ["星", "期", "一", "二", "天"],
            "answer": "星期一",
            "gloss": "星期一 (xīngqīyī = Monday)"
        }
    ],
    "quiz": [
        {
            "q": "How is Sunday exceptionally named in Chinese compared to Monday through Saturday?",
            "options": [
                "Monday–Saturday use digits 1–6 (星期一 to 星期六); Sunday uses 天 (tiān) or 日 (rì): 星期天 / 星期日 (never *星期七)!",
                "Sunday uses the number 0 (星期零)",
                "Sunday uses the word for rest (星期休)"
            ],
            "correct": 0,
            "explain": "Sunday replaces the number 7 with 天 (sky/day) or formal 日 (sun)."
        },
        {
            "q": "Which numeral for 'two' is preferred when stating '200 yuan' or '200 people'?",
            "options": [
                "两 (liǎng) — e.g. 两百块 (liǎngbǎi kuài)!",
                "二 (èr)",
                "双 (shuāng)"
            ],
            "correct": 0,
            "explain": "两 (liǎng) is standard when expressing quantities and currency before hundreds (两百)."
        },
        {
            "q": "Where must time phrases like '星期一' (on Monday) appear in a Chinese sentence?",
            "options": [
                "BEFORE the verb (e.g. '我们星期一见' = We on-Monday meet), never at the very end!",
                "Always at the very end of the sentence",
                "Directly after the direct object"
            ],
            "correct": 0,
            "explain": "Chinese word order strictly places time words either before the subject or directly before the verb."
        },
        {
            "q": "How is internal zero handled when reading numbers with gaps like 105 in Chinese?",
            "options": [
                "The character 零 (líng) is mandatory: 一百零五 (yībǎi líng wǔ)!",
                "The zero is completely ignored: 一百五",
                "A pause is made without saying anything"
            ],
            "correct": 0,
            "explain": "In Chinese numerals, internal zeros must be explicitly spoken as '零' (líng); '一百五' would mean 150!"
        },
        {
            "q": "What third-tone sandhi occurs when pronouncing '五百' (wǔbǎi = 500)?",
            "options": [
                "Because both characters are 3rd tone, the first character '五' changes to 2nd rising tone [wú-bǎi]!",
                "Both become 4th tone",
                "Neither changes tone"
            ],
            "correct": 0,
            "explain": "When two 3rd tones appear consecutively, the first changes to a 2nd tone: 3 + 3 $\to$ 2 + 3."
        }
    ]
}

# ------------------------------------------------------------------------------
# 6. GERMAN — STEP 6: SCHWARZWALD GASTHAUS MILESTONE REALM
# ------------------------------------------------------------------------------

GERMAN_STEP6 = {
    "sealName": "Schwarzwald Gasthaus Milestone Seal",
    "guide": {
        "name": "Herr Schmidt",
        "role": "Gasthaus Wirt & Master Craftsman",
        "avatar": "🥨",
        "prompt": "Herzlich willkommen in unserem gemütlichen Gasthaus! At this 6th milestone, we unite greetings, personal introductions, family stories, the days of the week (Montag bis Sonntag), and numbers from hundert to eintausend in lively tavern dialogue."
    },
    "cards": [
        {
            "id": "de6_c1",
            "type": "number",
            "glyph": "100 — hundert (einhundert)",
            "phonetic": "[ˈhʊn.dɐt]",
            "gloss": "one hundred • 100",
            "speakText": "hundert",
            "audioUrl": "",
            "whisper": "Can be said simply as 'hundert' or 'einhundert'. Combined into single words: 'hundertfünf' (105)."
        },
        {
            "id": "de6_c2",
            "type": "number",
            "glyph": "200 — zweihundert",
            "phonetic": "[ˈtsvaɪ̯ˌhʊn.dɐt]",
            "gloss": "two hundred • 200",
            "speakText": "zweihundert",
            "audioUrl": "",
            "whisper": "Compound word: zwei + hundert. German writes large numbers as one unbroken compound word!"
        },
        {
            "id": "de6_c3",
            "type": "number",
            "glyph": "500 — fünfhundert",
            "phonetic": "[ˈfʏnfˌhʊn.dɐt]",
            "gloss": "five hundred • 500",
            "speakText": "fünfhundert",
            "audioUrl": "",
            "whisper": "fünf + hundert = fünfhundert. Common denomination in euro bills and prices."
        },
        {
            "id": "de6_c4",
            "type": "number",
            "glyph": "1,000 — tausend (eintausend)",
            "phonetic": "[ˈtaʊ̯.zn̩t]",
            "gloss": "one thousand • 1,000",
            "speakText": "tausend",
            "audioUrl": "",
            "whisper": "'Tausend Dank!' = a thousand thanks! Plural 'Tausende' is used for thousands of people."
        },
        {
            "id": "de6_c5",
            "type": "weekday",
            "glyph": "Montag & Dienstag",
            "phonetic": "[ˈmoːn.taːk] / [ˈdiːns.taːk]",
            "gloss": "Monday & Tuesday",
            "speakText": "Montag, Dienstag",
            "audioUrl": "",
            "whisper": "All days of the week are masculine ('der Montag'). To say 'on Monday', use contraction 'am' (an + dem): 'am Montag'!"
        },
        {
            "id": "de6_c6",
            "type": "weekday",
            "glyph": "Mittwoch & Donnerstag",
            "phonetic": "[ˈmɪt.vɔχ] / [ˈdɔ.nɐs.taːk]",
            "gloss": "Wednesday & Thursday",
            "speakText": "Mittwoch, Donnerstag",
            "audioUrl": "",
            "whisper": "'Mittwoch' literally means 'mid-week' (Mitte der Woche); 'Donnerstag' is Thor's day (god of thunder, Donar)."
        },
        {
            "id": "de6_c7",
            "type": "weekday",
            "glyph": "Freitag, Samstag, Sonntag",
            "phonetic": "[ˈfʁaɪ̯.taːk], [ˈzams.taːk], [ˈzɔn.taːk]",
            "gloss": "Friday, Saturday, Sunday",
            "speakText": "Freitag, Samstag, Sonntag",
            "audioUrl": "",
            "whisper": "Freitag (goddess Freya), Samstag (Sabbath, or Sonnabend in northern Germany), and Sonntag (day of the Sun)."
        },
        {
            "id": "de6_c8",
            "type": "dialogue",
            "glyph": "Wie viel kostet das?",
            "phonetic": "[viː fiːl ˈkɔs.tət das]",
            "gloss": "How much does that cost?",
            "speakText": "Wie viel kostet das",
            "audioUrl": "",
            "whisper": "Universal shopping and tavern phrase: 'Wie viel' (how much) + 'kostet' (costs) + 'das' (that)."
        },
        {
            "id": "de6_c9",
            "type": "dialogue",
            "glyph": "Tausend Dank für alles!",
            "phonetic": "[ˈtaʊ̯.zn̩t daŋk fyːɐ̯ ˈa.ləs]",
            "gloss": "A thousand thanks for everything!",
            "speakText": "Tausend Dank für alles",
            "audioUrl": "",
            "whisper": "A warm, genuine German formula of deep gratitude to a gracious host."
        },
        {
            "id": "de6_c10",
            "type": "dialogue",
            "glyph": "Wir treffen uns am...",
            "phonetic": "[viːɐ̯ ˈtʁɛ.fn̩ ʊns am]",
            "gloss": "We meet on... [weekday]",
            "speakText": "Wir treffen uns am",
            "audioUrl": "",
            "whisper": "Reflexive verb 'sich treffen': 'Wir treffen uns am Freitag' (We meet on Friday)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the Gasthaus bill. How much was charged?",
            "speakAudio": "fünfhundert Euro",
            "options": ["500 euros ('fünfhundert')", "50 euros", "100 euros"],
            "correct": 0,
            "explain": "'Fünfhundert' is 500."
        },
        {
            "prompt": "Listen to the appointment. On what day will they meet?",
            "speakAudio": "Wir treffen uns am Freitag",
            "options": ["Friday ('am Freitag')", "Thursday ('am Donnerstag')", "Saturday ('am Samstag')"],
            "correct": 0,
            "explain": "'Freitag' is Friday; 'am Freitag' means on Friday."
        },
        {
            "prompt": "Listen to the gratitude. What does Herr Schmidt express?",
            "speakAudio": "Tausend Dank",
            "options": ["A thousand thanks ('Tausend Dank')", "Good evening", "See you later"],
            "correct": 0,
            "explain": "'Tausend Dank' expresses 'a thousand thanks'."
        },
        {
            "prompt": "Listen to the mid-week name: 'Mittwoch'. What is its origin?",
            "speakAudio": "Mittwoch",
            "options": ["Mid-week ('Mitte der Woche')", "Moon day", "Thunder day"],
            "correct": 0,
            "explain": "'Mittwoch' literally means 'middle of the week'."
        }
    ],
    "arena": [
        {
            "quest": "Gasthaus Appointment: 'We meet on Monday'",
            "clue": "Herr Schmidt: 'Wir treffen uns am Montag!'",
            "target": "Wir treffen uns am Montag",
            "tokens": ["Wir", "treffen", "uns", "am", "Montag", "Dienstag", "im"],
            "explain": "Preposition contraction 'am' (an + dem) precedes weekdays: 'am Montag'."
        },
        {
            "quest": "Gasthaus Bill: 'That comes to two hundred euros'",
            "clue": "Herr Schmidt: 'Das macht zweihundert Euro!'",
            "target": "Das macht zweihundert Euro",
            "tokens": ["Das", "macht", "zweihundert", "Euro", "hundert", "kostet"],
            "explain": "'Das macht' (that makes/comes to) + 'zweihundert Euro'."
        },
        {
            "quest": "Milestone Gratitude: 'A thousand thanks for everything'",
            "clue": "Herr Schmidt: 'Tausend Dank für alles!'",
            "target": "Tausend Dank für alles",
            "tokens": ["Tausend", "Dank", "für", "alles", "hundert", "bitte"],
            "explain": "'Tausend Dank' (a thousand thanks) + 'für alles' (for everything)."
        },
        {
            "quest": "Price Inquiry: 'How much does this cost?'",
            "clue": "Herr Schmidt: 'Wie viel kostet das?'",
            "target": "Wie viel kostet das",
            "tokens": ["Wie", "viel", "kostet", "das", "Wo", "macht"],
            "explain": "'Wie viel' (how much) + 'kostet das' (does that cost)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the German word for ONE HUNDRED (HUNDERT):",
            "tiles": ["H", "U", "N", "D", "E", "R", "T"],
            "answer": "HUNDERT",
            "gloss": "hundert (hundred)"
        },
        {
            "clue": "Spell the German word for ONE THOUSAND (TAUSEND):",
            "tiles": ["T", "A", "U", "S", "E", "N", "D"],
            "answer": "TAUSEND",
            "gloss": "tausend (thousand)"
        },
        {
            "clue": "Spell the mid-week weekday WEDNESDAY in German (MITTWOCH):",
            "tiles": ["M", "I", "T", "T", "W", "O", "C", "H"],
            "answer": "MITTWOCH",
            "gloss": "Mittwoch (Wednesday)"
        }
    ],
    "quiz": [
        {
            "q": "Which preposition contraction is mandatory when stating 'on [weekday]' in German (e.g. 'on Monday')?",
            "options": [
                "am (contraction of 'an dem': am Montag, am Freitag)!",
                "im (in dem)",
                "um"
            ],
            "correct": 0,
            "explain": "Days of the week are masculine dative after 'an': an + dem = am Montag."
        },
        {
            "q": "What grammatical gender do all seven days of the week share in German?",
            "options": [
                "Masculine (der Montag, der Dienstag, der Mittwoch...)!",
                "Feminine",
                "Neuter"
            ],
            "correct": 0,
            "explain": "All days of the week, months, and seasons are grammatically masculine in German."
        },
        {
            "q": "Why is Wednesday called 'Mittwoch' rather than being named after a pagan deity?",
            "options": [
                "Early Christian missionaries replaced the pagan god Wodan's day with a neutral translation of Latin 'media hebdomas' (mid-week)!",
                "It was named after an ancient German king",
                "It was created during the metric calendar reform"
            ],
            "correct": 0,
            "explain": "'Mittwoch' replaced Wodanstag (preserved in English Wednesday and Dutch woensdag) to diminish pagan references."
        },
        {
            "q": "How are large compound numbers like 250 written orthographically in German?",
            "options": [
                "As a single continuous word without spaces: 'zweihundertfünfzig'!",
                "With hyphens between each digit",
                "With commas separating each digit"
            ],
            "correct": 0,
            "explain": "German writes all numerals below one million as a single compound word: zweihundertfünfzig."
        },
        {
            "q": "What regional synonym is used in northern and eastern Germany for 'Samstag' (Saturday)?",
            "options": [
                "Sonnabend (literally 'eve of Sunday')!",
                "Wochenendtag",
                "Ruhetag"
            ],
            "correct": 0,
            "explain": "'Sonnabend' is widely used in northern and eastern Germany as a synonym for Samstag."
        }
    ]
}


# ==============================================================================
# TOP-LEVEL REGISTRIES
# ==============================================================================

STEP5_DATA = {
    "waray": WARAY_STEP5,
    "french": FRENCH_STEP5,
    "latin": LATIN_STEP5,
    "hebrew": HEBREW_STEP5,
    "chinese": CHINESE_STEP5,
    "german": GERMAN_STEP5
}

STEP6_DATA = {
    "waray": WARAY_STEP6,
    "french": FRENCH_STEP6,
    "latin": LATIN_STEP6,
    "hebrew": HEBREW_STEP6,
    "chinese": CHINESE_STEP6,
    "german": GERMAN_STEP6
}


# ==============================================================================
# SELF-VALIDATION ROUTINE
# ==============================================================================

def validate_datasets():
    """Validates the schema, linguistic tokens, and completeness of STEP5_DATA and STEP6_DATA."""
    expected_realms = ["waray", "french", "latin", "hebrew", "chinese", "german"]
    
    for step_num, step_dict in [(5, STEP5_DATA), (6, STEP6_DATA)]:
        assert set(step_dict.keys()) == set(expected_realms), f"Step {step_num} missing realms: {set(expected_realms) - set(step_dict.keys())}"
        
        for realm, data in step_dict.items():
            prefix = f"[Step {step_num} - {realm}]"
            
            # 1. sealName
            assert isinstance(data.get("sealName"), str) and len(data["sealName"]) > 0, f"{prefix} Invalid sealName"
            
            # 2. guide
            guide = data.get("guide", {})
            for gkey in ["name", "role", "avatar", "prompt"]:
                assert isinstance(guide.get(gkey), str) and len(guide[gkey]) > 0, f"{prefix} Guide missing {gkey}"
            
            # 3. cards (7 to 10)
            cards = data.get("cards", [])
            assert 7 <= len(cards) <= 10, f"{prefix} Cards count must be 7-10, got {len(cards)}"
            for idx, c in enumerate(cards):
                for ckey in ["id", "type", "glyph", "phonetic", "gloss", "speakText", "audioUrl", "whisper"]:
                    assert ckey in c, f"{prefix} Card {idx} missing key '{ckey}'"
                    assert isinstance(c[ckey], str), f"{prefix} Card {idx} key '{ckey}' must be str"
            
            # 4. earGym (3 to 4)
            earGym = data.get("earGym", [])
            assert 3 <= len(earGym) <= 4, f"{prefix} EarGym count must be 3-4, got {len(earGym)}"
            for idx, eg in enumerate(earGym):
                for ekey in ["prompt", "speakAudio", "options", "correct", "explain"]:
                    assert ekey in eg, f"{prefix} EarGym {idx} missing key '{ekey}'"
                assert isinstance(eg["options"], list) and len(eg["options"]) >= 3, f"{prefix} EarGym {idx} options must have >= 3 items"
                assert 0 <= eg["correct"] < len(eg["options"]), f"{prefix} EarGym {idx} correct index out of range"
            
            # 5. arena (3 to 4)
            arena = data.get("arena", [])
            assert 3 <= len(arena) <= 4, f"{prefix} Arena count must be 3-4, got {len(arena)}"
            for idx, a in enumerate(arena):
                for akey in ["quest", "clue", "target", "tokens", "explain"]:
                    assert akey in a, f"{prefix} Arena {idx} missing key '{akey}'"
                assert isinstance(a["tokens"], list) and len(a["tokens"]) >= 4, f"{prefix} Arena {idx} tokens must have >= 4 items"
                assert isinstance(a["target"], str) and len(a["target"]) > 0, f"{prefix} Arena {idx} target empty"
            
            # 6. scribe (exactly 3)
            scribe = data.get("scribe", [])
            assert len(scribe) == 3, f"{prefix} Scribe count must be 3, got {len(scribe)}"
            for idx, s in enumerate(scribe):
                for skey in ["clue", "tiles", "answer", "gloss"]:
                    assert skey in s, f"{prefix} Scribe {idx} missing key '{skey}'"
                assert isinstance(s["tiles"], list) and len(s["tiles"]) >= len(s["answer"]), f"{prefix} Scribe {idx} tiles count < answer length"
                # Check that answer can be assembled from tiles
                available_tiles = list(s["tiles"])
                for ch in s["answer"]:
                    assert ch in available_tiles, f"{prefix} Scribe {idx} tile '{ch}' not found in available tiles {available_tiles} for answer '{s['answer']}'"
                    available_tiles.remove(ch)
            
            # 7. quiz (exactly 5)
            quiz = data.get("quiz", [])
            assert len(quiz) == 5, f"{prefix} Quiz count must be exactly 5, got {len(quiz)}"
            for idx, q in enumerate(quiz):
                for qkey in ["q", "options", "correct", "explain"]:
                    assert qkey in q, f"{prefix} Quiz {idx} missing key '{qkey}'"
                assert isinstance(q["options"], list) and len(q["options"]) >= 3, f"{prefix} Quiz {idx} options must have >= 3 items"
                assert 0 <= q["correct"] < len(q["options"]), f"{prefix} Quiz {idx} correct index out of range"

    print("✅ All STEP5_DATA and STEP6_DATA validations passed flawlessly across all 6 realms!")


if __name__ == "__main__":
    validate_datasets()
    print("STEP5_DATA realms:", list(STEP5_DATA.keys()))
    print("STEP6_DATA realms:", list(STEP6_DATA.keys()))
