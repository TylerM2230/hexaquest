#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HexaQuest Step 7 & Step 8 Datasets
===================================
Step 7: Modal Verbs (The Phrase Multiplier — Want, Can, Must, Allowed/Should)
Step 8: Prepositions & Relational Markers (Spatial locations, directions, grammatical case markers)

Realm Curricula:
  - Waray:
      * S7: 'karuyag' + ergative, 'pwede' + absolutive, 'kinahanglan', 'diri pwede', 'angay', 'mahimo'
      * S8: Locative marker 'ha' + spatial nouns: 'ha sulod han', 'ha gawas han', 'ha igbaw han',
            'ha ilarom han', 'ha atubangan han', 'ha luyo han', 'ngadto ha', 'tikang ha'
  - French:
      * S7: vouloir, pouvoir, devoir, falloir ('il faut'), 'on ne peut pas', 'je voudrais'
      * S8: dans, sur, sous, devant, derrière, entre, à côté de (du/des), chez, vers
  - Latin:
      * S7: velle / volō, posse / possum, dēbēre, licet, nōlī + infinitive, oportet
      * S8: Prepositions with Ablative (SID SPACE: sub, in, dē, sine, prō, ab, cum, ex)
            vs. Accusative (ad, per, ante, post, in/sub motion)
  - Hebrew:
      * S7: rotsé/rotsáh, yachól/yecholáh, tsarích/tsricháh, efshár, asúr, chayáv, kedáy
      * S8: Preposition prefixes בְּ- (be-), לְ- (le-), מִ- (mi-),
            independent: עַל (al), תַּחַת (táchat), לִפְנֵי (lifnéy), אַחֲרֵי (acharèy), לְיַד (leyád), בֵּין (beyn)
  - Chinese:
      * S7: 想 (xiǎng), 要 (yào), 能 (néng), 会 (huì), 可以 (kěyǐ), 必须 (bìxū), 应该 (yīnggāi)
      * S8: Coverbs 在 (zài), 到 (dào), 从 (cóng), localizers 上 (shàng), 下 (xià), 里 (lǐ), 外 (wài),
            前 (qián), 后 (hòu), 中间 (zhōngjiān), 旁边 (pángbiān)
  - German:
      * S7: wollen, können, müssen, dürfen, möchten, sollen, Satzklammer (Verb-2 ... Infinitiv-Ende)
      * S8: Wechselpräpositionen (an, auf, hinter, in, neben, über, unter, vor, zwischen:
            Dativ for static rest vs. Akkusativ for motion), pure Dativ (aus, bei, mit, nach, von, zu)
"""

STEP7_DATA = {
    "waray": {
        "sealName": "San Juanico Modal Seal",
        "guide": {
            "name": "Manang Elena",
            "role": "Visayan Village Sage & Modal Guide",
            "avatar": "⛵",
            "prompt": "Maupay nga adlaw! In Waray, modal words like 'karuyag', 'pwede', and 'kinahanglan' unlock infinite expressions of desire, capability, and obligation. Notice how pronoun cases shift between 'ko' (ergative/genitive) and 'ka' (absolutive/nominative)!"
        },
        "cards": [
            {
                "id": "war_s7_c1",
                "type": "modal",
                "glyph": "karuyag",
                "phonetic": "[ka.ɾu.ˈjag]",
                "gloss": "want / desire / like",
                "speakText": "karuyag",
                "audioUrl": "",
                "whisper": "Takes an ergative pronoun for the experiencer: 'Karuyag ko' (I want), 'Karuyag niya' (He/She wants), followed by an actor-focus verb or noun ('Karuyag ko kumaon' = I want to eat)."
            },
            {
                "id": "war_s7_c2",
                "type": "modal",
                "glyph": "diri karuyag",
                "phonetic": "[dɪ.ˈɾi ka.ɾu.ˈjag]",
                "gloss": "do not want / refuse",
                "speakText": "diri karuyag",
                "audioUrl": "",
                "whisper": "'Diri' is the standard Visayan negator for verbs and adjectives. 'Diri ko karuyag' (I don't want / I dislike)."
            },
            {
                "id": "war_s7_c3",
                "type": "modal",
                "glyph": "pwede",
                "phonetic": "[ˈpwɛ.dɛ]",
                "gloss": "can / may / permitted",
                "speakText": "pwede",
                "audioUrl": "",
                "whisper": "Expresses permission and physical possibility. Takes absolutive pronouns: 'Pwede ka pumarapit' (You may approach). Borrowed from Spanish 'puede' but fully integrated into Visayan syntax."
            },
            {
                "id": "war_s7_c4",
                "type": "modal",
                "glyph": "diri pwede",
                "phonetic": "[dɪ.ˈɾi ˈpwɛ.dɛ]",
                "gloss": "cannot / not permitted / forbidden",
                "speakText": "diri pwede",
                "audioUrl": "",
                "whisper": "Crucial for prohibitions: 'Diri pwede sumulod' (Entering is not permitted / No entry)."
            },
            {
                "id": "war_s7_c5",
                "type": "modal",
                "glyph": "kinahanglan",
                "phonetic": "[kɪ.na.haŋ.ˈlan]",
                "gloss": "must / need / necessary",
                "speakText": "kinahanglan",
                "audioUrl": "",
                "whisper": "Expresses strong necessity or obligation: 'Kinahanglan ko mag-aram' (I must study / learn). Often takes ergative 'ko' or 'naton' (inclusive us)."
            },
            {
                "id": "war_s7_c6",
                "type": "modal",
                "glyph": "angay",
                "phonetic": "[a.ˈŋaj]",
                "gloss": "should / ought to / fitting",
                "speakText": "angay",
                "audioUrl": "",
                "whisper": "Denotes moral obligation, advice, or suitability: 'Angay kita magbulig' (We ought to help). Conveys propriety."
            },
            {
                "id": "war_s7_c7",
                "type": "modal",
                "glyph": "mahimo",
                "phonetic": "[ma.ˈhi.mɔ]",
                "gloss": "can / may / feasible",
                "speakText": "mahimo",
                "audioUrl": "",
                "whisper": "Native Visayan counterpart to 'pwede', derived from 'himo' (to make/do). 'Mahimo ba?' (Is it possible?)."
            },
            {
                "id": "war_s7_c8",
                "type": "modal",
                "glyph": "gusto",
                "phonetic": "[ˈɡus.tɔ]",
                "gloss": "want / like (colloquial synonym)",
                "speakText": "gusto",
                "audioUrl": "",
                "whisper": "Common Spanish loan used alongside 'karuyag': 'Gusto ko...' functions identically with ergative clitics."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the modal sentence. What intention is expressed?",
                "speakAudio": "Karuyag ko kumaon",
                "options": [
                    "I want to eat (Karuyag ko kumaon)",
                    "I must study (Kinahanglan ko mag-aram)",
                    "I cannot enter (Diri pwede sumulod)"
                ],
                "correct": 0,
                "explain": "'Karuyag ko kumaon' uses 'karuyag' (want) + 'ko' (I/my) + actor-focus infinitive 'kumaon' (to eat)."
            },
            {
                "prompt": "Listen to the prohibition. What is being commanded?",
                "speakAudio": "Diri pwede sumulod",
                "options": [
                    "You cannot enter / No entry (Diri pwede sumulod)",
                    "You may come near (Pwede ka pumarapit)",
                    "You must leave (Kinahanglan ka gumawas)"
                ],
                "correct": 0,
                "explain": "'Diri pwede' means not permitted/forbidden, combined with 'sumulod' (to enter)."
            },
            {
                "prompt": "Listen to the modal obligation. Who needs to study?",
                "speakAudio": "Kinahanglan ko mag-aram",
                "options": [
                    "I need to study (Kinahanglan ko mag-aram)",
                    "You need to study (Kinahanglan mo mag-aram)",
                    "We need to eat (Kinahanglan naton kumaon)"
                ],
                "correct": 0,
                "explain": "'Kinahanglan ko' indicates first-person singular obligation: 'I must / need'."
            },
            {
                "prompt": "Listen to the polite permission. What does the speaker say?",
                "speakAudio": "Pwede ka pumarapit",
                "options": [
                    "You may approach / come closer (Pwede ka pumarapit)",
                    "You must go away (Kinahanglan ka lumakat)",
                    "I want to speak (Karuyag ko magyakan)"
                ],
                "correct": 0,
                "explain": "'Pwede ka' (You may) + 'pumarapit' (-um- infix actor-focus verb 'to approach')."
            }
        ],
        "arena": [
            {
                "quest": "Expressing Desire",
                "clue": "Assemble: 'I want to eat' (want + I + to-eat)",
                "target": "Karuyag ko kumaon",
                "tokens": ["Karuyag", "ko", "kumaon", "ikaw", "diri", "balay"],
                "explain": "In Waray, 'karuyag' takes the ergative first-person enclitic 'ko', followed by the infinitive 'kumaon'."
            },
            {
                "quest": "Granting Permission",
                "clue": "Assemble: 'You can come closer' (can + you + approach)",
                "target": "Pwede ka pumarapit",
                "tokens": ["Pwede", "ka", "pumarapit", "mo", "kinahanglan", "sulod"],
                "explain": "'Pwede' pairs with the absolutive pronoun 'ka' (you) and the infinitive verb 'pumarapit'."
            },
            {
                "quest": "Expressing Obligation",
                "clue": "Assemble: 'I must study' (must + I + study)",
                "target": "Kinahanglan ko mag-aram",
                "tokens": ["Kinahanglan", "ko", "mag-aram", "ka", "diri", "kumaon"],
                "explain": "'Kinahanglan' expresses necessity, followed by ergative 'ko' and the prefix verb 'mag-aram' (to study/learn)."
            },
            {
                "quest": "Strict Prohibition",
                "clue": "Assemble: 'Entering is not allowed' (not + allowed + to-enter)",
                "target": "Diri pwede sumulod",
                "tokens": ["Diri", "pwede", "sumulod", "karuyag", "ko", "parapit"],
                "explain": "'Diri pwede' forms a firm prohibition, combined with the infinitive 'sumulod' (to enter)."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the modal root for 'want / desire':",
                "tiles": ["K", "A", "R", "U", "Y", "A", "G", "O"],
                "answer": "KARUYAG",
                "gloss": "karuyag (want / desire)"
            },
            {
                "clue": "Spell the modal word for 'can / may':",
                "tiles": ["P", "W", "E", "D", "E", "A", "O"],
                "answer": "PWEDE",
                "gloss": "pwede (can / may)"
            },
            {
                "clue": "Spell the modal word for 'must / need':",
                "tiles": ["K", "I", "N", "A", "H", "A", "N", "G", "L", "A", "N", "O"],
                "answer": "KINAHANGLAN",
                "gloss": "kinahanglan (must / obligation)"
            }
        ],
        "quiz": [
            {
                "q": "Which pronoun form must be used with 'karuyag' when saying 'I want'?",
                "options": [
                    "Ergative/Genitive 'ko' (Karuyag ko...)",
                    "Absolutive/Nominative 'ako' (Karuyag ako...)",
                    "Oblique 'ha akon' (Karuyag ha akon...)"
                ],
                "correct": 0,
                "explain": "In Waray, 'karuyag' acts as a pseudo-verb/predicate requiring an ergative agent pronoun ('ko', 'mo', 'niya')."
            },
            {
                "q": "How do you form a negative command or prohibition like 'Entering is forbidden' in Waray?",
                "options": [
                    "Diri pwede sumulod",
                    "Waray sumulod",
                    "Ayaw karuyag sumulod"
                ],
                "correct": 0,
                "explain": "'Diri pwede' directly negates possibility/permission, forming 'Diri pwede sumulod' (Not allowed to enter)."
            },
            {
                "q": "What is the key grammatical difference between 'pwede ka' and 'kinahanglan ko'?",
                "options": [
                    "'Pwede' uses absolutive 'ka', while 'kinahanglan' typically takes ergative 'ko' for personal obligation",
                    "'Pwede' is only for past tense",
                    "'Kinahanglan' can never be followed by a verb"
                ],
                "correct": 0,
                "explain": "'Pwede' pairs naturally with absolutive clitics ('ka', 'kita'), whereas 'kinahanglan' commonly takes the ergative agent ('ko', 'naton') who bears the necessity."
            },
            {
                "q": "What does 'Karuyag ko kumaon hin isda' mean?",
                "options": [
                    "I want to eat fish",
                    "I cannot eat fish",
                    "I must sell fish"
                ],
                "correct": 0,
                "explain": "'Karuyag ko' = I want, 'kumaon' = to eat, 'hin isda' = indefinite object marker + fish."
            },
            {
                "q": "Which Waray word expresses ethical appropriateness or 'should / ought to'?",
                "options": [
                    "angay",
                    "diri",
                    "ngadto"
                ],
                "correct": 0,
                "explain": "'Angay' signifies 'fitting, proper, should/ought to' (e.g., 'Angay kita magbulig' = We ought to help)."
            }
        ]
    },
    "french": {
        "sealName": "Lumière Volonté Seal",
        "guide": {
            "name": "Madame Claudine",
            "role": "Parisian Salonnière & Grammatical Sage",
            "avatar": "⚜️",
            "prompt": "Bonjour ! Modal verbs in French—vouloir, pouvoir, devoir, and the impersonal falloir—are your ultimate expressive toolkit. Once conjugated, they couple directly with any infinitive!"
        },
        "cards": [
            {
                "id": "fr_s7_c1",
                "type": "modal",
                "glyph": "vouloir (je veux, il veut)",
                "phonetic": "[vu.lwaʁ] • [ʒə vø] • [il vø]",
                "gloss": "to want (I want, he/she wants)",
                "speakText": "je veux, il veut, nous voulons",
                "audioUrl": "",
                "whisper": "Irregular stem changes: 'je veux', 'tu veux', 'il veut', 'nous voulons', 'vous voulez', 'ils veulent'. Directly followed by an infinitive without a preposition ('Je veux apprendre')."
            },
            {
                "id": "fr_s7_c2",
                "type": "modal",
                "glyph": "pouvoir (je peux, on peut)",
                "phonetic": "[pu.vwaʁ] • [ʒə pø] • [ɔ̃ pø]",
                "gloss": "to be able / can (I can, one can)",
                "speakText": "je peux, on peut, nous pouvons",
                "audioUrl": "",
                "whisper": "Expresses capability or permission: 'je peux', 'tu peux', 'il/on peut', 'nous pouvons', 'vous pouvez', 'ils peuvent'. Note: 'Puis-je?' is the formal inverted question."
            },
            {
                "id": "fr_s7_c3",
                "type": "modal",
                "glyph": "devoir (je dois, il doit)",
                "phonetic": "[də.vwaʁ] • [ʒə dwa] • [il dwa]",
                "gloss": "must / to have to (I must, he must)",
                "speakText": "je dois, il doit, nous devons",
                "audioUrl": "",
                "whisper": "Conjugations: 'je dois', 'tu dois', 'il doit', 'nous devons', 'vous devez', 'ils doivent'. In conditional ('je devrais'), it means 'I should'."
            },
            {
                "id": "fr_s7_c4",
                "type": "modal",
                "glyph": "il faut (falloir)",
                "phonetic": "[il fo]",
                "gloss": "it is necessary / one must / we need to",
                "speakText": "il faut",
                "audioUrl": "",
                "whisper": "A defective impersonal verb: exists ONLY in the 3rd person singular 'il faut' + infinitive ('Il faut partir' = One must leave / We must go)."
            },
            {
                "id": "fr_s7_c5",
                "type": "modal",
                "glyph": "nous voulons / ils veulent",
                "phonetic": "[nu vu.lɔ̃] • [il vœl]",
                "gloss": "we want / they want",
                "speakText": "nous voulons, ils veulent",
                "audioUrl": "",
                "whisper": "Notice the vowel shift from singular [ø] (veut) to 1st person plural [u] (voulons) and 3rd person plural open [œ] (veulent)."
            },
            {
                "id": "fr_s7_c6",
                "type": "modal",
                "glyph": "vous pouvez / ils peuvent",
                "phonetic": "[vu pu.ve] • [il pœv]",
                "gloss": "you can (formal/plural) / they can",
                "speakText": "vous pouvez, ils peuvent",
                "audioUrl": "",
                "whisper": "Essential for polite requests: 'Pouvez-vous m'aider ?' (Can you help me?). Notice the silent '-ent' in 'ils peuvent'."
            },
            {
                "id": "fr_s7_c7",
                "type": "modal",
                "glyph": "on ne peut pas",
                "phonetic": "[ɔ̃ nə pø pa]",
                "gloss": "one cannot / it is not allowed",
                "speakText": "on ne peut pas",
                "audioUrl": "",
                "whisper": "The universal French phrase for rules and prohibitions: 'On ne peut pas stationner ici' (Parking is forbidden here)."
            },
            {
                "id": "fr_s7_c8",
                "type": "modal",
                "glyph": "je voudrais",
                "phonetic": "[ʒə vu.dʁɛ]",
                "gloss": "I would like (polite conditional)",
                "speakText": "je voudrais",
                "audioUrl": "",
                "whisper": "The conditional of 'vouloir', vastly more polite in bakeries and cafés than blunt 'je veux'!"
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the French modal statement. What does the speaker desire?",
                "speakAudio": "Je veux apprendre le français",
                "options": [
                    "I want to learn French (Je veux apprendre)",
                    "I must speak French (Je dois parler)",
                    "I can read French (Je peux lire)"
                ],
                "correct": 0,
                "explain": "'Je veux' is the 1st person singular of 'vouloir' (to want)."
            },
            {
                "prompt": "Listen to the polite order in a café. What verb form is chosen?",
                "speakAudio": "Je voudrais un café s'il vous plaît",
                "options": [
                    "Je voudrais (polite conditional 'I would like')",
                    "Je veux (blunt present 'I want')",
                    "Il faut (impersonal 'it is needed')"
                ],
                "correct": 0,
                "explain": "'Je voudrais' is the polite conditional form of 'vouloir'."
            },
            {
                "prompt": "Listen to the impersonal obligation. What is being said?",
                "speakAudio": "Il faut partir maintenant",
                "options": [
                    "We must leave now / It is necessary to leave (Il faut partir)",
                    "We can leave tomorrow (On peut partir)",
                    "They want to leave (Ils veulent partir)"
                ],
                "correct": 0,
                "explain": "'Il faut' expresses general necessity followed directly by infinitive 'partir'."
            },
            {
                "prompt": "Listen to the prohibition. What is stated?",
                "speakAudio": "On ne peut pas fumer ici",
                "options": [
                    "One cannot smoke here / Smoking not allowed",
                    "One must smoke outside",
                    "We want to smoke here"
                ],
                "correct": 0,
                "explain": "'On ne peut pas' + infinitive indicates that the action is not permitted."
            }
        ],
        "arena": [
            {
                "quest": "Polite Request",
                "clue": "Assemble: 'I would like to understand' (I-would-like + to-understand)",
                "target": "Je voudrais comprendre",
                "tokens": ["Je", "voudrais", "comprendre", "peux", "dois", "nous"],
                "explain": "'Je voudrais' (conditional of politeness) connects directly with infinitive 'comprendre'."
            },
            {
                "quest": "Asking Permission",
                "clue": "Assemble: 'Can we enter?' (Can + one + enter)",
                "target": "Peut on entrer",
                "tokens": ["Peut", "on", "entrer", "veut", "doit", "pas"],
                "explain": "Inversion of modal verb 'peut' with subject pronoun 'on' followed by infinitive 'entrer'."
            },
            {
                "quest": "Expressing Necessity",
                "clue": "Assemble: 'It is necessary to work' (impersonal must + to-work)",
                "target": "Il faut travailler",
                "tokens": ["Il", "faut", "travailler", "doit", "veux", "bien"],
                "explain": "'Il faut' + infinitive 'travailler' expresses obligation for everyone."
            },
            {
                "quest": "Personal Duty",
                "clue": "Assemble: 'We must leave' (We + must + to-leave)",
                "target": "Nous devons partir",
                "tokens": ["Nous", "devons", "partir", "voulons", "pouvez", "ici"],
                "explain": "'Nous devons' is the 1st person plural of 'devoir', followed by the infinitive 'partir'."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the infinitive 'to want / to wish':",
                "tiles": ["V", "O", "U", "L", "O", "I", "R", "E"],
                "answer": "VOULOIR",
                "gloss": "vouloir (to want)"
            },
            {
                "clue": "Spell the infinitive 'to be able / can':",
                "tiles": ["P", "O", "U", "V", "O", "I", "R", "D"],
                "answer": "POUVOIR",
                "gloss": "pouvoir (to be able / can)"
            },
            {
                "clue": "Spell the 3rd person singular present of 'devoir' (he/she must):",
                "tiles": ["D", "O", "I", "T", "S", "E"],
                "answer": "DOIT",
                "gloss": "doit (must / has to)"
            }
        ],
        "quiz": [
            {
                "q": "Why is 'Je voudrais' preferred over 'Je veux' when ordering food or asking for assistance in French?",
                "options": [
                    "'Je voudrais' is the conditional of politeness ('I would like'), whereas 'Je veux' sounds demanding and abrupt!",
                    "'Je veux' is grammatically incorrect in France",
                    "'Je voudrais' is only used in the morning"
                ],
                "correct": 0,
                "explain": "'Je voudrais' softens the request into polite courtesy, standard in French daily etiquette."
            },
            {
                "q": "How is the impersonal verb 'falloir' unique among French modal verbs?",
                "options": [
                    "It can only be conjugated in the 3rd person singular: 'il faut'!",
                    "It requires two infinitives simultaneously",
                    "It can never be negated"
                ],
                "correct": 0,
                "explain": "'Falloir' is a defective impersonal verb with only one subject form: 'il faut' (present) or 'il fallait' / 'il faudra'."
            },
            {
                "q": "What preposition connects modal verbs (vouloir, pouvoir, devoir) to their following infinitives?",
                "options": [
                    "No preposition at all — they govern the bare infinitive directly!",
                    "Always 'de' (e.g. vouloir de faire)",
                    "Always 'à' (e.g. pouvoir à parler)"
                ],
                "correct": 0,
                "explain": "Unlike English ('want TO go'), French modal verbs take a direct bare infinitive: 'Je veux aller', 'Je peux voir', 'Je dois partir'."
            },
            {
                "q": "What does 'Nous ne pouvons pas accepter' mean?",
                "options": [
                    "We cannot accept",
                    "We do not want to accept",
                    "We must accept"
                ],
                "correct": 0,
                "explain": "'Nous ne pouvons pas' is the negative of 'pouvoir' (we cannot) + 'accepter' (to accept)."
            },
            {
                "q": "Which form completes the sentence: 'Ils _______ (devoir) réviser pour l'examen'?",
                "options": [
                    "doivent",
                    "devent",
                    "dois"
                ],
                "correct": 0,
                "explain": "The 3rd person plural of 'devoir' is 'ils/elles doivent' [dwav]."
            }
        ]
    },
    "latin": {
        "sealName": "SPQR Voluntas Seal",
        "guide": {
            "name": "Marcus",
            "role": "Forum Romanum Pontifex & Orator",
            "avatar": "🏛️",
            "prompt": "Salvē! In Classical Latin, modal verbs like 'volō' (to wish), 'possum' (to be able), 'dēbeō' (to owe/ought), and impersonal 'licet' (it is lawful) control complementary infinitives that govern Roman thought and law."
        },
        "cards": [
            {
                "id": "lat_s7_c1",
                "type": "modal",
                "glyph": "volō (velle)",
                "phonetic": "[ˈwɔ.loː] • [ˈwɛl.lɛ]",
                "gloss": "I want / to want (irregular)",
                "speakText": "volo, vis, vult, volumus, vultis, volunt",
                "audioUrl": "",
                "whisper": "Irregular conjugation: volō, vīs, vult, volumus, vultis, volunt. Takes a complementary infinitive: 'Legere volō' (I want to read)."
            },
            {
                "id": "lat_s7_c2",
                "type": "modal",
                "glyph": "nōlō (nōlle)",
                "phonetic": "[ˈnoː.loː] • [ˈnoːl.lɛ]",
                "gloss": "I am unwilling / I refuse",
                "speakText": "nolo, non vis, non vult",
                "audioUrl": "",
                "whisper": "Contraction of 'ne' + 'volō'. Crucial for polite negative imperatives: 'Nōlī timēre!' (Do not fear! / literally: 'Be unwilling to fear!')."
            },
            {
                "id": "lat_s7_c3",
                "type": "modal",
                "glyph": "possum (posse)",
                "phonetic": "[ˈpɔs.sʊm] • [ˈpɔs.sɛ]",
                "gloss": "I am able / can (possum, potes, potest)",
                "speakText": "possum, potes, potest, possumus, potestis, possunt",
                "audioUrl": "",
                "whisper": "Formed from 'potis' (able) + 'sum' (I am). Before 's', 'pot-' assimilates to 'pos-' ('possum', 'possumus'); before vowels, it stays 'pot-' ('potes', 'potest')."
            },
            {
                "id": "lat_s7_c4",
                "type": "modal",
                "glyph": "dēbeō (dēbēre)",
                "phonetic": "[ˈdeː.bɛ.oː] • [deː.ˈbeː.rɛ]",
                "gloss": "I ought / must / owe",
                "speakText": "debeo, debes, debet, debemus",
                "audioUrl": "",
                "whisper": "Etymologically from 'dē' + 'habeō' (to have from someone / to owe). Followed by infinitive: 'Veritātem dīcere dēbēs' (You ought to speak the truth)."
            },
            {
                "id": "lat_s7_c5",
                "type": "modal",
                "glyph": "licet (impersonal)",
                "phonetic": "[ˈlɪ.kɛt]",
                "gloss": "it is permitted / one may",
                "speakText": "licet, mihi licet",
                "audioUrl": "",
                "whisper": "Impersonal verb taking a dative of the person and complementary infinitive: 'Mihi licet' (I am allowed / It is permitted to me)."
            },
            {
                "id": "lat_s7_c6",
                "type": "modal",
                "glyph": "oportet (impersonal)",
                "phonetic": "[ɔ.ˈpɔr.tɛt]",
                "gloss": "it is necessary / proper / one ought",
                "speakText": "oportet, me oportet",
                "audioUrl": "",
                "whisper": "Impersonal modal denoting moral necessity. Takes an accusative subject of the infinitive: 'Mē oportet īre' (I ought to go / It behoves me to go)."
            },
            {
                "id": "lat_s7_c7",
                "type": "modal",
                "glyph": "vult / volunt",
                "phonetic": "[wʊlt] • [ˈwɔ.lʊnt]",
                "gloss": "he/she wants / they want",
                "speakText": "vult, volunt",
                "audioUrl": "",
                "whisper": "Third-person forms of 'velle'. Notice: 'vult' (singular: he wants), 'volunt' (plural: they want)."
            },
            {
                "id": "lat_s7_c8",
                "type": "modal",
                "glyph": "potest / possunt",
                "phonetic": "[ˈpɔ.tɛst] • [ˈpɔs.sʊnt]",
                "gloss": "he/she is able / they are able",
                "speakText": "potest, possunt",
                "audioUrl": "",
                "whisper": "Third-person singular and plural of 'possum'. 'Nēmō omnia scīre potest' (No one can know everything)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the famous Roman proverb. What does it claim no one can do?",
                "speakAudio": "Nemo omnia scire potest",
                "options": [
                    "No one can know everything (Nemo omnia scire potest)",
                    "Everyone must learn everything",
                    "No one wants to speak the truth"
                ],
                "correct": 0,
                "explain": "'Nēmō' (no one) + 'omnia' (all things) + 'scīre' (to know) + 'potest' (is able/can)."
            },
            {
                "prompt": "Listen to the imperative prohibition. How does Latin say 'Do not fear'?",
                "speakAudio": "Noli timere",
                "options": [
                    "Do not fear! (Noli timere — literally 'Be unwilling to fear!')",
                    "You cannot fear",
                    "You must fear"
                ],
                "correct": 0,
                "explain": "Latin expresses negative commands using 'Nōlī' (singular) or 'Nōlīte' (plural) + infinitive."
            },
            {
                "prompt": "Listen to the legal permission. Who is permitted to speak?",
                "speakAudio": "Tibi loqui licet",
                "options": [
                    "You are permitted to speak (Tibi loqui licet)",
                    "I must speak now",
                    "They wish to remain silent"
                ],
                "correct": 0,
                "explain": "'Licet' takes dative 'tibi' (to you) + infinitive 'loquī' (to speak)."
            },
            {
                "prompt": "Listen to the moral obligation. What ought we to do?",
                "speakAudio": "Veritatem dicere debemus",
                "options": [
                    "We ought to speak the truth (Veritatem dicere debemus)",
                    "We can see the truth",
                    "They want to hide the truth"
                ],
                "correct": 0,
                "explain": "'Dēbēmus' (we ought/must) + 'veritātem' (truth, accusative) + 'dīcere' (to speak)."
            }
        ],
        "arena": [
            {
                "quest": "Roman Determination",
                "clue": "Assemble: 'I want to speak' (to-speak + I-want)",
                "target": "Dicere volo",
                "tokens": ["Dicere", "volo", "vis", "potest", "audire", "non"],
                "explain": "Complementary infinitive 'dīcere' (to speak) combined with irregular 1st person 'volō' (I want)."
            },
            {
                "quest": "Expressing Capability",
                "clue": "Assemble: 'We can win' (to-conquer + we-can)",
                "target": "Vincere possumus",
                "tokens": ["Vincere", "possumus", "possum", "debent", "pugnare", "licet"],
                "explain": "Infinitive 'vincere' (to conquer/win) with 1st person plural 'possumus' (we are able)."
            },
            {
                "quest": "Negative Command",
                "clue": "Assemble: 'Do not fear!' (be-unwilling + to-fear)",
                "target": "Noli timere",
                "tokens": ["Noli", "timere", "volo", "debes", "videre", "semper"],
                "explain": "'Nōlī' (imperative of nōlle) + bare infinitive 'timēre' forms standard Latin negative imperative."
            },
            {
                "quest": "Permission Granted",
                "clue": "Assemble: 'It is permitted to enter' (it-is-permitted + to-enter)",
                "target": "Intrare licet",
                "tokens": ["Intrare", "licet", "oportet", "volumus", "nolo", "hic"],
                "explain": "Impersonal 'licet' (it is permitted) governing infinitive 'intrāre' (to enter)."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the 1st person modal 'I want / I wish':",
                "tiles": ["V", "O", "L", "O", "U", "S"],
                "answer": "VOLO",
                "gloss": "volō (I want)"
            },
            {
                "clue": "Spell the irregular verb 'I can / I am able':",
                "tiles": ["P", "O", "S", "S", "U", "M", "T"],
                "answer": "POSSUM",
                "gloss": "possum (I am able / can)"
            },
            {
                "clue": "Spell the impersonal modal for 'it is permitted / lawful':",
                "tiles": ["L", "I", "C", "E", "T", "O", "R"],
                "answer": "LICET",
                "gloss": "licet (it is permitted)"
            }
        ],
        "quiz": [
            {
                "q": "How is 'possum' formed etymologically from 'sum' (I am)?",
                "options": [
                    "From the adjective 'potis' (able) + 'sum' (I am), assimilating 't' to 's' before 's'!",
                    "From 'post' + 'sum'",
                    "From 'pono' + 'sum'"
                ],
                "correct": 0,
                "explain": "'Potis' + 'sum' -> 'possum'; 'potis' + 'es' -> 'potes'; 'potis' + 'est' -> 'potest'."
            },
            {
                "q": "How does Classical Latin formulate a standard polite negative command ('Don't do that!')?",
                "options": [
                    "Using 'nōlī' / 'nōlīte' + infinitive (e.g. 'Nōlī timēre' = Do not fear!)",
                    "Using 'nōn' + present imperative ('Nōn timē')",
                    "Using 'vetō' + accusative noun only"
                ],
                "correct": 0,
                "explain": "Classical Latin avoids 'nōn' + imperative; it regularly employs 'nōlī' (be unwilling) + complementary infinitive."
            },
            {
                "q": "What grammatical case does the impersonal modal 'licet' take for the person permitted to act?",
                "options": [
                    "Dative case (e.g. 'Mihi licet' = It is permitted to me)",
                    "Accusative case only",
                    "Ablative case only"
                ],
                "correct": 0,
                "explain": "'Licet' takes a dative of reference ('mihi licet', 'tibi licet') with an infinitive."
            },
            {
                "q": "What is the 2nd person singular form of 'velle' (You want)?",
                "options": [
                    "vīs",
                    "volis",
                    "vult"
                ],
                "correct": 0,
                "explain": "The present tense of 'velle' is: volō, vīs, vult, volumus, vultis, volunt."
            },
            {
                "q": "What is the meaning of the Latin phrase 'dēbeō tibi grātiās'?",
                "options": [
                    "I owe you thanks / I thank you",
                    "I want to see your grace",
                    "You must give me gifts"
                ],
                "correct": 0,
                "explain": "'Dēbeō' fundamentally means 'to owe' (hence 'debt'); 'dēbeō tibi grātiās' means 'I owe you thanks'."
            }
        ]
    },
    "hebrew": {
        "sealName": "Kavanah Silver Seal",
        "guide": {
            "name": "Eli",
            "role": "Jerusalem Scholar & Polyglot",
            "avatar": "📜",
            "prompt": "Shalom! Modal verbs in Hebrew reflect gender and number just like adjectives or present participles: 'rotsé' (m) / 'rotsáh' (f), 'yachól' (m) / 'yecholáh' (f), 'tsarích' (m) / 'tsricháh' (f). Meanwhile, impersonal modals like 'efshár' (possible) and 'asúr' (forbidden) stay uninflected!"
        },
        "cards": [
            {
                "id": "heb_s7_c1",
                "type": "modal",
                "glyph": "רוֹצֶה / רוֹצָה (rotsé / rotsáh)",
                "phonetic": "[ʁoˈtse] (m) • [ʁoˈtsa] (f)",
                "gloss": "want (rotsé m.sg / rotsáh f.sg)",
                "speakText": "רוצה",
                "audioUrl": "",
                "whisper": "Root ר-צ-ה (R-Ts-H). In the present tense, it conjugates by gender/number: 'aní rotsé' (m) / 'aní rotsáh' (f), followed by infinitive with לְ- prefix ('ani rotsé lilmód' = I want to learn)."
            },
            {
                "id": "heb_s7_c2",
                "type": "modal",
                "glyph": "יָכוֹל / יְכוֹלָה (yachól / yecholáh)",
                "phonetic": "[jaˈχol] (m) • [jeχoˈla] (f)",
                "gloss": "can / able to (yachól m / yecholáh f)",
                "speakText": "יכול",
                "audioUrl": "",
                "whisper": "Root י-כ-ל (Y-K-L). 'Atá yachól' (you can, m), 'At yecholáh' (you can, f), 'anách nu yecholím' (we can, m.pl)."
            },
            {
                "id": "heb_s7_c3",
                "type": "modal",
                "glyph": "צָרִיךְ / צְרִיכָה (tsarích / tsricháh)",
                "phonetic": "[tsaˈʁiχ] (m) • [tsʁiˈχa] (f)",
                "gloss": "need / must (tsarích m / tsricháh f)",
                "speakText": "צריך",
                "audioUrl": "",
                "whisper": "Root צ-ר-ך (Ts-R-K). Expresses obligation and personal need: 'Aní tsarích la-léchet' (I need to go, male speaker) / 'Aní tsricháh' (female speaker)."
            },
            {
                "id": "heb_s7_c4",
                "type": "modal",
                "glyph": "אֶפְשָׁר (efshár)",
                "phonetic": "[ʔefˈʃaʁ]",
                "gloss": "possible / one may / can one?",
                "speakText": "אפשר",
                "audioUrl": "",
                "whisper": "Impersonal modal adverb. Invaluable for polite inquiries: 'Efshár le-kabbél...?' (Is it possible to receive... / May I have...?). Never inflects for gender!"
            },
            {
                "id": "heb_s7_c5",
                "type": "modal",
                "glyph": "אָסוּר (asúr)",
                "phonetic": "[ʔaˈsuʁ]",
                "gloss": "forbidden / not allowed / prohibited",
                "speakText": "אסור",
                "audioUrl": "",
                "whisper": "Passive participle of א-ס-ר (to bind/prohibit). 'Asúr le-ashen' (Smoking is forbidden); 'asúr le-hikanés' (No entry)."
            },
            {
                "id": "heb_s7_c6",
                "type": "modal",
                "glyph": "חַיָּב / חַיֶּבֶת (chayáv / chayévet)",
                "phonetic": "[χaˈjav] (m) • [χaˈjevet] (f)",
                "gloss": "must / obligated / strictly required",
                "speakText": "חייב",
                "audioUrl": "",
                "whisper": "Expresses a non-negotiable legal or absolute duty (root ח-ו-ב): 'Aní chayáv la-dá'at' (I absolutely must know)."
            },
            {
                "id": "heb_s7_c7",
                "type": "modal",
                "glyph": "כְּדַאי (kedáy)",
                "phonetic": "[keˈdaj]",
                "gloss": "advisable / recommended / it's good to",
                "speakText": "כדאי",
                "audioUrl": "",
                "whisper": "Impersonal recommendation: 'Kedáy lecha' (You should / It's advisable for you) + infinitive: 'Kedáy la-vó' (It's worth coming)."
            },
            {
                "id": "heb_s7_c8",
                "type": "modal",
                "glyph": "רוֹצִים / רוֹצוֹת (rotsím / rotsót)",
                "phonetic": "[ʁoˈtsim] (m.pl) • [ʁoˈtsot] (f.pl)",
                "gloss": "want (plural: rotsím m.pl / rotsót f.pl)",
                "speakText": "רוצים",
                "audioUrl": "",
                "whisper": "Standard plural endings: '-im' for masculine/mixed groups, '-ot' for all-female groups ('anách nu rotsím lilmód' = we want to learn)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the speaker's request. What does he want to do?",
                "speakAudio": "אני רוצה ללמוד עברית",
                "options": [
                    "I want to learn Hebrew (Aní rotsé lilmód ivrít)",
                    "I can speak Hebrew (Aní yachól le-dabér ivrít)",
                    "I must write Hebrew (Aní tsarích lich-tóv ivrít)"
                ],
                "correct": 0,
                "explain": "'Aní rotsé' (I want, m) + infinitive 'lilmód' (to study/learn) + 'ivrít' (Hebrew)."
            },
            {
                "prompt": "Listen to the polite marketplace question. What is Eli asking?",
                "speakAudio": "אפשר לקבל מים בבקשה",
                "options": [
                    "May I have water please? (Efshár le-kabbél máyim bevakasháh?)",
                    "Do you want to drink tea?",
                    "Is it forbidden to drink water here?"
                ],
                "correct": 0,
                "explain": "'Efshár' (is it possible / may one) + 'le-kabbél' (to receive) + 'máyim' (water) + 'bevakasháh' (please)."
            },
            {
                "prompt": "Listen to the sign at the entrance. What is prohibited?",
                "speakAudio": "אסור להיכנס לכאן",
                "options": [
                    "Forbidden to enter here / No entry (Asúr le-hikanés le-chán)",
                    "You may enter here",
                    "We need to leave here"
                ],
                "correct": 0,
                "explain": "'Asúr' (forbidden) + infinitive 'le-hikanés' (to enter) + 'le-chán' (to here)."
            },
            {
                "prompt": "Listen to the female speaker. What does she need to do?",
                "speakAudio": "אני צריכה ללכת",
                "options": [
                    "I need to go (Aní tsricháh la-léchet)",
                    "I can wait here",
                    "I want to stay"
                ],
                "correct": 0,
                "explain": "'Tsricháh' is the feminine singular form of 'tsarích' (need/must) + 'la-léchet' (to go)."
            }
        ],
        "arena": [
            {
                "quest": "Male Speaker Desire",
                "clue": "Assemble: 'I want to learn' (I + want.m + to-learn)",
                "target": "אני רוצה ללמוד",
                "tokens": ["אני", "רוצה", "ללמוד", "יכול", "צריך", "הם"],
                "explain": "'Aní' (I) + 'rotsé' (want, masc. sg.) + 'lilmód' (to learn, prefixed with לְ-)."
            },
            {
                "quest": "Polite Request",
                "clue": "Assemble: 'Is it possible to help?' (possible + to-help)",
                "target": "אפשר לעזור",
                "tokens": ["אפשר", "לעזור", "אסור", "צריך", "כדאי", "אני"],
                "explain": "'Efshár' (possible / one can) + infinitive 'la'azór' (to help)."
            },
            {
                "quest": "Physical Capability",
                "clue": "Assemble: 'You can speak' (You.m + can.m + to-speak)",
                "target": "אתה יכול לדבר",
                "tokens": ["אתה", "יכול", "לדבר", "רוצה", "אסור", "היא"],
                "explain": "'Atá' (you, m) + 'yachól' (can, m) + 'le-dabér' (to speak)."
            },
            {
                "quest": "Public Prohibition",
                "clue": "Assemble: 'It is forbidden to enter' (forbidden + to-enter)",
                "target": "אסור להיכנס",
                "tokens": ["אסור", "להיכנס", "אפשר", "כדאי", "צריך", "שלום"],
                "explain": "'Asúr' (forbidden) + binyan Nif'al infinitive 'le-hikanés' (to enter)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the present modal 'want' (masculine singular - rotsé):",
                "tiles": ["ר", "ו", "צ", "ה", "י", "ם"],
                "answer": "רוצה",
                "gloss": "רוֹצֶה (want - m.sg)"
            },
            {
                "clue": "Assemble the impersonal modal 'possible / may one' (efshár):",
                "tiles": ["א", "פ", "ש", "ר", "ו", "ת"],
                "answer": "אפשר",
                "gloss": "אֶפְשָׁר (possible / may one)"
            },
            {
                "clue": "Assemble the word for 'forbidden / prohibited' (asúr):",
                "tiles": ["א", "ס", "ו", "ר", "ל", "ד"],
                "answer": "אסור",
                "gloss": "אָסוּר (forbidden)"
            }
        ],
        "quiz": [
            {
                "q": "Why do Hebrew modal verbs like 'rotsé' (רוֹצֶה) and 'tsarích' (צָרִיךְ) change form depending on whether a man or woman is speaking?",
                "options": [
                    "In the present tense, Hebrew verbs function as participles/adjectives and must agree in gender and number with the subject!",
                    "Only past tense verbs agree in gender",
                    "It is optional slang in modern Israel"
                ],
                "correct": 0,
                "explain": "Hebrew present tense stems (benoni) are nominal forms that decline for gender and number: rotsé (m), rotsáh (f), rotsím (m.pl), rotsót (f.pl)."
            },
            {
                "q": "What letter prefix is attached to the verb that follows modals like 'rotsé', 'yachól', or 'efshár'?",
                "options": [
                    "The prefix לְ- (Lamed), which forms the Hebrew infinitive construct (shem po'al)!",
                    "The prefix בְּ- (Bet)",
                    "The prefix הַ- (Heh)"
                ],
                "correct": 0,
                "explain": "Hebrew infinitives always start with the prefix Lamed (לְ-): lilmód (to learn), ledabér (to speak), la'asót (to do)."
            },
            {
                "q": "How do 'efshár' (אֶפְשָׁר) and 'asúr' (אָסוּר) differ from 'tsarích' (צָרִיךְ) when indicating rules?",
                "options": [
                    "'Efshár' and 'asúr' are impersonal predicates that do not conjugate for the speaker's gender!",
                    "They can only refer to children",
                    "They cannot be followed by an infinitive"
                ],
                "correct": 0,
                "explain": "'Efshár' and 'asúr' are impersonal statements of possibility and prohibition; they remain invariant regardless of who is speaking."
            },
            {
                "q": "How would a woman say 'I can speak Hebrew'?",
                "options": [
                    "אני יכולה לדבר עברית (Aní yecholáh le-dabér ivrít)",
                    "אני יכול לדבר עברית (Aní yachól le-dabér ivrít)",
                    "אני אפשר לדבר עברית (Aní efshár le-dabér ivrít)"
                ],
                "correct": 0,
                "explain": "A female speaker uses the feminine singular participle 'yecholáh' (יְכוֹלָה)."
            },
            {
                "q": "What does the modal word 'kedáy' (כְּדַאי) convey in everyday conversation?",
                "options": [
                    "Friendly advice or recommendation ('it is advisable / you should / it's worthwhile')",
                    "Strict military obligation",
                    "Total legal prohibition"
                ],
                "correct": 0,
                "explain": "'Kedáy' conveys advisability ('it's worth it', 'you should'): e.g., 'kedáy lecha lilmód' (it's worthwhile for you to study)."
            }
        ]
    },
    "chinese": {
        "sealName": "Jade Intention Seal",
        "guide": {
            "name": "Master Lao",
            "role": "Sanctuary Grammatist & Tea Master",
            "avatar": "🏮",
            "prompt": "Nǐ hǎo! In Mandarin Chinese, auxiliary modal verbs (能愿动词 néngyuàn dòngcí) precede the main verb without any conjugations or inflections. Distinguish clearly between physical capability (能 néng), learned skill (会 huì), permission (可以 kěyǐ), internal desire (想 xiǎng), and necessity (要 yào / 必须 bìxū)!"
        },
        "cards": [
            {
                "id": "zh_s7_c1",
                "type": "modal",
                "glyph": "想 (xiǎng)",
                "phonetic": "[ɕjɑŋ˨˩˦] (3rd tone)",
                "gloss": "to want to / would like to",
                "speakText": "想",
                "audioUrl": "",
                "whisper": "Expresses mental desire, aspiration, or 'would like to': 'Wǒ xiǎng xué Zhōngwén' (I would like to learn Chinese). Gentler than '要' (yào)."
            },
            {
                "id": "zh_s7_c2",
                "type": "modal",
                "glyph": "要 (yào)",
                "phonetic": "[jɑʊ̯˥˩] (4th tone)",
                "gloss": "to want / need / will / must",
                "speakText": "要",
                "audioUrl": "",
                "whisper": "Expresses strong desire, need, or future intention: 'Wǒ yào hē chá' (I want / must drink tea). In negation, 'bù xiǎng' means don't want, while 'bù yào' means 'don't!' (prohibition)."
            },
            {
                "id": "zh_s7_c3",
                "type": "modal",
                "glyph": "能 (néng)",
                "phonetic": "[nɤŋ˧˥] (2nd tone)",
                "gloss": "can / physically able to",
                "speakText": "能",
                "audioUrl": "",
                "whisper": "Expresses physical capability or circumstances permitting: 'Wǒ jīntiān néng lái' (I am able to come today). Contrasts with learned skill '会' (huì)."
            },
            {
                "id": "zh_s7_c4",
                "type": "modal",
                "glyph": "会 (huì)",
                "phonetic": "[xweɪ̯˥˩] (4th tone)",
                "gloss": "can / know how to (learned skill)",
                "speakText": "会",
                "audioUrl": "",
                "whisper": "Acquired skill through learning: 'Wǒ huì shuō Zhōngwén' (I know how to speak Chinese / I can speak Chinese). Also marks future probability ('tā huì lái' = he will come)."
            },
            {
                "id": "zh_s7_c5",
                "type": "modal",
                "glyph": "可以 (kěyǐ)",
                "phonetic": "[kʰɤ˨˩.i˨˩˦] (3rd+3rd -> 2nd+3rd)",
                "gloss": "can / may / permitted",
                "speakText": "可以",
                "audioUrl": "",
                "whisper": "Expresses permission or suitability: 'Wǒ kěyǐ jìnlái ma?' (May I come in?). Third tone sandhi turns 'kě' into 2nd tone [kʰɤ˧˥]."
            },
            {
                "id": "zh_s7_c6",
                "type": "modal",
                "glyph": "必须 (bìxū)",
                "phonetic": "[pi˥˩.ɕy˥] (4th + 1st tone)",
                "gloss": "must / have to / compulsory",
                "speakText": "必须",
                "audioUrl": "",
                "whisper": "Strong categorical obligation: 'Nǐ bìxū qù' (You must go). Its negative counterpart for 'no need to' is 'bùbì' (不必) rather than 'bù bìxū'."
            },
            {
                "id": "zh_s7_c7",
                "type": "modal",
                "glyph": "应该 (yīnggāi)",
                "phonetic": "[iŋ˥.kaɪ̯˥] (1st + 1st tone)",
                "gloss": "should / ought to",
                "speakText": "应该",
                "audioUrl": "",
                "whisper": "Expresses moral obligation, advice, or reasonable expectation: 'Nǐ yīnggāi xiūxi' (You should rest)."
            },
            {
                "id": "zh_s7_c8",
                "type": "modal",
                "glyph": "不能 / 不行 (bù néng / bù xíng)",
                "phonetic": "[pu˥˩ nɤŋ˧˥] • [pu˥˩ ɕiŋ˧˥]",
                "gloss": "cannot / not allowed / won't do",
                "speakText": "不能",
                "audioUrl": "",
                "whisper": "'Bù néng' expresses inability or prohibition ('Zhèlǐ bù néng chōuyān' = No smoking here). 'Bù xíng' means 'not acceptable / no way!'"
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the learner's goal. What is desired?",
                "speakAudio": "我想学中文",
                "options": [
                    "I want to learn Chinese (Wǒ xiǎng xué Zhōngwén)",
                    "I must speak English (Wǒ bìxū shuō Yīngwén)",
                    "I can write characters (Wǒ huì xiě hànzì)"
                ],
                "correct": 0,
                "explain": "'我想' (wǒ xiǎng = I would like to) + '学' (xué = learn) + '中文' (Zhōngwén = Chinese)."
            },
            {
                "prompt": "Listen to the polite entrance question. What does the speaker ask?",
                "speakAudio": "我可以进来吗",
                "options": [
                    "May I come in? (Wǒ kěyǐ jìnlái ma?)",
                    "Can you leave now?",
                    "Do you want tea?"
                ],
                "correct": 0,
                "explain": "'我可以' (wǒ kěyǐ = may I) + '进来' (jìnlái = enter/come in) + '吗' (ma = question particle)."
            },
            {
                "prompt": "Listen to the acquired skill. What language can the speaker speak?",
                "speakAudio": "他会说德语",
                "options": [
                    "He can speak German (Tā huì shuō Déyǔ)",
                    "He wants to learn French",
                    "He must study Latin"
                ],
                "correct": 0,
                "explain": "'会' (huì) denotes learned ability; '说德语' (shuō Déyǔ) means speak German."
            },
            {
                "prompt": "Listen to the elder's caring advice. What should the listener do?",
                "speakAudio": "你应该多喝水",
                "options": [
                    "You should drink more water (Nǐ yīnggāi duō hē shuǐ)",
                    "You cannot drink cold water",
                    "You must drink hot tea"
                ],
                "correct": 0,
                "explain": "'应该' (yīnggāi = should) + '多喝水' (duō hē shuǐ = drink more water)."
            }
        ],
        "arena": [
            {
                "quest": "Polite Entrance Request",
                "clue": "Assemble: 'May I come in?' (I + may + enter + question-particle)",
                "target": "我可以进来吗",
                "tokens": ["我", "可以", "进来", "吗", "想", "必须"],
                "explain": "'我' (I) + '可以' (kěyǐ = may) + '进来' (jìnlái = come in) + '吗' (ma = yes/no question particle)."
            },
            {
                "quest": "Stating Learned Skill",
                "clue": "Assemble: 'I can speak Chinese' (I + know-how-to + speak + Chinese)",
                "target": "我会说中文",
                "tokens": ["我", "会", "说", "中文", "要", "能"],
                "explain": "'会' (huì) marks acquired skill through study: '我会说中文' (I can speak Chinese)."
            },
            {
                "quest": "Giving Wise Advice",
                "clue": "Assemble: 'You should rest' (You + should + rest)",
                "target": "你应该休息",
                "tokens": ["你", "应该", "休息", "想", "不能", "我们"],
                "explain": "'你' (you) + '应该' (yīnggāi = should) + verb '休息' (xiūxi = rest)."
            },
            {
                "quest": "Categorical Duty",
                "clue": "Assemble: 'We must go' (We + must + go)",
                "target": "我们必须去",
                "tokens": ["我们", "必须", "去", "可以", "会", "来"],
                "explain": "'我们' (we) + '必须' (bìxū = must) + '去' (qù = go)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the character for 'want to / think' (xiǎng - with 心 heart radical):",
                "tiles": ["想", "相", "心", "要"],
                "answer": "想",
                "gloss": "想 (xiǎng - want to / would like)"
            },
            {
                "clue": "Assemble the modal compound for 'may / can' (kěyǐ):",
                "tiles": ["可", "以", "已", "能"],
                "answer": "可以",
                "gloss": "可以 (kěyǐ - can / may)"
            },
            {
                "clue": "Assemble the modal compound for 'should / ought to' (yīnggāi):",
                "tiles": ["应", "该", "刻", "当"],
                "answer": "应该",
                "gloss": "应该 (yīnggāi - should / ought to)"
            }
        ],
        "quiz": [
            {
                "q": "What is the crucial semantic distinction between '会' (huì) and '能' (néng) in Chinese?",
                "options": [
                    "'会' signifies an acquired skill learned through practice, while '能' denotes physical capability or circumstances permitting!",
                    "'会' is only used for children",
                    "'能' can only be used in questions"
                ],
                "correct": 0,
                "explain": "'我会游泳' means 'I know how to swim (learned skill)', whereas '我今天能游泳' means 'I am able/healthy enough to swim today'."
            },
            {
                "q": "How does the tone change when saying '可以' (kěyǐ) aloud?",
                "options": [
                    "Due to 3rd-tone sandhi, the first character '可' (kě) changes to a 2nd tone [kʰɤ˧˥]!",
                    "Both become 4th tone",
                    "The second character becomes neutral"
                ],
                "correct": 0,
                "explain": "When two 3rd-tone syllables meet (kě + yǐ), the first shifts to 2nd tone: kéyǐ."
            },
            {
                "q": "What does '不要' (bù yào) mean when addressing someone directly?",
                "options": [
                    "A strong prohibition: 'Don't!' / 'Do not do that!'",
                    "A gentle wish: 'I wouldn't prefer'",
                    "A question: 'Do you want?'"
                ],
                "correct": 0,
                "explain": "While 'bù xiǎng' means 'don't feel like / don't want to', 'bù yào' functions as 'Don't!' (imperative prohibition)."
            },
            {
                "q": "Where do modal verbs like 想, 能, 可以 sit in a standard Mandarin Chinese clause?",
                "options": [
                    "Immediately before the main verb (Subject + Modal + Verb + Object)!",
                    "At the very end of the sentence",
                    "After the direct object"
                ],
                "correct": 0,
                "explain": "Auxiliary modal verbs in Chinese precede the main verb phrase: 我 (S) + 想 (Modal) + 学 (V) + 中文 (O)."
            },
            {
                "q": "What is the natural negative response to '必须' (must) when indicating 'you don't have to'?",
                "options": [
                    "不必 (bùbì) or 不用 (bùyòng) — meaning 'no need to'",
                    "不必须 (bù bìxū)",
                    "无想 (wú xiǎng)"
                ],
                "correct": 0,
                "explain": "Chinese uses '不必' (bùbì) or '不用' (bùyòng) to express 'need not / do not have to', as '不必须' is unidiomatic."
            }
        ]
    },
    "german": {
        "sealName": "Kaiserwald Willenskraft Seal",
        "guide": {
            "name": "Bäcker Hans",
            "role": "Berlin Master Baker & Linguist",
            "avatar": "🥨",
            "prompt": "Guten Tag! German modal verbs—können, müssen, wollen, dürfen, sollen, and möchten—are the engine of Germanic syntax! Watch the famous 'Satzklammer' (Sentence Bracket): the modal takes 2nd position, sending the dependent infinitive all the way to the very end of the clause!"
        },
        "cards": [
            {
                "id": "de_s7_c1",
                "type": "modal",
                "glyph": "können (ich kann, er kann)",
                "phonetic": "[ˈkœ.nən] • [ɪç kan] • [eːɐ̯ kan]",
                "gloss": "can / to be able to",
                "speakText": "ich kann, du kannst, er kann, wir können",
                "audioUrl": "",
                "whisper": "Notice the vowel change from umlauted 'ö' to 'a' in singular: ich kann, du kannst, er kann (NO -t ending on 3rd person singular!)."
            },
            {
                "id": "de_s7_c2",
                "type": "modal",
                "glyph": "müssen (ich muss, er muss)",
                "phonetic": "[ˈmʏ.sn̩] • [ɪç mʊs] • [eːɐ̯ mʊs]",
                "gloss": "must / to have to (necessity)",
                "speakText": "ich muss, du musst, er muss, wir müssen",
                "audioUrl": "",
                "whisper": "Expresses absolute necessity: ich muss, du musst, er muss, wir müssen. FALSE FRIEND: 'nicht müssen' means 'don't have to / need not' (NOT 'must not'!)."
            },
            {
                "id": "de_s7_c3",
                "type": "modal",
                "glyph": "dürfen (ich darf, man darf nicht)",
                "phonetic": "[ˈdʏʁ.fn̩] • [ɪç daʁf] • [man daʁf nɪçt]",
                "gloss": "may / allowed to (permission/prohibition)",
                "speakText": "ich darf, du darfst, er darf, man darf nicht",
                "audioUrl": "",
                "whisper": "Expresses permission. 'Nicht dürfen' is the true German 'must not / forbidden': 'Hier darf man nicht parken' (No parking allowed here)."
            },
            {
                "id": "de_s7_c4",
                "type": "modal",
                "glyph": "wollen (ich will, er will)",
                "phonetic": "[ˈvɔ.lən] • [ɪç vɪl] • [eːɐ̯ vɪl]",
                "gloss": "to want / intend (strong will)",
                "speakText": "ich will, du willst, er will, wir wollen",
                "audioUrl": "",
                "whisper": "Stem vowel 'i' in singular: ich will, du willst, er will, wir wollen. FALSE FRIEND: 'will' means 'wants', NEVER English future 'will'!"
            },
            {
                "id": "de_s7_c5",
                "type": "modal",
                "glyph": "möchten (ich möchte, wir möchten)",
                "phonetic": "[ˈmœç.tn̩] • [ɪç ˈmœç.tə]",
                "gloss": "would like to (polite wish)",
                "speakText": "ich möchte, du möchtest, er möchte, wir möchten",
                "audioUrl": "",
                "whisper": "Subjunctive II of 'mögen', ubiquitous in bakeries and cafés: 'Ich möchte bitte einen Kaffee' (I would like a coffee, please)."
            },
            {
                "id": "de_s7_c6",
                "type": "modal",
                "glyph": "sollen (ich soll, er soll)",
                "phonetic": "[ˈzɔ.lən] • [ɪç zɔl] • [eːɐ̯ zɔl]",
                "gloss": "should / supposed to (duty/order)",
                "speakText": "ich soll, du sollst, er soll, wir sollen",
                "audioUrl": "",
                "whisper": "Expresses third-party instructions or moral duty: 'Der Arzt sagt, ich soll schlafen' (The doctor says I should sleep)."
            },
            {
                "id": "de_s7_c7",
                "type": "modal",
                "glyph": "Satzklammer (Verb-2 ... Infinitiv-Ende)",
                "phonetic": "[ˈzatsˌklamaʁ]",
                "gloss": "Sentence Bracket (Modal at V2, Infinitive at end)",
                "speakText": "Ich kann Deutsch sprechen",
                "audioUrl": "",
                "whisper": "The golden German syntax rule: 'Ich KANN (position 2) gut Deutsch SPRECHEN (clause end)'. The infinitive brackets the entire predicate!"
            },
            {
                "id": "de_s7_c8",
                "type": "modal",
                "glyph": "wir müssen / sie können",
                "phonetic": "[viːɐ̯ ˈmʏsn̩] • [ziː ˈkœnən]",
                "gloss": "we must / they can",
                "speakText": "wir müssen, sie können",
                "audioUrl": "",
                "whisper": "Plural forms retain the infinitive umlauts (wir müssen, wir können, wir dürfen) and take standard regular endings (-en, -t, -en)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the bakery customer. What polite request is made?",
                "speakAudio": "Ich möchte ein Brot kaufen",
                "options": [
                    "I would like to buy a loaf of bread (Ich möchte ein Brot kaufen)",
                    "I must bake a loaf of bread",
                    "I can sell a loaf of bread"
                ],
                "correct": 0,
                "explain": "'Ich möchte' (I would like) + object 'ein Brot' + infinitive bracket 'kaufen' at the end."
            },
            {
                "prompt": "Listen to the strict prohibition. What is forbidden?",
                "speakAudio": "Hier darf man nicht rauchen",
                "options": [
                    "Smoking is not allowed here (Hier darf man nicht rauchen)",
                    "One must smoke here",
                    "One wants to smoke here"
                ],
                "correct": 0,
                "explain": "'Darf man nicht' expresses strict prohibition ('must not / not allowed to')."
            },
            {
                "prompt": "Listen to the capability statement. What can the speaker do?",
                "speakAudio": "Ich kann sehr gut schwimmen",
                "options": [
                    "I can swim very well (Ich kann sehr gut schwimmen)",
                    "I want to learn how to swim",
                    "I should swim today"
                ],
                "correct": 0,
                "explain": "'Ich kann' (I can) + adverb 'sehr gut' + end-infinitive 'schwimmen'."
            },
            {
                "prompt": "Listen to the urgent obligation. What must we do?",
                "speakAudio": "Wir müssen jetzt gehen",
                "options": [
                    "We must go now (Wir müssen jetzt gehen)",
                    "We want to stay now",
                    "We may leave tomorrow"
                ],
                "correct": 0,
                "explain": "'Wir müssen' (we must) + 'jetzt' (now) + 'gehen' (go/leave)."
            }
        ],
        "arena": [
            {
                "quest": "German Sentence Bracket",
                "clue": "Assemble: 'I can speak German' (I + can + German + speak.INF)",
                "target": "Ich kann Deutsch sprechen",
                "tokens": ["Ich", "kann", "Deutsch", "sprechen", "will", "muss"],
                "explain": "The modal 'kann' sits in Position 2, while the infinitive 'sprechen' is banished to the final position!"
            },
            {
                "quest": "Polite Bakery Order",
                "clue": "Assemble: 'I would like to order' (I + would-like + to-order)",
                "target": "Ich möchte bestellen",
                "tokens": ["Ich", "möchte", "bestellen", "darf", "soll", "wir"],
                "explain": "'Ich möchte' (I would like) + infinitive 'bestellen' (to order)."
            },
            {
                "quest": "Strict Prohibition",
                "clue": "Assemble: 'One is not allowed to park here' (Here + may + one + not + park)",
                "target": "Hier darf man nicht parken",
                "tokens": ["Hier", "darf", "man", "nicht", "parken", "muss", "will"],
                "explain": "Inversion after adverb 'Hier': modal 'darf' in V2, subject 'man', negative 'nicht', infinitive 'parken' at end."
            },
            {
                "quest": "Expressing Necessity",
                "clue": "Assemble: 'We must leave now' (We + must + now + leave)",
                "target": "Wir müssen jetzt gehen",
                "tokens": ["Wir", "müssen", "jetzt", "gehen", "können", "wollen"],
                "explain": "'Wir müssen' (V2 modal) + 'jetzt' (adverb) + 'gehen' (closing infinitive)."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the 1st person modal 'I can':",
                "tiles": ["K", "A", "N", "N", "O", "T"],
                "answer": "KANN",
                "gloss": "kann (can / able to)"
            },
            {
                "clue": "Spell the infinitive 'to must / have to':",
                "tiles": ["M", "Ü", "S", "S", "E", "N", "T"],
                "answer": "MÜSSEN",
                "gloss": "müssen (must / to have to)"
            },
            {
                "clue": "Spell the modal for 'may / permitted to' (1st person 'I may'):",
                "tiles": ["D", "A", "R", "F", "T", "S"],
                "answer": "DARF",
                "gloss": "darf (may / am allowed)"
            }
        ],
        "quiz": [
            {
                "q": "What is the 'Satzklammer' (Sentence Bracket) rule when using modal verbs in German main clauses?",
                "options": [
                    "The finite modal verb takes position 2, and the dependent infinitive moves to the very end of the sentence!",
                    "Both verbs stand right next to each other",
                    "The modal verb must go to the end"
                ],
                "correct": 0,
                "explain": "In German main clauses, the modal verb occupies position 2 and sends the complementary infinitive to the sentence-final position."
            },
            {
                "q": "Why is German 'ich will' a dangerous false friend for English speakers?",
                "options": [
                    "'Ich will' means 'I want / I desire', NOT the future tense 'I will'!",
                    "'Ich will' means 'I won't'",
                    "'Ich will' is past tense"
                ],
                "correct": 0,
                "explain": "German 'wollen' expresses desire ('ich will ein Eis' = I want an ice cream). Future tense is formed with 'werden' ('ich werde')."
            },
            {
                "q": "What is the crucial difference between 'du musst nicht' and 'du darfst nicht'?",
                "options": [
                    "'Du musst nicht' means 'you don't have to (optional)', while 'du darfst nicht' means 'you must not (forbidden)'!",
                    "They are exact synonyms",
                    "'Du darfst nicht' means 'you are invited to'"
                ],
                "correct": 0,
                "explain": "Negating 'müssen' removes obligation (need not), whereas negating 'dürfen' expresses absolute prohibition (must not)."
            },
            {
                "q": "What unique conjugation feature do singular modal verbs (ich, er/sie/es) share in the present tense?",
                "options": [
                    "The 1st and 3rd person singular forms are identical and have no ending (ich kann / er kann, ich muss / er muss)!",
                    "They always end in -t",
                    "They always retain their umlaut"
                ],
                "correct": 0,
                "explain": "Preterite-present verbs in Germanic have zero-ending in 1st and 3rd singular: ich will / er will; ich kann / er kann."
            },
            {
                "q": "Which form correctly fills the blank: 'Wir _______ heute leider nicht kommen'?",
                "options": [
                    "können",
                    "kann",
                    "kannst"
                ],
                "correct": 0,
                "explain": "The 1st person plural 'wir' takes the regular plural infinitive-like form 'können'."
            }
        ]
    }
}

STEP8_DATA = {
    "waray": {
        "sealName": "San Juanico Compass Seal",
        "guide": {
            "name": "Manang Elena",
            "role": "Visayan Island Navigator & Spatial Guide",
            "avatar": "🏝️",
            "prompt": "Maupay nga adlaw! In Waray-Waray, location and direction revolve around the universal locative marker 'ha', combined with spatial relational nouns and the genitive marker 'han'. Master 'ha sulod', 'ha gawas', 'ngadto ha', and 'tikang ha'!"
        },
        "cards": [
            {
                "id": "war_s8_c1",
                "type": "preposition",
                "glyph": "ha",
                "phonetic": "[ha]",
                "gloss": "in / on / at (universal locative marker)",
                "speakText": "ha",
                "audioUrl": "",
                "whisper": "The cornerstone preposition of Visayan: marks static location ('ha balay' = at/in the house, 'ha Tacloban' = in Tacloban)."
            },
            {
                "id": "war_s8_c2",
                "type": "preposition",
                "glyph": "ha sulod han",
                "phonetic": "[ha ˈsu.lod han]",
                "gloss": "inside of (locative + inside + genitive)",
                "speakText": "ha sulod han balay",
                "audioUrl": "",
                "whisper": "'Sulod' means interior/inside. Followed by specific genitive marker 'han': 'ha sulod han balay' (inside the house)."
            },
            {
                "id": "war_s8_c3",
                "type": "preposition",
                "glyph": "ha gawas han",
                "phonetic": "[ha ˈɡa.was han]",
                "gloss": "outside of",
                "speakText": "ha gawas han balay",
                "audioUrl": "",
                "whisper": "'Gawas' means outside/exterior: 'ha gawas han tindahan' (outside the store)."
            },
            {
                "id": "war_s8_c4",
                "type": "preposition",
                "glyph": "ha igbaw han",
                "phonetic": "[ha ˈʔiɡ.baw han]",
                "gloss": "on top of / above / over",
                "speakText": "ha igbaw han lamesa",
                "audioUrl": "",
                "whisper": "'Igbaw' indicates upper surface or elevation: 'ha igbaw han lamesa' (on top of the table)."
            },
            {
                "id": "war_s8_c5",
                "type": "preposition",
                "glyph": "ha ilarom han",
                "phonetic": "[ha ʔi.ˈla.ɾom han]",
                "gloss": "underneath / below / beneath",
                "speakText": "ha ilarom han lingkuran",
                "audioUrl": "",
                "whisper": "'Ilarom' designates the lower space underneath: 'ha ilarom han lingkuran' (under the chair)."
            },
            {
                "id": "war_s8_c6",
                "type": "preposition",
                "glyph": "ha atubangan han",
                "phonetic": "[ha ʔa.tu.ˈba.ŋan han]",
                "gloss": "in front of / facing",
                "speakText": "ha atubangan han simbahan",
                "audioUrl": "",
                "whisper": "Derived from 'atubang' (to face): 'ha atubangan han simbahan' (in front of the church)."
            },
            {
                "id": "war_s8_c7",
                "type": "preposition",
                "glyph": "ha luyo han",
                "phonetic": "[ha ˈlu.jɔ han]",
                "gloss": "behind / at the back of",
                "speakText": "ha luyo han balay",
                "audioUrl": "",
                "whisper": "'Luyo' denotes the back or rear: 'ha luyo han balay' (behind the house)."
            },
            {
                "id": "war_s8_c8",
                "type": "preposition",
                "glyph": "ngadto ha / tikang ha",
                "phonetic": "[ˈŋad.to ha] • [tɪ.ˈkaŋ ha]",
                "gloss": "towards / to (ngadto ha) • from (tikang ha)",
                "speakText": "ngadto ha, tikang ha",
                "audioUrl": "",
                "whisper": "'Ngadto ha' marks directional movement away toward a location; 'tikang ha' marks provenance/origin: 'tikang ha Manila' (from Manila)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the location of the cat. Where is it?",
                "speakAudio": "ha ilarom han lamesa",
                "options": [
                    "Underneath the table (ha ilarom han lamesa)",
                    "On top of the table (ha igbaw han lamesa)",
                    "Inside the house (ha sulod han balay)"
                ],
                "correct": 0,
                "explain": "'Ha ilarom han' specifically means underneath / below."
            },
            {
                "prompt": "Listen to the meeting place. Where are they gathering?",
                "speakAudio": "ha atubangan han simbahan",
                "options": [
                    "In front of the church (ha atubangan han simbahan)",
                    "Behind the church (ha luyo han simbahan)",
                    "Inside the church (ha sulod han simbahan)"
                ],
                "correct": 0,
                "explain": "'Ha atubangan han' means in front of (facing)."
            },
            {
                "prompt": "Listen to where the traveler is coming from.",
                "speakAudio": "tikang ha Tacloban",
                "options": [
                    "From Tacloban (tikang ha Tacloban)",
                    "Going towards Tacloban (ngadto ha Tacloban)",
                    "Inside Tacloban (ha sulod han Tacloban)"
                ],
                "correct": 0,
                "explain": "'Tikang ha' indicates origin/provenance ('from')."
            },
            {
                "prompt": "Listen to the location of the children. Where are they playing?",
                "speakAudio": "ha gawas han balay",
                "options": [
                    "Outside the house (ha gawas han balay)",
                    "Inside the house (ha sulod han balay)",
                    "Behind the house (ha luyo han balay)"
                ],
                "correct": 0,
                "explain": "'Ha gawas han' means outside of."
            }
        ],
        "arena": [
            {
                "quest": "Interior Spatial Description",
                "clue": "Assemble: 'Inside the house' (at + inside + of-the + house)",
                "target": "ha sulod han balay",
                "tokens": ["ha", "sulod", "han", "balay", "gawas", "tikang"],
                "explain": "'Ha' (locative) + 'sulod' (interior) + 'han' (genitive marker) + 'balay' (house)."
            },
            {
                "quest": "Exterior Placement",
                "clue": "Assemble: 'Outside the house' (at + outside + of-the + house)",
                "target": "ha gawas han balay",
                "tokens": ["ha", "gawas", "han", "balay", "ilarom", "ngadto"],
                "explain": "'Ha' + 'gawas' (exterior) + 'han' + 'balay'."
            },
            {
                "quest": "Expressing Destination",
                "clue": "Assemble: 'Towards the market' (towards + at + market)",
                "target": "ngadto ha merkado",
                "tokens": ["ngadto", "ha", "merkado", "tikang", "sulod", "luyo"],
                "explain": "'Ngadto ha' signifies directional movement towards a specific location."
            },
            {
                "quest": "Expressing Origin",
                "clue": "Assemble: 'From the island' (from + at + island)",
                "target": "tikang ha puro",
                "tokens": ["tikang", "ha", "puro", "ngadto", "igbaw", "balay"],
                "explain": "'Tikang ha' marks the point of origin / departure."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the spatial noun for 'inside / interior':",
                "tiles": ["S", "U", "L", "O", "D", "A", "N"],
                "answer": "SULOD",
                "gloss": "sulod (inside / interior)"
            },
            {
                "clue": "Spell the spatial noun for 'outside / exterior':",
                "tiles": ["G", "A", "W", "A", "S", "H", "O"],
                "answer": "GAWAS",
                "gloss": "gawas (outside / exterior)"
            },
            {
                "clue": "Spell the directional preposition meaning 'from':",
                "tiles": ["T", "I", "K", "A", "N", "G", "H", "A"],
                "answer": "TIKANG",
                "gloss": "tikang (from / origin)"
            }
        ],
        "quiz": [
            {
                "q": "What is the primary grammatical role of 'ha' in Waray-Waray?",
                "options": [
                    "It serves as the universal locative case marker (in, at, on, to)!",
                    "It is a verb meaning 'to have'",
                    "It is an exclusive pronoun"
                ],
                "correct": 0,
                "explain": "'Ha' is the indispensable locative marker that anchors spatial phrases in Visayan syntax."
            },
            {
                "q": "How do Waray speakers form complex prepositions like 'inside the house' or 'under the table'?",
                "options": [
                    "By using 'ha' + relational noun + genitive marker 'han' (e.g. 'ha sulod han balay')!",
                    "By inventing completely new single prepositions",
                    "By putting the noun first without markers"
                ],
                "correct": 0,
                "explain": "Complex Visayan spatial expressions follow the formula: ha + [relational noun: sulod, gawas, igbaw, ilarom] + han + [noun]."
            },
            {
                "q": "Which pair correctly distinguishes movement 'towards' from movement 'from' in Waray?",
                "options": [
                    "'ngadto ha' (towards/to) vs. 'tikang ha' (from)",
                    "'dida ha' vs. 'didto ha'",
                    "'sulod ha' vs. 'gawas ha'"
                ],
                "correct": 0,
                "explain": "'Ngadto ha' denotes movement heading towards a destination, while 'tikang ha' denotes departure from an origin."
            },
            {
                "q": "What does 'ha igbaw han lamesa' mean?",
                "options": [
                    "On top of the table",
                    "Underneath the table",
                    "Beside the table"
                ],
                "correct": 0,
                "explain": "'Igbaw' means top or upper surface; 'ha igbaw han lamesa' = on top of the table."
            },
            {
                "q": "What root does 'ha atubangan' derive from?",
                "options": [
                    "'atubang' (to face / front)",
                    "'tuba' (coconut wine)",
                    "'bangon' (to rise)"
                ],
                "correct": 0,
                "explain": "'Atubangan' comes from 'atubang' (to face), meaning the area directly in front of or facing something."
            }
        ]
    },
    "french": {
        "sealName": "Lumière Solaire Spatial Seal",
        "guide": {
            "name": "Madame Claudine",
            "role": "Parisian Cartographer & Spatial Guide",
            "avatar": "🗺️",
            "prompt": "Bonjour ! Prepositions in French orchestrate space and direction: 'dans' (inside), 'sur' (on), 'sous' (under), 'devant' (in front), 'derrière' (behind), 'chez' (at someone's place), and contractions with 'à' and 'de' (au, du, aux, des)!"
        },
        "cards": [
            {
                "id": "fr_s8_c1",
                "type": "preposition",
                "glyph": "dans",
                "phonetic": "[dɑ̃]",
                "gloss": "in / inside (enclosed space)",
                "speakText": "dans la maison",
                "audioUrl": "",
                "whisper": "Expresses location inside a defined 3D space: 'dans la maison' (in the house). Nasal vowel [ɑ̃]."
            },
            {
                "id": "fr_s8_c2",
                "type": "preposition",
                "glyph": "sur / sous",
                "phonetic": "[syʁ] • [su]",
                "gloss": "on (sur) • under (sous)",
                "speakText": "sur la table, sous la table",
                "audioUrl": "",
                "whisper": "Pronunciation trap: 'sur' has the high rounded [y] (lips rounded for [u] while saying [i]), while 'sous' has [u]! 'Sur la table' (on the table) vs. 'sous la table' (under the table)."
            },
            {
                "id": "fr_s8_c3",
                "type": "preposition",
                "glyph": "devant / derrière",
                "phonetic": "[də.vɑ̃] • [dɛ.ʁjɛʁ]",
                "gloss": "in front of (devant) • behind (derrière)",
                "speakText": "devant, derrière",
                "audioUrl": "",
                "whisper": "'Devant le musée' (in front of the museum) vs. 'derrière la cathédrale' (behind the cathedral)."
            },
            {
                "id": "fr_s8_c4",
                "type": "preposition",
                "glyph": "chez",
                "phonetic": "[ʃe]",
                "gloss": "at the place/home of",
                "speakText": "chez moi, chez le médecin",
                "audioUrl": "",
                "whisper": "A uniquely French preposition: 'chez moi' (at my home), 'chez le boulanger' (at the baker's shop). Never used for objects, only for persons or professions!"
            },
            {
                "id": "fr_s8_c5",
                "type": "preposition",
                "glyph": "entre",
                "phonetic": "[ɑ̃tʁ]",
                "gloss": "between / among",
                "speakText": "entre nous",
                "audioUrl": "",
                "whisper": "'Entre deux chaises' (between two chairs); 'entre Paris et Lyon' (between Paris and Lyon)."
            },
            {
                "id": "fr_s8_c6",
                "type": "preposition",
                "glyph": "à côté de",
                "phonetic": "[a ko.te də]",
                "gloss": "next to / beside",
                "speakText": "à côté de la tour",
                "audioUrl": "",
                "whisper": "Compound preposition: note that 'de' contracts with 'le' into 'du' ('à côté du parc') and with 'les' into 'des' ('à côté des arbres')."
            },
            {
                "id": "fr_s8_c7",
                "type": "preposition",
                "glyph": "vers",
                "phonetic": "[vɛʁ]",
                "gloss": "towards (direction) / around (time)",
                "speakText": "vers le nord",
                "audioUrl": "",
                "whisper": "Spatial direction: 'vers la sortie' (towards the exit); approximate time: 'vers midi' (around noon)."
            },
            {
                "id": "fr_s8_c8",
                "type": "preposition",
                "glyph": "au (à+le) / du (de+le)",
                "phonetic": "[o] • [dy]",
                "gloss": "to the (au) • of/from the (du)",
                "speakText": "au parc, du musée",
                "audioUrl": "",
                "whisper": "Mandatory phonetic fusion: à + le = AU; à + les = AUX; de + le = DU; de + les = DES! Never say 'à le' or 'de le'."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the famous minimal pair: Is the book on the table or under it?",
                "speakAudio": "Le livre est sur la table",
                "options": [
                    "On the table (sur la table — [syʁ])",
                    "Under the table (sous la table — [su])",
                    "Next to the table (à côté de la table)"
                ],
                "correct": 0,
                "explain": "'Sur' [syʁ] means on/upon, while 'sous' [su] means under."
            },
            {
                "prompt": "Listen to the invitation. Where is the guest invited?",
                "speakAudio": "Viens chez moi ce soir",
                "options": [
                    "Come to my place this evening (chez moi)",
                    "Come to the bakery this evening",
                    "Come in front of the house"
                ],
                "correct": 0,
                "explain": "'Chez moi' specifically means 'at my place / to my house'."
            },
            {
                "prompt": "Listen to the location of the metro station.",
                "speakAudio": "La station est devant le musée",
                "options": [
                    "In front of the museum (devant le musée)",
                    "Behind the museum (derrière le musée)",
                    "Inside the museum (dans le musée)"
                ],
                "correct": 0,
                "explain": "'Devant' means in front of."
            },
            {
                "prompt": "Listen to the direction of travel.",
                "speakAudio": "Nous marchons vers la mer",
                "options": [
                    "We are walking towards the sea (vers la mer)",
                    "We are swimming in the sea",
                    "We are far from the sea"
                ],
                "correct": 0,
                "explain": "'Vers' indicates direction towards a destination."
            }
        ],
        "arena": [
            {
                "quest": "Enclosed Location",
                "clue": "Assemble: 'The key is in the house' (The key + is + in + the house)",
                "target": "La clef est dans la maison",
                "tokens": ["La", "clef", "est", "dans", "la", "maison", "sur", "sous"],
                "explain": "'Dans' indicates placement inside an enclosed structure."
            },
            {
                "quest": "Cultural Preposition 'Chez'",
                "clue": "Assemble: 'I am at my place' (I + am + at-the-place-of + me)",
                "target": "Je suis chez moi",
                "tokens": ["Je", "suis", "chez", "moi", "dans", "sur"],
                "explain": "'Chez' + tonic pronoun 'moi' signifies 'at my home / at my place'."
            },
            {
                "quest": "Relative Position",
                "clue": "Assemble: 'In front of the museum' (in-front-of + the + museum)",
                "target": "Devant le musee",
                "tokens": ["Devant", "le", "musee", "derriere", "sous", "vers"],
                "explain": "'Devant' specifies spatial placement in front of an entity."
            },
            {
                "quest": "Mandatory Contraction",
                "clue": "Assemble: 'Next to the park' (next-to + the.MASC + park: de+le -> du)",
                "target": "A cote du parc",
                "tokens": ["A", "cote", "du", "parc", "de", "le", "dans"],
                "explain": "'À côté de' + masculine singular 'le parc' must contract into 'du parc'."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the preposition for 'inside / in':",
                "tiles": ["D", "A", "N", "S", "E", "O"],
                "answer": "DANS",
                "gloss": "dans (in / inside)"
            },
            {
                "clue": "Spell the uniquely French preposition meaning 'at the place/home of':",
                "tiles": ["C", "H", "E", "Z", "O", "S"],
                "answer": "CHEZ",
                "gloss": "chez (at the place/home of)"
            },
            {
                "clue": "Spell the preposition for 'behind':",
                "tiles": ["D", "E", "R", "R", "I", "E", "R", "E", "A"],
                "answer": "DERRIERE",
                "gloss": "derrière (behind)"
            }
        ],
        "quiz": [
            {
                "q": "How do the vowel sounds of 'sur' (on) and 'sous' (under) phonetically differ?",
                "options": [
                    "'Sur' has the high close front rounded vowel [y], while 'sous' has the back rounded vowel [u]!",
                    "They are pronounced identically in Paris",
                    "'Sur' is nasal and 'sous' is not"
                ],
                "correct": 0,
                "explain": "French distinguishes [y] (sur) from [u] (sous); confusing them flips 'on top of' with 'underneath'!"
            },
            {
                "q": "When must 'de' and 'le' contract into 'du'?",
                "options": [
                    "Always — 'de + le' is strictly forbidden in French and must contract to 'du'!",
                    "Only before vowels",
                    "Only at the start of a sentence"
                ],
                "correct": 0,
                "explain": "The mandatory article contractions in French are 'de + le = du' and 'à + le = au'."
            },
            {
                "q": "Can you use the preposition 'chez' with an inanimate object or building (e.g. 'chez la boulangerie')?",
                "options": [
                    "No — 'chez' is only used with persons, professions, or pronouns ('chez Pierre', 'chez le boulanger', 'chez moi')!",
                    "Yes, it works with all nouns",
                    "Only with cities and countries"
                ],
                "correct": 0,
                "explain": "'Chez' comes from Latin 'casa' (house) and requires a human or occupational reference ('chez le dentiste', 'chez nous')."
            },
            {
                "q": "What does 'entre la poire et le fromage' figuratively mean in French culture?",
                "options": [
                    "At the relaxed tail end of a dinner party / between courses",
                    "Under the table",
                    "At the grocery store"
                ],
                "correct": 0,
                "explain": "'Entre' means between; the idiom 'entre la poire et le fromage' refers to casual conversation towards the end of a meal."
            },
            {
                "q": "Which preposition fills the blank: 'Le chat dort _______ (under) le lit'?",
                "options": [
                    "sous",
                    "sur",
                    "vers"
                ],
                "correct": 0,
                "explain": "'Sous' [su] means under; 'sous le lit' = under the bed."
            }
        ]
    },
    "latin": {
        "sealName": "SPQR Imperium Loci Seal",
        "guide": {
            "name": "Marcus",
            "role": "Forum Romanum Pontifex & Geographer",
            "avatar": "🦅",
            "prompt": "Salvē! In Classical Latin, prepositions are intimately bound to grammatical cases! The mnemonic 'SID SPACE' governs the Ablative (sub, in, dē, sine, prō, ab, cum, ex), while destination and through-motion demand the Accusative (ad, per, trāns, ante, post, inter). And beware the two-way chameleon: 'in'!"
        },
        "cards": [
            {
                "id": "lat_s8_c1",
                "type": "preposition",
                "glyph": "in (+ Abl. vs. + Acc.)",
                "phonetic": "[ɪn]",
                "gloss": "in/on (+ Ablative) • into/onto (+ Accusative)",
                "speakText": "in urbe, in urbem",
                "audioUrl": "",
                "whisper": "The ultimate Latin case test: static position takes the Ablative ('in urbe' = in the city), while motion into takes the Accusative ('in urbem' = into the city)!"
            },
            {
                "id": "lat_s8_c2",
                "type": "preposition",
                "glyph": "sub (+ Abl. / Acc.)",
                "phonetic": "[sʊb]",
                "gloss": "under/at the foot of (+ Abl.) • under (+ Acc. motion)",
                "speakText": "sub arbore, sub pontem",
                "audioUrl": "",
                "whisper": "'Sub arbore sedet' (He sits under the tree, Ablative); 'Sub pontem navigat' (He sails under the bridge, Accusative)."
            },
            {
                "id": "lat_s8_c3",
                "type": "preposition",
                "glyph": "ab / ā (+ Ablative)",
                "phonetic": "[ab] • [aː]",
                "gloss": "away from / from (source, origin, agent)",
                "speakText": "ab urbe, a magistro",
                "audioUrl": "",
                "whisper": "Always takes the Ablative! 'ā' before consonants, 'ab' before vowels. Marks separation: 'ab urbe' (away from the city)."
            },
            {
                "id": "lat_s8_c4",
                "type": "preposition",
                "glyph": "ex / ē (+ Ablative)",
                "phonetic": "[ɛks] • [eː]",
                "gloss": "out of / out from within (+ Ablative)",
                "speakText": "ex silva, e villa",
                "audioUrl": "",
                "whisper": "'ex silvā' (out of the forest); 'ex' before vowels or consonants, 'ē' only before consonants."
            },
            {
                "id": "lat_s8_c5",
                "type": "preposition",
                "glyph": "ad (+ Accusative)",
                "phonetic": "[ad]",
                "gloss": "to / towards / near (+ Accusative)",
                "speakText": "ad forum, ad urbem",
                "audioUrl": "",
                "whisper": "Always governs the Accusative for directional movement towards: 'Ad forum currit' (He runs to the forum)."
            },
            {
                "id": "lat_s8_c6",
                "type": "preposition",
                "glyph": "cum (+ Ablative)",
                "phonetic": "[kʊm]",
                "gloss": "with / together with (+ Ablative)",
                "speakText": "cum amicis, mecum",
                "audioUrl": "",
                "whisper": "Ablative of accompaniment: 'cum amīcīs' (with friends). With personal pronouns, it attaches as a suffix: 'mēcum' (with me), 'tēcum' (with you), 'nōbīscum' (with us)."
            },
            {
                "id": "lat_s8_c7",
                "type": "preposition",
                "glyph": "per (+ Accusative)",
                "phonetic": "[pɛr]",
                "gloss": "through / across / by means of (+ Accusative)",
                "speakText": "per silvam, per vias",
                "audioUrl": "",
                "whisper": "Always governs the Accusative: 'per silvam' (through the forest), 'per viās' (through the streets). Signifies traversal."
            },
            {
                "id": "lat_s8_c8",
                "type": "preposition",
                "glyph": "ante / post (+ Accusative)",
                "phonetic": "[ˈan.tɛ] • [pɔst]",
                "gloss": "before / in front of (ante) • behind / after (post)",
                "speakText": "ante portas, post bellum",
                "audioUrl": "",
                "whisper": "'Ante portās' (before the gates), 'post bellum' (after the war). Both govern the Accusative case."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the Latin case distinction. Is the senator currently inside the senate house, or entering into it?",
                "speakAudio": "Senator in curia sedet",
                "options": [
                    "Inside the senate house (in curia — Ablative of rest)",
                    "Entering into the senate house (in curiam — Accusative)",
                    "Away from the senate house (ab urbe)"
                ],
                "correct": 0,
                "explain": "'In cūriā' has the Ablative ending '-ā', denoting stationary presence ('sits in the senate')."
            },
            {
                "prompt": "Listen to the famous phrase about the enemy. Where is Hannibal?",
                "speakAudio": "Hannibal ad portas",
                "options": [
                    "Hannibal is at the gates (ad portas — Accusative)",
                    "Hannibal is behind the walls",
                    "Hannibal is inside the city"
                ],
                "correct": 0,
                "explain": "'Ad' governs the Accusative 'portās', indicating motion or proximity to the gates."
            },
            {
                "prompt": "Listen to the companionship phrase. Who is coming along?",
                "speakAudio": "Veni mecum ad forum",
                "options": [
                    "Come with me to the forum (Veni mecum)",
                    "Go away from me to the forest",
                    "Stay in the forum without me"
                ],
                "correct": 0,
                "explain": "'Mēcum' attaches the preposition 'cum' to the ablative pronoun 'mē' ('with me')."
            },
            {
                "prompt": "Listen to where the soldiers marched.",
                "speakAudio": "Milites per silvam ambulant",
                "options": [
                    "The soldiers walk through the forest (per silvam — Accusative)",
                    "The soldiers rest under the tree",
                    "The soldiers flee from the forest"
                ],
                "correct": 0,
                "explain": "'Per' governs the Accusative 'silvam', indicating movement through."
            }
        ],
        "arena": [
            {
                "quest": "Ablative of Static Place",
                "clue": "Assemble: 'In the city' (in + city.ABL)",
                "target": "in urbe",
                "tokens": ["in", "urbe", "urbem", "ad", "ex", "cum"],
                "explain": "Static location requires 'in' + the Ablative singular 'urbe'."
            },
            {
                "quest": "Accusative of Destination",
                "clue": "Assemble: 'To the forum' (to + forum.ACC)",
                "target": "ad forum",
                "tokens": ["ad", "forum", "foro", "ab", "in", "sub"],
                "explain": "Direction towards a destination uses 'ad' + Accusative 'forum'."
            },
            {
                "quest": "Accompaniment with Clitic Pronoun",
                "clue": "Assemble: 'With me' (me + with: enclitic cum)",
                "target": "mecum",
                "tokens": ["mecum", "cum", "me", "tecum", "ad", "in"],
                "explain": "With 1st/2nd person pronouns, 'cum' enclitically attaches to the ablative: 'mēcum'."
            },
            {
                "quest": "Motion Out Of",
                "clue": "Assemble: 'Out of the forest' (out-of + forest.ABL)",
                "target": "ex silva",
                "tokens": ["ex", "silva", "silvam", "ad", "in", "per"],
                "explain": "'Ex' governs the Ablative case ('silvā') to indicate movement outward."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the preposition governing Accusative for 'towards / to':",
                "tiles": ["A", "D", "B", "E", "X"],
                "answer": "AD",
                "gloss": "ad (to / towards - takes Accusative)"
            },
            {
                "clue": "Spell the preposition meaning 'with' (governs Ablative):",
                "tiles": ["C", "U", "M", "A", "B", "S"],
                "answer": "CUM",
                "gloss": "cum (with - takes Ablative)"
            },
            {
                "clue": "Spell the preposition meaning 'through / across' (governs Accusative):",
                "tiles": ["P", "E", "R", "O", "S", "T"],
                "answer": "PER",
                "gloss": "per (through - takes Accusative)"
            }
        ],
        "quiz": [
            {
                "q": "How does the case governed by the Latin preposition 'in' change the meaning of the clause?",
                "options": [
                    "'In' + Ablative denotes static location ('in/on'), while 'in' + Accusative denotes motion into ('into/onto')!",
                    "'In' + Ablative means 'outside', while 'in' + Accusative means 'inside'",
                    "There is no difference in meaning"
                ],
                "correct": 0,
                "explain": "'In urbe' (Ablative) = in the city; 'in urbem' (Accusative) = into the city. Motion vs. rest determines the case!"
            },
            {
                "q": "What is the famous mnemonic acronym 'SID SPACE' used for in Latin grammar?",
                "options": [
                    "Remembering the common prepositions that govern the Ablative: Sub, In, Dē, Sine, Prō, Ab, Cum, Ex!",
                    "Remembering the declension noun endings",
                    "Remembering irregular verbs"
                ],
                "correct": 0,
                "explain": "'SID SPACE' lists the primary Latin prepositions governing the Ablative case."
            },
            {
                "q": "How does the preposition 'cum' behave when combined with personal pronouns like 'mē', 'tē', or 'nōbīs'?",
                "options": [
                    "It attaches to the end as an enclitic suffix: 'mēcum', 'tēcum', 'nōbīscum'!",
                    "It disappears completely",
                    "It changes to 'ab'"
                ],
                "correct": 0,
                "explain": "In Classical Latin, 'cum' suffixes to personal/reflexive pronouns: mēcum (with me), tēcum (with you), sēcum (with himself), nōbīscum (with us)."
            },
            {
                "q": "Which preposition correctly fills the blank: 'Ambulāmus _______ (through) silvam'?",
                "options": [
                    "per",
                    "sine",
                    "dē"
                ],
                "correct": 0,
                "explain": "'Per' governs the Accusative ('silvam') and means through."
            },
            {
                "q": "What is the difference between 'ab' and 'ex' when indicating movement away from a place?",
                "options": [
                    "'Ab' means away from the outside/vicinity, while 'ex' means out from the inside of an enclosure!",
                    "'Ab' means above, while 'ex' means under",
                    "They are completely interchangeable in all contexts"
                ],
                "correct": 0,
                "explain": "'Ab urbe' = away from the city outskirts; 'ex urbe' = out from inside the city walls."
            }
        ]
    },
    "hebrew": {
        "sealName": "Mekomot Golden Seal",
        "guide": {
            "name": "Eli",
            "role": "Jerusalem Cartographer & Scribe",
            "avatar": "🕊️",
            "prompt": "Shalom! Hebrew uses both single-letter inseparable prefix prepositions—בְּ- (be- in/at), לְ- (le- to), מִ- (mi- from)—and rich independent spatial prepositions like עַל (al - on), תַּחַת (táchat - under), לִפְנֵי (lifnéy - in front of/before), and אַחֲרֵי (acharèy - behind/after)!"
        },
        "cards": [
            {
                "id": "heb_s8_c1",
                "type": "preposition",
                "glyph": "בְּ- / בַּ- (be- / ba-)",
                "phonetic": "[bə] • [ba]",
                "gloss": "in / at / with (inseparable prefix)",
                "speakText": "בבית, בחדר",
                "audioUrl": "",
                "whisper": "Prefix preposition: 'be-vàyit' (in a house). When the definite article 'ha-' is added, it merges into 'ba-': 'ba-bàyit' (in THE house)!"
            },
            {
                "id": "heb_s8_c2",
                "type": "preposition",
                "glyph": "לְ- / לַ- (le- / la-)",
                "phonetic": "[lə] • [la]",
                "gloss": "to / for / towards (inseparable prefix)",
                "speakText": "לירושלים, לשוק",
                "audioUrl": "",
                "whisper": "'le-Yerushalàyim' (to Jerusalem); merged with definite article: 'la-shuk' (to THE market)."
            },
            {
                "id": "heb_s8_c3",
                "type": "preposition",
                "glyph": "מִ- / מֵ- (mi- / me-)",
                "phonetic": "[mi] • [me]",
                "gloss": "from / of / since (inseparable prefix)",
                "speakText": "מהבית, מישראל",
                "audioUrl": "",
                "whisper": "Inseparable prefix: 'mi-Yisra'él' (from Israel). Before guttural letters (א, ע, ר, ה), the vowel lengthens to 'me-': 'me-ha-bàyit' (from the house)."
            },
            {
                "id": "heb_s8_c4",
                "type": "preposition",
                "glyph": "עַל (al)",
                "phonetic": "[ʔal]",
                "gloss": "on / upon / above / about",
                "speakText": "על השולחן",
                "audioUrl": "",
                "whisper": "Independent preposition: 'al ha-shulchán' (on the table). Also means 'about': 'medabrím al...' (talking about...)."
            },
            {
                "id": "heb_s8_c5",
                "type": "preposition",
                "glyph": "תַּחַת (táchat)",
                "phonetic": "[ˈtaχat]",
                "gloss": "under / beneath / below",
                "speakText": "תחת הכיסא",
                "audioUrl": "",
                "whisper": "'táchat ha-kisé' (under the chair); 'táchat ha-shémesh' (under the sun - Ecclesiastes)."
            },
            {
                "id": "heb_s8_c6",
                "type": "preposition",
                "glyph": "לִפְנֵי (lifnéy)",
                "phonetic": "[lifˈne]",
                "gloss": "in front of (space) / before (time)",
                "speakText": "לפני הבית, לפני שעה",
                "audioUrl": "",
                "whisper": "Formed from לְ- + 'paním' (faces): literally 'to the faces of'! Used for both space ('lifnéy ha-bàyit' = in front of the house) and time ('lifnéy sha'áh' = an hour ago)."
            },
            {
                "id": "heb_s8_c7",
                "type": "preposition",
                "glyph": "אַחֲרֵי (acharèy)",
                "phonetic": "[ʔaχaˈʁe]",
                "gloss": "behind (space) / after (time)",
                "speakText": "אחרי הבית, אחרי שעה",
                "audioUrl": "",
                "whisper": "Twin to 'lifnéy': 'acharèy ha-bàyit' (behind the house), 'acharèy ha-tsohoràyim' (afternoon)."
            },
            {
                "id": "heb_s8_c8",
                "type": "preposition",
                "glyph": "לְיַד / בֵּין (leyád / beyn)",
                "phonetic": "[leˈjad] • [bejn]",
                "gloss": "beside/near (leyád) • between (beyn)",
                "speakText": "ליד הים, בין העצים",
                "audioUrl": "",
                "whisper": "'leyád' literally means 'to the hand of' (beside/near): 'leyád ha-yam' (by the sea); 'beyn' means between: 'beyn ha-harím' (between the mountains)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to where the keys are located.",
                "speakAudio": "המפתחות על השולחן",
                "options": [
                    "The keys are on the table (al ha-shulchan)",
                    "The keys are under the chair (tachat ha-kise)",
                    "The keys are in the pocket"
                ],
                "correct": 0,
                "explain": "'עַל' (al) means on / upon."
            },
            {
                "prompt": "Listen to the spatial direction. Where is the cat sleeping?",
                "speakAudio": "החתול ישן תחת הכיסא",
                "options": [
                    "The cat sleeps under the chair (tachat ha-kise)",
                    "The cat sleeps on the table",
                    "The cat sleeps behind the house"
                ],
                "correct": 0,
                "explain": "'תַּחַת' (táchat) means under / beneath."
            },
            {
                "prompt": "Listen to the origin of the traveler.",
                "speakAudio": "הוא הגיע מירושלים",
                "options": [
                    "He arrived from Jerusalem (mi-Yerushalayim)",
                    "He is traveling to Jerusalem",
                    "He lives in Jerusalem"
                ],
                "correct": 0,
                "explain": "The prefix 'מִ-' (mi-) indicates origin ('from')."
            },
            {
                "prompt": "Listen to the meeting point. Where is the shop located?",
                "speakAudio": "החנות ליד הים",
                "options": [
                    "The shop is beside the sea (leyad ha-yam)",
                    "The shop is inside the city",
                    "The shop is between two mountains"
                ],
                "correct": 0,
                "explain": "'לְיַד' (leyád = next to / beside) + 'הַיָּם' (ha-yam = the sea)."
            }
        ],
        "arena": [
            {
                "quest": "Prefix Preposition + Definite Article",
                "clue": "Assemble: 'In the house' (in+THE + house: be+ha -> ba)",
                "target": "בבית",
                "tokens": ["בבית", "לבית", "מהבית", "על", "תחת", "שם"],
                "explain": "Prefix 'בְּ-' combined with 'הַבַּיִת' swallows the 'h' sound to become 'ba-bàyit' (בַּבַּיִת)."
            },
            {
                "quest": "Independent Spatial Preposition",
                "clue": "Assemble: 'On the table' (on + the-table)",
                "target": "על השולחן",
                "tokens": ["על", "השולחן", "תחת", "ליד", "בבית", "של"],
                "explain": "'עַל' (al = on) followed by the definite noun 'הַשֻּׁלְחָן' (ha-shulchán)."
            },
            {
                "quest": "Spatial Facing",
                "clue": "Assemble: 'In front of the house' (in-front-of + the-house)",
                "target": "לפני הבית",
                "tokens": ["לפני", "הבית", "אחרי", "תחת", "על", "שם"],
                "explain": "'לִפְנֵי' (lifnéy = in front of / before) + 'הַבַּיִת' (ha-bàyit)."
            },
            {
                "quest": "Proximity by the Sea",
                "clue": "Assemble: 'Beside the sea' (beside + the-sea)",
                "target": "ליד הים",
                "tokens": ["ליד", "הים", "בין", "על", "מ", "פה"],
                "explain": "'לְיַד' (leyád = beside, literally 'to the hand of') + 'הַיָּם' (ha-yam)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the independent preposition for 'on / upon' (al):",
                "tiles": ["ע", "ל", "א", "ם"],
                "answer": "על",
                "gloss": "עַל (on / upon)"
            },
            {
                "clue": "Assemble the spatial preposition for 'under / beneath' (táchat):",
                "tiles": ["ת", "ח", "ת", "ש", "כ"],
                "answer": "תחת",
                "gloss": "תַּחַת (under / beneath)"
            },
            {
                "clue": "Assemble the preposition for 'in front of / before' (lifnéy):",
                "tiles": ["ל", "פ", "נ", "י", "ם", "ת"],
                "answer": "לפני",
                "gloss": "לִפְנֵי (in front of / before)"
            }
        ],
        "quiz": [
            {
                "q": "What happens phonetically when the prefix preposition בְּ- (be-) attaches to a definite noun like הַבַּיִת (ha-bàyit)?",
                "options": [
                    "The 'heh' of the definite article is absorbed, and its vowel transfers to the Bet, pronouncing 'ba-bàyit'!",
                    "The Bet is pronounced twice",
                    "The definite article is moved to the end of the word"
                ],
                "correct": 0,
                "explain": "In Hebrew, inseparable prepositions (בּ, לּ, כּ) absorb the definite article: be- + ha-bàyit becomes ba-bàyit."
            },
            {
                "q": "What is the literal anatomical root meaning of 'לִפְנֵי' (lifnéy - in front of) and 'לְיַד' (leyád - beside)?",
                "options": [
                    "'To the faces of' (paním) and 'to the hand of' (yad)!",
                    "'To the heart of' and 'to the foot of'",
                    "'From the eyes of' and 'from the ear of'"
                ],
                "correct": 0,
                "explain": "Semitic spatial relational nouns originate from body parts: pānīm (face) -> lifnēy (in front of); yād (hand) -> leyād (beside)."
            },
            {
                "q": "How do 'lifnéy' and 'acharèy' function across both space and time?",
                "options": [
                    "Both express physical space ('in front of' / 'behind') AND temporal sequence ('before' / 'after')!",
                    "They can only be used for clock time",
                    "They can only refer to people"
                ],
                "correct": 0,
                "explain": "'Lifnéy' means both 'in front of' and 'before' (e.g. lifnéy sha'áh = an hour ago); 'acharèy' means 'behind' and 'after'."
            },
            {
                "q": "Which prefix indicates motion 'from' or origin in Hebrew?",
                "options": [
                    "מִ- (mi-)",
                    "לְ- (le-)",
                    "בְּ- (be-)"
                ],
                "correct": 0,
                "explain": "The prefix 'מִ-' (shortened from 'min') means from / out of: mi-chán (from here), me-ha-bàyit (from the house)."
            },
            {
                "q": "What does the Hebrew phrase 'táchat ha-shémesh' (תַּחַת הַשֶּׁמֶשׁ) famously mean?",
                "options": [
                    "Under the sun (a famous biblical idiom for life on earth)",
                    "Towards the sunrise",
                    "On the mountain peak"
                ],
                "correct": 0,
                "explain": "'Táchat ha-shémesh' (under the sun) appears throughout the Book of Kohelet (Ecclesiastes)."
            }
        ]
    },
    "chinese": {
        "sealName": "Jade Directional Compass Seal",
        "guide": {
            "name": "Master Lao",
            "role": "Sanctuary Geographer & Feng Shui Scholar",
            "avatar": "🧭",
            "prompt": "Nǐ hǎo! In Mandarin Chinese, spatial relationships work through a harmonious partnership: a coverb like 在 (zài - at/in), 到 (dào - to), or 从 (cóng - from) marks the frame, while postpositional localizers (方位词 fāngwèicí) like 上 (shàng), 下 (xià), 里 (lǐ), 外 (wài), 前 (qián), 后 (hòu) pin down exact orientation!"
        },
        "cards": [
            {
                "id": "zh_s8_c1",
                "type": "coverb",
                "glyph": "在 (zài)",
                "phonetic": "[tsaɪ̯˥˩] (4th tone)",
                "gloss": "at / in / on (locative coverb)",
                "speakText": "在",
                "audioUrl": "",
                "whisper": "The primary locative coverb in Chinese. Marks the location where an action takes place: 'Wǒ zài jiā' (I am at home). Usually pairs with localizers for specific positions."
            },
            {
                "id": "zh_s8_c2",
                "type": "localizer",
                "glyph": "上 / 下 (shàng / xià)",
                "phonetic": "[ʂɑŋ˥˩] • [ɕja˥˩]",
                "gloss": "on/above (shàng) • under/below (xià)",
                "speakText": "桌子上, 椅子下",
                "audioUrl": "",
                "whisper": "Localizers attached after the noun: 'zhuōzi shàng' (on the table), 'yǐzi xià' (under the chair). Notice: English puts prepositions before; Chinese localizers follow the noun!"
            },
            {
                "id": "zh_s8_c3",
                "type": "localizer",
                "glyph": "里 / 外 (lǐ / wài)",
                "phonetic": "[li˨˩˦] • [waɪ̯˥˩]",
                "gloss": "inside (lǐ) • outside (wài)",
                "speakText": "房间里, 门外",
                "audioUrl": "",
                "whisper": "'fángjiān lǐ' (inside the room), 'mén wài' (outside the door). Note: city and country names DO NOT take 'lǐ' ('zài Běijīng', never 'zài Běijīng lǐ')!"
            },
            {
                "id": "zh_s8_c4",
                "type": "localizer",
                "glyph": "前 / 后 (qián / hòu)",
                "phonetic": "[tɕʰjɛn˧˥] • [xɤʊ̯˥˩]",
                "gloss": "in front of (qián) • behind / after (hòu)",
                "speakText": "门前, 房子后",
                "audioUrl": "",
                "whisper": "'mén qián' (in front of the gate), 'fángzi hòu' (behind the house). Also applies to time: 'sān tiān qián' (3 days ago), 'yǐhòu' (afterwards)."
            },
            {
                "id": "zh_s8_c5",
                "type": "localizer",
                "glyph": "中间 / 旁边 (zhōngjiān / pángbiān)",
                "phonetic": "[tʂʊŋ˥.tɕjɛn˥] • [pʰɑŋ˧˥.pjɛn˥]",
                "gloss": "between/middle (zhōngjiān) • beside/next to (pángbiān)",
                "speakText": "中间, 旁边",
                "audioUrl": "",
                "whisper": "'zài liǎng ge rén zhōngjiān' (between two people); 'zài wǒ pángbiān' (beside me / at my side)."
            },
            {
                "id": "zh_s8_c6",
                "type": "coverb",
                "glyph": "从 (cóng)",
                "phonetic": "[tsʰʊŋ˧˥] (2nd tone)",
                "gloss": "from (origin / starting point)",
                "speakText": "从北京来",
                "audioUrl": "",
                "whisper": "Coverb marking origin: 'cóng Běijīng dào Shànghǎi' (from Beijing to Shanghai). Pairs with 'dào' (to)."
            },
            {
                "id": "zh_s8_c7",
                "type": "coverb",
                "glyph": "到 (dào)",
                "phonetic": "[taʊ̯˥˩] (4th tone)",
                "gloss": "to / arrive at (destination coverb)",
                "speakText": "到学校去",
                "audioUrl": "",
                "whisper": "Expresses destination: 'dào túshūguǎn qù' (go to the library). Combined structure: 'cóng... dào...' (from... to...)."
            },
            {
                "id": "zh_s8_c8",
                "type": "structure",
                "glyph": "在...上 / 在...里 (zài... shàng / lǐ)",
                "phonetic": "[tsaɪ̯... ʂɑŋ] • [tsaɪ̯... li]",
                "gloss": "at [noun] on / at [noun] inside",
                "speakText": "在桌子上, 在房间里",
                "audioUrl": "",
                "whisper": "The quintessential Chinese 'spatial sandwich': 在 (coverb) + Noun + 上/里 (postpositional localizer). Example: 'Shū zài zhuōzi shàng' (The book is on the table)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the location of the cat. Where is it resting?",
                "speakAudio": "猫在椅子下面",
                "options": [
                    "Under the chair (zài yǐzi xiàmiàn)",
                    "On top of the table (zài zhuōzi shàng)",
                    "Inside the box (zài hézi lǐ)"
                ],
                "correct": 0,
                "explain": "'在' + '椅子' (chair) + '下面' (underneath)."
            },
            {
                "prompt": "Listen to where the tea is located.",
                "speakAudio": "茶在桌子上",
                "options": [
                    "The tea is on the table (Chá zài zhuōzi shàng)",
                    "The tea is inside the teapot",
                    "The tea is in the cup"
                ],
                "correct": 0,
                "explain": "'茶' (tea) + '在' (at) + '桌子上' (on the table)."
            },
            {
                "prompt": "Listen to the travel itinerary.",
                "speakAudio": "从北京到上海",
                "options": [
                    "From Beijing to Shanghai (Cóng Běijīng dào Shànghǎi)",
                    "From Shanghai to Beijing",
                    "In Beijing and Shanghai"
                ],
                "correct": 0,
                "explain": "'从' (from) Beijing '到' (to) Shanghai."
            },
            {
                "prompt": "Listen to the student's whereabouts.",
                "speakAudio": "他在图书馆里",
                "options": [
                    "He is inside the library (Tā zài túshūguǎn lǐ)",
                    "He is in front of the library",
                    "He is walking to the library"
                ],
                "correct": 0,
                "explain": "'在' + '图书馆' (library) + '里' (inside)."
            }
        ],
        "arena": [
            {
                "quest": "The Spatial Sandwich",
                "clue": "Assemble: 'The book is on the table' (Book + is-at + table + on)",
                "target": "书在桌子上",
                "tokens": ["书", "在", "桌子", "上", "下", "里"],
                "explain": "Subject '书' + coverb '在' + noun '桌子' + localizer '上'."
            },
            {
                "quest": "Enclosed Location",
                "clue": "Assemble: 'Inside the room' (is-at + room + inside)",
                "target": "在房间里",
                "tokens": ["在", "房间", "里", "外", "上", "到"],
                "explain": "'在' + '房间' (room) + localizer '里' (inside)."
            },
            {
                "quest": "Origin to Destination",
                "clue": "Assemble: 'From Beijing to Shanghai' (from + Beijing + to + Shanghai)",
                "target": "从北京到上海",
                "tokens": ["从", "北京", "到", "上海", "在", "去"],
                "explain": "'从' (from) + origin + '到' (to) + destination."
            },
            {
                "quest": "Position in Front",
                "clue": "Assemble: 'In front of the door' (is-at + door + front)",
                "target": "在门前",
                "tokens": ["在", "门", "前", "后", "上", "中"],
                "explain": "'在' + '门' (door/gate) + localizer '前' (front)."
            }
        ],
        "scribe": [
            {
                "clue": "Assemble the core locative coverb 'at / in' (zài):",
                "tiles": ["在", "左", "存", "有"],
                "answer": "在",
                "gloss": "在 (zài - at / in)"
            },
            {
                "clue": "Assemble the localizer for 'inside' (lǐ):",
                "tiles": ["里", "重", "黑", "外"],
                "answer": "里",
                "gloss": "里 (lǐ - inside)"
            },
            {
                "clue": "Assemble the coverb meaning 'from' (cóng - two people following):",
                "tiles": ["从", "人", "众", "到"],
                "answer": "从",
                "gloss": "从 (cóng - from)"
            }
        ],
        "quiz": [
            {
                "q": "Why is the Chinese spatial structure called a 'sandwich' pattern (在...上 / 在...里)?",
                "options": [
                    "Because the noun is surrounded: the coverb 在 sits before it, while the localizer (上/下/里) follows after it!",
                    "Because it can only be used when ordering sandwiches",
                    "Because nouns can only have two syllables"
                ],
                "correct": 0,
                "explain": "Chinese frames spatial locations with a leading coverb (在) and a trailing postpositional localizer (上, 里, 下, etc.)."
            },
            {
                "q": "Why is saying '在北京里' (zài Běijīng lǐ) considered ungrammatical in standard Chinese?",
                "options": [
                    "Proper geographical place names (cities, countries) are inherently locative and do not take the localizer '里'!",
                    "Because Beijing is too large",
                    "'里' can only be used with food"
                ],
                "correct": 0,
                "explain": "Geographic entities (Beijing, China) are inherently locations: say '在上海', '在中国', never '在上海里'."
            },
            {
                "q": "What is the function of '从...到...' (cóng... dào...) in Chinese sentence structure?",
                "options": [
                    "It links a point of origin to a destination in both space ('from A to B') and time ('from 9am to 5pm')!",
                    "It is only used for prices",
                    "It expresses cause and effect"
                ],
                "correct": 0,
                "explain": "'从...到...' connects start point and end point across distance, time, and abstract scales."
            },
            {
                "q": "Which localizer means 'beside' or 'next to'?",
                "options": [
                    "旁边 (pángbiān)",
                    "中间 (zhōngjiān)",
                    "上面 (shàngmian)"
                ],
                "correct": 0,
                "explain": "'旁边' (pángbiān) means side, next to, or beside."
            },
            {
                "q": "Where does the prepositional phrase '在桌子上' sit in the sentence 'I read books at the table'?",
                "options": [
                    "Before the main verb: '我在桌子上看书' (Wǒ zài zhuōzi shàng kàn shū)!",
                    "At the very end: '我看书在桌子上'",
                    "Between the verb and the object"
                ],
                "correct": 0,
                "explain": "In Chinese, adverbial prepositional phrases of location normally precede the verb: Subject + [Location Phrase] + Verb + Object."
            }
        ]
    },
    "german": {
        "sealName": "Kaiserwald Kompass Seal",
        "guide": {
            "name": "Bäcker Hans",
            "role": "Berlin Wayfarer & Case Master",
            "avatar": "🌲",
            "prompt": "Guten Tag! German prepositions are the true master test of grammatical case! Master the 'Wechselpräpositionen' (Two-Way Prepositions: an, auf, hinter, in, neben, über, unter, vor, zwischen): they take the Dative for stationary position (Wo? Where?), but switch to the Accusative for directed motion (Wohin? Whereto?)!"
        },
        "cards": [
            {
                "id": "de_s8_c1",
                "type": "preposition",
                "glyph": "Wechselpräpositionen (Dativ vs. Akkusativ)",
                "phonetic": "[ˈvɛksl̩.pʁɛpozitsjoːnən]",
                "gloss": "Two-Way Prepositions (Dative: rest • Accusative: motion)",
                "speakText": "in dem Haus, in das Haus",
                "audioUrl": "",
                "whisper": "9 prepositions: an, auf, hinter, in, neben, über, unter, vor, zwischen. Rule: 'Wo?' (Stationary rest) -> Dativ ('im Wald'); 'Wohin?' (Directed movement/destination) -> Akkusativ ('in den Wald')!"
            },
            {
                "id": "de_s8_c2",
                "type": "preposition",
                "glyph": "in (im = in dem • ins = in das)",
                "phonetic": "[ɪm] • [ɪns]",
                "gloss": "in the (+ Dat.) • into the (+ Acc.)",
                "speakText": "im Haus, ins Haus",
                "audioUrl": "",
                "whisper": "Contractions: 'in dem' (Dativ) merges to 'im' ('im Haus' = inside the house); 'in das' (Akkusativ) merges to 'ins' ('ins Haus' = into the house)!"
            },
            {
                "id": "de_s8_c3",
                "type": "preposition",
                "glyph": "auf / unter",
                "phonetic": "[aʊ̯f] • [ˈʊn.tɐ]",
                "gloss": "on (horizontal surface) • under / beneath",
                "speakText": "auf dem Tisch, unter dem Bett",
                "audioUrl": "",
                "whisper": "'Auf dem Tisch' (on the table - Dative rest); 'Sie legt das Buch auf den Tisch' (She places the book onto the table - Accusative motion). 'Unter dem Bett' (under the bed)."
            },
            {
                "id": "de_s8_c4",
                "type": "preposition",
                "glyph": "vor / hinter",
                "phonetic": "[foːɐ̯] • [ˈhɪn.tɐ]",
                "gloss": "in front of / before (vor) • behind (hinter)",
                "speakText": "vor der Tür, hinter dem Haus",
                "audioUrl": "",
                "whisper": "'Vor der Tür' (in front of the door, Dativ); 'vor drei Tagen' (3 days ago). 'Hinter dem Haus' (behind the house, Dativ)."
            },
            {
                "id": "de_s8_c5",
                "type": "preposition",
                "glyph": "neben / zwischen",
                "phonetic": "[ˈneː.bn̩] • [ˈtsvɪ.ʃn̩]",
                "gloss": "next to / beside (neben) • between (zwischen)",
                "speakText": "neben mir, zwischen den Bäumen",
                "audioUrl": "",
                "whisper": "'neben der Bäckerei' (next to the bakery); 'zwischen den Stühlen' (between the chairs - Dative plural '-n')."
            },
            {
                "id": "de_s8_c6",
                "type": "preposition",
                "glyph": "aus, bei, mit, nach, von, zu",
                "phonetic": "[aʊ̯s] • [baɪ̯] • [mɪt] • [naːx] • [fɔn] • [tsuː]",
                "gloss": "Always Dative Prepositions (from, at, with, to/after, from, to)",
                "speakText": "mit dem Bus, nach Hause, beim Bäcker",
                "audioUrl": "",
                "whisper": "The golden Dative chant: 'Aus, bei, mit, nach, seit, von, zu — immer mit dem Dativ, weißt du!'. No matter if there is motion or rest, these ALWAYS govern the Dative!"
            },
            {
                "id": "de_s8_c7",
                "type": "preposition",
                "glyph": "beim (bei dem) / zum (zu dem) / zur (zu der)",
                "phonetic": "[baɪ̯m] • [tsʊm] • [tsuːɐ̯]",
                "gloss": "at the (beim) • to the (zum m/n, zur f)",
                "speakText": "beim Arzt, zum Bahnhof, zur Schule",
                "audioUrl": "",
                "whisper": "Standard spoken contractions: bei + dem = beim; zu + dem = zum; zu + der = zur. Essential for everyday German geography!"
            },
            {
                "id": "de_s8_c8",
                "type": "preposition",
                "glyph": "an (am = an dem • ans = an das)",
                "phonetic": "[an] • [am] • [ans]",
                "gloss": "at / on (vertical contact or border)",
                "speakText": "am Fenster, ans Fenster",
                "audioUrl": "",
                "whisper": "'Auf' is for horizontal surfaces (table, floor); 'an' is for vertical contact (wall, window, coast): 'das Bild an der Wand' (on the wall); 'am Meer' (by the sea)."
            }
        ],
        "earGym": [
            {
                "prompt": "Listen to the famous two-way case test. Is the cat resting on the sofa, or jumping onto it?",
                "speakAudio": "Die Katze schläft auf dem Sofa",
                "options": [
                    "Resting on the sofa (auf dem Sofa — Dative rest)",
                    "Jumping onto the sofa (auf das Sofa — Accusative motion)",
                    "Hiding under the sofa"
                ],
                "correct": 0,
                "explain": "'Auf dem Sofa' uses Dative 'dem', answering 'Wo?' (Where is it resting?)."
            },
            {
                "prompt": "Listen to where the person is going.",
                "speakAudio": "Ich gehe in die Bäckerei",
                "options": [
                    "Into the bakery (in die Bäckerei — Accusative destination)",
                    "Inside the bakery already (in der Bäckerei)",
                    "Behind the bakery"
                ],
                "correct": 0,
                "explain": "'In die Bäckerei' uses Accusative 'die', answering 'Wohin?' (Where to?)."
            },
            {
                "prompt": "Listen to the transportation method. Which pure Dative preposition is used?",
                "speakAudio": "Wir fahren mit dem Zug",
                "options": [
                    "By train (mit dem Zug — pure Dative)",
                    "By bus (mit dem Bus)",
                    "By car (mit dem Auto)"
                ],
                "correct": 0,
                "explain": "'Mit' is a pure Dative preposition: 'mit dem Zug' (with the train)."
            },
            {
                "prompt": "Listen to the traveler's origin.",
                "speakAudio": "Er kommt aus Deutschland",
                "options": [
                    "He comes from Germany (aus Deutschland)",
                    "He is traveling to Germany",
                    "He lives in Germany"
                ],
                "correct": 0,
                "explain": "'Aus' governs the Dative and signifies origin from inside a country or building."
            }
        ],
        "arena": [
            {
                "quest": "Two-Way Preposition (Rest: Dative)",
                "clue": "Assemble: 'The book is on the table' (The book + lies + on + the.DAT + table)",
                "target": "Das Buch liegt auf dem Tisch",
                "tokens": ["Das", "Buch", "liegt", "auf", "dem", "Tisch", "den", "in"],
                "explain": "'Wo liegt das Buch?' -> Dative: 'auf dem Tisch' (masculine Dative article 'dem')."
            },
            {
                "quest": "Two-Way Preposition (Motion: Accusative)",
                "clue": "Assemble: 'I put the book on the table' (I + place + the book + onto + the.ACC + table)",
                "target": "Ich lege das Buch auf den Tisch",
                "tokens": ["Ich", "lege", "das", "Buch", "auf", "den", "Tisch", "dem"],
                "explain": "'Wohin lege ich das Buch?' -> Accusative: 'auf den Tisch' (masculine Accusative 'den')."
            },
            {
                "quest": "Pure Dative Preposition",
                "clue": "Assemble: 'We travel with the train' (We + travel + with + the.DAT + train)",
                "target": "Wir fahren mit dem Zug",
                "tokens": ["Wir", "fahren", "mit", "dem", "Zug", "den", "nach"],
                "explain": "'Mit' is strictly a Dative preposition; 'der Zug' becomes 'dem Zug'."
            },
            {
                "quest": "Everyday Contraction",
                "clue": "Assemble: 'I am at the baker' (I + am + at-the.DAT + baker)",
                "target": "Ich bin beim Baecker",
                "tokens": ["Ich", "bin", "beim", "Baecker", "zum", "in", "den"],
                "explain": "'Bei dem' contracts into 'beim', governing the Dative for visiting a tradesperson."
            }
        ],
        "scribe": [
            {
                "clue": "Spell the two-way preposition for 'on / upon' (horizontal):",
                "tiles": ["A", "U", "F", "O", "S", "T"],
                "answer": "AUF",
                "gloss": "auf (on / upon)"
            },
            {
                "clue": "Spell the pure Dative preposition meaning 'with':",
                "tiles": ["M", "I", "T", "E", "R", "S"],
                "answer": "MIT",
                "gloss": "mit (with - pure Dative)"
            },
            {
                "clue": "Spell the preposition meaning 'under / beneath':",
                "tiles": ["U", "N", "T", "E", "R", "B", "S"],
                "answer": "UNTER",
                "gloss": "unter (under / beneath)"
            }
        ],
        "quiz": [
            {
                "q": "How do the nine German 'Wechselpräpositionen' decide whether to take Dative or Accusative?",
                "options": [
                    "They take Dative for stationary position ('Wo?' - Where?), and Accusative for directed movement/destination ('Wohin?' - Whereto?)!",
                    "They take Accusative in the morning and Dative in the evening",
                    "They take Dative only for feminine nouns"
                ],
                "correct": 0,
                "explain": "The golden rule of two-way prepositions: Location/Rest (Wo?) triggers Dative; Direction/Destination (Wohin?) triggers Accusative."
            },
            {
                "q": "Which list contains ONLY pure Dative prepositions that NEVER take Accusative?",
                "options": [
                    "aus, bei, mit, nach, seit, von, zu",
                    "an, auf, in, über, unter",
                    "durch, für, gegen, ohne, um"
                ],
                "correct": 0,
                "explain": "'Aus, bei, mit, nach, seit, von, zu' always govern the Dative case without exception."
            },
            {
                "q": "What is the difference between 'am Tisch' and 'auf dem Tisch'?",
                "options": [
                    "'Am Tisch' means sitting AT the table (by the side/edge), while 'auf dem Tisch' means on top of the tabletop!",
                    "'Am Tisch' is under the table",
                    "They mean the exact same thing"
                ],
                "correct": 0,
                "explain": "'An' indicates contact with an edge or vertical boundary ('am Tisch sitzen' = sitting at the table); 'auf' indicates placement on a horizontal surface."
            },
            {
                "q": "What contractions are formed by 'in + dem' and 'in + das'?",
                "options": [
                    "'im' (Dative) and 'ins' (Accusative)",
                    "'indem' and 'indas'",
                    "'am' and 'ans'"
                ],
                "correct": 0,
                "explain": "'in dem' contracts to 'im' (stationary: 'im Haus'), while 'in das' contracts to 'ins' (motion: 'ins Haus')."
            },
            {
                "q": "Why is 'Ich gehe zu die Schule' grammatically incorrect in German?",
                "options": [
                    "'Zu' strictly governs the Dative case, so feminine 'die Schule' must become 'der Schule' (or contract to 'zur Schule')!",
                    "'Zu' can only be used with people",
                    "'Schule' does not take prepositions"
                ],
                "correct": 0,
                "explain": "Because 'zu' is a pure Dative preposition, 'die Schule' must shift to Dative 'der Schule', contracting into 'zur Schule'."
            }
        ]
    }
}


def validate_curriculum(step_num, data_dict):
    """
    Validates that a step dictionary complies with all schema and curriculum constraints.
    """
    required_langs = ["waray", "french", "latin", "hebrew", "chinese", "german"]
    assert set(data_dict.keys()) == set(required_langs), f"Step {step_num} missing languages: {set(required_langs) - set(data_dict.keys())}"

    for lang in required_langs:
        entry = data_dict[lang]
        # 1. sealName
        assert "sealName" in entry and isinstance(entry["sealName"], str) and len(entry["sealName"]) > 0, f"Step {step_num} {lang} invalid sealName"

        # 2. guide
        assert "guide" in entry and isinstance(entry["guide"], dict), f"Step {step_num} {lang} missing guide"
        for k in ["name", "role", "avatar", "prompt"]:
            assert k in entry["guide"] and isinstance(entry["guide"][k], str) and len(entry["guide"][k]) > 0, f"Step {step_num} {lang} guide missing {k}"

        # 3. cards (7-10)
        assert "cards" in entry and isinstance(entry["cards"], list), f"Step {step_num} {lang} missing cards"
        assert 7 <= len(entry["cards"]) <= 10, f"Step {step_num} {lang} cards count {len(entry['cards'])} not in 7..10"
        card_ids = set()
        for idx, card in enumerate(entry["cards"]):
            assert "id" in card and card["id"] not in card_ids, f"Step {step_num} {lang} duplicate card id {card.get('id')}"
            card_ids.add(card["id"])
            for f in ["type", "glyph", "phonetic", "gloss", "speakText", "whisper"]:
                assert f in card and isinstance(card[f], str) and len(card[f]) > 0, f"Step {step_num} {lang} card {card.get('id')} invalid field {f}"
            assert "audioUrl" in card, f"Step {step_num} {lang} card {card.get('id')} missing audioUrl"

        # 4. earGym (3-4)
        assert "earGym" in entry and isinstance(entry["earGym"], list), f"Step {step_num} {lang} missing earGym"
        assert 3 <= len(entry["earGym"]) <= 4, f"Step {step_num} {lang} earGym count {len(entry['earGym'])} not in 3..4"
        for idx, item in enumerate(entry["earGym"]):
            for f in ["prompt", "speakAudio", "explain"]:
                assert f in item and isinstance(item[f], str) and len(item[f]) > 0, f"Step {step_num} {lang} earGym[{idx}] invalid {f}"
            assert "options" in item and isinstance(item["options"], list) and len(item["options"]) >= 3, f"Step {step_num} {lang} earGym[{idx}] options < 3"
            assert "correct" in item and isinstance(item["correct"], int) and 0 <= item["correct"] < len(item["options"]), f"Step {step_num} {lang} earGym[{idx}] invalid correct index"

        # 5. arena (3-4)
        assert "arena" in entry and isinstance(entry["arena"], list), f"Step {step_num} {lang} missing arena"
        assert 3 <= len(entry["arena"]) <= 4, f"Step {step_num} {lang} arena count {len(entry['arena'])} not in 3..4"
        for idx, item in enumerate(entry["arena"]):
            for f in ["quest", "clue", "target", "explain"]:
                assert f in item and isinstance(item[f], str) and len(item[f]) > 0, f"Step {step_num} {lang} arena[{idx}] invalid {f}"
            assert "tokens" in item and isinstance(item["tokens"], list) and len(item["tokens"]) >= 3, f"Step {step_num} {lang} arena[{idx}] tokens < 3"

        # 6. scribe (exactly 3)
        assert "scribe" in entry and isinstance(entry["scribe"], list), f"Step {step_num} {lang} missing scribe"
        assert len(entry["scribe"]) == 3, f"Step {step_num} {lang} scribe count {len(entry['scribe'])} != 3"
        for idx, item in enumerate(entry["scribe"]):
            for f in ["clue", "answer", "gloss"]:
                assert f in item and isinstance(item[f], str) and len(item[f]) > 0, f"Step {step_num} {lang} scribe[{idx}] invalid {f}"
            assert "tiles" in item and isinstance(item["tiles"], list) and len(item["tiles"]) >= len(item["answer"]), f"Step {step_num} {lang} scribe[{idx}] tiles insufficient"

        # 7. quiz (exactly 5)
        assert "quiz" in entry and isinstance(entry["quiz"], list), f"Step {step_num} {lang} missing quiz"
        assert len(entry["quiz"]) == 5, f"Step {step_num} {lang} quiz count {len(entry['quiz'])} != 5"
        for idx, item in enumerate(entry["quiz"]):
            for f in ["q", "explain"]:
                assert f in item and isinstance(item[f], str) and len(item[f]) > 0, f"Step {step_num} {lang} quiz[{idx}] invalid {f}"
            assert "options" in item and isinstance(item["options"], list) and len(item["options"]) >= 3, f"Step {step_num} {lang} quiz[{idx}] options < 3"
            assert "correct" in item and isinstance(item["correct"], int) and 0 <= item["correct"] < len(item["options"]), f"Step {step_num} {lang} quiz[{idx}] invalid correct index"

    print(f"✅ Step {step_num} validation PASSED for all 6 languages.")


if __name__ == "__main__":
    print("Validating STEP7_DATA and STEP8_DATA...")
    validate_curriculum(7, STEP7_DATA)
    validate_curriculum(8, STEP8_DATA)
    print("\nSummary Statistics:")
    print(f"STEP7_DATA languages: {list(STEP7_DATA.keys())}")
    print(f"STEP8_DATA languages: {list(STEP8_DATA.keys())}")
    for lang in STEP7_DATA:
        c7 = len(STEP7_DATA[lang]["cards"])
        c8 = len(STEP8_DATA[lang]["cards"])
        print(f"  • {lang.upper():8s} => Step 7 Cards: {c7}, Step 8 Cards: {c8}, Quizzes: 5/5, Scribes: 3/3, Arenas: 4/4")
    print("\n✨ ALL TESTS AND SCHEMA VERIFICATIONS COMPLETED SUCCESSFULLY!")
