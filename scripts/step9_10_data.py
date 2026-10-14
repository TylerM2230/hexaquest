#!/usr/bin/env python3
"""
HexaQuest Step 9 & Step 10 Complete Linguistic Datasets
======================================================
STEP 9: Verbs in the Present and Past Tense (Aspect Timelines & Completed vs Incompleted Action)
STEP 10: Food, Drinks & Real-Life Dining Roleplay (Capstone Banquet & Hospitality)

Covering all 6 language realms:
1. Waray (Winaray - Austronesian/Visayan)
2. French (Français - Romance)
3. Latin (Lingua Latina - Italic)
4. Hebrew (Ivrit - Semitic)
5. Chinese (Zhongwen - Sinitic)
6. German (Deutsch - Germanic)
"""

STEP9_DATA = {
    "waray": {
        "sealName": "Leyte Chronos Aspect Seal",
        "guide": {
            "name": "Maestro Dan",
            "role": "Visayan Bard & Aspect Chronologer",
            "avatar": "⏳",
            "prompt": "Maupay nga adlaw! Master the rhythmic flow of time in Waray through completed (nag-), ongoing (nag-C-V-), and contemplated actions."
        },
        "cards": [
            {
                "id": "war_s9_c1",
                "type": "aspect_verb",
                "glyph": "nagkaon",
                "phonetic": "[nɐɡ.kɐ.ˈʔɔn]",
                "gloss": "ate (completed / past aspect)",
                "speakText": "nagkaon",
                "audioUrl": "",
                "whisper": "The prefix 'nag-' marks completed action in actor focus: 'nagkaon ako' = I ate."
            },
            {
                "id": "war_s9_c2",
                "type": "aspect_verb",
                "glyph": "nagkakaon",
                "phonetic": "[nɐɡ.kɐ.kɐ.ˈʔɔn]",
                "gloss": "eating (incompleted / progressive aspect)",
                "speakText": "nagkakaon",
                "audioUrl": "",
                "whisper": "CV-reduplication of the root's first syllable (ka- -> nagkakaon) marks continuous or current action: 'nagkakaon hiya' = he/she is eating."
            },
            {
                "id": "war_s9_c3",
                "type": "aspect_verb",
                "glyph": "magkakaon",
                "phonetic": "[mɐɡ.kɐ.kɐ.ˈʔɔn]",
                "gloss": "will eat (contemplated / future aspect)",
                "speakText": "magkakaon",
                "audioUrl": "",
                "whisper": "The prefix 'mag-' combined with CV-reduplication (ka-) indicates contemplated future action: 'magkakaon kita' = we will eat."
            },
            {
                "id": "war_s9_c4",
                "type": "aspect_verb",
                "glyph": "nagsurat",
                "phonetic": "[nɐɡ.sʊ.ˈɾat]",
                "gloss": "wrote (completed / past aspect)",
                "speakText": "nagsurat",
                "audioUrl": "",
                "whisper": "Root 'surat' (write) + 'nag-' = 'nagsurat' (wrote): 'nagsurat hi Maria hin surat' = Maria wrote a letter."
            },
            {
                "id": "war_s9_c5",
                "type": "aspect_verb",
                "glyph": "nagsusurat",
                "phonetic": "[nɐɡ.sʊ.sʊ.ˈɾat]",
                "gloss": "writing (incompleted / progressive aspect)",
                "speakText": "nagsusurat",
                "audioUrl": "",
                "whisper": "Reduplicating 'su-' produces 'nagsusurat' (writing right now)."
            },
            {
                "id": "war_s9_c6",
                "type": "aspect_verb",
                "glyph": "magsusurat",
                "phonetic": "[mɐɡ.sʊ.sʊ.ˈɾat]",
                "gloss": "will write (contemplated / future aspect)",
                "speakText": "magsusurat",
                "audioUrl": "",
                "whisper": "Contemplated actor focus with 'mag-' + 'su-' = 'magsusurat hiya buwas' (he will write tomorrow)."
            },
            {
                "id": "war_s9_c7",
                "type": "aspect_verb",
                "glyph": "naglakat",
                "phonetic": "[nɐɡ.lɐ.ˈkat]",
                "gloss": "walked / left (completed aspect)",
                "speakText": "naglakat",
                "audioUrl": "",
                "whisper": "Root 'lakat' (walk/depart) with 'nag-' signals completed departure: 'naglakat na hira' = they have already walked/left."
            },
            {
                "id": "war_s9_c8",
                "type": "aspect_verb",
                "glyph": "naglalakat",
                "phonetic": "[nɐɡ.lɐ.lɐ.ˈkat]",
                "gloss": "walking (incompleted / progressive aspect)",
                "speakText": "naglalakat",
                "audioUrl": "",
                "whisper": "Progressive aspect: 'naglalakat ako tipakadto ha merkado' = I am walking towards the market."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the aspect marker. Is the person currently eating, or did they finish eating?",
                "speakAudio": "nagkakaon",
                "options": [
                    "Currently eating (nagkakaon — progressive with CV reduplication)",
                    "Already finished eating (nagkaon)",
                    "Will eat tomorrow (magkakaon)"
                ],
                "correct": 0,
                "explain": "'Nagkakaon' contains the reduplicated syllable 'ka-', signifying ongoing, incompleted action."
            },
            {
                "prompt": "Listen to the verb: 'Nagsurat hiya hin surat kakulop'. When did the writing take place?",
                "speakAudio": "nagsurat",
                "options": [
                    "In the past / completed ('nagsurat' with nag- prefix)",
                    "Right now in the present ('nagsusurat')",
                    "In the distant future ('magsusurat')"
                ],
                "correct": 0,
                "explain": "'Nagsurat' uses the non-reduplicated 'nag-' prefix, marking completed aspect in the past."
            },
            {
                "prompt": "Listen to the contemplated verb: 'maglalakat kita buwas'. When will the walking happen?",
                "speakAudio": "maglalakat",
                "options": [
                    "In the future / contemplated ('maglalakat' = will walk)",
                    "It already happened yesterday",
                    "It is happening this very second"
                ],
                "correct": 0,
                "explain": "'Mag-' combined with reduplication 'la-' marks contemplated or future action."
            }
        ],
        "arena": [
            {
                "quest": "Narrate an action in progress: 'He is eating rice right now.'",
                "clue": "Maestro Dan: 'Use the progressive reduplicated verb with pronoun hiya and patient kan-on.'",
                "target": "Nagkakaon hiya hin kan-on",
                "tokens": ["Nagkakaon", "hiya", "hin", "kan-on", "Nagkaon", "magkakaon"],
                "explain": "'Nagkakaon' marks ongoing action, 'hiya' is the 3rd person singular pronoun (he/she), and 'hin kan-on' is the direct object (rice)."
            },
            {
                "quest": "State a completed past letter: 'I wrote a letter yesterday.'",
                "clue": "Maestro Dan: 'Select the completed nag- form, 1st person pronoun ako, and time word kakulop.'",
                "target": "Nagsurat ako hin surat kakulop",
                "tokens": ["Nagsurat", "ako", "hin", "surat", "kakulop", "nagsusurat", "buwas"],
                "explain": "'Nagsurat' indicates completed action, 'ako' is I, 'hin surat' is a letter, and 'kakulop' means yesterday."
            },
            {
                "quest": "Announce future plans: 'We will walk tomorrow.'",
                "clue": "Maestro Dan: 'Combine the contemplated mag- form, inclusive we kita, and tomorrow buwas.'",
                "target": "Maglalakat kita buwas",
                "tokens": ["Maglalakat", "kita", "buwas", "Naglakat", "kakulop"],
                "explain": "'Maglalakat' combines contemplated prefix 'mag-' with reduplication 'la-' to signify 'will walk', and 'buwas' means tomorrow."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the completed verb 'ate' in Waray:",
                "tiles": ["N", "A", "G", "K", "A", "O", "N", "M"],
                "answer": "NAGKAON",
                "gloss": "nagkaon (ate / completed)"
            },
            {
                "clue": "Assemble the progressive verb 'writing' (ongoing):",
                "tiles": ["N", "A", "G", "S", "U", "S", "U", "R", "A", "T"],
                "answer": "NAGSUSURAT",
                "gloss": "nagsusurat (writing / incompleted)"
            },
            {
                "clue": "Assemble the completed verb 'walked':",
                "tiles": ["N", "A", "G", "L", "A", "K", "A", "T", "O"],
                "answer": "NAGLAKAT",
                "gloss": "naglakat (walked / departed)"
            }
        ],
        "quiz": [
            {
                "q": "How does Waray-Waray grammar primarily distinguish past (completed) from present (ongoing) action in verbs with the 'nag-' affix?",
                "options": [
                    "By reduplicating the first consonant and vowel (CV) of the root for ongoing actions (e.g. nagkaon vs nagkakaon)",
                    "By inserting an auxiliary verb like 'did' or 'was'",
                    "By changing the final vowel to -o"
                ],
                "correct": 0,
                "explain": "Philippine languages like Waray utilize aspectual CV-reduplication to distinguish ongoing (incompleted) actions from completed ones."
            },
            {
                "q": "If 'surat' is the root for 'write', what temporal aspect does 'magsusurat' express?",
                "options": [
                    "Contemplated / Future action ('will write') using prefix 'mag-' plus CV reduplication",
                    "Completed past action ('already wrote')",
                    "Imperative command ('Write now!')"
                ],
                "correct": 0,
                "explain": "'Mag-' combined with CV-reduplication (su-) marks future or contemplated action."
            },
            {
                "q": "Which prefix marks an action that was completed (past) in the actor focus?",
                "options": [
                    "nag- (e.g., nagkaon, naglakat, nagsurat)",
                    "mag- (e.g., magkaon, maglakat)",
                    "pag- (e.g., pagkaon, paglakat)"
                ],
                "correct": 0,
                "explain": "'Nag-' is the standard realis/completed actor focus prefix in Visayan."
            },
            {
                "q": "What does the sentence 'Naglalakat hi Pedro yana' mean?",
                "options": [
                    "Pedro is walking right now (ongoing aspect with 'yana' = now)",
                    "Pedro walked yesterday",
                    "Pedro will walk tomorrow"
                ],
                "correct": 0,
                "explain": "'Naglalakat' is progressive/incompleted and 'yana' means 'now/today'."
            },
            {
                "q": "Which sentence correctly says 'I ate rice yesterday' in Waray?",
                "options": [
                    "Nagkaon ako hin kan-on kakulop",
                    "Magkakaon ako hin kan-on buwas",
                    "Nagkakaon ako hin kan-on yana"
                ],
                "correct": 0,
                "explain": "'Nagkaon' (completed) + 'ako' (I) + 'hin kan-on' (rice) + 'kakulop' (yesterday) expresses completed past action."
            }
        ]
    },
    "french": {
        "sealName": "Lumière Chronographe Seal",
        "guide": {
            "name": "Professeur Éloi",
            "role": "Sorbonne Verb Stylist",
            "avatar": "🕰️",
            "prompt": "Bonjour ! Traverse the French timeline from the living present to the completed past with avoir and être."
        },
        "cards": [
            {
                "id": "fr_s9_c1",
                "type": "verb_tense",
                "glyph": "je mange",
                "phonetic": "[ʒə mɑ̃ʒ]",
                "gloss": "I eat / I am eating (Présent)",
                "speakText": "je mange",
                "audioUrl": "",
                "whisper": "The French present covers both simple present ('I eat') and continuous present ('I am eating')."
            },
            {
                "id": "fr_s9_c2",
                "type": "verb_tense",
                "glyph": "j'ai mangé",
                "phonetic": "[ʒe mɑ̃.ʒe]",
                "gloss": "I ate / I have eaten (Passé composé with avoir)",
                "speakText": "j'ai mangé",
                "audioUrl": "",
                "whisper": "Formed with auxiliary 'avoir' ('j'ai') + regular -er past participle 'mangé'."
            },
            {
                "id": "fr_s9_c3",
                "type": "verb_tense",
                "glyph": "j'écris",
                "phonetic": "[ʒe.kʁi]",
                "gloss": "I write / I am writing (Présent)",
                "speakText": "j'écris",
                "audioUrl": "",
                "whisper": "Irregular 3rd group verb 'écrire' ending in silent 's' in the 1st person singular."
            },
            {
                "id": "fr_s9_c4",
                "type": "verb_tense",
                "glyph": "j'ai écrit",
                "phonetic": "[ʒe e.kʁi]",
                "gloss": "I wrote / I have written (Passé composé)",
                "speakText": "j'ai écrit",
                "audioUrl": "",
                "whisper": "Past participle of écrire is 'écrit' with a silent final 't'."
            },
            {
                "id": "fr_s9_c5",
                "type": "verb_tense",
                "glyph": "je parle",
                "phonetic": "[ʒə paʁl]",
                "gloss": "I speak / I am speaking (Présent)",
                "speakText": "je parle",
                "audioUrl": "",
                "whisper": "Standard 1st conjugation verb with silent final '-e'."
            },
            {
                "id": "fr_s9_c6",
                "type": "verb_tense",
                "glyph": "j'ai parlé",
                "phonetic": "[ʒe paʁ.le]",
                "gloss": "I spoke / I have spoken (Passé composé)",
                "speakText": "j'ai parlé",
                "audioUrl": "",
                "whisper": "Passé composé with avoir: 'j'ai parlé au téléphone'."
            },
            {
                "id": "fr_s9_c7",
                "type": "verb_tense",
                "glyph": "je vais",
                "phonetic": "[ʒə vɛ]",
                "gloss": "I go / I am going (Présent)",
                "speakText": "je vais",
                "audioUrl": "",
                "whisper": "Irregular present tense of movement verb 'aller'."
            },
            {
                "id": "fr_s9_c8",
                "type": "verb_tense",
                "glyph": "je suis allé(e)",
                "phonetic": "[ʒə sɥi.z‿a.le]",
                "gloss": "I went / I have gone (Passé composé with être)",
                "speakText": "je suis allé",
                "audioUrl": "",
                "whisper": "Movement verbs like 'aller' require auxiliary 'être' and agree in gender: 'allé' (m) or 'allée' (f)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the verb auxiliary: 'j'ai parlé avec le professeur'. Did the action happen in present or past?",
                "speakAudio": "j'ai parlé avec le professeur",
                "options": [
                    "Past (Passé composé with auxiliary 'avoir' + 'parlé')",
                    "Present continuous ('je parle')",
                    "Future intention ('je vais parler')"
                ],
                "correct": 0,
                "explain": "'J'ai parlé' utilizes the auxiliary verb 'avoir' + past participle, indicating a completed past event."
            },
            {
                "prompt": "Listen carefully: 'je vais à Paris' vs 'je suis allé à Paris'. Which phrase was spoken?",
                "speakAudio": "je suis allé à Paris",
                "options": [
                    "I went to Paris (Past tense with être: 'je suis allé à Paris')",
                    "I am going to Paris (Present tense: 'je vais à Paris')",
                    "I want to go to Paris"
                ],
                "correct": 0,
                "explain": "'Je suis allé' is the passé composé of movement verb 'aller' conjugated with être."
            },
            {
                "prompt": "Listen to the phonetics: 'je mange' vs 'j'ai mangé'. Which expresses current eating?",
                "speakAudio": "je mange",
                "options": [
                    "I eat / I am eating ('je mange' — Présent ending in [ʒ])",
                    "I already ate ('j'ai mangé' — Passé composé ending in [e])",
                    "I will eat tomorrow"
                ],
                "correct": 0,
                "explain": "'Je mange' ends in the consonant [ʒ], while 'j'ai mangé' begins with [ʒe] and ends in the vowel [e]."
            }
        ],
        "arena": [
            {
                "quest": "Build the past meal statement: 'I ate a croissant this morning.'",
                "clue": "Professeur Éloi: 'Start with Ce matin, use auxiliary j'ai and participle mangé.'",
                "target": "Ce matin j'ai mangé un croissant",
                "tokens": ["Ce", "matin", "j'ai", "mangé", "un", "croissant", "je", "mange"],
                "explain": "'J'ai mangé' is the passé composé of manger with auxiliary 'avoir'."
            },
            {
                "quest": "Build the movement sentence: 'Yesterday I went to Paris.'",
                "clue": "Professeur Éloi: 'Remember that aller takes être: je suis allé.'",
                "target": "Hier je suis allé à Paris",
                "tokens": ["Hier", "je", "suis", "allé", "à", "Paris", "j'ai", "vais"],
                "explain": "Verbs of motion like 'aller' require 'être' as their auxiliary: 'je suis allé'."
            },
            {
                "quest": "Express daily habit: 'I speak French every day.'",
                "clue": "Professeur Éloi: 'Use the simple present tense je parle.'",
                "target": "Je parle français tous les jours",
                "tokens": ["Je", "parle", "français", "tous", "les", "jours", "j'ai", "parlé"],
                "explain": "'Je parle' represents habitual or continuous action in the present indicative."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the past participle 'eaten' (mangé):",
                "tiles": ["M", "A", "N", "G", "É", "R", "S"],
                "answer": "MANGÉ",
                "gloss": "mangé (eaten)"
            },
            {
                "clue": "Assemble the past participle 'written' (écrit):",
                "tiles": ["É", "C", "R", "I", "T", "E", "S"],
                "answer": "ÉCRIT",
                "gloss": "écrit (written)"
            },
            {
                "clue": "Assemble the present form 'I write' (écris):",
                "tiles": ["É", "C", "R", "I", "S", "T", "Z"],
                "answer": "ÉCRIS",
                "gloss": "écris (write)"
            }
        ],
        "quiz": [
            {
                "q": "Which auxiliary verb is required to form the passé composé of verbs of movement like 'aller', 'venir', and 'partir'?",
                "options": [
                    "être (e.g., je suis allé, je suis venu)",
                    "avoir (e.g., j'ai allé)",
                    "faire (e.g., je fais allé)"
                ],
                "correct": 0,
                "explain": "A specific group of movement and reflexive verbs (DR MRS VANDERTRAMP) take 'être' as auxiliary."
            },
            {
                "q": "How does the past participle agree when conjugated with 'être' if the subject is feminine singular ('elle')?",
                "options": [
                    "It adds an '-e' to agree in gender: 'elle est allée'",
                    "It remains unchanged with '-é'",
                    "It adds an '-s' at the end"
                ],
                "correct": 0,
                "explain": "With auxiliary 'être', the past participle agrees in both gender (-e) and number (-s) with the grammatical subject."
            },
            {
                "q": "What is the passé composé of 'j'écris' (I write)?",
                "options": [
                    "j'ai écrit",
                    "j'ai écrivé",
                    "je suis écrit"
                ],
                "correct": 0,
                "explain": "The verb 'écrire' takes auxiliary 'avoir' and forms the irregular past participle 'écrit'."
            },
            {
                "q": "In spoken French, how do 'je mange' and 'j'ai mangé' phonetically differ?",
                "options": [
                    "'je mange' ends in consonant [ʒ], while 'j'ai mangé' begins with [ʒe] and ends in vowel [e]",
                    "They are pronounced identically",
                    "'je mange' ends with a nasal vowel"
                ],
                "correct": 0,
                "explain": "'Je mange' [ʒə mɑ̃ʒ] has a final consonant sound, whereas 'j'ai mangé' [ʒe mɑ̃ʒe] has two distinct vowel syllables."
            },
            {
                "q": "Which sentence correctly says 'I came yesterday'?",
                "options": [
                    "Hier je suis venu(e)",
                    "Hier j'ai venu",
                    "Hier je viens"
                ],
                "correct": 0,
                "explain": "Venir is a verb of motion that requires 'être': 'je suis venu'."
            }
        ]
    },
    "latin": {
        "sealName": "SPQR Tempus Laurel Seal",
        "guide": {
            "name": "Magister Claudius",
            "role": "Roman Rhetorician & Chronicler",
            "avatar": "📜",
            "prompt": "Salvē! Compare the imperfective present stem with the perfect stem to narrate legendary deeds."
        },
        "cards": [
            {
                "id": "lat_s9_c1",
                "type": "verb_aspect",
                "glyph": "scrībō",
                "phonetic": "[ˈskriː.boː]",
                "gloss": "I write / I am writing (Present active indicative)",
                "speakText": "scribo",
                "audioUrl": "",
                "whisper": "Present stem 'scrīb-' indicates ongoing, incomplete, or habitual action in present time."
            },
            {
                "id": "lat_s9_c2",
                "type": "verb_aspect",
                "glyph": "scrīpsī",
                "phonetic": "[ˈskriːp.siː]",
                "gloss": "I wrote / I have written (Perfect active indicative)",
                "speakText": "scripsi",
                "audioUrl": "",
                "whisper": "Perfect stem formed with sigmatic -s- suffix (scrīb + s -> scrīpsī), expressing completed past action."
            },
            {
                "id": "lat_s9_c3",
                "type": "verb_aspect",
                "glyph": "legō",
                "phonetic": "[ˈlɛ.ɡoː]",
                "gloss": "I read / I gather (Present active indicative)",
                "speakText": "lego",
                "audioUrl": "",
                "whisper": "3rd conjugation present with short vowel 'e': [ˈlɛ.ɡoː]."
            },
            {
                "id": "lat_s9_c4",
                "type": "verb_aspect",
                "glyph": "lēgī",
                "phonetic": "[ˈleː.ɡiː]",
                "gloss": "I read / I have read (Perfect active indicative)",
                "speakText": "legi",
                "audioUrl": "",
                "whisper": "Notice the vowel lengthening ablaut: short 'e' in legō lengthens to long 'ē' in lēgī!"
            },
            {
                "id": "lat_s9_c5",
                "type": "verb_aspect",
                "glyph": "audiō",
                "phonetic": "[ˈau̯.di.oː]",
                "gloss": "I hear / I listen (Present active indicative)",
                "speakText": "audio",
                "audioUrl": "",
                "whisper": "4th conjugation present active indicative with characteristic 'ī' stem."
            },
            {
                "id": "lat_s9_c6",
                "type": "verb_aspect",
                "glyph": "audīvī",
                "phonetic": "[au̯ˈdiː.wiː]",
                "gloss": "I heard / I have heard (Perfect active indicative)",
                "speakText": "audivi",
                "audioUrl": "",
                "whisper": "Formed with the regular 4th conjugation -v- perfect marker: audī + v + ī."
            },
            {
                "id": "lat_s9_c7",
                "type": "verb_aspect",
                "glyph": "veniō",
                "phonetic": "[ˈwɛ.ni.oː]",
                "gloss": "I come / I arrive (Present active indicative)",
                "speakText": "venio",
                "audioUrl": "",
                "whisper": "Present tense with short 'e' [ˈwɛ.ni.oː]."
            },
            {
                "id": "lat_s9_c8",
                "type": "verb_aspect",
                "glyph": "vēnī",
                "phonetic": "[ˈweː.niː]",
                "gloss": "I came / I arrived (Perfect active indicative)",
                "speakText": "veni",
                "audioUrl": "",
                "whisper": "Perfect tense featuring lengthened root vowel 'ē' [ˈweː.niː], immortalized in 'Vēnī, vīdī, vīcī'."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to Caesar's dispatch: 'Vēnī, vīdī, vīcī'. In which grammatical tense are these actions?",
                "speakAudio": "Veni, vidi, vici",
                "options": [
                    "Perfect active indicative (completed historical actions: 'I came, I saw, I conquered')",
                    "Present active indicative ('I am coming, seeing, conquering')",
                    "Future active indicative ('I shall conquer')"
                ],
                "correct": 0,
                "explain": "All three verbs are first-person singular perfect active indicative forms marked by long vowels and completed aspect."
            },
            {
                "prompt": "Listen to the vowel length: 'legō' (short e) vs 'lēgī' (long ē). Which is the past/completed 'I have read'?",
                "speakAudio": "legi",
                "options": [
                    "lēgī (long vowel ē — Perfect completed 'I read / have read')",
                    "legō (short vowel e — Present ongoing 'I read')",
                    "legam (Future 'I will read')"
                ],
                "correct": 0,
                "explain": "Latin distinguishes present 'legō' from perfect 'lēgī' through vowel lengthening (apophony/ablaut)."
            },
            {
                "prompt": "Listen to the verb: 'audīvī vocem tuam'. When did this perception occur?",
                "speakAudio": "audivi vocem tuam",
                "options": [
                    "In the past ('audīvī' — Perfect active: 'I heard your voice')",
                    "In the present ('audiō')",
                    "In the future ('audiam')"
                ],
                "correct": 0,
                "explain": "'Audīvī' contains the characteristic 4th conjugation -v- perfect marker, signifying completed action."
            }
        ],
        "arena": [
            {
                "quest": "Assemble Caesar's legendary triad: 'I came, I saw, I conquered!'",
                "clue": "Magister Claudius: 'Place the three triumphant 1st person perfect forms in sequence.'",
                "target": "Vēnī vīdī vīcī",
                "tokens": ["Vēnī", "vīdī", "vīcī", "veniō", "videō", "vincō"],
                "explain": "Caesar's concise dispatch to the Roman Senate after the Battle of Zela (47 BC) utilizes three perfect active verbs."
            },
            {
                "quest": "Narrate epistolary completion: 'I wrote a letter to a friend.'",
                "clue": "Magister Claudius: 'Begin with accusative epistulam, prepositional phrase, and perfect scrīpsī.'",
                "target": "Epistulam ad amīcum scrīpsī",
                "tokens": ["Epistulam", "ad", "amīcum", "scrīpsī", "scrībō", "amīcō"],
                "explain": "'Scrīpsī' is the perfect active verb, taking direct object 'epistulam' (letter) and directional phrase 'ad amīcum'."
            },
            {
                "quest": "State completed presence: 'I was in Rome yesterday.'",
                "clue": "Magister Claudius: 'Combine heri (yesterday), locative Rōmae, and perfect fuī.'",
                "target": "Heri Rōmae fuī",
                "tokens": ["Heri", "Rōmae", "fuī", "sum", "crās", "Rōmam"],
                "explain": "'Fuī' is the perfect of 'sum' (I was), paired with the locative case 'Rōmae' (at Rome) and adverb 'heri' (yesterday)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the Latin perfect verb 'I wrote' (scrīpsī):",
                "tiles": ["S", "C", "R", "Ī", "P", "S", "Ī", "O"],
                "answer": "SCRĪPSĪ",
                "gloss": "scrīpsī (I wrote / have written)"
            },
            {
                "clue": "Assemble the Latin perfect verb 'I came' (vēnī):",
                "tiles": ["V", "Ē", "N", "Ī", "T", "U", "S"],
                "answer": "VĒNĪ",
                "gloss": "vēnī (I came / have arrived)"
            },
            {
                "clue": "Assemble the Latin perfect verb 'I heard' (audīvī):",
                "tiles": ["A", "U", "D", "Ī", "V", "Ī", "E"],
                "answer": "AUDĪVĪ",
                "gloss": "audīvī (I heard / have listened)"
            }
        ],
        "quiz": [
            {
                "q": "How does Latin form the perfect active stem in verbs like 'scrībō' -> 'scrīpsī'?",
                "options": [
                    "By adding an -s- suffix (sigmatic perfect) to the root consonant",
                    "By adding an auxiliary verb like 'habeō'",
                    "By duplicating the ending of the present tense"
                ],
                "correct": 0,
                "explain": "The sigmatic perfect (adding -s-) is a primary Indo-European method for forming perfect stems (scrīb- + s -> scrīps-)."
            },
            {
                "q": "What phonological change distinguishes the present 'legō' from the perfect 'lēgī'?",
                "options": [
                    "Vowel lengthening (short e [ɛ] lengthens to long ē [eː])",
                    "The addition of prefix re-",
                    "A change in grammatical person"
                ],
                "correct": 0,
                "explain": "Vowel lengthening with ablaut (legō -> lēgī) is seen in several key 3rd conjugation verbs."
            },
            {
                "q": "What is the 1st person singular perfect active form of 'sum' (I am)?",
                "options": [
                    "fuī",
                    "eram",
                    "essem"
                ],
                "correct": 0,
                "explain": "'Fuī' is the irregular perfect active indicative of 'sum' (stem fu-)."
            },
            {
                "q": "What is the key aspectual difference between the Latin Imperfect (scrībēbam) and Perfect (scrīpsī)?",
                "options": [
                    "The Imperfect expresses continuous, habitual, or incomplete past action; the Perfect expresses a completed, unified event in the past",
                    "The Imperfect is used only in poetry; the Perfect in prose",
                    "The Imperfect refers to the future; the Perfect to the past"
                ],
                "correct": 0,
                "explain": "Imperfect views an ongoing process in the past (aspect: imperfective), while the Perfect views an action as a completed whole (aspect: perfective)."
            },
            {
                "q": "Which suffix characterizes the regular 4th conjugation perfect stem in 'audiō' -> 'audīvī'?",
                "options": [
                    "-v- (audī-v-ī)",
                    "-u-",
                    "-t-"
                ],
                "correct": 0,
                "explain": "4th conjugation verbs typically form their perfect stem with -v- attached to the long stem vowel: audīvī."
            }
        ]
    },
    "hebrew": {
        "sealName": "Menorah Roots Timeline Seal",
        "guide": {
            "name": "Morah Tamar",
            "role": "Jerusalem Root & Binyan Scholar",
            "avatar": "🕎",
            "prompt": "Shalom! Discover the transition from the present participle (benoni) to the past tense root conjugations."
        },
        "cards": [
            {
                "id": "heb_s9_c1",
                "type": "root_tense",
                "glyph": "אֲנִי כּוֹתֵב",
                "phonetic": "aní kotév [aˈni koˈtev]",
                "gloss": "I write / am writing (Present participle m.sg.)",
                "speakText": "אני כותב",
                "audioUrl": "",
                "whisper": "The present tense is the 'Benoni' participle. It inflects for gender and number (kotév/kotevet), requiring pronoun 'aní' for person."
            },
            {
                "id": "heb_s9_c2",
                "type": "root_tense",
                "glyph": "כָּתַבְתִּי",
                "phonetic": "katávti [kaˈtavti]",
                "gloss": "I wrote (Past tense 1st person singular)",
                "speakText": "כתבתי",
                "audioUrl": "",
                "whisper": "Root כ-ת-ב. The suffix '-ti' unequivocally encodes 'I' in the past; 'aní' is therefore often omitted."
            },
            {
                "id": "heb_s9_c3",
                "type": "root_tense",
                "glyph": "אֲנִי אוֹכֵל",
                "phonetic": "aní ochél [aˈni oˈχel]",
                "gloss": "I eat / am eating (Present participle m.sg.)",
                "speakText": "אני אוכל",
                "audioUrl": "",
                "whisper": "Root א-כ-ל in Pa'al present pattern CōCēC: 'aní ochél lechem' = I am eating bread."
            },
            {
                "id": "heb_s9_c4",
                "type": "root_tense",
                "glyph": "אָכַלְתִּי",
                "phonetic": "achálti [aˈχalti]",
                "gloss": "I ate (Past tense 1st person singular)",
                "speakText": "אכלתי",
                "audioUrl": "",
                "whisper": "Past tense with 1st person suffix '-ti': 'achálti et ha-tapúach' = I ate the apple."
            },
            {
                "id": "heb_s9_c5",
                "type": "root_tense",
                "glyph": "אֲנִי מְדַבֵּר",
                "phonetic": "aní medabér [aˈni medaˈbeʁ]",
                "gloss": "I speak / am speaking (Pi'el Present m.sg.)",
                "speakText": "אני מדבר",
                "audioUrl": "",
                "whisper": "Root ד-ב-ר in Binyan Pi'el, marked by prefix 'me-' in the present participle."
            },
            {
                "id": "heb_s9_c6",
                "type": "root_tense",
                "glyph": "דִּבַּרְתִּי",
                "phonetic": "dibárti [diˈbaʁti]",
                "gloss": "I spoke (Pi'el Past 1st person singular)",
                "speakText": "דיברתי",
                "audioUrl": "",
                "whisper": "Pi'el past tense with internal vowel pattern i-a: 'dibárti ivrít' = I spoke Hebrew."
            },
            {
                "id": "heb_s9_c7",
                "type": "root_tense",
                "glyph": "אֲנִי הוֹלֵךְ",
                "phonetic": "aní holéch [aˈni hoˈleχ]",
                "gloss": "I walk / am going (Present participle m.sg.)",
                "speakText": "אני הולך",
                "audioUrl": "",
                "whisper": "Root ה-ל-ך in the present tense: 'aní holéch habáyta' = I am going home."
            },
            {
                "id": "heb_s9_c8",
                "type": "root_tense",
                "glyph": "הָלַכְתִּי",
                "phonetic": "haláchti [haˈlaχti]",
                "gloss": "I walked / went (Past tense 1st person singular)",
                "speakText": "הלכתי",
                "audioUrl": "",
                "whisper": "Past tense with '-ti': 'haláchti la-shuk etmol' = I went to the market yesterday."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the verb suffix: 'katávti mikhtav'. Did this action happen in the present or the past?",
                "speakAudio": "כתבתי מכתב",
                "options": [
                    "Past ('katávti' with suffix '-ti' = 'I wrote')",
                    "Present ('aní kotév' = 'I am writing')",
                    "Future ('ani ekhtov' = 'I will write')"
                ],
                "correct": 0,
                "explain": "The suffix '-ti' (תִּי-) is the unmistakable past tense marker for 1st person singular 'I'."
            },
            {
                "prompt": "Listen to the vowel pattern: 'aní ochél' vs 'achálti'. Which phrase means 'I am currently eating'?",
                "speakAudio": "אני אוכל",
                "options": [
                    "I am eating (aní ochél — Present participle)",
                    "I already ate (achálti — Past tense)",
                    "I will eat later"
                ],
                "correct": 0,
                "explain": "'Aní ochél' uses the Benoni participle with pattern CōCēC indicating current present action."
            },
            {
                "prompt": "Listen to the Pi'el verb: 'dibárti im ha-moré'. Who performed the action?",
                "speakAudio": "דיברתי עם המורה",
                "options": [
                    "I spoke ('-ti' suffix marks 1st person singular subject 'I')",
                    "He spoke ('diber')",
                    "We spoke ('dibárnu')"
                ],
                "correct": 0,
                "explain": "The suffix '-ti' directly encodes the subject 'I' within the verb 'dibárti'."
            }
        ],
        "arena": [
            {
                "quest": "State a completed letter: 'Yesterday I wrote a letter.'",
                "clue": "Morah Tamar: 'Begin with etmol (yesterday), past verb katávti, and noun mikhtav.'",
                "target": "אֶתְמוֹל כָּתַבְתִּי מִכְתָּב",
                "tokens": ["אתמול", "כתבתי", "מכתב", "אני", "כותב", "מחר"],
                "explain": "'Etmol' means yesterday, and 'katávti' is the 1st person past tense of the root כ-ת-ב without needing 'aní'."
            },
            {
                "quest": "Describe a completed meal: 'I ate bread in the restaurant.'",
                "clue": "Morah Tamar: 'Use past verb achálti, lechem (bread), and ba-mis'ada (in the restaurant).'",
                "target": "אָכַלְתִּי לֶחֶם בַּמִּסְעָדָה",
                "tokens": ["אכלתי", "לחם", "במסעדה", "אוכל", "אתמול"],
                "explain": "'Achálti' is the completed past form ('I ate') with 1st person suffix '-ti'."
            },
            {
                "quest": "Express ongoing motion: 'Now I am walking home.'",
                "clue": "Morah Tamar: 'Use achshav (now), present participle aní holéch, and directional habáyta.'",
                "target": "עַכְשָׁו אֲנִי הוֹלֵךְ הַבַּיְתָה",
                "tokens": ["עכשיו", "אני", "הולך", "הביתה", "הלכתי", "מחר"],
                "explain": "'Achshav' means now, and 'aní holéch' is the masculine singular present participle for ongoing movement."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the Hebrew past verb 'I wrote' (katávti):",
                "tiles": ["כ", "ת", "ב", "ת", "י", "ם"],
                "answer": "כתבתי",
                "gloss": "כָּתַבְתִּי (I wrote)"
            },
            {
                "clue": "Assemble the Hebrew past verb 'I ate' (achálti):",
                "tiles": ["א", "כ", "ל", "ת", "י", "ר"],
                "answer": "אכלתי",
                "gloss": "אָכַלְתִּי (I ate)"
            },
            {
                "clue": "Assemble the Hebrew past verb 'I spoke' (dibárti):",
                "tiles": ["ד", "ב", "ר", "ת", "י", "ש"],
                "answer": "דיברתי",
                "gloss": "דִּבַּרְתִּי (I spoke)"
            }
        ],
        "quiz": [
            {
                "q": "How is the present tense primarily constructed in Modern Hebrew?",
                "options": [
                    "Using the 'Benoni' (present participle), which inflects for gender and number rather than person",
                    "Using prefix conjugations identical to the future tense",
                    "By adding the auxiliary particle 'yesh' to every verb"
                ],
                "correct": 0,
                "explain": "The Hebrew present tense originates from the active participle (Benoni), meaning it inflects only for masculine/feminine and singular/plural."
            },
            {
                "q": "What suffix designates 1st person singular ('I') in the Hebrew past tense?",
                "options": [
                    "-ti (תִּי-) as in katávti, achálti, dibárti",
                    "-ta (תָּ-)",
                    "-nu (נוּ-)"
                ],
                "correct": 0,
                "explain": "The suffix '-ti' unambiguously identifies the subject as 'I' in the past suffix conjugation."
            },
            {
                "q": "Which triconsonantal root forms both 'kotév' (writes) and 'katávti' (I wrote)?",
                "options": [
                    "כ-ת-ב (K-T-V)",
                    "א-כ-ל (ʔ-K-L)",
                    "ד-ב-ר (D-B-R)"
                ],
                "correct": 0,
                "explain": "Roots in Semitic languages provide the core semantic meaning: כ-ת-ב relates to writing."
            },
            {
                "q": "If 'aní rotse' (אֲנִי רוֹצֶה) means 'I want' (m.), what is the past form 'I wanted'?",
                "options": [
                    "ratsíti (רָצִיתִי)",
                    "rotset (רוֹצָה)",
                    "eratse (אֶרְצֶה)"
                ],
                "correct": 0,
                "explain": "The root ר-צ-ה in the 1st person past forms 'ratsíti' (I wanted)."
            },
            {
                "q": "Why is the subject pronoun 'aní' (I) frequently omitted before past tense verbs like 'katávti'?",
                "options": [
                    "Because the suffix '-ti' already clearly marks the subject as 1st person singular",
                    "Because pronouns are strictly forbidden in biblical grammar",
                    "To make the sentence sound interrogative"
                ],
                "correct": 0,
                "explain": "Hebrew is a pro-drop language in the 1st and 2nd persons of the past and future tenses because the person is encoded in the verb affix."
            }
        ]
    },
    "chinese": {
        "sealName": "Jade Aspect Mirror Seal",
        "guide": {
            "name": "Laoshi Chen",
            "role": "Master Calligrapher & Aspect Guide",
            "avatar": "🏮",
            "prompt": "Nǐ hǎo! Notice how Chinese marks time not with tense inflections, but with elegant aspect markers like 在, 了, and 过."
        },
        "cards": [
            {
                "id": "zh_s9_c1",
                "type": "aspect_particle",
                "glyph": "在看书",
                "phonetic": "zài kàn shū [tsaɪ˥˩ kʰan˥˩ ʂu˥]",
                "gloss": "reading a book (Continuous / Progressive aspect)",
                "speakText": "在看书",
                "audioUrl": "",
                "whisper": "The preposition/particle '在' (zài) placed immediately before a verb indicates that the action is actively in progress."
            },
            {
                "id": "zh_s9_c2",
                "type": "aspect_particle",
                "glyph": "正在看书",
                "phonetic": "zhèngzài kàn shū [ʈʂɤŋ˥˩ tsaɪ˥˩ kʰan˥˩ ʂu˥]",
                "gloss": "in the very process of reading (Intensive progressive)",
                "speakText": "正在看书",
                "audioUrl": "",
                "whisper": "'正在' emphasizes the precise present timing of the ongoing action: '我正在看书' = I am right in the middle of reading."
            },
            {
                "id": "zh_s9_c3",
                "type": "aspect_particle",
                "glyph": "看了那本书",
                "phonetic": "kàn le nà běn shū [kʰan˥˩ lə na˥˩ pən˨˩˦ ʂu˥]",
                "gloss": "read that book (Completed action marker 了)",
                "speakText": "看了那本书",
                "audioUrl": "",
                "whisper": "Verbal '了' (le) placed right after the verb denotes the completion/realization of an action, not merely past tense."
            },
            {
                "id": "zh_s9_c4",
                "type": "aspect_particle",
                "glyph": "去过北京",
                "phonetic": "qù guo Běijīng [tɕʰy˥˩ ɡwɔ peɪ˨˩˦ tɕiŋ˥]",
                "gloss": "have been to Beijing (Experiential aspect marker 过)",
                "speakText": "去过北京",
                "audioUrl": "",
                "whisper": "'过' (guò) placed after the verb signifies that an action has been experienced at least once in the past."
            },
            {
                "id": "zh_s9_c5",
                "type": "aspect_particle",
                "glyph": "在吃饭",
                "phonetic": "zài chī fàn [tsaɪ˥˩ ʈʂʰʐ̩˥ fan˥˩]",
                "gloss": "eating a meal (Ongoing action)",
                "speakText": "在吃饭",
                "audioUrl": "",
                "whisper": "'在吃饭' indicates the speaker is dining right now: '我正在吃饭，请稍等' = I am eating right now, please wait a moment."
            },
            {
                "id": "zh_s9_c6",
                "type": "aspect_particle",
                "glyph": "吃了饭",
                "phonetic": "chī le fàn [ʈʂʰʐ̩˥ lə fan˥˩]",
                "gloss": "had the meal / ate food (Completed action)",
                "speakText": "吃了饭",
                "audioUrl": "",
                "whisper": "'吃了饭就走' = leave once you have finished eating. '了' marks the action as finished."
            },
            {
                "id": "zh_s9_c7",
                "type": "aspect_particle",
                "glyph": "吃过北京烤鸭",
                "phonetic": "chī guo Běijīng kǎoyā",
                "gloss": "have eaten Peking duck before (Experiential)",
                "speakText": "吃过北京烤鸭",
                "audioUrl": "",
                "whisper": "'你吃过北京烤鸭吗？' = Have you ever experienced eating Peking duck?"
            },
            {
                "id": "zh_s9_c8",
                "type": "aspect_particle",
                "glyph": "还没看",
                "phonetic": "hái méi kàn [xaɪ˧˥ meɪ˧˥ kʰan˥˩]",
                "gloss": "have not yet read (Negation of completion with 没)",
                "speakText": "还没看",
                "audioUrl": "",
                "whisper": "Completed aspect with '了' is negated using '没' or '没有', dropping the '了': '我没看那本书'."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the aspect marker: 'wǒ zài kàn shū'. What is the status of the action?",
                "speakAudio": "我在看书",
                "options": [
                    "Currently reading ('在' marks ongoing progressive aspect)",
                    "Already finished reading ('看了')",
                    "Have never read before ('没看过')"
                ],
                "correct": 0,
                "explain": "The pre-verbal marker '在' (zài) signals that the action is actively taking place right now."
            },
            {
                "prompt": "Listen to the particle: 'wǒ qù guo Běijīng'. What does this sentence convey?",
                "speakAudio": "我去过北京",
                "options": [
                    "Past personal experience ('过' indicates having visited Beijing at least once)",
                    "Currently travelling to Beijing right now ('在去')",
                    "Planning to visit Beijing tomorrow"
                ],
                "correct": 0,
                "explain": "'过' (guò) functions as the experiential aspect marker, showing that an event occurred as a life experience."
            },
            {
                "prompt": "Listen to the sentence: 'tā chī le wǔfàn'. What happened?",
                "speakAudio": "他吃了午饭",
                "options": [
                    "He completed eating lunch ('了' marks completion)",
                    "He is currently eating lunch ('在吃')",
                    "He refuses to eat lunch"
                ],
                "correct": 0,
                "explain": "'了' immediately following the verb '吃' indicates the action of eating lunch has been completed."
            }
        ],
        "arena": [
            {
                "quest": "Build the progressive sentence: 'I am reading a book right now.'",
                "clue": "Laoshi Chen: 'Combine wǒ (I), xiànzài (now), progressive zài, and kàn shū.'",
                "target": "我现在在看书",
                "tokens": ["我", "现在", "在", "看书", "了", "过", "去"],
                "explain": "'在' placed directly in front of '看书' marks continuous progressive aspect."
            },
            {
                "quest": "Build the completed sentence: 'Yesterday I read that book.'",
                "clue": "Laoshi Chen: 'Place dynamic particle le directly after the verb kàn.'",
                "target": "我昨天看了那本书",
                "tokens": ["我", "昨天", "看", "了", "那", "本", "书", "在", "过"],
                "explain": "Verbal '了' placed immediately after '看' signifies completion within the past temporal context of '昨天'."
            },
            {
                "quest": "Express experiential travel: 'I have been to Beijing before.'",
                "clue": "Laoshi Chen: 'Combine yǐqián (previously), qù (go), and experiential guò.'",
                "target": "我以前去过北京",
                "tokens": ["我", "以前", "去", "过", "北京", "了", "在"],
                "explain": "'过' directly attached to '去' marks an experiential past event that occurred at least once."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the progressive reading phrase (在看书):",
                "tiles": ["在", "看", "书", "了", "过"],
                "answer": "在看书",
                "gloss": "在看书 (reading a book / ongoing)"
            },
            {
                "clue": "Assemble the completed verb phrase (看了):",
                "tiles": ["看", "了", "在", "的", "过"],
                "answer": "看了",
                "gloss": "看了 (read / watched [completed])"
            },
            {
                "clue": "Assemble the experiential travel phrase (去过):",
                "tiles": ["去", "过", "在", "来", "了"],
                "answer": "去过",
                "gloss": "去过 (have been to / experienced)"
            }
        ],
        "quiz": [
            {
                "q": "What is the primary grammatical role of the particle '过' (guò) placed after a verb?",
                "options": [
                    "It marks experiential aspect—that an event has occurred as a past life experience at least once",
                    "It indicates an action happening right at this very moment",
                    "It transforms the verb into a polite future request"
                ],
                "correct": 0,
                "explain": "'过' emphasizes past personal experience: '我去过中国' = I have had the experience of going to China."
            },
            {
                "q": "How does Mandarin indicate continuous progressive action without changing the verb stem?",
                "options": [
                    "By placing the aspect marker '在' (zài) or '正在' (zhèngzài) before the verb",
                    "By adding a suffix -ed to the character",
                    "By changing the grammatical tone of the verb"
                ],
                "correct": 0,
                "explain": "Chinese has no inflectional conjugation; pre-verbal markers like '在' convey ongoing aspect."
            },
            {
                "q": "What does verbal '了' (le) primarily indicate when placed immediately after a verb?",
                "options": [
                    "The completion or realization of the action within a temporal frame",
                    "An ongoing habitual action in present time",
                    "A hypothetical conditional state"
                ],
                "correct": 0,
                "explain": "Verbal '了' is a perfective aspect marker indicating the realization or completion of an event."
            },
            {
                "q": "How do you correctly negate a completed action that would use '了' (e.g. 'I did not eat')?",
                "options": [
                    "Use '没有' (méiyǒu) or '没' (méi) before the verb, and drop the '了'",
                    "Keep '了' and insert '不' (bù) before it",
                    "Add '过' at the end of the sentence"
                ],
                "correct": 0,
                "explain": "Completed actions are negated with '没'/'没有', and the verbal particle '了' is omitted: '我没吃' (I didn't eat)."
            },
            {
                "q": "Which sentence correctly says 'I have eaten Peking duck before'?",
                "options": [
                    "我吃过北京烤鸭 (Wǒ chī guo Běijīng kǎoyā)",
                    "我正在吃北京烤鸭 (Wǒ zhèngzài chī Běijīng kǎoyā)",
                    "我要吃北京烤鸭 (Wǒ yào chī Běijīng kǎoyā)"
                ],
                "correct": 0,
                "explain": "'吃过' combines the verb to eat with experiential marker '过'."
            }
        ]
    },
    "german": {
        "sealName": "Schwarzwald Zeitrad Seal",
        "guide": {
            "name": "Herr Schmidt",
            "role": "Bavarian Clockmaker & Philologist",
            "avatar": "⏱️",
            "prompt": "Guten Tag! Master precision German verb forms: Präsens in the moment, and Perfekt with haben and sein for past deeds."
        },
        "cards": [
            {
                "id": "de_s9_c1",
                "type": "verb_conjugation",
                "glyph": "ich lerne",
                "phonetic": "[ɪç ˈlɛʁnə]",
                "gloss": "I learn / I am learning (Präsens)",
                "speakText": "ich lerne",
                "audioUrl": "",
                "whisper": "Standard German Präsens covers both simple present ('I learn') and continuous present ('I am learning')."
            },
            {
                "id": "de_s9_c2",
                "type": "verb_conjugation",
                "glyph": "ich habe gelernt",
                "phonetic": "[ɪç ˈhaːbə ɡəˈlɛʁnt]",
                "gloss": "I learned / have learned (Perfekt with haben)",
                "speakText": "ich habe gelernt",
                "audioUrl": "",
                "whisper": "Regular weak verb Perfekt: auxiliary 'haben' + ge- + verb stem + -t (ge-lern-t)."
            },
            {
                "id": "de_s9_c3",
                "type": "verb_conjugation",
                "glyph": "ich schreibe",
                "phonetic": "[ɪç ˈʃʁaɪbə]",
                "gloss": "I write / I am writing (Präsens)",
                "speakText": "ich schreibe",
                "audioUrl": "",
                "whisper": "Strong verb present tense with diphthong 'ei' [aɪ]: 'ich schreibe einen Brief'."
            },
            {
                "id": "de_s9_c4",
                "type": "verb_conjugation",
                "glyph": "ich habe geschrieben",
                "phonetic": "[ɪç ˈhaːbə ɡəˈʃʁiːbn̩]",
                "gloss": "I wrote / have written (Perfekt with ablaut)",
                "speakText": "ich habe geschrieben",
                "audioUrl": "",
                "whisper": "Notice the strong vowel ablaut from 'ei' to long 'ie' [iː]: schreiben -> geschrieben."
            },
            {
                "id": "de_s9_c5",
                "type": "verb_conjugation",
                "glyph": "ich esse",
                "phonetic": "[ɪç ˈʔɛsə]",
                "gloss": "I eat / I am eating (Präsens)",
                "speakText": "ich esse",
                "audioUrl": "",
                "whisper": "Present tense of essen: 'ich esse ein Brötchen'."
            },
            {
                "id": "de_s9_c6",
                "type": "verb_conjugation",
                "glyph": "ich habe gegessen",
                "phonetic": "[ɪç ˈhaːbə ɡəˈɡɛsn̩]",
                "gloss": "I ate / have eaten (Perfekt with haben)",
                "speakText": "ich habe gegessen",
                "audioUrl": "",
                "whisper": "Past participle 'gegessen' features double ge- prefix: ge + gessen."
            },
            {
                "id": "de_s9_c7",
                "type": "verb_conjugation",
                "glyph": "ich gehe",
                "phonetic": "[ɪç ˈɡeːə]",
                "gloss": "I go / I am walking (Präsens)",
                "speakText": "ich gehe",
                "audioUrl": "",
                "whisper": "Basic verb of motion in the present tense."
            },
            {
                "id": "de_s9_c8",
                "type": "verb_conjugation",
                "glyph": "ich bin gegangen",
                "phonetic": "[ɪç bɪn ɡəˈɡaŋən]",
                "gloss": "I went / have gone (Perfekt with sein)",
                "speakText": "ich bin gegangen",
                "audioUrl": "",
                "whisper": "Verbs of motion involving a change of location require 'sein' as auxiliary in the Perfekt!"
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the auxiliary verb: 'Ich bin nach Hause gegangen'. Why is 'bin' used instead of 'habe'?",
                "speakAudio": "Ich bin nach Hause gegangen",
                "options": [
                    "Movement verb indicating change of location requires auxiliary 'sein' (bin)",
                    "All past tense verbs in German must use 'bin'",
                    "'Gehen' is a reflexive verb"
                ],
                "correct": 0,
                "explain": "Verbs expressing movement with a change of location (e.g., gehen, fahren, laufen) conjugate with 'sein' in the Perfekt."
            },
            {
                "prompt": "Listen to the verb forms: 'ich lerne Deutsch' vs 'ich habe Deutsch gelernt'. Which represents completed past study?",
                "speakAudio": "ich habe Deutsch gelernt",
                "options": [
                    "ich habe Deutsch gelernt (Perfekt past: 'I learned German')",
                    "ich lerne Deutsch (Präsens: 'I am learning German')",
                    "ich werde Deutsch lernen (Future: 'I will learn')"
                ],
                "correct": 0,
                "explain": "'Habe gelernt' is the conversational past tense (Perfekt) formed with auxiliary haben + Partizip II."
            },
            {
                "prompt": "Listen to the sentence: 'Ich habe einen Brief geschrieben'. What did the speaker complete?",
                "speakAudio": "Ich habe einen Brief geschrieben",
                "options": [
                    "Wrote a letter ('geschrieben' is the past participle of schreiben)",
                    "Read a letter ('gelesen')",
                    "Sent an email"
                ],
                "correct": 0,
                "explain": "'Geschrieben' is the strong past participle of 'schreiben' with vowel change ei -> ie."
            }
        ],
        "arena": [
            {
                "quest": "Assemble the verbal bracket: 'Yesterday I wrote a letter.'",
                "clue": "Herr Schmidt: 'Start with Gestern, place auxiliary habe in V2 position, and participle geschrieben at the end.'",
                "target": "Gestern habe ich einen Brief geschrieben",
                "tokens": ["Gestern", "habe", "ich", "einen", "Brief", "geschrieben", "bin", "schreibe"],
                "explain": "In German main clauses, the conjugated auxiliary occupies position 2, while the non-finite participle stands at the very end of the sentence (Satzklammer)."
            },
            {
                "quest": "Assemble motion in the past: 'I went to Berlin.'",
                "clue": "Herr Schmidt: 'Use auxiliary bin with destination nach Berlin and participle gegangen.'",
                "target": "Ich bin nach Berlin gegangen",
                "tokens": ["Ich", "bin", "nach", "Berlin", "gegangen", "habe", "gehe"],
                "explain": "Movement with change of place requires auxiliary 'sein' (ich bin ... gegangen)."
            },
            {
                "quest": "Express industrious present study: 'Today I am studying German diligently.'",
                "clue": "Herr Schmidt: 'Start with Heute, verb lerne in V2, pronoun ich, and adverb fleißig.'",
                "target": "Heute lerne ich fleißig Deutsch",
                "tokens": ["Heute", "lerne", "ich", "fleißig", "Deutsch", "habe", "gelernt"],
                "explain": "With time adverb 'Heute' in first position, the conjugated verb 'lerne' must occupy the second position (V2 rule)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the past participle 'learned' (gelernt):",
                "tiles": ["G", "E", "L", "E", "R", "N", "T", "S"],
                "answer": "GELERNT",
                "gloss": "gelernt (learned / weak participle)"
            },
            {
                "clue": "Assemble the past participle 'written' (geschrieben):",
                "tiles": ["G", "E", "S", "C", "H", "R", "I", "E", "B", "E", "N"],
                "answer": "GESCHRIEBEN",
                "gloss": "geschrieben (written / strong participle)"
            },
            {
                "clue": "Assemble the past participle 'eaten' (gegessen):",
                "tiles": ["G", "E", "G", "E", "S", "S", "E", "N"],
                "answer": "GEGESSEN",
                "gloss": "gegessen (eaten)"
            }
        ],
        "quiz": [
            {
                "q": "Which class of verbs requires 'sein' rather than 'haben' as their auxiliary in the German Perfekt tense?",
                "options": [
                    "Intransitive verbs of motion indicating change of location (gehen, fahren) or change of state (einschlafen), plus sein and bleiben",
                    "All transitive verbs that take a direct accusative object",
                    "All verbs ending in -ieren"
                ],
                "correct": 0,
                "explain": "Verbs of motion and state change, along with 'sein' and 'bleiben', uniquely take 'sein' as auxiliary in the Perfekt."
            },
            {
                "q": "Where does the past participle (Partizip II) typically appear in a standard German declarative main clause?",
                "options": [
                    "At the very end of the clause, closing the sentence bracket (Satzklammer)",
                    "Directly following the auxiliary verb in second position",
                    "At the very start of the sentence"
                ],
                "correct": 0,
                "explain": "The 'Satzklammer' (sentence bracket) places the finite auxiliary in position 2 and the non-finite participle at the clause terminus."
            },
            {
                "q": "What is the past participle of the strong verb 'schreiben' (to write)?",
                "options": [
                    "geschrieben (with vowel ablaut from ei to ie)",
                    "geschreibt",
                    "gegeschrieben"
                ],
                "correct": 0,
                "explain": "Strong verbs form participles with ge- ... -en and frequently undergo stem vowel ablaut (ei -> ie)."
            },
            {
                "q": "How is the English continuous aspect ('I am eating') expressed naturally in everyday spoken German?",
                "options": [
                    "Using the simple Präsens ('Ich esse'), frequently reinforced with adverbs like 'gerade' ('Ich esse gerade')",
                    "By constructing a continuous participle: 'Ich bin essend'",
                    "By adding the prefix mit-"
                ],
                "correct": 0,
                "explain": "German has no continuous verb tense; the simple present (Präsens) along with temporal adverbs like 'gerade' fulfills this role."
            },
            {
                "q": "Which sentence correctly says 'We drove to Munich' in the conversational past?",
                "options": [
                    "Wir sind nach München gefahren",
                    "Wir haben nach München gefahren",
                    "Wir werden nach München gefahren"
                ],
                "correct": 0,
                "explain": "'Fahren' involves locomotion/change of location and therefore requires auxiliary 'sein': 'wir sind ... gefahren'."
            }
        ]
    }
}


STEP10_DATA = {
    "waray": {
        "sealName": "Banquet of San Juanico Seal",
        "guide": {
            "name": "Manang Elena",
            "role": "Carinderia Chef of Tacloban",
            "avatar": "🍲",
            "prompt": "Makaon kita! Welcome to our authentic Leyte carinderia—order local favorites like kinilaw and humba with tuba."
        },
        "cards": [
            {
                "id": "war_s10_c1",
                "type": "dish",
                "glyph": "kinilaw",
                "phonetic": "[kɪ.nɪ.ˈlaʊ̯]",
                "gloss": "raw fish ceviche cured in vinegar & calamansi",
                "speakText": "kinilaw",
                "audioUrl": "",
                "whisper": "Fresh tuna or tanigue cured in native coconut vinegar, calamansi juice, minced ginger, onions, and spicy siling labuyo."
            },
            {
                "id": "war_s10_c2",
                "type": "dish",
                "glyph": "humba",
                "phonetic": "[hʊm.ˈbaʔ]",
                "gloss": "braised pork belly with black beans & banana blossoms",
                "speakText": "humba",
                "audioUrl": "",
                "whisper": "The quintessential Visayan feast dish: tender pork belly slow-braised with soy sauce, vinegar, brown sugar, tausi, and dried banana blossoms."
            },
            {
                "id": "war_s10_c3",
                "type": "dish",
                "glyph": "binagol",
                "phonetic": "[bɪ.na.ˈgɔl]",
                "gloss": "sweet grated taro delicacy baked in coconut shell",
                "speakText": "binagol",
                "audioUrl": "",
                "whisper": "Famous delicacy of Dagami and Tacloban, Leyte: grated talyan taro, condensed milk, and coconut milk with sweet kalamay and egg yolk center in a 'bagol' (coconut shell)."
            },
            {
                "id": "war_s10_c4",
                "type": "dish",
                "glyph": "moron",
                "phonetic": "[mɔ.ˈɾɔn]",
                "gloss": "chocolate & coconut sticky rice roll",
                "speakText": "moron",
                "audioUrl": "",
                "whisper": "Sumptuous Leyte delicacy: smooth glutinous rice kneaded with tablea chocolate and coconut milk, wrapped in banana leaves and steamed."
            },
            {
                "id": "war_s10_c5",
                "type": "beverage",
                "glyph": "tuba",
                "phonetic": "[tʊ.ˈbaʔ]",
                "gloss": "coconut red palm wine",
                "speakText": "tuba",
                "audioUrl": "",
                "whisper": "Naturally fermented sap of the coconut palm dyed an amber-red with pulverized mangrove bark (barok); the social spirit of Leyte and Samar."
            },
            {
                "id": "war_s10_c6",
                "type": "dining_phrase",
                "glyph": "Pabili hin...",
                "phonetic": "[pa.bɪ.ˈli hɪn]",
                "gloss": "Please sell me... / I would like to buy...",
                "speakText": "Pabili hin",
                "audioUrl": "",
                "whisper": "The standard polite formula when ordering food at a local carinderia or counter: 'Pabili hin kinilaw'."
            },
            {
                "id": "war_s10_c7",
                "type": "dining_phrase",
                "glyph": "Makaon kita!",
                "phonetic": "[ma.ka.ˈʔɔn kɪ.ˈta]",
                "gloss": "Let's eat! (Hospitality invitation)",
                "speakText": "Makaon kita",
                "audioUrl": "",
                "whisper": "The universal warm Filipino greeting inviting everyone present to partake in the meal."
            },
            {
                "id": "war_s10_c8",
                "type": "dining_phrase",
                "glyph": "Marasa!",
                "phonetic": "[ma.ɾa.ˈsaʔ]",
                "gloss": "Delicious! / Savory! / Flavorful!",
                "speakText": "Marasa",
                "audioUrl": "",
                "whisper": "'Marasa' means delicious in Waray; 'Marasa duro!' = truly delicious!"
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the carinderia order: 'Pabili hin usa ka putos nga binagol'. What is being ordered?",
                "speakAudio": "Pabili hin usa ka putos nga binagol",
                "options": [
                    "One package of binagol (the famous Leyte taro delicacy)",
                    "A plate of raw fish kinilaw",
                    "A cup of hot coffee"
                ],
                "correct": 0,
                "explain": "'Pabili hin' means 'please sell me', and 'binagol' is the iconic Leyte delicacy."
            },
            {
                "prompt": "Listen to the enthusiastic compliment: 'Marasa duro hiton nga humba!'. What does the diner think?",
                "speakAudio": "Marasa duro hiton nga humba",
                "options": [
                    "That humba is exceedingly delicious! ('marasa duro')",
                    "The food is too spicy",
                    "The dish is cold"
                ],
                "correct": 0,
                "explain": "'Marasa' means delicious and 'duro' means very/exceedingly."
            },
            {
                "prompt": "Listen to the transaction: 'Bayad palihog, pira ini?'. What is happening?",
                "speakAudio": "Bayad palihog, pira ini",
                "options": [
                    "The diner is paying ('Bayad palihog') and asking how much it costs ('Pira ini?')",
                    "The diner is asking for a menu",
                    "The diner is asking for the restroom"
                ],
                "correct": 0,
                "explain": "'Bayad palihog' means 'Payment please', and 'Pira ini?' asks 'How much is this?'."
            }
        ],
        "arena": [
            {
                "quest": "Order food at the carinderia: 'Please sell me kinilaw and cold water.'",
                "clue": "Manang Elena: 'Combine Pabili hin, kinilaw, ngan (and), mahagkot nga tubig (cold water).'",
                "target": "Pabili hin kinilaw ngan mahagkot nga tubig",
                "tokens": ["Pabili", "hin", "kinilaw", "ngan", "mahagkot", "nga", "tubig", "Makaon", "pira"],
                "explain": "'Pabili hin' is the classic carinderia request formula; 'ngan' means and, 'mahagkot' means cold, and 'tubig' is water."
            },
            {
                "quest": "Welcome friends to the feast: 'Let's eat! The lechon is very delicious!'",
                "clue": "Manang Elena: 'Start with Makaon kita, praise marasa duro, and subject an lechon.'",
                "target": "Makaon kita marasa duro an lechon",
                "tokens": ["Makaon", "kita", "marasa", "duro", "an", "lechon", "humba", "Pabili"],
                "explain": "'Makaon kita!' invites everyone to eat, followed by 'marasa duro an lechon' (the roast pig is very delicious)."
            },
            {
                "quest": "Settle the bill gracefully: 'Payment please, thank you very much.'",
                "clue": "Manang Elena: 'Say Bayad palihog followed by salamat hin duro.'",
                "target": "Bayad palihog salamat hin duro",
                "tokens": ["Bayad", "palihog", "salamat", "hin", "duro", "pira", "ini"],
                "explain": "'Bayad palihog' hands over the payment politely, and 'salamat hin duro' conveys heartfelt gratitude."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the iconic Leyte coconut-taro delicacy in a coconut shell:",
                "tiles": ["B", "I", "N", "A", "G", "O", "L", "K"],
                "answer": "BINAGOL",
                "gloss": "binagol (taro & kalamay delicacy)"
            },
            {
                "clue": "Assemble the beloved red coconut palm wine of the Visayas:",
                "tiles": ["T", "U", "B", "A", "O", "P"],
                "answer": "TUBA",
                "gloss": "tuba (coconut palm wine)"
            },
            {
                "clue": "Assemble the Waray word for 'delicious / tasty':",
                "tiles": ["M", "A", "R", "A", "S", "A", "K"],
                "answer": "MARASA",
                "gloss": "marasa (delicious / savory)"
            }
        ],
        "quiz": [
            {
                "q": "What is 'binagol', one of the most celebrated culinary treasures of Leyte?",
                "options": [
                    "A rich, sweet delicacy of grated talyan taro root, coconut milk, and condensed milk with an egg yolk center, packed inside a polished coconut half-shell",
                    "A spicy soup made from stingray meat",
                    "A sun-dried salted mackerel"
                ],
                "correct": 0,
                "explain": "Binagol is named after 'bagol' (coconut shell) and is a renowned specialty of Dagami, Leyte."
            },
            {
                "q": "How do you politely order an item at a Visayan carinderia counter?",
                "options": [
                    "Pabili hin... (e.g., 'Pabili hin kinilaw')",
                    "Hatagi dayon ako...",
                    "Kuhaa ini..."
                ],
                "correct": 0,
                "explain": "'Pabili hin...' literally means 'Please allow me to purchase...' and is the customary polite ordering phrase."
            },
            {
                "q": "What traditional beverage is 'tuba', central to social gatherings across Samar and Leyte?",
                "options": [
                    "Naturally fermented coconut palm sap dyed amber-red with powdered mangrove bark (barok)",
                    "Imported sparkling grape wine",
                    "Boiled sugarcane juice with ginger"
                ],
                "correct": 0,
                "explain": "Tuba is tapped daily from coconut palms and blended with barok bark to create its distinct color and flavor."
            },
            {
                "q": "Which expression warmly invites guests and companions to begin eating?",
                "options": [
                    "Makaon kita!",
                    "Makadto kita!",
                    "Maturog kita!"
                ],
                "correct": 0,
                "explain": "'Makaon kita!' combines the contemplative actor focus of 'kaon' (to eat) with inclusive 'kita' (we all)."
            },
            {
                "q": "How do you ask 'How much is this?' in Waray when paying for your meal?",
                "options": [
                    "Pira ini?",
                    "Hain ini?",
                    "Hin-o ini?"
                ],
                "correct": 0,
                "explain": "'Pira' is the interrogative for price and quantity ('How much?'), and 'ini' means 'this'."
            }
        ]
    },
    "french": {
        "sealName": "Festin de Paris Gourmet Seal",
        "guide": {
            "name": "Chef Marcel",
            "role": "Montmartre Bistro Host",
            "avatar": "🍷",
            "prompt": "Bienvenue au bistrot ! Order exquisite delicacies, sip café au lait, and conclude like a true Parisian."
        },
        "cards": [
            {
                "id": "fr_s10_c1",
                "type": "dish",
                "glyph": "soupe à l'oignon",
                "phonetic": "[sup a lɔ.ɲɔ̃]",
                "gloss": "French onion soup gratineed with cheese",
                "speakText": "soupe à l'oignon",
                "audioUrl": "",
                "whisper": "Slowly caramelized onions in rich beef broth, topped with toasted baguette slices and melted Gruyère cheese crust."
            },
            {
                "id": "fr_s10_c2",
                "type": "dish",
                "glyph": "quiche lorraine",
                "phonetic": "[kiʃ lɔ.ʁɛn]",
                "gloss": "savory egg custard tart with smoked bacon lardons",
                "speakText": "quiche lorraine",
                "audioUrl": "",
                "whisper": "Classic tart from Lorraine filled with rich custard of crème fraîche, eggs, and crisp smoked lardons."
            },
            {
                "id": "fr_s10_c3",
                "type": "dish",
                "glyph": "crème brûlée",
                "phonetic": "[kʁɛm bʁy.le]",
                "gloss": "rich custard topped with caramelized sugar crust",
                "speakText": "crème brûlée",
                "audioUrl": "",
                "whisper": "Creamy vanilla custard finished with a brittle, torched sheet of caramelized sugar that cracks when tapped with a spoon."
            },
            {
                "id": "fr_s10_c4",
                "type": "beverage",
                "glyph": "café au lait",
                "phonetic": "[ka.fe o lɛ]",
                "gloss": "coffee with steamed milk",
                "speakText": "café au lait",
                "audioUrl": "",
                "whisper": "Strong brewed dark coffee or espresso served with hot steamed milk, traditionally enjoyed at breakfast."
            },
            {
                "id": "fr_s10_c5",
                "type": "dining_phrase",
                "glyph": "Je voudrais...",
                "phonetic": "[ʒə vu.dʁɛ]",
                "gloss": "I would like... (Polite conditional)",
                "speakText": "Je voudrais",
                "audioUrl": "",
                "whisper": "The polite conditional mood of vouloir, essential for courteous bistro orders instead of blunt 'je veux'."
            },
            {
                "id": "fr_s10_c6",
                "type": "dining_phrase",
                "glyph": "L'addition, s'il vous plaît",
                "phonetic": "[la.di.sjɔ̃ sil vu plɛ]",
                "gloss": "The bill / check, please",
                "speakText": "L'addition s'il vous plaît",
                "audioUrl": "",
                "whisper": "The standard French formula to request the dining bill at the end of the meal."
            },
            {
                "id": "fr_s10_c7",
                "type": "dining_phrase",
                "glyph": "Bon appétit !",
                "phonetic": "[bɔ̃.n‿a.pe.ti]",
                "gloss": "Enjoy your meal!",
                "speakText": "Bon appétit",
                "audioUrl": "",
                "whisper": "Liaison: the 'n' in 'bon' links to the vowel in 'appétit' as [bɔ̃.n‿a.pe.ti]."
            },
            {
                "id": "fr_s10_c8",
                "type": "dining_phrase",
                "glyph": "C'était délicieux !",
                "phonetic": "[se.tɛ de.li.sjø]",
                "gloss": "It was delicious!",
                "speakText": "C'était délicieux",
                "audioUrl": "",
                "whisper": "Imperfect tense 'c'était' used to praise the quality of the meal upon concluding."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the polite ordering request: 'Je voudrais une carafe d'eau s'il vous plaît'. What was ordered?",
                "speakAudio": "Je voudrais une carafe d'eau s'il vous plaît",
                "options": [
                    "A pitcher of tap water (free in French restaurants)",
                    "A bottle of expensive red wine",
                    "A cup of black espresso"
                ],
                "correct": 0,
                "explain": "'Une carafe d'eau' is a pitcher of tap water, which French restaurants provide free of charge by law."
            },
            {
                "prompt": "Listen to the dining phrase: 'L'addition, s'il vous plaît'. What is the patron requesting?",
                "speakAudio": "L'addition s'il vous plaît",
                "options": [
                    "The bill / check to pay for the meal",
                    "A second dessert",
                    "A table outside on the terrace"
                ],
                "correct": 0,
                "explain": "'L'addition' is the dining bill or check in French restaurants."
            },
            {
                "prompt": "Listen to the server's description: 'La soupe à l'oignon est faite maison'. What does 'faite maison' mean?",
                "speakAudio": "La soupe à l'oignon est faite maison",
                "options": [
                    "Homemade / prepared from scratch in the restaurant kitchen",
                    "Imported from another country",
                    "Pre-packaged and frozen"
                ],
                "correct": 0,
                "explain": "'Fait maison' is a certified French label indicating dishes made on the premises from raw ingredients."
            }
        ],
        "arena": [
            {
                "quest": "Order lunch with refinement: 'I would like a quiche lorraine, please.'",
                "clue": "Chef Marcel: 'Use polite conditional Je voudrais and courtesy s'il vous plaît.'",
                "target": "Je voudrais une quiche lorraine s'il vous plaît",
                "tokens": ["Je", "voudrais", "une", "quiche", "lorraine", "s'il", "vous", "plaît", "veux", "l'addition"],
                "explain": "'Je voudrais' expresses polite desire ('I would like'), followed by the feminine dish 'une quiche lorraine'."
            },
            {
                "quest": "Compliment the bistro kitchen: 'Thank you, the onion soup was delicious!'",
                "clue": "Chef Marcel: 'Combine Merci, la soupe à l'oignon, and feminine adjective délicieuse.'",
                "target": "Merci la soupe à l'oignon était délicieuse",
                "tokens": ["Merci", "la", "soupe", "à", "l'oignon", "était", "délicieuse", "c'était", "addition"],
                "explain": "'Était délicieuse' agrees in gender with the feminine subject 'la soupe'."
            },
            {
                "quest": "Conclude your meal: 'The check please, and keep the change.'",
                "clue": "Chef Marcel: 'Combine L'addition s'il vous plaît and gardez la monnaie.'",
                "target": "L'addition s'il vous plaît gardez la monnaie",
                "tokens": ["L'addition", "s'il", "vous", "plaît", "gardez", "la", "monnaie", "je", "voudrais"],
                "explain": "'L'addition s'il vous plaît' asks for the check, and 'gardez la monnaie' graciously leaves a tip."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the quintessential French crescent breakfast pastry:",
                "tiles": ["C", "R", "O", "I", "S", "S", "A", "N", "T"],
                "answer": "CROISSANT",
                "gloss": "croissant (crescent pastry)"
            },
            {
                "clue": "Assemble the French noun for the restaurant bill / check:",
                "tiles": ["A", "D", "D", "I", "T", "I", "O", "N", "E"],
                "answer": "ADDITION",
                "gloss": "addition (bill / check)"
            },
            {
                "clue": "Assemble the polite conditional verb form 'I would like' (voudrais):",
                "tiles": ["V", "O", "U", "D", "R", "A", "I", "S", "E"],
                "answer": "VOUDRAIS",
                "gloss": "voudrais (would like)"
            }
        ],
        "quiz": [
            {
                "q": "Why do polite French speakers say 'Je voudrais...' instead of 'Je veux...' when ordering in a bistro?",
                "options": [
                    "'Je voudrais' is in the polite conditional mood ('I would like'), whereas 'je veux' ('I want') sounds demanding and rude",
                    "'Je veux' is strictly forbidden by the French Academy",
                    "'Je voudrais' is only used for beverages"
                ],
                "correct": 0,
                "explain": "The conditional of politeness softens the statement into a courteous request rather than a direct command."
            },
            {
                "q": "How can you order free table water in any French restaurant or café?",
                "options": [
                    "Une carafe d'eau, s'il vous plaît",
                    "Une bouteille d'eau gazeuse payante",
                    "Un grand vin rouge"
                ],
                "correct": 0,
                "explain": "'Une carafe d'eau' designates tap water served in a glass pitcher, provided free of charge by French law."
            },
            {
                "q": "What does the expression 'L'addition, s'il vous plaît' literally mean?",
                "options": [
                    "The addition (sum of the charges), please — meaning the bill or check",
                    "Additional bread, please",
                    "A visit with the head chef"
                ],
                "correct": 0,
                "explain": "'L'addition' comes from adding up the items consumed on the check."
            },
            {
                "q": "What classic French dessert consists of chilled vanilla custard with a brittle layer of torched caramelized sugar?",
                "options": [
                    "Crème brûlée",
                    "Tarte Tatin",
                    "Mille-feuille"
                ],
                "correct": 0,
                "explain": "'Crème brûlée' literally means 'burnt cream', referring to the torched sugar crust."
            },
            {
                "q": "When a waiter serves your table and wishes you 'Bon appétit !', how do you courteously respond?",
                "options": [
                    "Merci, à vous aussi ! (or simply 'Merci !')",
                    "Au revoir !",
                    "Non, merci !"
                ],
                "correct": 0,
                "explain": "'Merci !' or 'Merci, à vous aussi !' is the polite response to a dining wish."
            }
        ]
    },
    "latin": {
        "sealName": "Convivium Thermopolii Seal",
        "guide": {
            "name": "Sabina",
            "role": "Thermopolium Hostess & Convivium Keeper",
            "avatar": "🏺",
            "prompt": "Salvēte hospitēs! Welcome to our Pompeian thermopolium—order fresh pānis, caseus, and spiced mulsum wine."
        },
        "cards": [
            {
                "id": "lat_s10_c1",
                "type": "cibus",
                "glyph": "pānis",
                "phonetic": "[ˈpaː.nɪs]",
                "gloss": "bread / loaf (staple Roman food)",
                "speakText": "panis",
                "audioUrl": "",
                "whisper": "Roman round loaves (pānis quadrātus) were baked in brick ovens with eight scored wedge segments, preserved intact at Pompeii."
            },
            {
                "id": "lat_s10_c2",
                "type": "cibus",
                "glyph": "caseus",
                "phonetic": "[ˈkaː.sɛ.ʊs]",
                "gloss": "cheese (fresh or aged sheep/goat cheese)",
                "speakText": "caseus",
                "audioUrl": "",
                "whisper": "Romans relished sheep and goat cheeses, eaten fresh with figs or smoked over wood fires."
            },
            {
                "id": "lat_s10_c3",
                "type": "cibus",
                "glyph": "olīvae",
                "phonetic": "[ɔˈliː.wae̯]",
                "gloss": "olives in brine & fennel",
                "speakText": "olivae",
                "audioUrl": "",
                "whisper": "Plump green and black olives cured with sea salt, fennel seeds, and vinegar; an essential appetizer (gustātiō)."
            },
            {
                "id": "lat_s10_c4",
                "type": "pōtiō",
                "glyph": "mulsum",
                "phonetic": "[ˈmʊɫ.sʊ̃]",
                "gloss": "sweet honeyed wine aperitif",
                "speakText": "mulsum",
                "audioUrl": "",
                "whisper": "White or red wine sweetened with four parts wine to one part aromatic honey and pepper, inaugurating Roman banquets."
            },
            {
                "id": "lat_s10_c5",
                "type": "dining_phrase",
                "glyph": "Da mihi...",
                "phonetic": "[daː ˈmɪ.hɪ]",
                "gloss": "Give to me... / Serve me...",
                "speakText": "Da mihi",
                "audioUrl": "",
                "whisper": "Imperative of dare ('da') paired with dative singular pronoun 'mihi' (to me): 'Da mihi pānem' = Give me bread."
            },
            {
                "id": "lat_s10_c6",
                "type": "dining_phrase",
                "glyph": "Bene sapiat!",
                "phonetic": "[ˈbɛ.nɛ ˈsa.pɪ.at]",
                "gloss": "May it taste good! / Bon appétit!",
                "speakText": "Bene sapiat",
                "audioUrl": "",
                "whisper": "Present subjunctive of 'sapiō' (to taste / savor): an authentic Roman table blessing to fellow diners."
            },
            {
                "id": "lat_s10_c7",
                "type": "dining_phrase",
                "glyph": "Quantī cōnstat?",
                "phonetic": "[ˈkʷan.tiː ˈkoːn.stat]",
                "gloss": "How much does it cost?",
                "speakText": "Quanti constat",
                "audioUrl": "",
                "whisper": "'Quantī' is the genitive of price, used with 'cōnstat' (stands at / costs) to ask the price at the thermopolium."
            },
            {
                "id": "lat_s10_c8",
                "type": "dining_phrase",
                "glyph": "Grātiās tibi agō",
                "phonetic": "[ˈɡraː.tɪ.aːs ˈtɪ.bɪ ˈa.ɡoː]",
                "gloss": "I give thanks to you / Thank you",
                "speakText": "Gratias tibi ago",
                "audioUrl": "",
                "whisper": "The classic idiom for expressing gratitude: literally 'I drive/render thanks to you'."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the customer at the thermopolium counter: 'Da mihi pānem et caseum'. What two items are requested?",
                "speakAudio": "Da mihi panem et caseum",
                "options": [
                    "Bread and cheese (pānem and caseum in accusative)",
                    "Wine and olives",
                    "Fish and garum sauce"
                ],
                "correct": 0,
                "explain": "'Pānem' is the accusative of pānis (bread) and 'caseum' is the accusative of caseus (cheese)."
            },
            {
                "prompt": "Listen to the famous convivial proverb: 'In vīnō vēritās'. What philosophical truth is spoken?",
                "speakAudio": "In vino veritas",
                "options": [
                    "In wine there is truth",
                    "Water is better than wine",
                    "Wine costs too much money"
                ],
                "correct": 0,
                "explain": "'In vīnō vēritās' is the ancient proverb noting that wine loosens tongues to reveal truth."
            },
            {
                "prompt": "Listen to the Roman host's dining blessing: 'Bene sapiat omnibus convīvīs!'. What is the host wishing?",
                "speakAudio": "Bene sapiat omnibus convivis",
                "options": [
                    "May it taste good to all dinner guests (Bon appétit!)",
                    "May everyone go home now",
                    "May the bill be paid promptly"
                ],
                "correct": 0,
                "explain": "'Bene sapiat' uses the optative subjunctive meaning 'may it taste good / delicious'."
            }
        ],
        "arena": [
            {
                "quest": "Order at the marble counter: 'Give me bread and honeyed wine!'",
                "clue": "Sabina: 'Use imperative Da, dative mihi, and accusatives pānem et mulsum.'",
                "target": "Da mihi pānem et mulsum",
                "tokens": ["Da", "mihi", "pānem", "et", "mulsum", "caseus", "vīnum"],
                "explain": "'Da mihi' takes accusative direct objects 'pānem' (bread) and 'mulsum' (honeyed wine)."
            },
            {
                "quest": "Inquire about prices: 'How much do these olives cost?'",
                "clue": "Sabina: 'Use genitive quantī, plural verb cōnstant, and demonstrative hae olīvae.'",
                "target": "Quantī cōnstant hae olīvae",
                "tokens": ["Quantī", "cōnstant", "hae", "olīvae", "cōnstat", "bene"],
                "explain": "'Quantī' is the genitive of price, and 'cōnstant' agrees with the plural subject 'hae olīvae' (these olives)."
            },
            {
                "quest": "Toast the company: 'May it taste good and thank you!'",
                "clue": "Sabina: 'Combine the subjunctive wish Bene sapiat with grātiās tibi agō.'",
                "target": "Bene sapiat et grātiās tibi agō",
                "tokens": ["Bene", "sapiat", "et", "grātiās", "tibi", "agō", "da", "mihi"],
                "explain": "'Bene sapiat' wishes good appetite, followed by the idiom of thanks 'grātiās tibi agō'."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the Latin staple food 'bread' (pānis):",
                "tiles": ["P", "Ā", "N", "I", "S", "T", "O"],
                "answer": "PĀNIS",
                "gloss": "pānis (bread / loaf)"
            },
            {
                "clue": "Assemble the sweet Roman honeyed wine 'mulsum':",
                "tiles": ["M", "U", "L", "S", "U", "M", "E"],
                "answer": "MULSUM",
                "gloss": "mulsum (honeyed wine)"
            },
            {
                "clue": "Assemble the Latin word for 'cheese' (caseus):",
                "tiles": ["C", "A", "S", "E", "U", "S", "O"],
                "answer": "CASEUS",
                "gloss": "caseus (cheese)"
            }
        ],
        "quiz": [
            {
                "q": "What was an ancient Roman 'thermopolium' found along street corners in Pompeii and Herculaneum?",
                "options": [
                    "A commercial street food counter and tavern serving hot food and spiced wine to the urban public",
                    "A public bathhouse reserved exclusively for the Emperor",
                    "A gladiator combat training arena"
                ],
                "correct": 0,
                "explain": "Thermopolia featured L-shaped stone counters with embedded earthenware dolia serving ready-to-eat hot food."
            },
            {
                "q": "What was 'mulsum' in Roman dining culture?",
                "options": [
                    "Wine blended with aromatic honey and spices, traditionally served during the appetizer course (gustātiō)",
                    "A fermented fish paste used as salt substitute",
                    "Vinegar mixed with water drunk by soldiers"
                ],
                "correct": 0,
                "explain": "Mulsum was a sweet, prized honeyed wine opening banquets."
            },
            {
                "q": "In the phrase 'Da mihi pānem', what grammatical case is 'mihi'?",
                "options": [
                    "Dative case (indirect object: 'to me')",
                    "Accusative case (direct object)",
                    "Ablative of accompaniment"
                ],
                "correct": 0,
                "explain": "'Mihi' is the dative singular of the personal pronoun 'ego' (to me)."
            },
            {
                "q": "Why does the question 'Quantī cōnstat?' employ the form 'quantī'?",
                "options": [
                    "It is a genitive of value or price ('at what price does it stand?')",
                    "It is an accusative plural agreeing with money",
                    "It is an adverbial ablative"
                ],
                "correct": 0,
                "explain": "Latin uses genitive adjectives of indefinite quantity (tantī, quantī, magnī) to express commercial cost or value."
            },
            {
                "q": "What pungent, fermented fish sauce was the universal condiment on ancient Roman dining tables?",
                "options": [
                    "Garum (or liquāmen)",
                    "Mulsum",
                    "Defrutum"
                ],
                "correct": 0,
                "explain": "Garum was made by fermenting salted fish viscera in the sun, adding savory umami to Roman cuisine."
            }
        ]
    },
    "hebrew": {
        "sealName": "Shuk HaCarmel Feast Seal",
        "guide": {
            "name": "Eli & Yael",
            "role": "Shuk HaCarmel Food Masters",
            "avatar": "🥙",
            "prompt": "Bete'avon! Step up to our bustling Shuk stall for hot pita, golden falafel, and refreshing limonada."
        },
        "cards": [
            {
                "id": "heb_s10_c1",
                "type": "ma'akhal",
                "glyph": "פָלָאפֶל",
                "phonetic": "faláfel [faˈlafel]",
                "gloss": "crispy deep-fried spiced chickpea balls",
                "speakText": "פלאפל",
                "audioUrl": "",
                "whisper": "Ground chickpeas seasoned with coriander, cumin, parsley, and garlic, deep-fried until crisp and golden brown."
            },
            {
                "id": "heb_s10_c2",
                "type": "ma'akhal",
                "glyph": "חוּמוּס",
                "phonetic": "chúmus [ˈχumus]",
                "gloss": "creamy whipped chickpea puree with tahini",
                "speakText": "חומוס",
                "audioUrl": "",
                "whisper": "Creamy blend of boiled chickpeas, raw sesame tahini, lemon juice, and garlic, drizzled with olive oil and za'atar."
            },
            {
                "id": "heb_s10_c3",
                "type": "ma'akhal",
                "glyph": "שַׁקְשׁוּקָה",
                "phonetic": "shakshúka [ʃakˈʃuka]",
                "gloss": "eggs poached in spicy tomato & pepper sauce",
                "speakText": "שקשוקה",
                "audioUrl": "",
                "whisper": "A sizzling skillet of eggs gently poached in a rich, simmering sauce of sweet tomatoes, red peppers, garlic, and cumin."
            },
            {
                "id": "heb_s10_c4",
                "type": "ma'akhal",
                "glyph": "פִּיתָה",
                "phonetic": "píta [ˈpita]",
                "gloss": "fluffy pocket flatbread",
                "speakText": "פיתה",
                "audioUrl": "",
                "whisper": "Soft, pillowy yeast-leavened flatbread baked at high heat so steam creates a natural hollow pocket."
            },
            {
                "id": "heb_s10_c5",
                "type": "dining_phrase",
                "glyph": "אֶפְשָׁר... בְּבַקָּשָׁה?",
                "phonetic": "efshár... bevakashá?",
                "gloss": "Could I please have...?",
                "speakText": "אפשר בבקשה",
                "audioUrl": "",
                "whisper": "The ubiquitous Israeli ordering phrase: 'efshár faláfel be-píta bevakashá?' = Could I please get falafel in a pita?"
            },
            {
                "id": "heb_s10_c6",
                "type": "dining_phrase",
                "glyph": "כַּמָּה זֶה עוֹלֶה?",
                "phonetic": "káma ze olé?",
                "gloss": "How much does this cost?",
                "speakText": "כמה זה עולה",
                "audioUrl": "",
                "whisper": "Essential market phrase: 'káma' (how much) + 'ze' (this) + 'olé' (ascends/costs)."
            },
            {
                "id": "heb_s10_c7",
                "type": "dining_phrase",
                "glyph": "חֶשְׁבּוֹן בְּבַקָּשָׁה",
                "phonetic": "cheshbón bevakashá",
                "gloss": "The bill / check, please",
                "speakText": "חשבון בבקשה",
                "audioUrl": "",
                "whisper": "Used when asking the server for the dining bill: 'cheshbón' (account/bill) + 'bevakashá' (please)."
            },
            {
                "id": "heb_s10_c8",
                "type": "dining_phrase",
                "glyph": "בְּתֵאָבוֹן!",
                "phonetic": "bete'avón! [beteʔaˈvon]",
                "gloss": "Bon appétit! / Enjoy your meal!",
                "speakText": "בתאבון",
                "audioUrl": "",
                "whisper": "Formed from preposition 'b'-' (with) + 'te'avón' (appetite): 'with good appetite!'"
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the customer at the Shuk counter: 'Efshar pita im falafel ve-t'china bevakasha?'. What fillings were asked for?",
                "speakAudio": "אפשר פיתה עם פלאפל וטחינה בבקשה",
                "options": [
                    "Falafel and tahini inside a pita (פלאפל וטחינה)",
                    "Hummus and eggs only",
                    "Just french fries"
                ],
                "correct": 0,
                "explain": "'Im falafel ve-t'china' specifies falafel balls and sesame tahini sauce."
            },
            {
                "prompt": "Listen to the market price inquiry: 'Kama ze oleh?'. What is the customer asking?",
                "speakAudio": "כמה זה עולה",
                "options": [
                    "How much does this cost?",
                    "Where is the exit?",
                    "Do you have fresh bread?"
                ],
                "correct": 0,
                "explain": "'Kama ze oleh?' is the standard Hebrew expression for inquiring about price."
            },
            {
                "prompt": "Listen to the dining compliment: 'Ha-shakshuka te'ima me'od!'. What is the diner praising?",
                "speakAudio": "השקשוקה טעימה מאוד",
                "options": [
                    "The shakshuka is very delicious! ('te'ima me'od')",
                    "The food is too spicy to eat",
                    "The coffee was too sweet"
                ],
                "correct": 0,
                "explain": "'Te'ima' is the feminine adjective for tasty (agreeing with shakshuka), and 'me'od' means very."
            }
        ],
        "arena": [
            {
                "quest": "Order food at the market: 'Can I have falafel in a pita, please?'",
                "clue": "Eli: 'Begin with efshár, noun faláfel, prepositional be-píta, and bevakashá.'",
                "target": "אֶפְשָׁר פָלָאפֶל בְּפִיתָה בְּבַקָּשָׁה",
                "tokens": ["אפשר", "פלאפל", "בפיתה", "בבקשה", "כמה", "עולה", "חשבון"],
                "explain": "'Efshár' (is it possible) + noun + 'bevakashá' (please) is the classic Israeli ordering formula."
            },
            {
                "quest": "Inquire about cost: 'How much does this hummus cost?'",
                "clue": "Eli: 'Use káma olé, definite noun ha-chúmus, and demonstrative ha-zé.'",
                "target": "כַּמָּה עוֹלֶה הַחוּמוּס הַזֶּה",
                "tokens": ["כמה", "עולה", "החומוס", "הזה", "אפשר", "בבקשה"],
                "explain": "'Káma olé' means 'how much does it cost', followed by 'ha-chúmus ha-zé' (this hummus)."
            },
            {
                "quest": "Ask for the bill with thanks: 'The check please, thank you very much!'",
                "clue": "Eli: 'Combine cheshbón bevakashá with todáh rabáh.'",
                "target": "חֶשְׁבּוֹן בְּבַקָּשָׁה תּוֹדָה רַבָּה",
                "tokens": ["חשבון", "בבקשה", "תודה", "רבה", "טעים", "מאוד"],
                "explain": "'Cheshbón bevakashá' requests the dining bill politely, followed by 'todáh rabáh' (many thanks)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the famous Israeli whipped chickpea dish (hummus):",
                "tiles": ["ח", "ו", "מ", "ו", "ס", "ר"],
                "answer": "חומוס",
                "gloss": "חוּמוּס (hummus)"
            },
            {
                "clue": "Assemble the Hebrew word for 'the check / bill' (cheshbon):",
                "tiles": ["ח", "ש", "ב", "ו", "ן", "מ"],
                "answer": "חשבון",
                "gloss": "חֶשְׁבּוֹן (bill / check)"
            },
            {
                "clue": "Assemble the mealtime blessing 'Bon appétit!' (bete'avon):",
                "tiles": ["ב", "ת", "א", "ב", "ו", "ן"],
                "answer": "בתאבון",
                "gloss": "בְּתֵאָבוֹן (Bon appétit)"
            }
        ],
        "quiz": [
            {
                "q": "What does the polite formula 'Efshár...' (אֶפְשָׁר) literally mean when ordering in Israeli food establishments?",
                "options": [
                    "'Is it possible...?' (e.g. 'Is it possible to have falafel, please?')",
                    "'You must give me immediately...'",
                    "'Do you have any money?'"
                ],
                "correct": 0,
                "explain": "'Efshár' means 'it is possible', offering a polite and natural way to request items."
            },
            {
                "q": "How is 'Bon appétit' phrased in Hebrew?",
                "options": [
                    "Bete'avón! (בְּתֵאָבוֹן! — literally 'with appetite!')",
                    "Lecháim! (לְחַיִּים!)",
                    "Mazal tov!"
                ],
                "correct": 0,
                "explain": "'Bete'avón' combines preposition 'b'-' with 'te'avón' (appetite)."
            },
            {
                "q": "What popular breakfast and dinner dish consists of eggs poached in a zesty sauce of tomatoes, bell peppers, onions, and cumin?",
                "options": [
                    "Shakshuka (שַׁקְשׁוּקָה)",
                    "Knafeh (כְּנָאפֶה)",
                    "Bourekas (בּוּרֵקַס)"
                ],
                "correct": 0,
                "explain": "Shakshuka is a beloved North African dish that has become a staple of Israeli dining."
            },
            {
                "q": "How do you request the bill at the end of a meal in Israel?",
                "options": [
                    "Cheshbón bevakashá (חֶשְׁבּוֹן בְּבַקָּשָׁה)",
                    "Toda raba",
                    "Kama ze"
                ],
                "correct": 0,
                "explain": "'Cheshbón' means account or bill, and 'bevakashá' means please."
            },
            {
                "q": "What refreshing Israeli drink combines fresh lemonade with crushed mint leaves?",
                "options": [
                    "Limonana (לִימוֹנָנָה — from limon + nana/mint)",
                    "Kafe botz",
                    "Gazoz"
                ],
                "correct": 0,
                "explain": "Limonana is a blend of 'limon' (lemon) and 'nana' (fresh mint)."
            }
        ]
    },
    "chinese": {
        "sealName": "Grand Jade Pavilion Banquet Seal",
        "guide": {
            "name": "Chef Zhang",
            "role": "Sichuan & Jiangnan Dim Sum Master",
            "avatar": "🥟",
            "prompt": "Huānyíng! Take a seat in our teahouse—order steaming xiǎolóngbāo, fragrant green tea, and master dining etiquette."
        },
        "cards": [
            {
                "id": "zh_s10_c1",
                "type": "dish",
                "glyph": "小笼包",
                "phonetic": "xiǎolóngbāo [ɕjaʊ̯˨˩˦ lʊŋ˧˥ paʊ̯˥]",
                "gloss": "steamed soup dumplings with hot broth inside",
                "speakText": "小笼包",
                "audioUrl": "",
                "whisper": "Delicate Jiangnan steamed dumplings filled with minced pork and rich gelatinized broth that melts into hot soup inside a bamboo steamer."
            },
            {
                "id": "zh_s10_c2",
                "type": "dish",
                "glyph": "麻婆豆腐",
                "phonetic": "mápó dòufu [ma˧˥ pʰwɔ˧˥ toʊ̯˥˩ fu]",
                "gloss": "spicy Sichuan silken tofu with chili & Sichuan pepper",
                "speakText": "麻婆豆腐",
                "audioUrl": "",
                "whisper": "Legendary Sichuan dish: silken tofu cubes simmered with fermented bean paste (dòubànjiàng), minced beef, and numbing Sichuan peppercorn oil (málà)."
            },
            {
                "id": "zh_s10_c3",
                "type": "dish",
                "glyph": "宫保鸡丁",
                "phonetic": "gōngbǎo jīdīng [kʊŋ˥ paʊ̯˨˩˦ tɕi˥ tiŋ˥]",
                "gloss": "Kung Pao diced chicken with peanuts & chilies",
                "speakText": "宫保鸡丁",
                "audioUrl": "",
                "whisper": "Stir-fried chicken breast cubes tossed with roasted peanuts, dried red chilies, scallions, and a sweet, sour, and savory glaze."
            },
            {
                "id": "zh_s10_c4",
                "type": "beverage",
                "glyph": "龙井绿茶",
                "phonetic": "lóngjǐng lǜchá [lʊŋ˧˥ tɕiŋ˨˩˦ ly˥˩ ʈʂʰa˧˥]",
                "gloss": "Longjing 'Dragon Well' green tea",
                "speakText": "龙井绿茶",
                "audioUrl": "",
                "whisper": "World-famous pan-roasted green tea from Hangzhou, prized for flat sword-shaped leaves, chestnut aroma, and sweet aftertaste."
            },
            {
                "id": "zh_s10_c5",
                "type": "dining_phrase",
                "glyph": "服务员，点菜！",
                "phonetic": "Fúwùyuán, diǎncài! [fu˧˥ u˥˩ ɥan˧˥ tjan˨˩˦ tsʰaɪ̯˥˩]",
                "gloss": "Waiter, we are ready to order!",
                "speakText": "服务员点菜",
                "audioUrl": "",
                "whisper": "The polite, standard call across restaurants in China to announce readiness to place an order: 'fúwùyuán' (server) + 'diǎncài' (order dishes)."
            },
            {
                "id": "zh_s10_c6",
                "type": "dining_phrase",
                "glyph": "我要一份...",
                "phonetic": "Wǒ yào yí fèn... [wɔ˨˩˦ jaʊ̯˥˩ i˧˥ fən˥˩]",
                "gloss": "I would like one portion / serving of...",
                "speakText": "我要一份",
                "audioUrl": "",
                "whisper": "'一份' (yí fèn) is the proper measure word for an order/portion of food: 'wǒ yào yí fèn xiǎolóngbāo'."
            },
            {
                "id": "zh_s10_c7",
                "type": "dining_phrase",
                "glyph": "买单！",
                "phonetic": "Mǎidān! [maɪ˨˩˦ tan˥]",
                "gloss": "The bill / check, please!",
                "speakText": "买单",
                "audioUrl": "",
                "whisper": "Widely used term borrowed from Cantonese (maai1 daan1) to ask for the dining bill."
            },
            {
                "id": "zh_s10_c8",
                "type": "dining_phrase",
                "glyph": "很好吃！",
                "phonetic": "Hěn hǎochī! [xən˨˩˦ xaʊ̯˨˩˦ ʈʂʰʐ̩˥]",
                "gloss": "Very delicious!",
                "speakText": "很好吃",
                "audioUrl": "",
                "whisper": "Tone sandhi: 'hěn' (3rd tone) followed by 'hǎo' (3rd tone) is pronounced with 'hěn' shifting to 2nd tone: [xən˧˥ xaʊ̯˨˩˦ ʈʂʰʐ̩˥]."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the customer: 'Fúwùyuán, wǒ yào yí fèn xiǎolóngbāo'. What did they order?",
                "speakAudio": "服务员我要一份小笼包",
                "options": [
                    "One portion of steamed soup dumplings (xiǎolóngbāo)",
                    "A bowl of spicy noodles",
                    "A pot of black tea"
                ],
                "correct": 0,
                "explain": "'Xiǎolóngbāo' are delicate steamed soup dumplings served in a bamboo steamer."
            },
            {
                "prompt": "Listen to the call at the end of the meal: 'Fúwùyuán, mǎidān, xièxie!'. What is the guest asking for?",
                "speakAudio": "服务员买单谢谢",
                "options": [
                    "The bill / check to pay for the meal ('买单')",
                    "A refill of hot water",
                    "A takeaway container"
                ],
                "correct": 0,
                "explain": "'买单' (mǎidān) is the standard term for requesting the dining bill."
            },
            {
                "prompt": "Listen to the dining hospitality wish: 'Mànman chī!'. What does this wish convey?",
                "speakAudio": "慢慢吃",
                "options": [
                    "Eat slowly and enjoy your meal! (Chinese equivalent of 'Bon appétit')",
                    "You must eat very quickly",
                    "The food is still frozen"
                ],
                "correct": 0,
                "explain": "'慢慢吃' (literally 'eat slowly') is the courteous host blessing encouraging guests to savor their meal."
            }
        ],
        "arena": [
            {
                "quest": "Call the waiter to order: 'Waiter, we would like to order dishes!'",
                "clue": "Chef Zhang: 'Combine fúwùyuán, wǒmen (we), yào (want), and diǎncài.'",
                "target": "服务员我们要点菜",
                "tokens": ["服务员", "我们", "要", "点菜", "买单", "吃过", "了"],
                "explain": "'服务员' is the polite address for restaurant servers, followed by '点菜' (to order dishes)."
            },
            {
                "quest": "Order spicy tofu: 'I want one portion of mapo tofu.'",
                "clue": "Chef Zhang: 'Combine wǒ yào, measure phrase yí fèn, and dish mápó dòufu.'",
                "target": "我要一份麻婆豆腐",
                "tokens": ["我", "要", "一份", "麻婆豆腐", "买单", "龙井茶"],
                "explain": "'一份' (yí fèn) is the proper classifier for a portion/order of a dish."
            },
            {
                "quest": "Compliment and settle the bill: 'The dumplings are delicious, waiter, check please!'",
                "clue": "Chef Zhang: 'Assemble jiǎozi, hěn hǎochī, fúwùyuán, and mǎidān.'",
                "target": "饺子很好吃服务员买单",
                "tokens": ["饺子", "很", "好吃", "服务员", "买单", "在", "不"],
                "explain": "'很' + '好吃' praises the delicious food, while '买单' requests the bill."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the characters for 'soup dumplings' (小笼包):",
                "tiles": ["小", "笼", "包", "大", "点"],
                "answer": "小笼包",
                "gloss": "小笼包 (soup dumplings)"
            },
            {
                "clue": "Assemble the characters for requesting the restaurant bill (买单):",
                "tiles": ["买", "单", "点", "菜", "饭"],
                "answer": "买单",
                "gloss": "买单 (pay the bill)"
            },
            {
                "clue": "Assemble the characters for 'delicious / tasty to eat' (好吃):",
                "tiles": ["好", "吃", "喝", "茶", "水"],
                "answer": "好吃",
                "gloss": "好吃 (delicious to eat)"
            }
        ],
        "quiz": [
            {
                "q": "How do you politely call the attention of waitstaff across restaurants in China?",
                "options": [
                    "Fúwùyuán! (服务员! — 'Server / Waiter!')",
                    "Tóngzhì! (Comrade!)",
                    "Shīfu! to everyone"
                ],
                "correct": 0,
                "explain": "'服务员' (fúwùyuán) is the standard, universally respectful address for service staff."
            },
            {
                "q": "What measure word is typically used when ordering a serving or portion of a dish?",
                "options": [
                    "份 (fèn) — e.g. 一份麻婆豆腐 (yí fèn mápó dòufu)",
                    "个 (gè)",
                    "只 (zhī)"
                ],
                "correct": 0,
                "explain": "'份' (fèn) specifically quantifies servings, portions, or sets of food items."
            },
            {
                "q": "What does the common host blessing 'Mànman chī!' (慢慢吃!) literally mean and convey?",
                "options": [
                    "Literally 'Eat slowly!' — a warm dining blessing equivalent to 'Enjoy your meal / take your time!'",
                    "A warning that the dish contains hot peppers",
                    "An instruction to finish within 5 minutes"
                ],
                "correct": 0,
                "explain": "'慢慢吃' invites diners to relax and enjoy the meal at leisure without rushing."
            },
            {
                "q": "When someone refills your teacup at a Chinese table, what non-verbal gesture expresses gratitude without interrupting conversation?",
                "options": [
                    "Tapping the table lightly with bent index and middle fingertips (the finger kowtow / 叩手礼)",
                    "Clapping hands twice",
                    "Blowing gently across the tea"
                ],
                "correct": 0,
                "explain": "The finger kowtow originated in the Qing dynasty as a discreet silent gesture of thanks when tea is poured."
            },
            {
                "q": "What is the most widely spoken term to ask for the bill at the end of a meal?",
                "options": [
                    "买单 (mǎidān) or 结账 (jiézhàng)",
                    "退菜 (tuìcài)",
                    "打包 (dǎbāo)"
                ],
                "correct": 0,
                "explain": "'买单' (mǎidān) is the ubiquitous term for settling the restaurant check."
            }
        ]
    },
    "german": {
        "sealName": "Gasthaus zur Gemütlichkeit Seal",
        "guide": {
            "name": "Gastwirt Klaus",
            "role": "Gasthaus Host & Master of the Feast",
            "avatar": "🍺",
            "prompt": "Guten Appetit! Welcome to our cozy Gasthaus—order Schnitzel, Brezeln, and celebrate genuine Gemütlichkeit."
        },
        "cards": [
            {
                "id": "de_s10_c1",
                "type": "gericht",
                "glyph": "Schnitzel mit Kartoffelsalat",
                "phonetic": "[ˈʃnɪtsl̩ mɪt kaʁˈtɔfl̩zaˌlaːt]",
                "gloss": "breaded cutlet with warm Bavarian potato salad",
                "speakText": "Schnitzel mit Kartoffelsalat",
                "audioUrl": "",
                "whisper": "Golden pan-fried breaded cutlet served with tender potato salad tossed in warm broth, vinegar, and mustard."
            },
            {
                "id": "de_s10_c2",
                "type": "gericht",
                "glyph": "Bratwurst mit Sauerkraut",
                "phonetic": "[ˈbʁaːtvʊʁst mɪt ˈzaʊ̯ɐˌkʁaʊ̯t]",
                "gloss": "grilled pork sausage with fermented cabbage",
                "speakText": "Bratwurst mit Sauerkraut",
                "audioUrl": "",
                "whisper": "Savory grilled German pork sausage paired with tangy braised sauerkraut and spicy German Senf (mustard)."
            },
            {
                "id": "de_s10_c3",
                "type": "backware",
                "glyph": "Brezel",
                "phonetic": "[ˈbʁeːt͡sl̩]",
                "gloss": "traditional Bavarian lye pretzel with coarse salt",
                "speakText": "Brezel",
                "audioUrl": "",
                "whisper": "Characteristic knotted pastry dipped in lye before baking to develop a deep mahogany crust dusted with coarse sea salt."
            },
            {
                "id": "de_s10_c4",
                "type": "getraenk",
                "glyph": "Apfelschorle",
                "phonetic": "[ˈʔapfl̩ˌʃɔʁlə]",
                "gloss": "sparkling mineral water with apple juice",
                "speakText": "Apfelschorle",
                "audioUrl": "",
                "whisper": "Germany's favorite everyday refreshment: crisp blend of carbonated mineral water and cloudy or clear apple juice."
            },
            {
                "id": "de_s10_c5",
                "type": "dining_phrase",
                "glyph": "Ich hätte gern...",
                "phonetic": "[ɪç ˈhɛtə ɡɛʁn]",
                "gloss": "I would like to have... (Polite Konjunktiv II)",
                "speakText": "Ich hätte gern",
                "audioUrl": "",
                "whisper": "The standard polite formula when ordering in German restaurants: 'Ich hätte gern ein Wiener Schnitzel'."
            },
            {
                "id": "de_s10_c6",
                "type": "dining_phrase",
                "glyph": "Die Rechnung, bitte!",
                "phonetic": "[diː ˈʁɛçnʊŋ ˈbɪtə]",
                "gloss": "The bill / check, please!",
                "speakText": "Die Rechnung bitte",
                "audioUrl": "",
                "whisper": "Clear and polite request to settle the bill at a Gasthaus or café."
            },
            {
                "id": "de_s10_c7",
                "type": "dining_phrase",
                "glyph": "Guten Appetit!",
                "phonetic": "[ˈɡuːtn̩ ʔapeˈtiːt]",
                "gloss": "Enjoy your meal!",
                "speakText": "Guten Appetit",
                "audioUrl": "",
                "whisper": "The universal German wish shared around the table before the first bite."
            },
            {
                "id": "de_s10_c8",
                "type": "dining_phrase",
                "glyph": "Das schmeckt ausgezeichnet!",
                "phonetic": "[das ʃmɛkt ˈʔaʊ̯sɡəˌtsaɪ̯çnət]",
                "gloss": "That tastes extraordinary / exquisite!",
                "speakText": "Das schmeckt ausgezeichnet",
                "audioUrl": "",
                "whisper": "'Schmecken' means to taste; 'ausgezeichnet' means excellent or top-tier."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the guest ordering at the Gasthaus: 'Ich hätte gern ein Schnitzel und eine Apfelschorle'. What was ordered?",
                "speakAudio": "Ich hätte gern ein Schnitzel und eine Apfelschorle",
                "options": [
                    "A Schnitzel and an apple spritzer (Apfelschorle)",
                    "A Bratwurst and a beer",
                    "A bowl of potato soup"
                ],
                "correct": 0,
                "explain": "'Ich hätte gern' means 'I would like to have', ordering Schnitzel and sparkling apple spritzer."
            },
            {
                "prompt": "Listen to the server's question at payment: 'Zusammen oder getrennt?'. What is being asked?",
                "speakAudio": "Zusammen oder getrennt",
                "options": [
                    "Together or separate? (Asking whether guests want a single bill or split checks)",
                    "Cash or credit card?",
                    "Inside or outside seating?"
                ],
                "correct": 0,
                "explain": "In German restaurants, servers customarily ask 'Zusammen oder getrennt?' to allow each diner to pay only for their own items."
            },
            {
                "prompt": "Listen to the compliment: 'Das Essen schmeckt wunderbar!'. What does the guest mean?",
                "speakAudio": "Das Essen schmeckt wunderbar",
                "options": [
                    "The food tastes wonderful! ('schmeckt wunderbar')",
                    "The food is too salty",
                    "The portion is too small"
                ],
                "correct": 0,
                "explain": "'Schmeckt wunderbar' expresses that the food tastes wonderful."
            }
        ],
        "arena": [
            {
                "quest": "Order dinner politely: 'I would like a Schnitzel with potato salad, please.'",
                "clue": "Gastwirt Klaus: 'Use polite Ich hätte gern, ein Schnitzel, mit Kartoffelsalat, and bitte.'",
                "target": "Ich hätte gern ein Schnitzel mit Kartoffelsalat bitte",
                "tokens": ["Ich", "hätte", "gern", "ein", "Schnitzel", "mit", "Kartoffelsalat", "bitte", "will", "Rechnung"],
                "explain": "'Ich hätte gern' (Konjunktiv II) is the hallmark of German polite dining etiquette."
            },
            {
                "quest": "Compliment the feast: 'Thank you very much, the Bratwurst tastes very delicious!'",
                "clue": "Gastwirt Klaus: 'Combine Vielen Dank, die Bratwurst, schmeckt, and sehr lecker.'",
                "target": "Vielen Dank die Bratwurst schmeckt sehr lecker",
                "tokens": ["Vielen", "Dank", "die", "Bratwurst", "schmeckt", "sehr", "lecker", "bitte", "Rechnung"],
                "explain": "'Schmecken' takes the food as subject and means 'to taste [good/delicious]'."
            },
            {
                "quest": "Request the bill: 'The check please, we would like to pay.'",
                "clue": "Gastwirt Klaus: 'Combine Die Rechnung bitte with wir möchten bezahlen.'",
                "target": "Die Rechnung bitte wir möchten bezahlen",
                "tokens": ["Die", "Rechnung", "bitte", "wir", "möchten", "bezahlen", "hätte", "gern"],
                "explain": "'Die Rechnung, bitte' and 'wir möchten bezahlen' are standard closing requests in German restaurants."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the famous breaded German cutlet (Schnitzel):",
                "tiles": ["S", "C", "H", "N", "I", "T", "Z", "E", "L"],
                "answer": "SCHNITZEL",
                "gloss": "Schnitzel (cutlet)"
            },
            {
                "clue": "Assemble the salted Bavarian knotted lye pastry (Brezel):",
                "tiles": ["B", "R", "E", "Z", "E", "L", "T"],
                "answer": "BREZEL",
                "gloss": "Brezel (pretzel)"
            },
            {
                "clue": "Assemble the German word for the dining bill / check (Rechnung):",
                "tiles": ["R", "E", "C", "H", "N", "U", "N", "G", "E"],
                "answer": "RECHNUNG",
                "gloss": "Rechnung (bill / check)"
            }
        ],
        "quiz": [
            {
                "q": "Why is 'Ich hätte gern...' preferred over 'Ich will...' when placing an order in German restaurants?",
                "options": [
                    "'Ich hätte gern...' is the polite subjunctive II form ('I would like to have'), whereas 'Ich will...' sounds blunt and discourteous",
                    "'Ich will' is only used when speaking to children or pets",
                    "'Ich hätte gern' indicates that you want the chef to cook at your table"
                ],
                "correct": 0,
                "explain": "Konjunktiv II ('hätte gern') is standard German restaurant etiquette for polite requests."
            },
            {
                "q": "When settling the bill at a German Gasthaus, the server customarily asks: 'Zusammen oder getrennt?'. What does this mean?",
                "options": [
                    "'Together or separate?' (Asking whether diners wish to pay on one combined check or itemize individual bills)",
                    "'Cash or card?'",
                    "'Would you like dessert or coffee?'"
                ],
                "correct": 0,
                "explain": "Itemized separate checks ('getrennt zahlen') are common and standard practice across Germany and Austria."
            },
            {
                "q": "What popular non-alcoholic German beverage is made by blending sparkling mineral water with apple juice?",
                "options": [
                    "Apfelschorle",
                    "Spezi",
                    "Radler"
                ],
                "correct": 0,
                "explain": "Apfelschorle is a ubiquitous sparkling apple juice spritzer."
            },
            {
                "q": "What is the customary way to wish your dining companions an enjoyable meal in German before eating?",
                "options": [
                    "Guten Appetit! (or 'Mahlzeit!')",
                    "Gute Reise!",
                    "Herzlichen Glückwunsch!"
                ],
                "correct": 0,
                "explain": "'Guten Appetit!' is the German equivalent of 'Enjoy your meal!' or 'Bon appétit!'."
            },
            {
                "q": "How do you politely ask for the check in a German Gasthaus or café?",
                "options": [
                    "Die Rechnung, bitte! (or 'Wir möchten bitte bezahlen')",
                    "Geld her!",
                    "Ich bin fertig, Tschüss!"
                ],
                "correct": 0,
                "explain": "'Die Rechnung, bitte!' is the standard polite phrase for requesting the dining bill."
            }
        ]
    }
}


def validate_data():
    """Verify data integrity across all realms for Step 9 and Step 10."""
    realms = ["waray", "french", "latin", "hebrew", "chinese", "german"]
    for step_num, step_dict in [(9, STEP9_DATA), (10, STEP10_DATA)]:
        for realm in realms:
            assert realm in step_dict, f"Missing realm {realm} in STEP{step_num}_DATA"
            data = step_dict[realm]
            assert "sealName" in data and isinstance(data["sealName"], str), f"Missing sealName in {realm} Step {step_num}"
            assert "guide" in data, f"Missing guide in {realm} Step {step_num}"
            for g_field in ["name", "role", "avatar", "prompt"]:
                assert g_field in data["guide"], f"Missing guide.{g_field} in {realm} Step {step_num}"
            
            # Cards check: 7-10 cards
            assert "cards" in data, f"Missing cards in {realm} Step {step_num}"
            assert 7 <= len(data["cards"]) <= 10, f"Expected 7-10 cards in {realm} Step {step_num}, got {len(data['cards'])}"
            for card in data["cards"]:
                for c_field in ["id", "type", "glyph", "phonetic", "gloss", "speakText", "audioUrl", "whisper"]:
                    assert c_field in card, f"Missing card field {c_field} in {realm} Step {step_num} card {card.get('id')}"

            # EarGym check: 3-4 items
            assert "earGym" in data, f"Missing earGym in {realm} Step {step_num}"
            assert 3 <= len(data["earGym"]) <= 4, f"Expected 3-4 earGym in {realm} Step {step_num}, got {len(data['earGym'])}"
            for eg in data["earGym"]:
                for eg_field in ["prompt", "speakAudio", "options", "correct", "explain"]:
                    assert eg_field in eg, f"Missing earGym field {eg_field} in {realm} Step {step_num}"
                assert isinstance(eg["options"], list) and len(eg["options"]) >= 3, f"earGym options must have at least 3 items in {realm} Step {step_num}"
                assert 0 <= eg["correct"] < len(eg["options"]), f"earGym correct index out of bounds in {realm} Step {step_num}"

            # Arena check: 3-4 items
            assert "arena" in data, f"Missing arena in {realm} Step {step_num}"
            assert 3 <= len(data["arena"]) <= 4, f"Expected 3-4 arena quests in {realm} Step {step_num}, got {len(data['arena'])}"
            for ar in data["arena"]:
                for ar_field in ["quest", "clue", "target", "tokens", "explain"]:
                    assert ar_field in ar, f"Missing arena field {ar_field} in {realm} Step {step_num}"
                assert isinstance(ar["tokens"], list) and len(ar["tokens"]) >= 3, f"arena tokens must have at least 3 items in {realm} Step {step_num}"

            # Scribe check: exactly 3 items
            assert "scribe" in data, f"Missing scribe in {realm} Step {step_num}"
            assert len(data["scribe"]) == 3, f"Expected exactly 3 scribe items in {realm} Step {step_num}, got {len(data['scribe'])}"
            for sc in data["scribe"]:
                for sc_field in ["clue", "tiles", "answer", "gloss"]:
                    assert sc_field in sc, f"Missing scribe field {sc_field} in {realm} Step {step_num}"

            # Quiz check: exactly 5 items
            assert "quiz" in data, f"Missing quiz in {realm} Step {step_num}"
            assert len(data["quiz"]) == 5, f"Expected exactly 5 quiz questions in {realm} Step {step_num}, got {len(data['quiz'])}"
            for qz in data["quiz"]:
                for qz_field in ["q", "options", "correct", "explain"]:
                    assert qz_field in qz, f"Missing quiz field {qz_field} in {realm} Step {step_num}"
                assert isinstance(qz["options"], list) and len(qz["options"]) == 3, f"quiz options must have exactly 3 items in {realm} Step {step_num}"
                assert 0 <= qz["correct"] < len(qz["options"]), f"quiz correct index out of bounds in {realm} Step {step_num}"

    print("ALL VALIDATION CHECKS PASSED: STEP9_DATA and STEP10_DATA are structurally sound and complete!")


if __name__ == "__main__":
    validate_data()
    print("Step 9 & Step 10 data successfully loaded.")
