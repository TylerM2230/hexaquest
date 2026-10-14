#!/usr/bin/env python3
"""
HexaQuest Step 3 & Step 4 Comprehensive Pedagogical Dataset
===========================================================
Defines complete, linguistically validated datasets for:
- STEP 3: Verb To Be / To Have & Personal Pronouns
- STEP 4: Vocabulary to Talk About Yourself (Name, age, origin, profession, residence, hobbies)

Across all 6 HexaQuest Language Realms:
1. Waray-Waray (Austronesian / Visayan)
2. French (Romance)
3. Latin (Classical Italic)
4. Hebrew (Semitic)
5. Mandarin Chinese (Sinitic)
6. German (West Germanic)
"""

# ==============================================================================
# STEP 3: VERB TO BE / TO HAVE & PERSONAL PRONOUNS
# ==============================================================================

WARAY_STEP3 = {
    "sealName": "Balay han Yana Existential Seal",
    "guide": {
        "name": "Manang Elena",
        "role": "Village Elder & Storyteller",
        "avatar": "🥥",
        "prompt": "Maupay nga adlaw! In Waray, we do not need a verb 'to be'—the predicate leads the sentence! And we have 'may-ada' (there is/to have) and 'waray' (none). Let us master our pronouns and existentials."
    },
    "cards": [
        {
            "id": "war3_c1",
            "type": "subject_pronoun",
            "glyph": "ako",
            "phonetic": "[ʔa.ˈko]",
            "gloss": "I / me (1st person singular)",
            "speakText": "ako",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-ako.wav",
            "whisper": "Waray is a predicate-initial language: 'Maabtik ako' = 'I am energetic'. 'Ako' is the focal/absolutive 1st person singular pronoun placed after the predicate."
        },
        {
            "id": "war3_c2",
            "type": "subject_pronoun",
            "glyph": "ikaw / ka",
            "phonetic": "[ʔi.ˈkaw] / [ka]",
            "gloss": "you (2nd person singular)",
            "speakText": "ikaw, ka",
            "audioUrl": "",
            "whisper": "'Ikaw' is used in standalone, preposed, or emphatic positions ('Ikaw an magturutdo'), while 'ka' is the enclitic form attached after the initial predicate ('Mag-opay ka')."
        },
        {
            "id": "war3_c3",
            "type": "subject_pronoun",
            "glyph": "hiya",
            "phonetic": "[hi.ˈja]",
            "gloss": "he / she / it (3rd person singular)",
            "speakText": "hiya",
            "audioUrl": "",
            "whisper": "Waray pronouns are completely gender-neutral! 'Hiya' translates to both he and she: 'Magsusurat hiya' (He/She is a writer)."
        },
        {
            "id": "war3_c4",
            "type": "subject_pronoun",
            "glyph": "kita (inc.) vs kami (exc.)",
            "phonetic": "[ki.ˈta] / [ka.ˈmi]",
            "gloss": "we inclusive (kita) / we exclusive (kami)",
            "speakText": "kita, kami",
            "audioUrl": "",
            "whisper": "Crucial Austronesian clusivity distinction! 'Kita' includes the listener ('all of us together'), whereas 'kami' excludes the listener ('us, but not you')."
        },
        {
            "id": "war3_c5",
            "type": "subject_pronoun",
            "glyph": "kamo / hira",
            "phonetic": "[ka.ˈmo] / [hi.ˈɾa]",
            "gloss": "you all (kamo) / they (hira)",
            "speakText": "kamo, hira",
            "audioUrl": "",
            "whisper": "'Kamo' addresses multiple people (2nd plural); 'hira' refers to third-person plural ('they'): 'Mag-opay hira' (They are good)."
        },
        {
            "id": "war3_c6",
            "type": "existential",
            "glyph": "may-ada / may",
            "phonetic": "[maj.ˈʔa.da] / [maj]",
            "gloss": "there is / to have (existential positive)",
            "speakText": "may-ada",
            "audioUrl": "",
            "whisper": "Waray has no verb 'to have'; instead, it uses the existential particle 'may-ada' (or shortened 'may'): 'May-ada ako libro' = 'I have a book' (lit. 'There is my book')."
        },
        {
            "id": "war3_c7",
            "type": "existential",
            "glyph": "waray",
            "phonetic": "[wa.ˈɾaj]",
            "gloss": "there is none / to not have",
            "speakText": "waray",
            "audioUrl": "",
            "whisper": "The iconic namesake of the language! 'Waray' negates existence and possession: 'Waray ako kwarta' = 'I have no money'. It also negates completed actions."
        },
        {
            "id": "war3_c8",
            "type": "possessive_pronoun",
            "glyph": "akon / imo / iya",
            "phonetic": "[ˈʔa.kon] / [ˈʔi.mo] / [ˈʔi.ja]",
            "gloss": "my / your / his, her (preposed genitive)",
            "speakText": "akon, imo, iya",
            "audioUrl": "",
            "whisper": "Preposed possessive pronouns preceded by the article: 'An akon balay' (My house), 'An imo libro' (Your book), 'An iya lapis' (His/Her pencil). Enclitic postposed forms are 'ko', 'mo', 'niya'."
        },
        {
            "id": "war3_c9",
            "type": "possessive_pronoun",
            "glyph": "aton / amon / iyo / ira",
            "phonetic": "[ˈʔa.ton] / [ˈʔa.mon] / [ˈʔi.jo] / [ˈʔi.ɾa]",
            "gloss": "our inc. / our exc. / your pl. / their",
            "speakText": "aton, amon, iyo, ira",
            "audioUrl": "",
            "whisper": "Preposed plural genitives: 'An aton tuna' = our (all of our) land; 'An amon balay' = our (excluding you) house; 'An ira kanta' = their song."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the Waray sentence. Is it about having or not having?",
            "speakAudio": "May-ada ako libro",
            "options": ["I have a book (May-ada ako libro)", "I have no book (Waray ako libro)", "She has a book"],
            "correct": 0,
            "explain": "'May-ada' marks positive existence/possession; 'ako' = I; 'libro' = book."
        },
        {
            "prompt": "Listen to the clusivity marker. Does 'kita' include or exclude the listener?",
            "speakAudio": "Mag-opay kita ngatanan",
            "options": ["Includes everyone (kita = inclusive we)", "Excludes the listener (kami = exclusive we)", "Refers only to they (hira)"],
            "correct": 0,
            "explain": "'Kita' is the inclusive 1st person plural ('all of us together, including you')."
        },
        {
            "prompt": "Listen to the predicate-initial nominal sentence. What does it mean?",
            "speakAudio": "Maabtik hi Pedro",
            "options": ["Pedro is energetic (Maabtik hi Pedro)", "Pedro has arrived", "Pedro is resting"],
            "correct": 0,
            "explain": "Waray has zero copula: Adjective predicate 'Maabtik' (energetic) + personal marker 'hi' + name 'Pedro'."
        },
        {
            "prompt": "Listen to the negative existential statement. What is being expressed?",
            "speakAudio": "Waray hiya kwarta",
            "options": ["He/She has no money (Waray hiya kwarta)", "He/She has lots of money", "Where is the money?"],
            "correct": 0,
            "explain": "'Waray' indicates non-existence/absence of possession: 'Waray hiya kwarta'."
        }
    ],
    "arena": [
        {
            "quest": "Expressing Possession: 'I have a house'",
            "clue": "Manang Elena: 'Combine the existential particle, pronoun, and noun!'",
            "target": "May-ada ako balay",
            "tokens": ["May-ada", "ako", "balay", "Waray", "hiya"],
            "explain": "'May-ada' (there is/have) + 'ako' (I) + 'balay' (house)."
        },
        {
            "quest": "Zero Copula State: 'You are energetic'",
            "clue": "Manang Elena: 'Put the adjective first, then the enclitic pronoun!'",
            "target": "Maabtik ka",
            "tokens": ["Maabtik", "ka", "ako", "balay", "may-ada"],
            "explain": "Adjective 'Maabtik' comes first, followed by enclitic 2nd-person pronoun 'ka'."
        },
        {
            "quest": "Negative Possession: 'We (exclusive) have no food'",
            "clue": "Manang Elena: 'Use the negative existential particle with kami and pagkaon!'",
            "target": "Waray kami pagkaon",
            "tokens": ["Waray", "kami", "pagkaon", "kita", "may-ada"],
            "explain": "'Waray' (none/have not) + 'kami' (we excl.) + 'pagkaon' (food)."
        },
        {
            "quest": "Possessive Pronoun: 'My book is good'",
            "clue": "Manang Elena: 'Build: Mag-opay an akon libro!'",
            "target": "Mag-opay an akon libro",
            "tokens": ["Mag-opay", "an", "akon", "libro", "imo", "waray"],
            "explain": "Predicate 'Mag-opay' (good) + case marker 'an' + preposed possessive 'akon' + 'libro'."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the iconic existential negator WARAY (none / not have):",
            "tiles": ["W", "A", "R", "A", "Y", "O", "K"],
            "answer": "WARAY",
            "gloss": "waray (none / to not have)"
        },
        {
            "clue": "Spell the inclusive 1st person plural pronoun KITA (we / all of us):",
            "tiles": ["K", "I", "T", "A", "M", "O"],
            "answer": "KITA",
            "gloss": "kita (we inclusive)"
        },
        {
            "clue": "Spell the preposed 1st person possessive AKON (my / mine):",
            "tiles": ["A", "K", "O", "N", "I", "M"],
            "answer": "AKON",
            "gloss": "akon (my / mine)"
        }
    ],
    "quiz": [
        {
            "q": "How does Waray-Waray typically express sentences like 'I am energetic' or 'Pedro is good'?",
            "options": [
                "Predicate-initial order with zero copula (e.g. 'Maabtik ako', 'Mag-opay hi Pedro')",
                "Using a mandatory linking verb identical to English 'is'",
                "Placing the pronoun first followed by an auxiliary copula"
            ],
            "correct": 0,
            "explain": "Waray is predicate-initial and uses zero copula for nominal and adjectival predicates."
        },
        {
            "q": "What is the key grammatical difference between 'kita' and 'kami' in Waray?",
            "options": [
                "'kita' includes the listener (inclusive we), while 'kami' excludes the listener (exclusive we)",
                "'kita' is past tense and 'kami' is future tense",
                "'kita' is singular and 'kami' is plural"
            ],
            "correct": 0,
            "explain": "Austronesian clusivity distinguishes 'kita' (you + me/us) from 'kami' (me/us, not you)."
        },
        {
            "q": "How is possession ('to have') expressed in Waray-Waray?",
            "options": [
                "Using the existential particle 'may-ada' (or 'may') + pronoun + noun (e.g. 'May-ada ako libro')",
                "With a dedicated transitive verb inflected like English 'to have'",
                "By placing the possessive suffix '-ing' on the direct object"
            ],
            "correct": 0,
            "explain": "Visayan languages express possession via existential markers: 'May-ada' (there exists/have) and 'Waray' (none/have not)."
        },
        {
            "q": "Which particle negates existence or possession in Waray ('there is no...', 'to not have')?",
            "options": ["waray (e.g. 'Waray ako kwarta')", "diri", "ayaw"],
            "correct": 0,
            "explain": "'Waray' negates existentials and past actions; 'diri' negates future/present verbs and adjectives; 'ayaw' is prohibitive ('don't')."
        },
        {
            "q": "What is the difference between preposed 'akon' and postposed 'ko' in expressing possession?",
            "options": [
                "'akon' stands before the noun with an article ('an akon balay'), while 'ko' cliticizes directly after the noun ('an balay ko')",
                "'akon' is only for food items while 'ko' is for people",
                "'akon' is plural and 'ko' is singular"
            ],
            "correct": 0,
            "explain": "Waray possesses both preposed genitive forms ('an akon balay') and enclitic genitive forms ('an balay ko')."
        }
    ]
}

FRENCH_STEP3 = {
    "sealName": "Sceau Royal d'Identité et Possession",
    "guide": {
        "name": "Maître Luc",
        "role": "Sorbonne Philosopher & Grammarian",
        "avatar": "⚜️",
        "prompt": "Bienvenue ! In French, identity relies on 'être' (to be) and possession on 'avoir' (to have). Master subject pronouns, verb conjugations, and gendered possessive determiners."
    },
    "cards": [
        {
            "id": "fr3_c1",
            "type": "subject_pronoun",
            "glyph": "je / tu / il / elle / on",
            "phonetic": "[ʒə], [ty], [il], [ɛl], [ɔ̃]",
            "gloss": "I, you (informal), he/it, she/it, one/we",
            "speakText": "je, tu, il, elle, on",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-je.ogg",
            "whisper": "Subject pronouns are mandatory in French because verb endings are often homophonous. 'On' is widely used in spoken French for 'nous' (we)!"
        },
        {
            "id": "fr3_c2",
            "type": "subject_pronoun",
            "glyph": "nous / vous / ils / elles",
            "phonetic": "[nu], [vu], [il], [ɛl]",
            "gloss": "we, you (formal/plural), they (m./f.)",
            "speakText": "nous, vous, ils, elles",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/Fr-nous.ogg",
            "whisper": "Note the silent final 's'. When followed by a vowel, 's' links via liaison as a [z] sound: 'nous avons' [nu.za.vɔ̃]!"
        },
        {
            "id": "fr3_c3",
            "type": "verb_conjugation",
            "glyph": "être: suis, es, est",
            "phonetic": "[ʒə sɥi], [ty ɛ], [il ɛ]",
            "gloss": "to be: I am, you are, he/she is",
            "speakText": "je suis, tu es, il est",
            "audioUrl": "",
            "whisper": "The irregular auxiliary 'être'. 'Es' and 'est' are phonetically identical ([ɛ]), distinguished only by the subject pronoun."
        },
        {
            "id": "fr3_c4",
            "type": "verb_conjugation",
            "glyph": "être: sommes, êtes, sont",
            "phonetic": "[nu sɔm], [vu.z‿ɛt], [il sɔ̃]",
            "gloss": "we are, you are, they are",
            "speakText": "nous sommes, vous êtes, ils sont",
            "audioUrl": "",
            "whisper": "Notice the liaison in 'vous êtes' [vu.z‿ɛt] and the nasal contrast between 'ils sont' [il sɔ̃] (they are) and 'ils ont' [il.z‿ɔ̃] (they have)!"
        },
        {
            "id": "fr3_c5",
            "type": "verb_conjugation",
            "glyph": "avoir: ai, as, a",
            "phonetic": "[ʒe], [ty a], [il a]",
            "gloss": "to have: I have, you have, he/she has",
            "speakText": "j'ai, tu as, il a",
            "audioUrl": "",
            "whisper": "Elision happens before a vowel: 'je + ai' becomes 'j'ai' [ʒe]. Never write 'je ai'!"
        },
        {
            "id": "fr3_c6",
            "type": "verb_conjugation",
            "glyph": "avoir: avons, avez, ont",
            "phonetic": "[nu.za.vɔ̃], [vu.za.ve], [il.z‿ɔ̃]",
            "gloss": "we have, you have, they have",
            "speakText": "nous avons, vous avez, ils ont",
            "audioUrl": "",
            "whisper": "Acoustic Minimal Pair: 'ils sont' has an unvoiced [s] ([il sɔ̃] = they are), while 'ils ont' has a voiced liaison [z] ([il.z‿ɔ̃] = they have)!"
        },
        {
            "id": "fr3_c7",
            "type": "possessive_determiner",
            "glyph": "mon / ma / mes",
            "phonetic": "[mɔ̃], [ma], [me]",
            "gloss": "my (masc. / fem. / plural)",
            "speakText": "mon, ma, mes",
            "audioUrl": "",
            "whisper": "Possessives agree with the possessed object, not the owner: 'mon livre' (masc.), 'ma table' (fem.), 'mes amis' (plural). Special rule: 'mon amie' (fem. starting with vowel takes 'mon')!"
        },
        {
            "id": "fr3_c8",
            "type": "possessive_determiner",
            "glyph": "ton / ta / tes & son / sa / ses",
            "phonetic": "[tɔ̃, ta, te] / [sɔ̃, sa, se]",
            "gloss": "your / his, her, its",
            "speakText": "ton, ta, tes, son, sa, ses",
            "audioUrl": "",
            "whisper": "'Son / sa / ses' means his, her, OR its depending on the gender of the noun possessed: 'son vélo' = his or her bicycle!"
        },
        {
            "id": "fr3_c9",
            "type": "possessive_determiner",
            "glyph": "notre / nos, votre / vos, leur / leurs",
            "phonetic": "[nɔtʁ / no], [vɔtʁ / vo], [lœʁ / lœʁ]",
            "gloss": "our, your, their (singular / plural)",
            "speakText": "notre, nos, votre, vos, leur, leurs",
            "audioUrl": "",
            "whisper": "For plural possessors, there is no gender distinction in the singular: 'notre maison' (fem.) and 'notre jardin' (masc.) both use 'notre'!"
        }
    ],
    "earGym": [
        {
            "prompt": "Acoustic Minimal Pair: Did the speaker say 'they are' (ils sont) or 'they have' (ils ont)?",
            "speakAudio": "ils ont un livre",
            "options": [
                "They have a book (ils ont — voiced [z] liaison)",
                "They are a book (ils sont — unvoiced [s])",
                "We have a book"
            ],
            "correct": 0,
            "explain": "'ils ont' produces a voiced liaison [z] ([il.z‿ɔ̃]), whereas 'ils sont' produces an unvoiced [s] ([il sɔ̃])."
        },
        {
            "prompt": "Listen to the conjugated verb. Which form of être was used?",
            "speakAudio": "nous sommes heureux",
            "options": ["nous sommes (we are)", "vous êtes (you are)", "ils sont (they are)"],
            "correct": 0,
            "explain": "'sommes' [sɔm] is the 1st person plural of être: 'nous sommes'."
        },
        {
            "prompt": "Listen to the elision. Which phrase was pronounced?",
            "speakAudio": "j'ai un ami",
            "options": ["I have a friend (j'ai un ami)", "I am a friend (je suis un ami)", "You have a friend"],
            "correct": 0,
            "explain": "'j'ai' [ʒe] is 'avoir' with elision before the vowel 'ai'."
        },
        {
            "prompt": "Listen to the possessive determiner. Is the object singular or plural?",
            "speakAudio": "mes livres",
            "options": ["Plural (mes livres [me livʁ])", "Singular masculine (mon livre)", "Singular feminine (ma livre)"],
            "correct": 0,
            "explain": "'mes' [me] is the plural possessive determiner for 'my'."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'I am a student'",
            "clue": "Maître Luc: 'Combine subject pronoun, conjugated être, and noun!'",
            "target": "Je suis étudiant",
            "tokens": ["Je", "suis", "étudiant", "ai", "sommes"],
            "explain": "'Je' + 'suis' (1st sing. of être) + 'étudiant' (no indefinite article needed with profession)."
        },
        {
            "quest": "Build: 'We have a house'",
            "clue": "Maître Luc: 'Use the 1st person plural of avoir: nous avons!'",
            "target": "Nous avons une maison",
            "tokens": ["Nous", "avons", "une", "maison", "sommes", "avez"],
            "explain": "'Nous avons' (we have) + 'une maison' (a house)."
        },
        {
            "quest": "Build: 'He has his book'",
            "clue": "Maître Luc: 'Select il, a, son, and livre!'",
            "target": "Il a son livre",
            "tokens": ["Il", "a", "son", "livre", "est", "sa"],
            "explain": "'Il a' (he has) + 'son' (masculine possessive matching 'livre') + 'livre'."
        },
        {
            "quest": "Build: 'You are our friends'",
            "clue": "Maître Luc: 'Use vous êtes and nos amis!'",
            "target": "Vous êtes nos amis",
            "tokens": ["Vous", "êtes", "nos", "amis", "notre", "avez"],
            "explain": "'Vous êtes' (you are) + 'nos' (plural possessive) + 'amis' (friends)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the 1st person singular form of ÊTRE ('I am' -> SUIS):",
            "tiles": ["S", "U", "I", "S", "E", "T"],
            "answer": "SUIS",
            "gloss": "suis (am)"
        },
        {
            "clue": "Spell the 1st person plural form of ÊTRE ('we are' -> SOMMES):",
            "tiles": ["S", "O", "M", "M", "E", "S", "N"],
            "answer": "SOMMES",
            "gloss": "sommes (are)"
        },
        {
            "clue": "Spell the 2nd person plural form of AVOIR ('you have' -> AVEZ):",
            "tiles": ["A", "V", "E", "Z", "O", "R"],
            "answer": "AVEZ",
            "gloss": "avez (have)"
        }
    ],
    "quiz": [
        {
            "q": "How do French listeners distinguish between 'ils sont' (they are) and 'ils ont' (they have) in speech?",
            "options": [
                "'ils sont' has an unvoiced [s] sound ([il sɔ̃]), while 'ils ont' has a voiced liaison [z] ([il.z‿ɔ̃])",
                "There is no phonetic distinction; only context decides",
                "'ils ont' is pronounced with an aspirated 'h'"
            ],
            "correct": 0,
            "explain": "The letter 's' before vowel in 'ils ont' produces voiced [z]; in 'ils sont', the 's' in 'sont' produces unvoiced [s]."
        },
        {
            "q": "Why do we say 'mon amie' (feminine friend) instead of 'ma amie'?",
            "options": [
                "To avoid hiatus (two consecutive vowel sounds), masculine possessives 'mon, ton, son' are used before feminine words starting with a vowel",
                "Because 'amie' is actually grammatically masculine in formal French",
                "It is a modern slang abbreviation"
            ],
            "correct": 0,
            "explain": "Euphony rule: 'mon, ton, son' replace 'ma, ta, sa' before feminine singular nouns starting with a vowel or mute h."
        },
        {
            "q": "Which conjugation of 'avoir' means 'we have'?",
            "options": ["nous avons", "nous sommes", "nous avez"],
            "correct": 0,
            "explain": "'nous avons' is the 1st person plural present indicative of avoir."
        },
        {
            "q": "What does the possessive determiner 'son' agree with in French?",
            "options": [
                "The gender and number of the noun that is possessed, NOT the gender of the owner",
                "The gender of the person who owns the object",
                "It is always masculine regardless of the noun"
            ],
            "correct": 0,
            "explain": "In French, possessives agree with the possessed object: 'son livre' can mean his book OR her book."
        },
        {
            "q": "What is the contracted form of 'je + ai' (I have)?",
            "options": ["j'ai", "je ai", "j'suis"],
            "correct": 0,
            "explain": "Mandatory elision occurs with 'je' before a vowel sound: 'j'ai'."
        }
    ]
}

LATIN_STEP3 = {
    "sealName": "Sigillum Esse et Possidendi",
    "guide": {
        "name": "Magister Lucius",
        "role": "Roman Grammarian & Scribe",
        "avatar": "🏛️",
        "prompt": "Salvē! In Latin, the verb 'esse' (to be) anchors existence, while possession is expressed with the elegant Dative of Possession ('mihi est...') alongside 'habēre'."
    },
    "cards": [
        {
            "id": "lat3_c1",
            "type": "pronoun",
            "glyph": "ego / tū / is, ea, id",
            "phonetic": "[ˈɛ.ɡɔ], [tuː], [ɪs, ˈɛ.a, ɪd]",
            "gloss": "I / you / he, she, it",
            "speakText": "ego, tu, is, ea, id",
            "audioUrl": "",
            "whisper": "Latin is a pro-drop language: subject pronouns are usually omitted unless needed for emphasis or contrast: 'Ego sum Rōmānus' = 'I (specifically) am a Roman!'"
        },
        {
            "id": "lat3_c2",
            "type": "pronoun",
            "glyph": "nōs / vōs",
            "phonetic": "[noːs], [woːs]",
            "gloss": "we / you (plural)",
            "speakText": "nos, vos",
            "audioUrl": "",
            "whisper": "Both have long vowels: nōs [noːs] and vōs [woːs]. In Classical Latin, 'v' is pronounced as an English [w]."
        },
        {
            "id": "lat3_c3",
            "type": "verb_esse",
            "glyph": "esse: sum, es, est",
            "phonetic": "[sʊm], [ɛs], [ɛst]",
            "gloss": "to be: I am, you are, he/she/it is",
            "speakText": "sum, es, est",
            "audioUrl": "",
            "whisper": "The irregular copula 'esse'. 'Sum' = I am; 'es' = you are; 'est' = he/she/it is. Often placed at the end or following the predicate: 'Discipulus sum'."
        },
        {
            "id": "lat3_c4",
            "type": "verb_esse",
            "glyph": "esse: sumus, estis, sunt",
            "phonetic": "[ˈsʊ.mʊs], [ˈɛs.tɪs], [sʊnt]",
            "gloss": "we are, you are, they are",
            "speakText": "sumus, estis, sunt",
            "audioUrl": "",
            "whisper": "Notice the vocalic rhythm: sŭmus, estis, sunt. In Classical poetry and prose, esse freely shifts position for rhetorical weight."
        },
        {
            "id": "lat3_c5",
            "type": "dative_possession",
            "glyph": "mihi est / tibi est",
            "phonetic": "[ˈmɪ.hɪ ɛst] / [ˈtɪ.bɪ ɛst]",
            "gloss": "to me there is (I have) / to you there is",
            "speakText": "mihi est, tibi est",
            "audioUrl": "",
            "whisper": "The pinnacle of Classical Latin idiom! Instead of 'I have a book', Romans often said 'Mihi est liber' (lit. 'To me there is a book'). The possessed item is the nominative subject!"
        },
        {
            "id": "lat3_c6",
            "type": "verb_habere",
            "glyph": "habēre: habeō, habēs, habet",
            "phonetic": "[haˈbe.oː], [ˈha.beːs], [ˈha.bɛt]",
            "gloss": "to have: I have, you have, he/she has",
            "speakText": "habeo, habes, habet",
            "audioUrl": "",
            "whisper": "Second conjugation verb 'habēre'. While Classical style prefers the dative of possession for intrinsic ownership, habēre is widespread for holding or having physical objects."
        },
        {
            "id": "lat3_c7",
            "type": "possessive_adjective",
            "glyph": "meus, mea, meum / tuus",
            "phonetic": "[ˈmɛ.ʊs], [ˈtʊ.ʊs]",
            "gloss": "my, mine / your, yours (singular)",
            "speakText": "meus, tuus",
            "audioUrl": "",
            "whisper": "Latin possessives are 1st/2nd declension adjectives that decline to match their noun in gender, number, and case: 'fīlius meus' (nom. sing. masc.), 'fīlia mea' (fem.)."
        },
        {
            "id": "lat3_c8",
            "type": "reflexive_possessive",
            "glyph": "suus, sua, suum",
            "phonetic": "[ˈsʊ.ʊs, ˈsʊ.a, ˈsʊ.ʊ̃]",
            "gloss": "his own, her own, its own, their own",
            "speakText": "suus, sua, suum",
            "audioUrl": "",
            "whisper": "Strictly reflexive! 'Suus' refers back to the subject of the clause: 'Claudius librum suum legit' = Claudius reads his own book. For non-reflexive 'his', Romans used genitive 'eius'!"
        },
        {
            "id": "lat3_c9",
            "type": "possessive_adjective",
            "glyph": "noster / vester",
            "phonetic": "[ˈnɔs.tɛr], [ˈwɛs.tɛr]",
            "gloss": "our / your (plural)",
            "speakText": "noster, vester",
            "audioUrl": "",
            "whisper": "Possessives for plural owners: 'pater noster' = our father; 'urbs nostra' = our city."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the Classical Latin construction. Which structure of possession is used?",
            "speakAudio": "Mihi est liber",
            "options": [
                "Dative of Possession ('To me there is a book' = I have a book)",
                "Accusative direct object with habeō",
                "Genitive partitive construction"
            ],
            "correct": 0,
            "explain": "'Mihi' (dative singular of ego) + 'est' + nominative 'liber' forms the classic Dative of Possession."
        },
        {
            "prompt": "Listen to the verb ending. What person is 'sumus'?",
            "speakAudio": "Rōmānī sumus",
            "options": ["1st person plural: We are (sumus)", "2nd person plural: You are (estis)", "3rd person plural: They are (sunt)"],
            "correct": 0,
            "explain": "'sumus' is 1st person plural: 'Rōmānī sumus' = We are Romans."
        },
        {
            "prompt": "Listen to the reflexive possessive. Who does 'suus' refer to?",
            "speakAudio": "Marcus amīcum suum videt",
            "options": ["Marcus's own friend (suus is reflexive to the subject)", "Someone else's friend (eius)", "Our friend (noster)"],
            "correct": 0,
            "explain": "'suus' is strictly reflexive, referring to the grammatical subject Marcus."
        },
        {
            "prompt": "Listen to the copula phrase. What is being stated?",
            "speakAudio": "Discipula bona es",
            "options": ["You are a good female student (es = you are)", "I am a good student", "She is a good student"],
            "correct": 0,
            "explain": "'es' is 2nd person singular of esse: 'You are'."
        }
    ],
    "arena": [
        {
            "quest": "Build Dative of Possession: 'I have a book'",
            "clue": "Magister Lucius: 'Assemble mihi, est, and the nominative liber!'",
            "target": "Mihi est liber",
            "tokens": ["Mihi", "est", "liber", "habeō", "tibi"],
            "explain": "'Mihi' (to me) + 'est' (there is) + 'liber' (a book) = I have a book."
        },
        {
            "quest": "Build Identity: 'I am a Roman citizen'",
            "clue": "Magister Lucius: 'Assemble Cīvis Rōmānus sum!'",
            "target": "Cīvis Rōmānus sum",
            "tokens": ["Cīvis", "Rōmānus", "sum", "es", "est"],
            "explain": "Nominative predicate 'Cīvis Rōmānus' + 1st person copula 'sum'."
        },
        {
            "quest": "Build: 'We have peace'",
            "clue": "Magister Lucius: 'Use the verb habēre: Pācem habēmus!'",
            "target": "Pācem habēmus",
            "tokens": ["Pācem", "habēmus", "habet", "sumus", "mihi"],
            "explain": "'Pācem' (accusative sing. of pāx) + 'habēmus' (1st plural of habēre)."
        },
        {
            "quest": "Build Possessive: 'This is our city'",
            "clue": "Magister Lucius: 'Haec est urbs nostra!'",
            "target": "Haec est urbs nostra",
            "tokens": ["Haec", "est", "urbs", "nostra", "vester", "sunt"],
            "explain": "'Haec' (this fem.) + 'est' + 'urbs nostra' (our city, feminine nominative)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the 1st person singular of ESSE ('I am' -> SUM):",
            "tiles": ["S", "U", "M", "E", "S"],
            "answer": "SUM",
            "gloss": "sum (I am)"
        },
        {
            "clue": "Spell the dative pronoun 'to me' in Dative of Possession (MIHI):",
            "tiles": ["M", "I", "H", "I", "T", "B"],
            "answer": "MIHI",
            "gloss": "mihi (to/for me)"
        },
        {
            "clue": "Spell the 1st person plural of ESSE ('we are' -> SUMUS):",
            "tiles": ["S", "U", "M", "U", "S", "O"],
            "answer": "SUMUS",
            "gloss": "sumus (we are)"
        }
    ],
    "quiz": [
        {
            "q": "How do Classical Romans frequently express ownership in phrases like 'I have a dog'?",
            "options": [
                "Using the Dative of Possession: 'Mihi est canis' (lit. 'To me there is a dog')",
                "Only with the preposition 'cum' + ablative",
                "By turning the noun into an adverb"
            ],
            "correct": 0,
            "explain": "The Dative of Possession ('mihi est...') is one of the most elegant and common idioms in Classical Latin."
        },
        {
            "q": "Why are subject pronouns like 'ego' and 'tū' frequently omitted in Latin sentences?",
            "options": [
                "Because Latin is a pro-drop language; the verb ending unambiguously indicates the person and number",
                "Because ancient Roman law forbade referring directly to oneself",
                "Because subject pronouns only existed in poetry"
            ],
            "correct": 0,
            "explain": "Latin verb endings (e.g. -ō/-m, -s, -t, -mus, -tis, -nt) carry person and number, making independent subject pronouns redundant unless emphatic."
        },
        {
            "q": "What is the key grammatical distinction between 'suus' and 'eius'?",
            "options": [
                "'suus' is reflexive (referring back to the clause's subject), while 'eius' is non-reflexive (referring to someone else)",
                "'suus' is feminine and 'eius' is masculine",
                "'suus' is only used for inanimate objects"
            ],
            "correct": 0,
            "explain": "'suus, sua, suum' always reflects back to the subject of its own clause ('his/her own'). 'eius' is the genitive of is/ea/id meaning of him/her."
        },
        {
            "q": "Which conjugation form of 'esse' means 'they are'?",
            "options": ["sunt", "sumus", "estis"],
            "correct": 0,
            "explain": "'sunt' is the 3rd person plural present indicative of esse."
        },
        {
            "q": "In the sentence 'Noster canis celer est', why is 'noster' masculine nominative singular?",
            "options": [
                "Because it agrees in gender, number, and case with the noun 'canis' (masculine)",
                "Because the owners are all male",
                "Possessives in Latin never change form"
            ],
            "correct": 0,
            "explain": "Latin possessive determiners are true adjectives and agree with the noun they modify in gender, number, and case."
        }
    ]
}

HEBREW_STEP3 = {
    "sealName": "Chotam HaKiyum VeHaKinyan (Seal of Being & Ownership)",
    "guide": {
        "name": "Noa",
        "role": "Jerusalem Linguist & Scribe",
        "avatar": "📜",
        "prompt": "Shalom! In Hebrew present tense, there is no verb 'to be'—we use nominal zero-copula sentences ('אֲנִי תַּלְמִיד'). And for possession, we say 'יש לי' (yesh li - there is to me)!"
    },
    "cards": [
        {
            "id": "heb3_c1",
            "type": "pronoun",
            "glyph": "אֲנִי / אַתָּה / אַתְּ",
            "phonetic": "aní [ʔaˈni], atá [ʔaˈta], at [ʔat]",
            "gloss": "I / you (masc.) / you (fem.)",
            "speakText": "אני, אתה, את",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-ani.ogg",
            "whisper": "Hebrew marks grammatical gender even in the second person: 'atá' is masculine 'you', while 'at' is feminine 'you'. 'Aní' (I) is gender-neutral."
        },
        {
            "id": "heb3_c2",
            "type": "pronoun",
            "glyph": "הוּא / הִיא",
            "phonetic": "hu [hu], hi [hi]",
            "gloss": "he / she",
            "speakText": "הוא, היא",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/He-hu.ogg",
            "whisper": "Famous memory trap for English speakers: 'hu' (הוּא) means HE, 'hi' (הִיא) means SHE, and 'mi' (מִי) means WHO!"
        },
        {
            "id": "heb3_c3",
            "type": "pronoun",
            "glyph": "אֲנַחְנוּ / אַתֶּם / הֵם",
            "phonetic": "anáchnu [aˈnaχnu], atém [aˈtem], hem [hem]",
            "gloss": "we, you (masc. pl.), they (masc. pl.)",
            "speakText": "אנחנו, אתם, הם",
            "audioUrl": "",
            "whisper": "Plural pronouns distinguish masculine and feminine (atén/hen for feminine). A mixed group defaults to the masculine forms ('atém', 'hem')."
        },
        {
            "id": "heb3_c4",
            "type": "nominal_sentence",
            "glyph": "Zero Copula: אֲנִי תַּלְמִיד",
            "phonetic": "aní talmíd [ʔaˈni talˈmid]",
            "gloss": "I am a student (nominal zero-copula)",
            "speakText": "אני תלמיד",
            "audioUrl": "",
            "whisper": "The present tense of 'to be' DOES NOT EXIST in Hebrew! You juxtapose subject and predicate directly: 'Aní talmíd' = 'I [am a] student'."
        },
        {
            "id": "heb3_c5",
            "type": "existential_possession",
            "glyph": "יֵשׁ לִי",
            "phonetic": "yesh li [jeʃ li]",
            "gloss": "I have (lit. 'there is to me')",
            "speakText": "יש לי",
            "audioUrl": "",
            "whisper": "To express 'to have', Hebrew uses the existential particle 'יֵשׁ' (yesh = there is) + preposition 'לְ-' inflected with personal suffix: 'li' (to me). 'Yesh li séfer' = I have a book!"
        },
        {
            "id": "heb3_c6",
            "type": "existential_negation",
            "glyph": "אֵין לִי",
            "phonetic": "eyn li [ʔen li]",
            "gloss": "I do not have (lit. 'there is not to me')",
            "speakText": "אין לי",
            "audioUrl": "",
            "whisper": "'אֵין' (eyn) is the absolute negator of existence. 'Eyn li zman' = I have no time! (lit. 'There is no time to me')."
        },
        {
            "id": "heb3_c7",
            "type": "existential_possession",
            "glyph": "יֵשׁ לְךָ / יֵשׁ לָךְ / יֵשׁ לוֹ / יֵשׁ לָהּ",
            "phonetic": "yesh lechá, yesh lach, yesh lo, yesh lah",
            "gloss": "you have (m/f) / he has / she has",
            "speakText": "יש לך, יש לו, יש לה",
            "audioUrl": "",
            "whisper": "The preposition 'לְ-' inflects for every person: lechá (to you m.), lach (to you f.), lo (to him), lah (to her), lánu (to us), lachem (to you pl.), lahém (to them)."
        },
        {
            "id": "heb3_c8",
            "type": "possessive_pronoun",
            "glyph": "שֶׁלִּי / שֶׁלְּךָ / שֶׁלָּךְ / שֶׁלּוֹ / שֶׁלָּהּ",
            "phonetic": "shelí [ʃeˈli], shelchá, shelách, sheló, sheláh",
            "gloss": "my, mine / your (m/f) / his / her",
            "speakText": "שלי, שלך, שלו, שלה",
            "audioUrl": "",
            "whisper": "Formed from 'שֶׁל' (shel = of) + pronominal suffixes. In modern Hebrew, possessives typically follow the definite noun: 'ha-séfer shelí' = my book (lit. the-book of-me)!"
        },
        {
            "id": "heb3_c9",
            "type": "possessive_pronoun",
            "glyph": "שֶׁלָּנוּ / שֶׁלָּכֶם / שֶׁלָּהֶם",
            "phonetic": "shelánu [ʃeˈlanu], shelachem, shelahém",
            "gloss": "our / your pl. / their",
            "speakText": "שלנו, שלכם, שלהם",
            "audioUrl": "",
            "whisper": "Plural possessives: 'ha-báyit shelánu' = our home; 'ha-talmidím shelahém' = their students."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the possession phrase. Does the speaker have something or not?",
            "speakAudio": "יש לי חבר",
            "options": [
                "I have a friend (yesh li chaver — positive possession)",
                "I do not have a friend (eyn li chaver)",
                "He has a friend"
            ],
            "correct": 0,
            "explain": "'יֵשׁ לִי' (yesh li) means 'I have' (lit. 'there is to me')."
        },
        {
            "prompt": "Listen to the nominal sentence. Notice there is no verb 'to be'. What does it mean?",
            "speakAudio": "אני תלמיד",
            "options": [
                "I am a student (aní talmíd — zero copula)",
                "I have a student",
                "Where is the student?"
            ],
            "correct": 0,
            "explain": "Hebrew present tense has zero copula: 'אני' (I) + 'תלמיד' (student) = I am a student."
        },
        {
            "prompt": "Mnemonic alert! Which pronoun was pronounced: 'hu' (he) or 'hi' (she)?",
            "speakAudio": "הוא בבית",
            "options": [
                "He is at home (hu = he!)",
                "She is at home (hi = she!)",
                "Who is at home? (mi = who!)"
            ],
            "correct": 0,
            "explain": "In Hebrew, 'hu' (הוּא) means 'he', while 'hi' (הִיא) means 'she'."
        },
        {
            "prompt": "Listen to the negative existential. What does the speaker lack?",
            "speakAudio": "אין לי זמן",
            "options": [
                "I have no time (eyn li zman)",
                "I have no money (eyn li kesef)",
                "I have no book"
            ],
            "correct": 0,
            "explain": "'אֵין לִי' (eyn li) means 'I don't have'; 'זְמַן' (zman) means 'time'."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'I have a book' (יֵשׁ לִי סֵפֶר)",
            "clue": "Noa: 'Combine yesh, li, and séfer!'",
            "target": "יש לי ספר",
            "tokens": ["יש", "לי", "ספר", "אין", "של"],
            "explain": "'יש' (there is) + 'לי' (to me) + 'ספר' (a book) = I have a book."
        },
        {
            "quest": "Build: 'I am a teacher' (female: אֲנִי מוֹרָה)",
            "clue": "Noa: 'Direct zero-copula: pronoun + feminine profession!'",
            "target": "אני מורה",
            "tokens": ["אני", "מורה", "יש", "תלמיד", "לי"],
            "explain": "Nominal sentence: 'אני' (I) + 'מורה' (teacher f.) with zero copula."
        },
        {
            "quest": "Build: 'I do not have time' (אֵין לִי זְמַן)",
            "clue": "Noa: 'Use the negative existential particle eyn!'",
            "target": "אין לי זמן",
            "tokens": ["אין", "לי", "זמן", "יש", "ספר"],
            "explain": "'אין' (there is not) + 'לי' (to me) + 'זמן' (time)."
        },
        {
            "quest": "Build: 'This is my home' (זֶה הַבַּיִת שֶׁלִּי)",
            "clue": "Noa: 'Assemble ze, ha-bayit, and shelí!'",
            "target": "זה הבית שלי",
            "tokens": ["זה", "הבית", "שלי", "שלך", "אין"],
            "explain": "'זה' (this m.) + 'הבית' (the house) + 'שלי' (mine) = This is my home."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the existential word YESH ('there is / have' -> יש):",
            "tiles": ["י", "ש", "א", "ל", "מ"],
            "answer": "יש",
            "gloss": "yesh (there is / to have)"
        },
        {
            "clue": "Assemble the existential negator EYN ('there is none / do not have' -> אין):",
            "tiles": ["א", "י", "ן", "ה", "ב"],
            "answer": "אין",
            "gloss": "eyn (there is not / have not)"
        },
        {
            "clue": "Assemble the 1st person pronoun ANÍ ('I' -> אני):",
            "tiles": ["א", "נ", "י", "ת", "ם"],
            "answer": "אני",
            "gloss": "aní (I)"
        }
    ],
    "quiz": [
        {
            "q": "How does Modern Hebrew express the present tense verb 'to be' (e.g. 'I am a student')?",
            "options": [
                "There is no present-tense copula; subject and predicate are placed directly side-by-side (zero copula)",
                "Using the verb 'lihyot' inflected in the present",
                "With a required prefix particle 'she-'"
            ],
            "correct": 0,
            "explain": "In Hebrew present tense, there is no copula: 'Aní student' directly translates to 'I [am a] student'."
        },
        {
            "q": "How is possession ('I have') constructed in Hebrew?",
            "options": [
                "Using the existential particle 'yesh' + preposition 'le-' with pronominal suffix ('yesh li...')",
                "With a transitive verb identical to English 'to have'",
                "By putting the noun in the genitive construct state alone"
            ],
            "correct": 0,
            "explain": "'יֵשׁ לִי' (yesh li) literally means 'there is to me'."
        },
        {
            "q": "What is the famous mnemonic for Hebrew pronouns 'hu' (הוּא) and 'hi' (הִיא)?",
            "options": [
                "'Hu' is HE, 'Hi' is SHE, and 'Mi' is WHO",
                "'Hu' is WHO and 'Hi' is HE",
                "Both are completely gender neutral"
            ],
            "correct": 0,
            "explain": "A classic mnemonic: Hebrew 'hu' = he, 'hi' = she, and 'mi' = who!"
        },
        {
            "q": "Which particle negates existence and possession in Hebrew ('I do not have')?",
            "options": ["אֵין (eyn, e.g. 'eyn li')", "לֹא (lo)", "אַל (al)"],
            "correct": 0,
            "explain": "'אֵין' (eyn) negates existence and possession ('eyn li'); 'לֹא' (lo) negates verbs and adjectives; 'אַל' (al) is for prohibitions."
        },
        {
            "q": "Where does the possessive word 'shelí' (my/mine) usually sit relative to the noun in Modern Hebrew?",
            "options": [
                "After the definite noun: 'ha-séfer shelí' (lit. the-book of-me)",
                "Before the indefinite noun without any articles",
                "At the very beginning of the entire sentence"
            ],
            "correct": 0,
            "explain": "Modern Hebrew typically places 'shel-' phrases after the noun, which takes the definite article: 'ha-báyit shelí' (my house)."
        }
    ]
}

CHINESE_STEP3 = {
    "sealName": "Tiānshū Shì-Yǒu Seal (天书·是与有之印)",
    "guide": {
        "name": "Lǎo Wáng (老王)",
        "role": "Beijing Tea Master & Scholar",
        "avatar": "🍵",
        "prompt": "Nǐ hǎo! In Mandarin, verbs never conjugate! Master pronouns with plural '-men', copula 是 (shì), adjective predicates without 是 (我很好), and possession with 有 (yǒu) / 没有 (méiyǒu)."
    },
    "cards": [
        {
            "id": "zh3_c1",
            "type": "personal_pronoun",
            "glyph": "我 / 你 / 他 / 她",
            "phonetic": "wǒ [wo˨˩˦], nǐ [ni˨˩˦], tā [tʰa˥]",
            "gloss": "I / you / he / she",
            "speakText": "我, 你, 他, 她",
            "audioUrl": "",
            "whisper": "In spoken Chinese, 他 (he) and 她 (she) sound identical: 'tā' in first tone! The difference appears only in written Hanzi."
        },
        {
            "id": "zh3_c2",
            "type": "plural_pronoun",
            "glyph": "我们 / 你们 / 他们",
            "phonetic": "wǒmen [wo˨˩˦.mən], nǐmen, tāmen",
            "gloss": "we / you (plural) / they",
            "speakText": "我们, 你们, 他们",
            "audioUrl": "",
            "whisper": "The suffix 们 (men) turns any human singular pronoun into plural. No irregular plural pronouns exist in Mandarin!"
        },
        {
            "id": "zh3_c3",
            "type": "copula",
            "glyph": "是 (shì) — Copula 'To Be'",
            "phonetic": "shì [ʂɨ˥˩]",
            "gloss": "to be (equating nouns)",
            "speakText": "是, 我是学生",
            "audioUrl": "",
            "whisper": "Used to connect two NOUNS or noun phrases: '我是学生' (I am a student). CRITICAL RULE: NEVER use 是 before simple adjectives! Saying '我是好' is ungrammatical!"
        },
        {
            "id": "zh3_c4",
            "type": "adjective_predicate",
            "glyph": "Adjective Predicate: 很 (hěn)",
            "phonetic": "hěn [xən˨˩˦]",
            "gloss": "very / structural adjective linker",
            "speakText": "很, 我很好",
            "audioUrl": "",
            "whisper": "Adjectives act as verbs in Chinese! Instead of 是, use '很' (hěn) as an unstressed structural bridge: '我很好' (I am good). Here '很' simply links subject and adjective without strong emphasis on 'very'."
        },
        {
            "id": "zh3_c5",
            "type": "possession",
            "glyph": "有 (yǒu) — Possession & Existence",
            "phonetic": "yǒu [joʊ˨˩˦]",
            "gloss": "to have / there is",
            "speakText": "有, 我有书",
            "audioUrl": "",
            "whisper": "'我有书' = I have a book; '这里有水' = There is water here. Chinese uses the same verb 有 for personal possession and ambient existence."
        },
        {
            "id": "zh3_c6",
            "type": "negation",
            "glyph": "没有 (méiyǒu) — Negation of 有",
            "phonetic": "méiyǒu [meɪ̯˧˥.joʊ˨˩˦]",
            "gloss": "do not have / there is no",
            "speakText": "没有, 我没有书",
            "audioUrl": "",
            "whisper": "CRITICAL GRAMMAR RULE: 有 CANNOT be negated with 不 (bù)! '不有' does not exist in Chinese. You MUST always negate with 没 (méi): '没有' (méiyǒu)!"
        },
        {
            "id": "zh3_c7",
            "type": "particle",
            "glyph": "的 (de) — Possessive Particle",
            "phonetic": "de [də]",
            "gloss": "'s / of (possessive particle)",
            "speakText": "的, 我的",
            "audioUrl": "",
            "whisper": "Attaches to pronouns or nouns to indicate possession: 我的 (my), 你的 (your), 他的 (his), 老师的书 (the teacher's book). One of the most frequently used characters in all of Chinese!"
        },
        {
            "id": "zh3_c8",
            "type": "copular_negation",
            "glyph": "不是 (bú shì) — Negation of 是",
            "phonetic": "bú shì [pu˧˥.ʂɨ˥˩]",
            "gloss": "is not / are not",
            "speakText": "不是, 我不是老师",
            "audioUrl": "",
            "whisper": "Tone Sandhi rule: 不 (bù) is naturally 4th tone, but shifts to 2nd tone 'bú' when followed by another 4th-tone character like 是 (shì): 'bú shì'!"
        },
        {
            "id": "zh3_c9",
            "type": "adverb",
            "glyph": "也 (yě) & 都 (dōu)",
            "phonetic": "yě [jɛ˨˩˦], dōu [toʊ˥]",
            "gloss": "also, too (yě) / all, both (dōu)",
            "speakText": "也, 都, 我们都是学生",
            "audioUrl": "",
            "whisper": "Adverbs always precede the verb in Chinese! '我也是学生' = I am ALSO a student. '我们都是学生' = We are ALL students."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the sentence. Does the speaker use 是 or an adjective predicate?",
            "speakAudio": "我很好",
            "options": [
                "Adjective predicate: 'I am good' (我很好 — uses 很, not 是!)",
                "Noun equational sentence with 是",
                "Negative possession with 没有"
            ],
            "correct": 0,
            "explain": "Chinese adjectives do not use 是; they take the structural linker 很: '我很好'."
        },
        {
            "prompt": "Listen to the negation. Is it 'is not' (不是) or 'does not have' (没有)?",
            "speakAudio": "我没有书",
            "options": [
                "I do not have a book (我没有书 — méiyǒu)",
                "I am not a book (我不是书 — bú shì)",
                "I have a book (我有书)"
            ],
            "correct": 0,
            "explain": "'没有' (méiyǒu) indicates absence of possession ('do not have')."
        },
        {
            "prompt": "Listen to the plural pronoun. Who is being referred to?",
            "speakAudio": "他们是老师",
            "options": [
                "They are teachers (他们 — tāmen)",
                "We are teachers (我们 — wǒmen)",
                "You all are teachers (你们 — nǐmen)"
            ],
            "correct": 0,
            "explain": "'他们' (tāmen) is the 3rd person plural pronoun 'they'."
        },
        {
            "prompt": "Listen to the possessive phrase. Whose book is it?",
            "speakAudio": "这是我的书",
            "options": [
                "This is my book (我的书 — wǒ de shū)",
                "This is your book (你的书)",
                "This is his book (他的书)"
            ],
            "correct": 0,
            "explain": "'我的' (wǒ de) is the 1st person possessive 'my'."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'I am a teacher' (我是老师)",
            "clue": "Lǎo Wáng: 'Connect subject pronoun, copula 是, and noun!'",
            "target": "我是老师",
            "tokens": ["我", "是", "老师", "很", "有"],
            "explain": "'我' (I) + '是' (am) + '老师' (teacher)."
        },
        {
            "quest": "Build: 'I am very good' (我很好)",
            "clue": "Lǎo Wáng: 'Remember: NO 是 before adjectives! Use 很!'",
            "target": "我很好",
            "tokens": ["我", "很", "好", "是", "有"],
            "explain": "Adjective predicate: '我' (I) + '很' (structural linker) + '好' (good)."
        },
        {
            "quest": "Build: 'I do not have tea' (我没有茶)",
            "clue": "Lǎo Wáng: 'Negate 有 with 没有!'",
            "target": "我没有茶",
            "tokens": ["我", "没有", "茶", "不是", "很"],
            "explain": "'我' + '没有' (do not have) + '茶' (tea). 有 can only be negated with 没."
        },
        {
            "quest": "Build: 'This is my book' (这是我的书)",
            "clue": "Lǎo Wáng: 'Assemble 这, 是, 我的, and 书!'",
            "target": "这是我的书",
            "tokens": ["这", "是", "我的", "书", "有", "老师"],
            "explain": "'这' (this) + '是' (is) + '我的' (my) + '书' (book)."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the negative possession compound MÉIYǑU (没有):",
            "tiles": ["没", "有", "不", "是"],
            "answer": "没有",
            "gloss": "没有 (méiyǒu = to not have)"
        },
        {
            "clue": "Assemble the plural pronoun WǑMEN ('we / us' -> 我们):",
            "tiles": ["我", "们", "你", "他"],
            "answer": "我们",
            "gloss": "我们 (wǒmen = we / us)"
        },
        {
            "clue": "Assemble the copular phrase BÚ SHÌ ('is not' -> 不是):",
            "tiles": ["不", "是", "没", "有"],
            "answer": "不是",
            "gloss": "不是 (bú shì = is not)"
        }
    ],
    "quiz": [
        {
            "q": "Why is saying '我是好' (I am good) grammatically incorrect in Mandarin?",
            "options": [
                "In Chinese, 是 is only used between nouns; adjectives act as predicates directly with structural linkers like 很 (e.g. '我很好')",
                "Because 是 can only be used with negative statements",
                "Because 好 is a noun and requires a measure word"
            ],
            "correct": 0,
            "explain": "The copula 是 connects nouns (e.g. '我是学生'). Adjectives predicate directly without 是, typically supported by 很 ('我很好')."
        },
        {
            "q": "How must the verb of possession '有' (yǒu) be negated in Chinese?",
            "options": [
                "Only with 没 (méi) -> 没有 (méiyǒu); '不有' is completely ungrammatical in Chinese",
                "With 不 (bù) -> 不有",
                "With 别 (bié) -> 别有"
            ],
            "correct": 0,
            "explain": "有 is unique among Chinese verbs in that it can never be negated by 不; it must always take 没: 没有 (méiyǒu)."
        },
        {
            "q": "How are plural personal pronouns formed in Mandarin (e.g. we, you all, they)?",
            "options": [
                "By attaching the suffix 们 (men) to the singular pronoun (我们, 你们, 他们)",
                "By repeating the pronoun twice (我我, 你你)",
                "By adding the number 三 (sān) before the pronoun"
            ],
            "correct": 0,
            "explain": "The invariable suffix 们 (men) pluralizes human pronouns: 我 (I) -> 我们 (we); 你 (you) -> 你们 (you all); 他/她 (he/she) -> 他们/她们 (they)."
        },
        {
            "q": "What role does the particle 的 (de) play in the phrase '我的老师'?",
            "options": [
                "It marks possession and association ('my teacher')",
                "It indicates past tense",
                "It turns the phrase into a question"
            ],
            "correct": 0,
            "explain": "的 (de) is the primary possessive/attributive particle in Chinese, linking possessor to possessed."
        },
        {
            "q": "What tone change (Tone Sandhi) happens to 不 (bù) in '不是' (bú shì)?",
            "options": [
                "不 changes from 4th tone to 2nd tone ('bú') when followed by another 4th tone character (shì)",
                "不 becomes 1st tone",
                "不 becomes neutral tone"
            ],
            "correct": 0,
            "explain": "When 不 (bù, 4th tone) precedes another 4th-tone syllable like 是 (shì), it shifts to 2nd tone: 'bú shì'."
        }
    ]
}

GERMAN_STEP3 = {
    "sealName": "Siegel des Seins und Habens",
    "guide": {
        "name": "Frau Hildegard",
        "role": "Freiburg Scholar & Lexicographer",
        "avatar": "🦉",
        "prompt": "Guten Tag! In German, the two foundational pillars of speech are 'sein' (to be) and 'haben' (to have). Master pronoun forms, verb conjugations, and gender-inflected possessives."
    },
    "cards": [
        {
            "id": "de3_c1",
            "type": "personal_pronoun",
            "glyph": "ich / du / er, sie, es",
            "phonetic": "[ɪç], [duː], [eːɐ̯, ziː, ɛs]",
            "gloss": "I / you (informal) / he, she, it",
            "speakText": "ich, du, er, sie, es",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-ich.ogg",
            "whisper": "Note the Ich-Laut [ç] in 'ich' (soft palate friction, like a hissing cat). 'Du' is strictly informal for friends, family, and children."
        },
        {
            "id": "de3_c2",
            "type": "personal_pronoun",
            "glyph": "wir / ihr / sie / Sie",
            "phonetic": "[viːɐ̯], [iːɐ̯], [ziː], [ziː]",
            "gloss": "we / you (plural informal) / they / You (formal)",
            "speakText": "wir, ihr, sie, Sie",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-wir.ogg",
            "whisper": "German distinguishes between informal plural 'ihr' (you all) and formal 'Sie' (capitalized, for both singular and plural formal address)!"
        },
        {
            "id": "de3_c3",
            "type": "verb_sein",
            "glyph": "sein: ich bin, du bist, er ist",
            "phonetic": "[ɪç bɪn], [duː bɪst], [eːɐ̯ ɪst]",
            "gloss": "to be: I am, you are, he/she/it is",
            "speakText": "ich bin, du bist, er ist",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-sein.ogg",
            "whisper": "The irregular verb 'sein'. 'Du bist' takes the characteristic '-st' ending of 2nd person singular."
        },
        {
            "id": "de3_c4",
            "type": "verb_sein",
            "glyph": "sein: wir sind, ihr seid, sie sind",
            "phonetic": "[viːɐ̯ zɪnt], [iːɐ̯ zaɪ̯t], [ziː zɪnt]",
            "gloss": "we are, you are, they/You are",
            "speakText": "wir sind, ihr seid, sie sind",
            "audioUrl": "",
            "whisper": "Notice final devoicing (Auslautverhärtung): 'sind' and 'seid' both end with the crisp unvoiced sound [t]!"
        },
        {
            "id": "de3_c5",
            "type": "verb_haben",
            "glyph": "haben: ich habe, du hast, er hat",
            "phonetic": "[ɪç ˈhaː.bə], [duː hast], [eːɐ̯ hat]",
            "gloss": "to have: I have, you have, he/she/it has",
            "speakText": "ich habe, du hast, er hat",
            "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/De-haben.ogg",
            "whisper": "Notice that 'du hast' and 'er hat' drop the 'b' stem consonant from 'haben'!"
        },
        {
            "id": "de3_c6",
            "type": "verb_haben",
            "glyph": "haben: wir haben, ihr habt, sie haben",
            "phonetic": "[viːɐ̯ ˈhaː.bn̩], [iːɐ̯ hapt], [ziː ˈhaː.bn̩]",
            "gloss": "we have, you have, they/You have",
            "speakText": "wir haben, ihr habt, sie haben",
            "audioUrl": "",
            "whisper": "In 'ihr habt', the 'b' is devoiced to [p] before 't': [hapt]!"
        },
        {
            "id": "de3_c7",
            "type": "possessive_determiner",
            "glyph": "mein / meine",
            "phonetic": "[maɪ̯n], [ˈmaɪ̯.nə]",
            "gloss": "my (masc./neut. vs. fem./plural nom.)",
            "speakText": "mein, meine",
            "audioUrl": "",
            "whisper": "German possessives take adjective endings based on gender and case: 'mein Bruder' (masc.), 'mein Buch' (neut.), 'meine Schwester' (fem.), 'meine Bücher' (plural)!"
        },
        {
            "id": "de3_c8",
            "type": "possessive_determiner",
            "glyph": "dein / sein / ihr",
            "phonetic": "[daɪ̯n], [zaɪ̯n], [iːɐ̯]",
            "gloss": "your / his, its / her, their",
            "speakText": "dein, sein, ihr",
            "audioUrl": "",
            "whisper": "'sein' means his or its (referring to masc. or neuter possessor); 'ihr' means her, their, or (capitalized 'Ihr') your formal."
        },
        {
            "id": "de3_c9",
            "type": "possessive_determiner",
            "glyph": "unser / euer",
            "phonetic": "[ˈʊn.zɐ], [ˈɔʏ̯.ɐ]",
            "gloss": "our / your (plural informal)",
            "speakText": "unser, euer",
            "audioUrl": "",
            "whisper": "When 'euer' takes an ending like feminine '-e', it often contracts: 'eure Schule' (not 'euere')!"
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the conjugated verb. Which form of 'sein' was spoken?",
            "speakAudio": "wir sind hier",
            "options": [
                "wir sind (we are)",
                "ihr seid (you all are)",
                "ich bin (I am)"
            ],
            "correct": 0,
            "explain": "'sind' [zɪnt] is 1st person plural of sein: 'wir sind'."
        },
        {
            "prompt": "Listen to the vowel length and verb stem. Is it 'haben' (to have) or 'sein' (to be)?",
            "speakAudio": "du hast ein Buch",
            "options": [
                "You have a book (du hast — from haben)",
                "You are a book (du bist — from sein)",
                "We have a book (wir haben)"
            ],
            "correct": 0,
            "explain": "'du hast' is the 2nd person singular of haben."
        },
        {
            "prompt": "Listen to the possessive ending. Is the noun masculine/neuter or feminine/plural?",
            "speakAudio": "meine Katze",
            "options": [
                "Feminine/Plural ending -e (meine Katze)",
                "Masculine ending - (mein Hund)",
                "Dative plural ending -en"
            ],
            "correct": 0,
            "explain": "Feminine nominative takes '-e': 'meine Katze' (my cat)."
        },
        {
            "prompt": "Listen to the pronoun. Is it informal plural 'ihr' or formal 'Sie'?",
            "speakAudio": "ihr seid klug",
            "options": [
                "ihr seid (you all are — informal plural)",
                "Sie sind (you are — formal)",
                "sie ist (she is)"
            ],
            "correct": 0,
            "explain": "'ihr seid' addresses a group of friends or children informally."
        }
    ],
    "arena": [
        {
            "quest": "Build: 'I am a student' (Ich bin Student)",
            "clue": "Frau Hildegard: 'Combine ich, bin, and Student! No indefinite article needed!'",
            "target": "Ich bin Student",
            "tokens": ["Ich", "bin", "Student", "habe", "sind"],
            "explain": "'Ich bin Student' (German omits 'ein' for professions/status)."
        },
        {
            "quest": "Build: 'We have a book' (Wir haben ein Buch)",
            "clue": "Frau Hildegard: 'Use wir haben and neuter accusative ein Buch!'",
            "target": "Wir haben ein Buch",
            "tokens": ["Wir", "haben", "ein", "Buch", "sind", "eine"],
            "explain": "'Wir haben' (we have) + 'ein Buch' (a book, neuter accusative)."
        },
        {
            "quest": "Build: 'You are our friend' (Du bist unser Freund)",
            "clue": "Frau Hildegard: 'Assemble du bist and masculine unser Freund!'",
            "target": "Du bist unser Freund",
            "tokens": ["Du", "bist", "unser", "Freund", "unsere", "seid"],
            "explain": "'Du bist' + masculine nominative possessive 'unser Freund'."
        },
        {
            "quest": "Build: 'He has his key' (Er hat seinen Schlüssel)",
            "clue": "Frau Hildegard: 'Accusative masculine takes -en: seinen Schlüssel!'",
            "target": "Er hat seinen Schlüssel",
            "tokens": ["Er", "hat", "seinen", "Schlüssel", "sein", "ist"],
            "explain": "'Er hat' + masculine accusative possessive 'seinen Schlüssel'."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the 1st person singular form of SEIN ('I am' -> BIN):",
            "tiles": ["B", "I", "N", "S", "T"],
            "answer": "BIN",
            "gloss": "bin (am)"
        },
        {
            "clue": "Spell the 2nd person singular form of HABEN ('you have' -> HAST):",
            "tiles": ["H", "A", "S", "T", "E", "B"],
            "answer": "HAST",
            "gloss": "hast (have)"
        },
        {
            "clue": "Spell the 1st person plural of SEIN ('we are' -> SIND):",
            "tiles": ["S", "I", "N", "D", "E", "R"],
            "answer": "SIND",
            "gloss": "sind (are)"
        }
    ],
    "quiz": [
        {
            "q": "Why do 'du hast' and 'er hat' drop the 'b' from the infinitive 'haben'?",
            "options": [
                "They are irregular 2nd and 3rd person singular forms that experienced historic stem contraction",
                "Because German grammar forbids the letter 'b' before 's'",
                "It is a dialectal slang that entered standard German"
            ],
            "correct": 0,
            "explain": "In Middle High German, habēst/habēt contracted into hast/hat, dropping the labial consonant."
        },
        {
            "q": "How does German differ from English when stating professions (e.g. 'I am a teacher')?",
            "options": [
                "German typically omits the indefinite article: 'Ich bin Lehrer' (not 'Ich bin ein Lehrer')",
                "German requires two indefinite articles",
                "German places the profession before the subject"
            ],
            "correct": 0,
            "explain": "In German, professions and nationalities in predicate position standardly drop the article: 'Ich bin Student / Lehrer'."
        },
        {
            "q": "What is the difference between 'ihr' and 'Sie'?",
            "options": [
                "'ihr' is the informal plural address ('you guys/all'), while 'Sie' (capitalized) is the formal address (both singular and plural)",
                "'ihr' is formal and 'Sie' is informal",
                "'ihr' is only used for inanimate objects"
            ],
            "correct": 0,
            "explain": "'ihr' is informal 2nd-person plural (with verb ending -t), while 'Sie' is formal (with verb ending -en)."
        },
        {
            "q": "What ending does the possessive determiner 'mein' take before a feminine noun in nominative case (e.g. 'my sister')?",
            "options": ["-e -> meine (e.g. 'meine Schwester')", "-en -> meinen", "-er -> meiner"],
            "correct": 0,
            "explain": "Feminine nominative takes the '-e' ending: 'meine Schwester'."
        },
        {
            "q": "Which conjugation form of 'sein' corresponds to 'ihr' (you all)?",
            "options": ["seid (e.g. 'ihr seid')", "sind", "bist"],
            "correct": 0,
            "explain": "'ihr seid' is the 2nd person plural informal form of sein."
        }
    ]
}


# ==============================================================================
# STEP 4: VOCABULARY TO TALK ABOUT YOURSELF
# ==============================================================================

WARAY_STEP4 = {
    "sealName": "Tanda han Kinabuhi Identity Seal",
    "guide": {
        "name": "Mano Doy",
        "role": "Tacloban Navigator & Community Chronicler",
        "avatar": "⛵",
        "prompt": "Maupay nga kulop! Introduce yourself to our Visayan community: state your name, your age, where you come from ('taga-diin ka'), your occupation, where you live, and what brings you joy!"
    },
    "cards": [
        {
            "id": "war4_c1",
            "type": "identity_name",
            "glyph": "Hi [ngaran] ako / An akon ngaran hi...",
            "phonetic": "[hi ... ʔa.ˈko] / [ʔan ʔa.ˈkon ŋa.ˈɾan hi ...]",
            "gloss": "I am [name] / My name is...",
            "speakText": "Hi Pedro ako",
            "audioUrl": "",
            "whisper": "In Waray, you introduce yourself simply with personal article 'hi' + name + 'ako': 'Hi Pedro ako' (I am Pedro), or more formally 'An akon ngaran hi Pedro' (My name is Pedro)."
        },
        {
            "id": "war4_c2",
            "type": "identity_age",
            "glyph": "Pira it imo panuigon? / ... anyos na ako",
            "phonetic": "[ˈpi.ɾa ʔɪt ˈʔi.mo pa.nʊ.ʔi.ˈɡon] / [ˈʔan.jos na ʔa.ˈko]",
            "gloss": "How old are you? / I am ... years old",
            "speakText": "Pira it imo panuigon? Baynte anyos na ako",
            "audioUrl": "",
            "whisper": "Age uses Spanish loan numbers ('Kinatsila') + 'anyos na ako': 'Baynte anyos na ako' = I am 20 years old. 'Panuigon' comes from 'tuig' (year)!"
        },
        {
            "id": "war4_c3",
            "type": "identity_origin",
            "glyph": "Taga-diin ka? / Taga-[lugar] ako",
            "phonetic": "[ta.ɡa.ˈdi.ʔɪn ka] / [ta.ɡa-... ʔa.ˈko]",
            "gloss": "Where are you from? / I am from...",
            "speakText": "Taga-diin ka? Taga-Tacloban ako",
            "audioUrl": "",
            "whisper": "The prefix 'taga-' signifies native provenance or origin: 'Taga-diin ka?' (Where are you from?) -> 'Taga-Tacloban ako' (I am from Tacloban)!"
        },
        {
            "id": "war4_c4",
            "type": "identity_residence",
            "glyph": "Naukoy ako ha...",
            "phonetic": "[na.ˈʔu.kɔj ʔa.ˈko ha ...]",
            "gloss": "I live in / reside at...",
            "speakText": "Naukoy ako ha Samar",
            "audioUrl": "",
            "whisper": "The verb 'ukoy' (to reside/stay) takes the actor affix 'na-' for present habitual state: 'Naukoy ako ha Samar' = I live in Samar. 'Ha' is the universal locative marker."
        },
        {
            "id": "war4_c5",
            "type": "identity_profession",
            "glyph": "Magturutdo ako (Teacher)",
            "phonetic": "[maɡ.tʊ.ɾʊt.ˈdo ʔa.ˈko]",
            "gloss": "I am a teacher",
            "speakText": "Magturutdo ako",
            "audioUrl": "",
            "whisper": "Professions often use the prefix 'mag-' with reduplication of the root: 'tutdo' (teach) -> 'magturutdo' (teacher). Zero copula: 'Magturutdo ako'."
        },
        {
            "id": "war4_c6",
            "type": "identity_profession",
            "glyph": "Magsusurat / Mananagat ako",
            "phonetic": "[maɡ.sʊ.sʊ.ˈɾat], [ma.na.ˈna.ɡat ʔa.ˈko]",
            "gloss": "I am a writer / fisherman",
            "speakText": "Magsusurat ako",
            "audioUrl": "",
            "whisper": "'Surat' (write) -> 'magsusurat' (writer). 'Mananagat' is fisherman ('dagat' = sea); 'parag-uma' is farmer."
        },
        {
            "id": "war4_c7",
            "type": "identity_hobby",
            "glyph": "Karuyag ko magbasa (I like to read)",
            "phonetic": "[ka.ɾʊ.ˈjaɡ ko maɡ.ba.ˈsa]",
            "gloss": "I want / like to read",
            "speakText": "Karuyag ko magbasa",
            "audioUrl": "",
            "whisper": "'Karuyag' expresses liking or wanting. It takes the postposed genitive pronoun 'ko' (by me) + infinitive 'magbasa' (to read): 'Karuyag ko magbasa hin libro'."
        },
        {
            "id": "war4_c8",
            "type": "identity_hobby",
            "glyph": "Karuyag ko magkanta / mamati hin musika",
            "phonetic": "[ka.ɾʊ.ˈjaɡ ko maɡ.kan.ˈta]",
            "gloss": "I like to sing / listen to music",
            "speakText": "Karuyag ko magkanta",
            "audioUrl": "",
            "whisper": "'Magkanta' (to sing) or 'mamati hin musika' (to listen to music). 'Karuyag ko magkanta' = I like singing!"
        },
        {
            "id": "war4_c9",
            "type": "question_name",
            "glyph": "Hin-o it imo ngaran?",
            "phonetic": "[hɪn.ˈʔo ʔɪt ˈʔi.mo ŋa.ˈɾan]",
            "gloss": "Who/What is your name?",
            "speakText": "Hin-o it imo ngaran?",
            "audioUrl": "",
            "whisper": "Literally 'Who is your name?' Waray uses interrogative 'Hin-o' (who) rather than 'Ano' (what) when asking someone's name respectfully!"
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the origin phrase. Where does the speaker hail from?",
            "speakAudio": "Taga-Tacloban ako",
            "options": [
                "From Tacloban (Taga-Tacloban ako)",
                "From Manila (Taga-Manila ako)",
                "From Cebu (Taga-Cebu ako)"
            ],
            "correct": 0,
            "explain": "'Taga-' is the prefix of origin; 'Taga-Tacloban ako' = I am from Tacloban."
        },
        {
            "prompt": "Listen to the age declaration. How old is the speaker?",
            "speakAudio": "Baynte anyos na ako",
            "options": [
                "20 years old (Baynte anyos na ako)",
                "30 years old (Trenta anyos na ako)",
                "15 years old (Kinse anyos na ako)"
            ],
            "correct": 0,
            "explain": "'Baynte' is 20 in Kinatsila; 'anyos na ako' = years old already."
        },
        {
            "prompt": "Listen to the profession. What does the speaker do?",
            "speakAudio": "Magturutdo ako",
            "options": [
                "Teacher (Magturutdo ako)",
                "Fisherman (Mananagat ako)",
                "Writer (Magsusurat ako)"
            ],
            "correct": 0,
            "explain": "'Magturutdo' means teacher (from 'tutdo' = teach)."
        },
        {
            "prompt": "Listen to the hobby. What does the speaker enjoy?",
            "speakAudio": "Karuyag ko magbasa",
            "options": [
                "I like to read (Karuyag ko magbasa)",
                "I like to cook (Karuyag ko magluto)",
                "I like to sing (Karuyag ko magkanta)"
            ],
            "correct": 0,
            "explain": "'Karuyag ko magbasa' = I like to read ('basa' = read)."
        }
    ],
    "arena": [
        {
            "quest": "Name Introduction: 'I am Pedro'",
            "clue": "Mano Doy: 'Use personal article hi, name, and ako!'",
            "target": "Hi Pedro ako",
            "tokens": ["Hi", "Pedro", "ako", "an", "ngaran"],
            "explain": "Predicate-initial personal name construction with marker 'hi': 'Hi Pedro ako'."
        },
        {
            "quest": "Stating Origin: 'I am from Tacloban'",
            "clue": "Mano Doy: 'Use the origin prefix taga-!'",
            "target": "Taga-Tacloban ako",
            "tokens": ["Taga-Tacloban", "ako", "ha", "naukoy", "hiya"],
            "explain": "Prefix 'taga-' marks origin/native provenance: 'Taga-Tacloban ako'."
        },
        {
            "quest": "Expressing Residence: 'I live in Samar'",
            "clue": "Mano Doy: 'Assemble Naukoy ako ha Samar!'",
            "target": "Naukoy ako ha Samar",
            "tokens": ["Naukoy", "ako", "ha", "Samar", "taga", "balay"],
            "explain": "'Naukoy' (residing) + 'ako' (I) + locative 'ha' + place name."
        },
        {
            "quest": "Expressing a Joy / Hobby: 'I like to read'",
            "clue": "Mano Doy: 'Combine Karuyag, ko, and magbasa!'",
            "target": "Karuyag ko magbasa",
            "tokens": ["Karuyag", "ko", "magbasa", "magkanta", "ako"],
            "explain": "'Karuyag' (desire/like) + postposed genitive 'ko' + infinitive 'magbasa'."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the Waray word for 'NAME' (NGARAN):",
            "tiles": ["N", "G", "A", "R", "A", "N", "O"],
            "answer": "NGARAN",
            "gloss": "ngaran (name)"
        },
        {
            "clue": "Spell the origin prefix TAGA ('origin from' -> TAGA):",
            "tiles": ["T", "A", "G", "A", "D", "I"],
            "answer": "TAGA",
            "gloss": "taga- (native of / from)"
        },
        {
            "clue": "Spell the verb root for 'TO READ' (BASA):",
            "tiles": ["B", "A", "S", "A", "K", "O"],
            "answer": "BASA",
            "gloss": "basa (read)"
        }
    ],
    "quiz": [
        {
            "q": "Why do Waray speakers often ask 'Hin-o it imo ngaran?' instead of 'Ano it imo ngaran?'",
            "options": [
                "'Hin-o' (Who) is traditionally preferred for human identity, treating a name with personal respect",
                "Because 'Ano' cannot be used at the beginning of any sentence",
                "'Hin-o' is only used for children's names"
            ],
            "correct": 0,
            "explain": "In Visayan languages, asking 'Hin-o it imo ngaran?' (Who is your name?) is standard and polite for persons."
        },
        {
            "q": "How do you state where you are from in Waray-Waray?",
            "options": [
                "Prefix 'Taga-' + place name + 'ako' (e.g. 'Taga-Tacloban ako')",
                "Preposition 'Tikang' alone without a pronoun",
                "Suffix '-anon' attached to the pronoun"
            ],
            "correct": 0,
            "explain": "The prefix 'taga-' denotes provenance or native residence: 'Taga-Tacloban ako'."
        },
        {
            "q": "Which counting system is standard when stating your age in Waray (e.g. 'I am 20 years old')?",
            "options": [
                "Spanish loan numbers ('Kinatsila') + anyos na ako (e.g. 'Baynte anyos na ako')",
                "Native Ihap counting + bulan",
                "Ordinal numbers with ika-"
            ],
            "correct": 0,
            "explain": "Age in Philippine languages conventionally uses Kinatsila numerals with 'anyos': 'Baynte anyos na ako'."
        },
        {
            "q": "In the expression 'Karuyag ko magbasa', why is the pronoun 'ko' used instead of 'ako'?",
            "options": [
                "'Karuyag' is a pseudo-verb/noun predicate that requires the genitive actor clitic 'ko' (by me)",
                "Because 'ako' cannot appear after vowels",
                "Because 'ko' is plural"
            ],
            "correct": 0,
            "explain": "'Karuyag' governs genitive pronouns ('ko', 'mo', 'niya'): 'Karuyag ko' literally means 'My desire is to read'."
        },
        {
            "q": "What does the verb 'Naukoy' mean in 'Naukoy ako ha Samar'?",
            "options": [
                "I live / reside (from root 'ukoy')",
                "I am traveling",
                "I was born"
            ],
            "correct": 0,
            "explain": "'Ukoy' means to reside or dwell; with actor affix 'na-', 'naukoy' means 'residing / living'."
        }
    ]
}

FRENCH_STEP4 = {
    "sealName": "Sceau de l'Identité Personnelle",
    "guide": {
        "name": "Chloé",
        "role": "Parisian Journalist & Biographer",
        "avatar": "✍️",
        "prompt": "Enchantée ! Learn to present yourself in French: your name ('Je m'appelle...'), your age with 'avoir' ('J'ai 20 ans'), your origin, profession, residence, and passions!"
    },
    "cards": [
        {
            "id": "fr4_c1",
            "type": "identity_name",
            "glyph": "Je m'appelle...",
            "phonetic": "[ʒə ma.pɛl]",
            "gloss": "My name is... (lit. 'I call myself')",
            "speakText": "Je m'appelle Chloé",
            "audioUrl": "",
            "whisper": "Reflexive verb 's'appeler'. Notice double 'l' in 'appelle' which makes the vowel open [ɛ], while infinitive has single 'l' ('s'appeler' [sa.pə.le])!"
        },
        {
            "id": "fr4_c2",
            "type": "identity_age",
            "glyph": "J'ai ... ans",
            "phonetic": "[ʒe ... ɑ̃]",
            "gloss": "I am ... years old (lit. 'I have ... years')",
            "speakText": "J'ai vingt ans",
            "audioUrl": "",
            "whisper": "CRITICAL FRENCH IDIOM: You DO NOT say 'Je suis 20 ans'! French uses 'avoir' (to have): 'J'ai vingt ans' [ʒe vɛ̃.t‿ɑ̃], with liaison linking [t] to [ɑ̃]!"
        },
        {
            "id": "fr4_c3",
            "type": "identity_origin",
            "glyph": "Je viens de... / Je suis de...",
            "phonetic": "[ʒə vjɛ̃ də ...] / [ʒə sɥi də ...]",
            "gloss": "I come from... / I am from...",
            "speakText": "Je viens de Paris",
            "audioUrl": "",
            "whisper": "Use 'venir de' for origin: 'Je viens de Paris', 'Je viens du Canada' (de + le = du), 'Je viens de France' (feminine country uses 'de')."
        },
        {
            "id": "fr4_c4",
            "type": "identity_residence",
            "glyph": "J'habite à...",
            "phonetic": "[ʒa.bi.t‿a ...]",
            "gloss": "I live in...",
            "speakText": "J'habite à Lyon",
            "audioUrl": "",
            "whisper": "Elision occurs with 'habiter' because 'h' is mute: 'j'habite' [ʒa.bit]. Cities take preposition 'à': 'J'habite à Paris'!"
        },
        {
            "id": "fr4_c5",
            "type": "identity_profession",
            "glyph": "Je suis étudiant / étudiante",
            "phonetic": "[ʒə sɥi.z‿e.ty.djɑ̃] / [e.ty.djɑ̃t]",
            "gloss": "I am a student (m/f)",
            "speakText": "Je suis étudiant",
            "audioUrl": "",
            "whisper": "No article before professions in French! Say 'Je suis étudiant' (masc.) or 'Je suis étudiante' (fem.). Adding 'un' ('Je suis un étudiant') sounds unnatural unless qualified!"
        },
        {
            "id": "fr4_c6",
            "type": "identity_profession",
            "glyph": "Je suis professeur / écrivain",
            "phonetic": "[pʁɔ.fɛ.sœʁ], [e.kʁi.vɛ̃]",
            "gloss": "I am a teacher / writer",
            "speakText": "Je suis professeur",
            "audioUrl": "",
            "whisper": "Other common professions: 'journaliste' (journalist), 'ingénieur' (engineer), 'médecin' (doctor), 'artiste' (artist)."
        },
        {
            "id": "fr4_c7",
            "type": "identity_hobby",
            "glyph": "J'aime lire (I like to read)",
            "phonetic": "[ʒɛm liʁ]",
            "gloss": "I like to read",
            "speakText": "J'aime lire",
            "audioUrl": "",
            "whisper": "The conjugated verb 'aimer' is followed directly by an infinitive: 'J'aime lire des livres' = I like reading books."
        },
        {
            "id": "fr4_c8",
            "type": "identity_hobby",
            "glyph": "J'aime écouter de la musique / voyager",
            "phonetic": "[ʒɛm e.ku.te də la my.zik] / [vwa.ja.ʒe]",
            "gloss": "I like listening to music / traveling",
            "speakText": "J'aime écouter de la musique",
            "audioUrl": "",
            "whisper": "'Écouter' takes a direct object or partitive: 'écouter de la musique'. 'Voyager' = to travel."
        },
        {
            "id": "fr4_c9",
            "type": "greeting_courtesy",
            "glyph": "Enchanté / Enchantée",
            "phonetic": "[ɑ̃.ʃɑ̃.te]",
            "gloss": "Delighted / Nice to meet you (m/f)",
            "speakText": "Enchanté",
            "audioUrl": "",
            "whisper": "Spoken identically ([ɑ̃.ʃɑ̃.te]), but spelled with an extra 'e' if written by a woman: 'Enchantée'!"
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the age expression. Did the speaker use 'avoir' or 'être'?",
            "speakAudio": "J'ai vingt-cinq ans",
            "options": [
                "Used avoir: 'J'ai 25 ans' (correct French idiom for age)",
                "Used être: 'Je suis 25 ans' (incorrect English calque)",
                "Stated a birth year"
            ],
            "correct": 0,
            "explain": "French strictly uses 'avoir' for age: 'J'ai ... ans'."
        },
        {
            "prompt": "Listen to the profession. What is the speaker's occupation?",
            "speakAudio": "Je suis étudiante à Paris",
            "options": [
                "Female student (étudiante — final [t] pronounced)",
                "Male student (étudiant — nasal vowel [ɑ̃])",
                "Professor"
            ],
            "correct": 0,
            "explain": "The feminine form 'étudiante' pronounces the final 't' [e.ty.djɑ̃t]."
        },
        {
            "prompt": "Listen to the residence phrase. Where does the speaker live?",
            "speakAudio": "J'habite à Marseille",
            "options": [
                "In Marseille (J'habite à Marseille)",
                "In Paris (J'habite à Paris)",
                "In Lyon"
            ],
            "correct": 0,
            "explain": "'J'habite à Marseille' states residence in the city of Marseille."
        },
        {
            "prompt": "Listen to the hobby. What does the speaker enjoy?",
            "speakAudio": "J'aime voyager et lire",
            "options": [
                "Traveling and reading (voyager et lire)",
                "Singing and dancing",
                "Cooking and sleeping"
            ],
            "correct": 0,
            "explain": "'voyager' = to travel, 'lire' = to read."
        }
    ],
    "arena": [
        {
            "quest": "Self Introduction: Name",
            "clue": "Chloé: 'Use reflexive Je m'appelle!'",
            "target": "Je m'appelle Chloé",
            "tokens": ["Je", "m'appelle", "Chloé", "suis", "mon"],
            "explain": "'Je m'appelle' (I call myself) + personal name."
        },
        {
            "quest": "Declaring Age",
            "clue": "Chloé: 'Remember: use avoir, NOT être!'",
            "target": "J'ai vingt ans",
            "tokens": ["J'ai", "vingt", "ans", "Je", "suis"],
            "explain": "French age formula: 'J'ai' + number + 'ans'."
        },
        {
            "quest": "Stating Origin",
            "clue": "Chloé: 'Assemble Je viens de Paris!'",
            "target": "Je viens de Paris",
            "tokens": ["Je", "viens", "de", "Paris", "habite", "à"],
            "explain": "'Je viens de' (I come from) + city name."
        },
        {
            "quest": "Stating Residence",
            "clue": "Chloé: 'Tell where you live: J'habite à Lyon!'",
            "target": "J'habite à Lyon",
            "tokens": ["J'habite", "à", "Lyon", "viens", "de"],
            "explain": "'J'habite' + preposition 'à' + city."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the French word for 'YEARS' in age expressions (ANS):",
            "tiles": ["A", "N", "S", "O", "T"],
            "answer": "ANS",
            "gloss": "ans (years)"
        },
        {
            "clue": "Spell the French verb for 'TO READ' (LIRE):",
            "tiles": ["L", "I", "R", "E", "A", "V"],
            "answer": "LIRE",
            "gloss": "lire (to read)"
        },
        {
            "clue": "Spell the greeting for 'NICE TO MEET YOU' (masculine ENCHANTÉ):",
            "tiles": ["E", "N", "C", "H", "A", "N", "T", "É", "S"],
            "answer": "ENCHANTÉ",
            "gloss": "enchanté (delighted / nice to meet you)"
        }
    ],
    "quiz": [
        {
            "q": "Why is saying 'Je suis vingt ans' incorrect in French?",
            "options": [
                "French expresses age using the verb 'avoir' ('J'ai vingt ans' = lit. I have twenty years)",
                "Because 'ans' must always come before the number",
                "Because 'vingt' cannot follow 'suis'"
            ],
            "correct": 0,
            "explain": "Romance languages use 'avoir' (to have) rather than 'être' (to be) for age."
        },
        {
            "q": "Why is there no article in 'Je suis médecin' (I am a doctor)?",
            "options": [
                "In French, professions function like predicate adjectives after être and drop the indefinite article",
                "Because 'médecin' is an uncountable noun",
                "Articles are only used in writing"
            ],
            "correct": 0,
            "explain": "After 'être', profession nouns act as adjectives and drop 'un/une': 'Je suis médecin'."
        },
        {
            "q": "What preposition introduces a city of residence in 'J'habite ... Paris'?",
            "options": ["à (e.g. 'J'habite à Paris')", "en", "dans le"],
            "correct": 0,
            "explain": "Cities take the preposition 'à': 'à Paris', 'à Lyon', 'à Tokyo'."
        },
        {
            "q": "What is the phonetic difference between 'étudiant' (masculine) and 'étudiante' (feminine)?",
            "options": [
                "Masculine ends with nasal vowel [ɑ̃] and silent 't'; feminine pronounces the final consonant [t] ([e.ty.djɑ̃t])",
                "There is no phonetic difference",
                "Feminine drops the 'é'"
            ],
            "correct": 0,
            "explain": "In French phonology, feminine '-e' causes the preceding consonant ('t') to be fully pronounced."
        },
        {
            "q": "What does the greeting 'Enchanté' literally mean?",
            "options": ["Enchanted / Delighted (to meet you)", "Good evening", "Welcome to my home"],
            "correct": 0,
            "explain": "'Enchanté' comes from the participle meaning delighted/enchanted to make your acquaintance."
        }
    ]
}

LATIN_STEP4 = {
    "sealName": "Sigillum Nōminis et Vītae",
    "guide": {
        "name": "Cornēlia",
        "role": "Patrician Scholar & Chronicler",
        "avatar": "📜",
        "prompt": "Salvēte! Introduce yourself as a Roman citizen: declare your name ('Nōmen mihi est...'), your age in years ('annōs nātus sum'), your homeland, residence, craft, and studious pursuits!"
    },
    "cards": [
        {
            "id": "lat4_c1",
            "type": "identity_name",
            "glyph": "Nōmen mihi est...",
            "phonetic": "[ˈnoː.mɛn ˈmɪ.hɪ ɛst ...]",
            "gloss": "My name is... (lit. 'Name to me is...')",
            "speakText": "Nomen mihi est Cornelia",
            "audioUrl": "",
            "whisper": "The classical formula for introducing oneself! Uses the dative of possession 'mihi' (to me) + nominative 'nōmen' (name) + 'est'."
        },
        {
            "id": "lat4_c2",
            "type": "identity_age",
            "glyph": "... annōs nātus / nāta sum",
            "phonetic": "[ˈan.noːs ˈnaː.tʊs sʊm] / [ˈnaː.ta]",
            "gloss": "I am ... years old (lit. 'born ... years')",
            "speakText": "Viginti annos natus sum",
            "audioUrl": "",
            "whisper": "Age is expressed with the participle 'nātus' (m.) / 'nāta' (f.) + Accusative of Duration of Time ('annōs'): 'Vīgintī annōs nātus sum' = I am 20 years old!"
        },
        {
            "id": "lat4_c3",
            "type": "identity_origin",
            "glyph": "Ex Italiā sum / Oriundus sum...",
            "phonetic": "[ɛks ɪˈta.li.aː sʊm] / [ɔ.rɪˈʊn.dʊs sʊm]",
            "gloss": "I am from Italy / origin",
            "speakText": "Ex Italia sum",
            "audioUrl": "",
            "whisper": "Origin is expressed with preposition 'ex' or 'ē' + Ablative of Place: 'Ex Italiā sum' (I am from Italy), 'Ex Hispāniā sum' (from Spain)."
        },
        {
            "id": "lat4_c4",
            "type": "identity_residence",
            "glyph": "Rōmae habitō / In urbe habitō",
            "phonetic": "[ˈroː.mae̯ ˈha.bɪ.toː]",
            "gloss": "I live in Rome (locative case)",
            "speakText": "Romae habito",
            "audioUrl": "",
            "whisper": "Cities and small islands use the ancient LOCATIVE CASE with no preposition! 'Rōmae' is the locative of 'Rōma' (1st declension ends in -ae): 'Rōmae habitō' = I live in Rome!"
        },
        {
            "id": "lat4_c5",
            "type": "identity_profession",
            "glyph": "Discipulus / discipula sum",
            "phonetic": "[dɪsˈkɪ.pʊ.lʊs sʊm] / [dɪsˈkɪ.pʊ.la]",
            "gloss": "I am a student (male / female)",
            "speakText": "Discipulus sum",
            "audioUrl": "",
            "whisper": "Nominative predicate with copula 'sum': 'Discipulus sum' (I am a male student); 'Discipula sum' (I am a female student)."
        },
        {
            "id": "lat4_c6",
            "type": "identity_profession",
            "glyph": "Scrība / medicus / philosophus sum",
            "phonetic": "[ˈskriː.ba], [ˈmɛ.dɪ.kʊs], [pʰɪˈlɔ.sɔ.pʰʊs]",
            "gloss": "I am a scribe / physician / philosopher",
            "speakText": "Scriba sum",
            "audioUrl": "",
            "whisper": "Note that 'scrība' (clerk/scribe) is a 1st-declension masculine noun! 'Medicus' is doctor; 'magister' is teacher."
        },
        {
            "id": "lat4_c7",
            "type": "identity_hobby",
            "glyph": "Legere mihi placet (I like to read)",
            "phonetic": "[ˈlɛ.ɡɛ.rɛ ˈmɪ.hɪ ˈpla.kɛt]",
            "gloss": "It pleases me to read / I like reading",
            "speakText": "Legere mihi placet",
            "audioUrl": "",
            "whisper": "Romans commonly expressed enjoyment using the impersonal verb 'placet' (it pleases) + dative: 'Legere mihi placet' (Reading pleases me = I like to read)!"
        },
        {
            "id": "lat4_c8",
            "type": "identity_hobby",
            "glyph": "Cantāre / scrībere / nāvigāre mihi placet",
            "phonetic": "[kanˈtaː.rɛ], [ˈskriː.bɛ.rɛ], [naː.wɪˈɡaː.rɛ]",
            "gloss": "I like to sing / write / sail",
            "speakText": "Scribere mihi placet",
            "audioUrl": "",
            "whisper": "Infinitives ending in '-āre', '-ēre', '-ere', '-īre': 'Scrībere mihi placet' = I love writing."
        },
        {
            "id": "lat4_c9",
            "type": "question_name",
            "glyph": "Quid est nōmen tibi?",
            "phonetic": "[kwɪd ɛst ˈnoː.mɛn ˈtɪ.bɪ]",
            "gloss": "What is your name?",
            "speakText": "Quid est nomen tibi?",
            "audioUrl": "",
            "whisper": "Literally 'What is the name to you?' Combines interrogative 'Quid' (what) + 'est' + 'nōmen' + dative 'tibi'."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the locative case. Where does Cornelia reside?",
            "speakAudio": "Rōmae habitō",
            "options": [
                "In Rome (Rōmae is the ancient locative case of Rōma)",
                "In Greece",
                "Outside the city"
            ],
            "correct": 0,
            "explain": "Towns and cities take the locative case without a preposition: 'Rōmae' = in Rome."
        },
        {
            "prompt": "Listen to the age construction. What grammatical case is 'annōs'?",
            "speakAudio": "Vīgintī annōs nātus sum",
            "options": [
                "Accusative of duration of time (annōs nātus sum)",
                "Nominative subject",
                "Ablative of means"
            ],
            "correct": 0,
            "explain": "Latin expresses age using accusative of duration: 'annōs' (accusative plural of annus) + 'nātus sum'."
        },
        {
            "prompt": "Listen to the expression of pleasure. What activity pleases the speaker?",
            "speakAudio": "Legere mihi placet",
            "options": [
                "Reading (legere mihi placet)",
                "Singing (cantāre)",
                "Fighting (pugnāre)"
            ],
            "correct": 0,
            "explain": "'Legere' is the present active infinitive 'to read'."
        },
        {
            "prompt": "Listen to the self-introduction. What is the speaker's name?",
            "speakAudio": "Nōmen mihi est Mārcus",
            "options": [
                "Marcus (Nōmen mihi est Mārcus)",
                "Lucius",
                "Cornelius"
            ],
            "correct": 0,
            "explain": "'Nōmen mihi est Mārcus' = My name is Marcus."
        }
    ],
    "arena": [
        {
            "quest": "Roman Name Introduction",
            "clue": "Cornēlia: 'Declare your name: Nōmen mihi est Cornēlia!'",
            "target": "Nōmen mihi est Cornēlia",
            "tokens": ["Nōmen", "mihi", "est", "Cornēlia", "tibi", "sum"],
            "explain": "Dative of possession: 'Nōmen' (name) + 'mihi' (to me) + 'est' (is) + name."
        },
        {
            "quest": "Declaring Age",
            "clue": "Cornēlia: 'State your age: Vīgintī annōs nātus sum!'",
            "target": "Vīgintī annōs nātus sum",
            "tokens": ["Vīgintī", "annōs", "nātus", "sum", "nāta", "habeō"],
            "explain": "Accusative of duration 'Vīgintī annōs' + participle 'nātus sum'."
        },
        {
            "quest": "Roman Residence",
            "clue": "Cornēlia: 'Express that you live in Rome using the locative: Rōmae habitō!'",
            "target": "Rōmae habitō",
            "tokens": ["Rōmae", "habitō", "in", "Rōmā", "sum"],
            "explain": "Locative case 'Rōmae' + verb 'habitō' (no preposition for cities)."
        },
        {
            "quest": "Expressing a Hobby",
            "clue": "Cornēlia: 'State that reading pleases you: Legere mihi placet!'",
            "target": "Legere mihi placet",
            "tokens": ["Legere", "mihi", "placet", "scrībere", "volō"],
            "explain": "Infinitive 'Legere' + dative pronoun 'mihi' + impersonal 'placet'."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the Latin word for 'NAME' (NŌMEN):",
            "tiles": ["N", "O", "M", "E", "N", "T", "I"],
            "answer": "NOMEN",
            "gloss": "nōmen (name)"
        },
        {
            "clue": "Spell the impersonal verb 'IT PLEASES / I LIKE' (PLACET):",
            "tiles": ["P", "L", "A", "C", "E", "T", "O"],
            "answer": "PLACET",
            "gloss": "placet (it pleases)"
        },
        {
            "clue": "Spell the accusative plural for 'YEARS' (ANNŌS):",
            "tiles": ["A", "N", "N", "O", "S", "U", "M"],
            "answer": "ANNOS",
            "gloss": "annōs (years [acc. pl.])"
        }
    ],
    "quiz": [
        {
            "q": "Why do Romans say 'Rōmae habitō' instead of 'In Rōmā habitō'?",
            "options": [
                "Names of towns, cities, and small islands use the locative case without any preposition",
                "Because 'in' was only invented in Medieval Latin",
                "Because Rōma is an adjective"
            ],
            "correct": 0,
            "explain": "In Classical Latin, names of cities, towns, and small islands use the bare Locative case (e.g. Rōmae, Athēnīs, Corinthī) without prepositions."
        },
        {
            "q": "What grammatical case is used for 'annōs' in 'Vīgintī annōs nātus sum'?",
            "options": [
                "Accusative of duration of time",
                "Ablative of specification",
                "Genitive of value"
            ],
            "correct": 0,
            "explain": "Time duration in Latin is regularly placed in the accusative case ('annōs' = for [twenty] years)."
        },
        {
            "q": "How is personal enjoyment commonly phrased in Classical Latin (e.g. 'I like reading')?",
            "options": [
                "Using the impersonal verb 'placet' + dative pronoun + infinitive ('Legere mihi placet')",
                "With the verb 'amāre' followed by a genitive noun",
                "By using a passive subjunctive verb"
            ],
            "correct": 0,
            "explain": "'Mihi placet' (it pleases me) + infinitive is a central idiom for expressing personal liking and preference."
        },
        {
            "q": "What is the gender of the 1st-declension occupational noun 'scrība' (scribe)?",
            "options": ["Masculine (masculine of the 1st declension)", "Feminine", "Neuter"],
            "correct": 0,
            "explain": "Words like 'scrība', 'nauta' (sailor), 'agricola' (farmer), and 'poēta' (poet) belong to the 1st declension but are grammatically masculine."
        },
        {
            "q": "What does the expression 'Nōmen mihi est' literally mean?",
            "options": [
                "The name to me is... (dative of possession)",
                "I call my name",
                "My name was given"
            ],
            "correct": 0,
            "explain": "It uses the dative of possession: 'nōmen' (subject) + 'mihi' (to me) + 'est' (is)."
        }
    ]
}

HEBREW_STEP4 = {
    "sealName": "Chotam HaZehut HaIshit (Seal of Personal Identity)",
    "guide": {
        "name": "Yoni",
        "role": "Tel Aviv Architect & Guide",
        "avatar": "🏛️",
        "prompt": "Shalom! Let us learn how to introduce yourself in Hebrew: your name ('שְׁמִי...' or 'קוֹרְאִים לִי...'), your age with 'ben/bat' ('אֲנִי בֶּן...'), your city, profession, and what you love doing!"
    },
    "cards": [
        {
            "id": "heb4_c1",
            "type": "identity_name",
            "glyph": "שְׁמִי... / קוֹרְאִים לִי...",
            "phonetic": "shmí... [ʃmi] / kor'ím li... [koʁˈʔim li]",
            "gloss": "My name is... / People call me...",
            "speakText": "שמי יוני, קוראים לי יוני",
            "audioUrl": "",
            "whisper": "'Shmí...' is the formal construct ('my name'); 'Kor'ím li...' (lit. 'They call to me...') is the most natural, widespread everyday way Israelis introduce themselves!"
        },
        {
            "id": "heb4_c2",
            "type": "identity_age",
            "glyph": "אֲנִי בֶּן ... / אֲנִי בַּת ...",
            "phonetic": "aní ben ... [ʔaˈni ben] / aní bat ...",
            "gloss": "I am ... years old (m: ben / f: bat)",
            "speakText": "אני בן עשרים",
            "audioUrl": "",
            "whisper": "Age in Hebrew literally means 'son of' (בֶּן, ben) or 'daughter of' (בַּת, bat) + number: 'Aní ben esrím' (male: I am 20), 'Aní bat esrím' (female: I am 20)!"
        },
        {
            "id": "heb4_c3",
            "type": "identity_origin",
            "glyph": "אֲנִי מִ... / מִיְּרוּשָׁלַיִם",
            "phonetic": "aní mi-... [ʔaˈni mi...]",
            "gloss": "I am from...",
            "speakText": "אני מירושלים",
            "audioUrl": "",
            "whisper": "The prefix 'מִ-' (mi-) attaches directly to the place name with no space: 'Aní mi-Yerushaláyim' (I am from Jerusalem), 'Aní me-Artzót HaBrít' (from the USA; 'me-' before gutturals)."
        },
        {
            "id": "heb4_c4",
            "type": "identity_residence",
            "glyph": "אֲנִי גָּר / גָּרָה בְּ...",
            "phonetic": "aní gar [ʔaˈni ɡaʁ] / aní gará [ʔaˈni ɡaˈʁa]",
            "gloss": "I live in... (m: gar / f: gará)",
            "speakText": "אני גר בתל אביב",
            "audioUrl": "",
            "whisper": "Present participle verbs inflect for gender! Men say 'Aní gar' [ɡaʁ]; women say 'Aní gará' [ɡaˈʁa]. The prefix 'בְּ-' (be-) means 'in'."
        },
        {
            "id": "heb4_c5",
            "type": "identity_profession",
            "glyph": "אֲנִי סְטוּדֶנְט / סְטוּדֶנְטִית",
            "phonetic": "aní studént [stuˈdent] / studentít",
            "gloss": "I am a student (male / female)",
            "speakText": "אני סטודנט",
            "audioUrl": "",
            "whisper": "Professions add the feminine suffix '-it' or '-a': 'studént' -> 'studentít'; 'talmíd' -> 'talmidá' (pupil); 'moré' -> 'morá' (teacher)."
        },
        {
            "id": "heb4_c6",
            "type": "identity_profession",
            "glyph": "אֲנִי סוֹפֵר / סוֹפֶרֶת",
            "phonetic": "aní sofér [soˈfeʁ] / soféret",
            "gloss": "I am a writer / scribe (m/f)",
            "speakText": "אני סופר",
            "audioUrl": "",
            "whisper": "Hebrew root ס-פ-ר (S-P-R) connects counting, telling stories, and books! 'Sofér' = writer/scribe; 'séfer' = book; 'sipur' = story."
        },
        {
            "id": "heb4_c7",
            "type": "identity_hobby",
            "glyph": "אֲנִי אוֹהֵב / אוֹהֶבֶת לִקְרֹא",
            "phonetic": "aní ohév / ohévet likró [likˈʁo]",
            "gloss": "I love to read (m/f)",
            "speakText": "אני אוהב לקרוא",
            "audioUrl": "",
            "whisper": "To express hobbies, use 'ohév' (m.) / 'ohévet' (f.) + infinitive with prefix 'לִ-' (li-): 'likró' (to read, from root ק-ר-א)."
        },
        {
            "id": "heb4_c8",
            "type": "identity_hobby",
            "glyph": "אֲנִי אוֹהֵב לִנְסֹעַ / לְהַקְשִׁיב לְמוּזִיקָה",
            "phonetic": "linsóa [linˈsoaʕ], lehakshív [lehakˈʃiv]",
            "gloss": "I love to travel / listen to music",
            "speakText": "אני אוהב לנסוע",
            "audioUrl": "",
            "whisper": "'Linsóa' = to travel/journey; 'lehakshív le-múzika' = to listen to music."
        },
        {
            "id": "heb4_c9",
            "type": "greeting_courtesy",
            "glyph": "נָעִים מְאֹד",
            "phonetic": "na'ím me'ód [naˈʔim meˈʔod]",
            "gloss": "Very pleasant / Nice to meet you",
            "speakText": "נעים מאוד",
            "audioUrl": "",
            "whisper": "Literally 'Very pleasant!' The universal, friendly greeting upon meeting someone new in Israel."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the gendered age expression. Is the speaker male or female?",
            "speakAudio": "אני בת עשרים",
            "options": [
                "Female speaker ('Aní bat esrím' uses bat = daughter of)",
                "Male speaker ('Aní ben esrím')",
                "Plural speakers"
            ],
            "correct": 0,
            "explain": "Women say 'bat' (daughter of) for age; men say 'ben' (son of)."
        },
        {
            "prompt": "Listen to the natural Israeli greeting. How is the name introduced?",
            "speakAudio": "קוראים לי יוני",
            "options": [
                "Kor'ím li Yoni (People call me Yoni — most common spoken idiom)",
                "Shmí Yoni (My formal name)",
                "Yesh li Yoni"
            ],
            "correct": 0,
            "explain": "'Kor'ím li...' literally means 'They call me...', standard for introductions."
        },
        {
            "prompt": "Listen to the residence verb. Is it masculine (gar) or feminine (gara)?",
            "speakAudio": "אני גרה בירושלים",
            "options": [
                "Feminine: 'Aní gará' (I live in Jerusalem)",
                "Masculine: 'Aní gar'",
                "Past tense"
            ],
            "correct": 0,
            "explain": "'gará' [ɡaˈʁa] is the feminine singular present participle of the verb lagúr (to live/reside)."
        },
        {
            "prompt": "Listen to the polite phrase. What does it mean?",
            "speakAudio": "נעים מאוד",
            "options": [
                "Nice to meet you ('Na'ím me'ód' = Very pleasant!)",
                "Goodbye",
                "Thank you very much"
            ],
            "correct": 0,
            "explain": "'Na'ím me'ód' is the standard Hebrew equivalent of 'Pleased to meet you'."
        }
    ],
    "arena": [
        {
            "quest": "Name Introduction",
            "clue": "Yoni: 'Assemble the conversational phrase: Kor'ím, li, Yoni!'",
            "target": "קוראים לי יוני",
            "tokens": ["קוראים", "לי", "יוני", "שמי", "אני"],
            "explain": "'קוראים' (they call) + 'לי' (to me) + 'יוני' (Yoni)."
        },
        {
            "quest": "Declaring Age",
            "clue": "Yoni: 'Male speaker uses ben: Aní ben esrím!'",
            "target": "אני בן עשרים",
            "tokens": ["אני", "בן", "עשרים", "בת", "שנים"],
            "explain": "'אני' (I) + 'בן' (son of) + 'עשרים' (twenty)."
        },
        {
            "quest": "Stating Residence",
            "clue": "Yoni: 'Combine aní, gar, and be-Tel Aviv!'",
            "target": "אני גר בתל אביב",
            "tokens": ["אני", "גר", "בתל אביב", "גרה", "מירושלים"],
            "explain": "'אני' (I) + 'גר' (live m.) + 'בתל אביב' (in Tel Aviv)."
        },
        {
            "quest": "Expressing a Passion",
            "clue": "Yoni: 'Assemble aní, ohév, and likró!'",
            "target": "אני אוהב לקרוא",
            "tokens": ["אני", "אוהב", "לקרוא", "אוהבת", "לנסוע"],
            "explain": "'אני' + 'אוהב' (love m.) + 'לקרוא' (to read)."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the Hebrew word for 'SON' used in male age (BEN -> בן):",
            "tiles": ["ב", "ן", "ת", "א", "ם"],
            "answer": "בן",
            "gloss": "ben (son of / age marker m.)"
        },
        {
            "clue": "Assemble the present verb for 'LIVES / RESIDES' (GAR -> גר):",
            "tiles": ["ג", "ר", "ד", "ל", "ה"],
            "answer": "גר",
            "gloss": "gar (lives / resides m.)"
        },
        {
            "clue": "Assemble the courtesy greeting NA'ÍM ('pleasant' -> נעים):",
            "tiles": ["נ", "ע", "י", "ם", "ש", "כ"],
            "answer": "נעים",
            "gloss": "na'ím (pleasant / nice to meet you)"
        }
    ],
    "quiz": [
        {
            "q": "How do Hebrew speakers express age (e.g. 'I am 20 years old')?",
            "options": [
                "Using 'ben' (son of, for males) or 'bat' (daughter of, for females) + number (e.g. 'aní ben/bat esrím')",
                "Using the verb 'lihyot' + years",
                "With the word 'shanim' placed before the pronoun"
            ],
            "correct": 0,
            "explain": "Hebrew uniquely uses familial lineage terms: 'ben' (son of) or 'bat' (daughter of) followed by the cardinal number."
        },
        {
            "q": "What is the most colloquial, everyday way to say 'My name is...' in Israel?",
            "options": [
                "קוֹרְאִים לִי... (Kor'ím li... — lit. 'They call me...')",
                "הַשֵּׁם שֶׁלִּי הוּא...",
                "אֲנִי נִקְרָא..."
            ],
            "correct": 0,
            "explain": "'Kor'ím li...' is the ubiquitous, friendly way Israelis introduce themselves in daily life."
        },
        {
            "q": "How does the verb 'to live / reside' change depending on whether a man or a woman is speaking?",
            "options": [
                "A man says 'Aní gar' (גָּר), while a woman says 'Aní gará' (גָּרָה)",
                "Hebrew verbs never change for gender in present tense",
                "Only the pronoun changes, the verb is identical"
            ],
            "correct": 0,
            "explain": "All Hebrew present-tense verbs are participles that agree in gender and number with the subject (gar / gará)."
        },
        {
            "q": "How are the prepositions 'from' (מִ-) and 'in' (בְּ-) attached to place names in Hebrew?",
            "options": [
                "As inseparable single-letter prefixes directly attached to the first letter of the place name (e.g. מִירוּשָׁלַיִם, בְּתֵל אָבִיב)",
                "As standalone separate words with a space",
                "As suffixes attached at the end of the city name"
            ],
            "correct": 0,
            "explain": "Prepositions like בְּ (in/at), לְ (to), and מִ (from) are prefixes written attached to the following word."
        },
        {
            "q": "What is the root of the words 'sofér' (writer), 'séfer' (book), and 'sipur' (story)?",
            "options": [
                "ס-פ-ר (S-P-R, relating to recording, counting, and narrating)",
                "כ-ת-ב (K-T-V)",
                "ל-מ-ד (L-M-D)"
            ],
            "correct": 0,
            "explain": "Semitic tri-consonantal root ס-פ-ר governs literature, narration, and recording."
        }
    ]
}

CHINESE_STEP4 = {
    "sealName": "Tōngxíng Zhi Shēnfen Seal (通行·身份文牒之印)",
    "guide": {
        "name": "Xiǎo Lǐ (小李)",
        "role": "Beijing Cultural Diplomat & Tour Guide",
        "avatar": "🏮",
        "prompt": "Nǐ hǎo! Introduce yourself with pride in Chinese: your name ('我叫...'), your age with 岁 ('我二十岁'), where you come from ('我来自...'), where you live ('我住在...'), your profession, and your hobbies!"
    },
    "cards": [
        {
            "id": "zh4_c1",
            "type": "identity_name",
            "glyph": "我叫...",
            "phonetic": "wǒ jiào... [wo˨˩˦ tɕjaʊ̯˥˩]",
            "gloss": "I am called... / My name is...",
            "speakText": "我叫李华",
            "audioUrl": "",
            "whisper": "The primary verb for introducing your name is 叫 (jiào = to be called): '我叫李华' (My name is Li Hua). You can also say '我的名字是...' (My name is...)."
        },
        {
            "id": "zh4_c2",
            "type": "identity_age",
            "glyph": "我 ... 岁",
            "phonetic": "wǒ ... suì [wo˨˩˦ ... sweɪ̯˥˩]",
            "gloss": "I am ... years old",
            "speakText": "我二十岁",
            "audioUrl": "",
            "whisper": "To state age, simply say '我' + number + '岁' (suì = years of age): '我二十岁' (I am 20 years old). Notice: NO VERB is needed at all! Neither 是 nor 有 is used here."
        },
        {
            "id": "zh4_c3",
            "type": "identity_origin",
            "glyph": "我来自...",
            "phonetic": "wǒ láizì... [wo˨˩˦ laɪ̯˧˥.tsɨ˥˩ ...]",
            "gloss": "I come from...",
            "speakText": "我来自北京",
            "audioUrl": "",
            "whisper": "来自 (láizì) combines 来 (come) + 自 (from): '我来自北京' (I come from Beijing), '我来自中国' (I come from China)."
        },
        {
            "id": "zh4_c4",
            "type": "identity_residence",
            "glyph": "我住在...",
            "phonetic": "wǒ zhù zài... [wo˨˩˦ ʈʂu˥˩ tsaɪ̯˥˩ ...]",
            "gloss": "I live in...",
            "speakText": "我住在上海",
            "audioUrl": "",
            "whisper": "住 (zhù = to live/reside) + 在 (zài = at/in): '我住在上海' (I live in Shanghai). Preposition 在 indicates location."
        },
        {
            "id": "zh4_c5",
            "type": "identity_profession",
            "glyph": "我是学生 / 老师",
            "phonetic": "wǒ shì xuésheng [ʂɨ˥˩ ɕyɛ˧˥.ʂəŋ] / lǎoshī",
            "gloss": "I am a student / teacher",
            "speakText": "我是学生",
            "audioUrl": "",
            "whisper": "Here 是 IS used because '学生' (xuésheng) and '老师' (lǎoshī) are nouns! No measure words or articles are required: '我是学生'."
        },
        {
            "id": "zh4_c6",
            "type": "identity_profession",
            "glyph": "医生 / 工程师 / 程序员",
            "phonetic": "yīshēng [i˥.ʂəŋ], gōngchéngshī, chéngxùyuán",
            "gloss": "doctor / engineer / programmer",
            "speakText": "我是工程师",
            "audioUrl": "",
            "whisper": "Useful modern professions: 医生 (doctor), 工程师 (engineer), 程序员 (programmer), 艺术家 (artist)."
        },
        {
            "id": "zh4_c7",
            "type": "identity_hobby",
            "glyph": "我喜欢看书",
            "phonetic": "wǒ xǐhuan kàn shū [wo˨˩˦ ɕi˨˩˦.xwan kʰan˥˩ ʂu˥]",
            "gloss": "I like to read books",
            "speakText": "我喜欢看书",
            "audioUrl": "",
            "whisper": "喜欢 (xǐhuan) = to like. It is followed directly by verb phrases: '看书' (kàn shū = read books, lit. look at books)!"
        },
        {
            "id": "zh4_c8",
            "type": "identity_hobby",
            "glyph": "我喜欢听音乐 / 旅游",
            "phonetic": "tīng yīnyuè [tʰiŋ˥ in˥.yɛ˥˩] / lǚyóu [ly˨˩˦.joʊ̯˧˥]",
            "gloss": "I like listening to music / traveling",
            "speakText": "我喜欢听音乐",
            "audioUrl": "",
            "whisper": "听音乐 (tīng yīnyuè) = listen to music; 旅游 (lǚyóu) = travel. '我喜欢旅游' = I like traveling."
        },
        {
            "id": "zh4_c9",
            "type": "greeting_courtesy",
            "glyph": "很高兴认识你",
            "phonetic": "hěn gāoxìng rènshi nǐ [xən˨˩˦ kaʊ̯˥.ɕiŋ˥˩ ʐən˥˩.ʂɨ ni˨˩˦]",
            "gloss": "Very glad to meet you",
            "speakText": "很高兴认识你",
            "audioUrl": "",
            "whisper": "The universal courtesy phrase when meeting someone! 很高兴 (hěn gāoxìng = very happy) + 认识你 (rènshi nǐ = to know/meet you)."
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the age phrase. Notice whether a verb was spoken.",
            "speakAudio": "我二十岁",
            "options": [
                "No verb: pronoun + number + 岁 (wǒ èrshí suì — standard Chinese age)",
                "Used 是 (wǒ shì èrshí suì)",
                "Used 有 (wǒ yǒu èrshí suì)"
            ],
            "correct": 0,
            "explain": "In Chinese, age statements require no verb: '我二十岁' directly states 'I [am] twenty years of age'."
        },
        {
            "prompt": "Listen to the origin sentence. Where does the speaker come from?",
            "speakAudio": "我来自北京",
            "options": [
                "From Beijing (来自北京 — láizì Běijīng)",
                "From Shanghai (来自上海)",
                "From Guangzhou"
            ],
            "correct": 0,
            "explain": "'来自' (láizì) means 'to come from'; '北京' is Beijing."
        },
        {
            "prompt": "Listen to the hobby verb. What does the speaker enjoy?",
            "speakAudio": "我喜欢听音乐",
            "options": [
                "Listening to music (听音乐 — tīng yīnyuè)",
                "Reading books (看书 — kàn shū)",
                "Playing soccer (踢足球)"
            ],
            "correct": 0,
            "explain": "'听音乐' (tīng yīnyuè) means listening to music."
        },
        {
            "prompt": "Listen to the courtesy phrase. What is being expressed?",
            "speakAudio": "很高兴认识你",
            "options": [
                "Nice to meet you (很高兴认识你 — hěn gāoxìng rènshi nǐ)",
                "Thank you very much (非常感谢你)",
                "Goodbye and see you tomorrow"
            ],
            "correct": 0,
            "explain": "'很高兴认识你' is the standard polite expression for 'Pleased to meet you'."
        }
    ],
    "arena": [
        {
            "quest": "Name Introduction",
            "clue": "Xiǎo Lǐ: 'Introduce yourself: 我叫李华 (wǒ jiào Lǐ Huá)!'",
            "target": "我叫李华",
            "tokens": ["我", "叫", "李华", "是", "岁"],
            "explain": "'我' (I) + '叫' (called) + '李华' (Li Hua)."
        },
        {
            "quest": "Declaring Age",
            "clue": "Xiǎo Lǐ: 'State that you are 20 years old: 我二十岁 (no copula!)!'",
            "target": "我二十岁",
            "tokens": ["我", "二十", "岁", "是", "有"],
            "explain": "Chinese age structure requires no verb: '我' + '二十' + '岁'."
        },
        {
            "quest": "Stating Residence",
            "clue": "Xiǎo Lǐ: 'State that you live in Shanghai: 我住在上海!'",
            "target": "我住在上海",
            "tokens": ["我", "住", "在", "上海", "来自", "叫"],
            "explain": "'我' + '住' (live) + '在' (at/in) + '上海' (Shanghai)."
        },
        {
            "quest": "Expressing a Hobby",
            "clue": "Xiǎo Lǐ: 'State that you like reading books: 我喜欢看书!'",
            "target": "我喜欢看书",
            "tokens": ["我", "喜欢", "看书", "听音乐", "是"],
            "explain": "'我' + '喜欢' (like) + '看书' (read books)."
        }
    ],
    "scribe": [
        {
            "clue": "Assemble the hobby compound KÀNSHŪ ('to read books' -> 看书):",
            "tiles": ["看", "书", "听", "写"],
            "answer": "看书",
            "gloss": "看书 (kàn shū = read books)"
        },
        {
            "clue": "Assemble the origin verb LÁIZÌ ('to come from' -> 来自):",
            "tiles": ["来", "自", "去", "住"],
            "answer": "来自",
            "gloss": "来自 (láizì = come from)"
        },
        {
            "clue": "Assemble the verb for 'TO LIVE / RESIDE' (ZHÙZÀI -> 住在):",
            "tiles": ["住", "在", "去", "从"],
            "answer": "住在",
            "gloss": "住在 (zhù zài = live in/at)"
        }
    ],
    "quiz": [
        {
            "q": "How is age expressed in Chinese (e.g. 'I am 20 years old')?",
            "options": [
                "Subject + number + 岁 (suì), with NO verb like 是 or 有 (e.g. '我二十岁')",
                "Subject + 是 + number + 岁",
                "Subject + 有 + number + 年"
            ],
            "correct": 0,
            "explain": "Age statements in Chinese are nominal predicates requiring neither 是 nor 有: '我二十岁'."
        },
        {
            "q": "What is the primary conversational verb used to introduce one's name in Chinese?",
            "options": ["叫 (jiào, e.g. '我叫...')", "名 (míng)", "说 (shuō)"],
            "correct": 0,
            "explain": "叫 (jiào = to be called) is the standard and most common verb for introducing your name: '我叫...'."
        },
        {
            "q": "In the sentence '我住在上海', what grammatical function does '在' (zài) serve?",
            "options": [
                "It functions as a locative preposition meaning 'at/in', introducing the place of residence",
                "It marks the past tense of 住",
                "It indicates a question"
            ],
            "correct": 0,
            "explain": "在 (zài) acts as a preposition indicating location after motion or posture verbs like 住 (to live): '住在上海'."
        },
        {
            "q": "Why is 是 used in '我是学生' (I am a student) but omitted in '我很好' (I am good)?",
            "options": [
                "是 connects two nouns (我 and 学生); adjectives in Chinese predicate directly with words like 很 instead of 是",
                "Because 学生 is an older word",
                "Because 好 already contains the sound of 是"
            ],
            "correct": 0,
            "explain": "Mandarin uses 是 strictly for nominal equations (noun = noun). Adjectives act as verb predicates and do not take 是."
        },
        {
            "q": "What does the polite formula '很高兴认识你' literally translate to?",
            "options": [
                "Very happy to know/meet you",
                "May you have good fortune",
                "Where are you going?"
            ],
            "correct": 0,
            "explain": "很高兴 (very happy) + 认识 (to know/acquaint) + 你 (you)."
        }
    ]
}

GERMAN_STEP4 = {
    "sealName": "Siegel der Persönlichen Identität",
    "guide": {
        "name": "Lukas",
        "role": "Freiburg Apprentice & Traveler",
        "avatar": "🎒",
        "prompt": "Hallo! Learn to tell your story in German: your name ('Ich heiße...'), your age with 'sein' ('Ich bin 20 Jahre alt'), where you come from ('Ich komme aus...'), where you reside ('Ich wohne in...'), and your hobbies!"
    },
    "cards": [
        {
            "id": "de4_c1",
            "type": "identity_name",
            "glyph": "Ich heiße... / Mein Name ist...",
            "phonetic": "[ɪç ˈhaɪ̯.sə] / [maɪ̯n ˈnaː.mə ɪst ...]",
            "gloss": "I am called... / My name is...",
            "speakText": "Ich heiße Lukas",
            "audioUrl": "",
            "whisper": "The letter 'ß' (Eszett) represents a sharp unvoiced [s] after a diphthong: 'heißen' -> 'ich heiße' [ˈhaɪ̯.sə]. You can also say 'Mein Name ist Lukas'."
        },
        {
            "id": "de4_c2",
            "type": "identity_age",
            "glyph": "Ich bin ... Jahre alt",
            "phonetic": "[ɪç bɪn ... ˈjaː.ʁə alt]",
            "gloss": "I am ... years old",
            "speakText": "Ich bin zwanzig Jahre alt",
            "audioUrl": "",
            "whisper": "GERMAN USES SEIN (to be) for age, just like English: 'Ich bin zwanzig Jahre alt'. Do not say 'Ich habe ... Jahre'!"
        },
        {
            "id": "de4_c3",
            "type": "identity_origin",
            "glyph": "Ich komme aus...",
            "phonetic": "[ɪç ˈkɔ.mə aʊ̯s ...]",
            "gloss": "I come from...",
            "speakText": "Ich komme aus Berlin",
            "audioUrl": "",
            "whisper": "'Aus' is a dative preposition meaning 'out of / from': 'Ich komme aus Deutschland', 'Ich komme aus der Schweiz' (feminine countries take the dative article 'der')!"
        },
        {
            "id": "de4_c4",
            "type": "identity_residence",
            "glyph": "Ich wohne in...",
            "phonetic": "[ɪç ˈvoː.nə ɪn ...]",
            "gloss": "I live / reside in...",
            "speakText": "Ich wohne in München",
            "audioUrl": "",
            "whisper": "'Wohnen' refers to your apartment or home residence: 'Ich wohne in München'. 'In' takes dative for stationary location."
        },
        {
            "id": "de4_c5",
            "type": "identity_profession",
            "glyph": "Ich bin Student / Studentin",
            "phonetic": "[ʃtuˈdɛnt] / [ʃtuˈdɛn.tɪn]",
            "gloss": "I am a student (male / female)",
            "speakText": "Ich bin Student",
            "audioUrl": "",
            "whisper": "German creates female professions with the suffix '-in': Student -> Studentin; Lehrer -> Lehrerin; Arzt -> Ärztin. No article used after sein!"
        },
        {
            "id": "de4_c6",
            "type": "identity_profession",
            "glyph": "Ich bin Entwickler / Lehrer / Schreiber",
            "phonetic": "[ɛntˈvɪk.lɐ], [ˈleː.ʁɐ]",
            "gloss": "developer / teacher / writer",
            "speakText": "Ich bin Lehrer",
            "audioUrl": "",
            "whisper": "The agentive suffix '-er' marks male practitioners; adding '-in' creates the female form (Lehrerin, Entwicklerin)."
        },
        {
            "id": "de4_c7",
            "type": "identity_hobby",
            "glyph": "Ich mag lesen / Ich lese gern",
            "phonetic": "[ɪç maːk ˈleː.zn̩] / [ɪç ˈleː.zə ɡɛʁn]",
            "gloss": "I like reading / I gladly read",
            "speakText": "Ich lese gern",
            "audioUrl": "",
            "whisper": "GERMAN IDIOM ALERT: While 'Ich mag lesen' is understood, native speakers almost universally use the adverb 'gern' (gladly) directly after the verb: 'Ich lese gern' (I like reading)!"
        },
        {
            "id": "de4_c8",
            "type": "identity_hobby",
            "glyph": "Ich höre gern Musik / Ich reise gern",
            "phonetic": "[ɪç ˈhøː.ʁə ɡɛʁn muˈziːk] / [ˈʁaɪ̯.zə]",
            "gloss": "I like listening to music / traveling",
            "speakText": "Ich reise gern",
            "audioUrl": "",
            "whisper": "'gern' turns any action into a beloved hobby! 'Ich reise gern' (I like traveling), 'Ich koche gern' (I like cooking)."
        },
        {
            "id": "de4_c9",
            "type": "greeting_courtesy",
            "glyph": "Freut mich! / Angenehm!",
            "phonetic": "[fʁɔʏ̯t mɪç], [ˈan.ɡə.neːm]",
            "gloss": "Pleased to meet you!",
            "speakText": "Freut mich",
            "audioUrl": "",
            "whisper": "Short for 'Es freut mich, Sie kennenzulernen' (It pleases me to get to know you). Quick, warm, and natural!"
        }
    ],
    "earGym": [
        {
            "prompt": "Listen to the age construction. Does German use 'haben' or 'sein' for age?",
            "speakAudio": "Ich bin fünfundzwanzig Jahre alt",
            "options": [
                "Uses sein: 'Ich bin ... Jahre alt' (like English, unlike French/Spanish!)",
                "Uses haben: 'Ich habe ... Jahre'",
                "Uses werden"
            ],
            "correct": 0,
            "explain": "German uses 'sein' (ich bin) with 'Jahre alt' to express age."
        },
        {
            "prompt": "Listen to the favorite hobby. Which construction did the speaker use?",
            "speakAudio": "Ich lese gern Bücher",
            "options": [
                "Verb + gern ('Ich lese gern' — the natural German idiom for hobbies)",
                "Ich will lesen",
                "Ich muss lesen"
            ],
            "correct": 0,
            "explain": "The adverb 'gern' after a verb is the primary native German way to state that you enjoy doing that activity."
        },
        {
            "prompt": "Listen to the origin sentence. Where does the speaker come from?",
            "speakAudio": "Ich komme aus Deutschland",
            "options": [
                "From Germany (aus Deutschland)",
                "From Austria (aus Österreich)",
                "From Switzerland (aus der Schweiz)"
            ],
            "correct": 0,
            "explain": "'aus Deutschland' means from Germany."
        },
        {
            "prompt": "Listen to the female profession ending. Which job was mentioned?",
            "speakAudio": "Ich bin Lehrerin",
            "options": [
                "Female teacher (Lehrerin — suffix -in)",
                "Male teacher (Lehrer)",
                "Female student (Studentin)"
            ],
            "correct": 0,
            "explain": "The suffix '-in' marks the female profession: 'Lehrerin'."
        }
    ],
    "arena": [
        {
            "quest": "Name Introduction",
            "clue": "Lukas: 'Assemble Ich heiße Lukas!'",
            "target": "Ich heiße Lukas",
            "tokens": ["Ich", "heiße", "Lukas", "bin", "mein"],
            "explain": "'Ich heiße' (I am called) + name."
        },
        {
            "quest": "Declaring Age",
            "clue": "Lukas: 'Remember: German uses bin, NOT habe!'",
            "target": "Ich bin zwanzig Jahre alt",
            "tokens": ["Ich", "bin", "zwanzig", "Jahre", "alt", "habe"],
            "explain": "German age formula: 'Ich bin' + number + 'Jahre alt'."
        },
        {
            "quest": "Stating Residence",
            "clue": "Lukas: 'Assemble Ich wohne in München!'",
            "target": "Ich wohne in München",
            "tokens": ["Ich", "wohne", "in", "München", "komme", "aus"],
            "explain": "'Ich wohne' (I live) + 'in München'."
        },
        {
            "quest": "Expressing a Hobby",
            "clue": "Lukas: 'Combine Ich, lese, and gern!'",
            "target": "Ich lese gern",
            "tokens": ["Ich", "lese", "gern", "mag", "Buch"],
            "explain": "'Ich lese gern' (I like reading / I read gladly)."
        }
    ],
    "scribe": [
        {
            "clue": "Spell the German word for 'YEARS' (JAHRE):",
            "tiles": ["J", "A", "H", "R", "E", "S", "T"],
            "answer": "JAHRE",
            "gloss": "Jahre (years)"
        },
        {
            "clue": "Spell the German adverb for 'GLADLY / ENJOY DOING' (GERN):",
            "tiles": ["G", "E", "R", "N", "O", "T"],
            "answer": "GERN",
            "gloss": "gern (gladly / like doing)"
        },
        {
            "clue": "Spell the city name of the Bavarian capital (MÜNCHEN):",
            "tiles": ["M", "Ü", "N", "C", "H", "E", "N", "S"],
            "answer": "MÜNCHEN",
            "gloss": "München (Munich)"
        }
    ],
    "quiz": [
        {
            "q": "How is age expressed in German (e.g. 'I am 20 years old')?",
            "options": [
                "Using 'sein': 'Ich bin 20 Jahre alt' (like English, NOT like Romance languages!)",
                "Using 'haben': 'Ich habe 20 Jahre'",
                "Using 'halten': 'Ich halte 20 Jahre'"
            ],
            "correct": 0,
            "explain": "German uses 'sein' (to be) for age: 'Ich bin ... Jahre alt'."
        },
        {
            "q": "What is the most idiomatic, natural German way to express that you like doing a hobby?",
            "options": [
                "Placing the adverb 'gern' directly after the conjugated verb (e.g. 'Ich lese gern', 'Ich schwimme gern')",
                "Using the verb 'mögen' with a past participle",
                "Translating word-for-word: 'Ich wie zu lesen'"
            ],
            "correct": 0,
            "explain": "German speakers standardly express enjoyment using the adverb 'gern' after the verb."
        },
        {
            "q": "How are female professions formed from male titles in German (e.g. Lehrer -> Lehrerin)?",
            "options": [
                "By adding the suffix '-in' (and sometimes an umlaut, like Arzt -> Ärztin)",
                "By changing the article to 'das'",
                "By adding the prefix 'Frau-'"
            ],
            "correct": 0,
            "explain": "The suffix '-in' marks female professions (Lehrerin, Studentin, Professorin, Entwicklerin)."
        },
        {
            "q": "Why is there no article in 'Ich bin Student'?",
            "options": [
                "German drops the indefinite article 'ein' when stating professions, nationalities, or institutional statuses after sein",
                "Because 'Student' is a neuter mass noun",
                "Only formal German drops the article"
            ],
            "correct": 0,
            "explain": "In German predicate nominatives, professions drop the indefinite article: 'Ich bin Student'."
        },
        {
            "q": "What is the grammatical difference between 'Ich komme aus...' and 'Ich wohne in...'?",
            "options": [
                "'Ich komme aus...' expresses geographic origin/hometown, while 'Ich wohne in...' expresses current residence",
                "'Ich wohne in...' is only used for hotel stays",
                "There is no difference"
            ],
            "correct": 0,
            "explain": "'Kommen aus' denotes origin or where you come from; 'wohnen in' denotes current dwelling or home."
        }
    ]
}


# ==============================================================================
# TOP-LEVEL REGISTRIES
# ==============================================================================

STEP3_DATA = {
    "waray": WARAY_STEP3,
    "french": FRENCH_STEP3,
    "latin": LATIN_STEP3,
    "hebrew": HEBREW_STEP3,
    "chinese": CHINESE_STEP3,
    "german": GERMAN_STEP3
}

STEP4_DATA = {
    "waray": WARAY_STEP4,
    "french": FRENCH_STEP4,
    "latin": LATIN_STEP4,
    "hebrew": HEBREW_STEP4,
    "chinese": CHINESE_STEP4,
    "german": GERMAN_STEP4
}


# ==============================================================================
# SELF-VALIDATION ROUTINE
# ==============================================================================

def validate_datasets():
    """Validates the schema, linguistic tokens, and completeness of STEP3_DATA and STEP4_DATA."""
    expected_realms = ["waray", "french", "latin", "hebrew", "chinese", "german"]
    
    for step_num, step_dict in [(3, STEP3_DATA), (4, STEP4_DATA)]:
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

    print("✅ All STEP3_DATA and STEP4_DATA validations passed flawlessly across all 6 realms!")


if __name__ == "__main__":
    validate_datasets()
    print("STEP3_DATA realms:", list(STEP3_DATA.keys()))
    print("STEP4_DATA realms:", list(STEP4_DATA.keys()))
