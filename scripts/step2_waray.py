#!/usr/bin/env python3
"""
Modular builder for HexaQuest Step 1 & Step 2
"""
import json

WARAY_STEP2 = {
    "sealName": "Leyte Sunstone Calendar Seal",
    "timekeeper": {
        "name": "Lolo Pedring",
        "role": "Fisherman & Village Timekeeper",
        "avatar": "📅",
        "prompt": "Maupay nga adlaw! Mark the festival and harvest dates on our traditional Samar/Leyte calendar."
    },
    "cards": [
        {"id": "war_m1", "type": "month", "monthNum": 1, "glyph": "Enero", "phonetic": "[ɛ.ˈnɛ.ɾo]", "gloss": "January • 31 adlaw", "speakText": "Enero", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Enero.wav", "whisper": "January. In Leyte & Samar, the famous Feast of Santo Niño is celebrated in January!"},
        {"id": "war_m2", "type": "month", "monthNum": 2, "glyph": "Pebrero", "phonetic": "[pɛ.ˈbɾɛ.ɾo]", "gloss": "February • 28/29 adlaw", "speakText": "Pebrero", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Pebrero.wav", "whisper": "February. Note the unaspirated 'p' and tapped 'r'."},
        {"id": "war_m3", "type": "month", "monthNum": 3, "glyph": "Marso", "phonetic": "[ˈmaɾ.so]", "gloss": "March • 31 adlaw", "speakText": "Marso", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Marso.wav", "whisper": "March. Clear tapped [ɾ] before the 's'."},
        {"id": "war_m4", "type": "month", "monthNum": 4, "glyph": "Abril", "phonetic": "[ab.ˈɾil]", "gloss": "April • 30 adlaw", "speakText": "Abril", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Abril.wav", "whisper": "April. Stress falls on the final syllable: ab-RIL."},
        {"id": "war_m5", "type": "month", "monthNum": 5, "glyph": "Mayo", "phonetic": "[ˈma.jo]", "gloss": "May • 31 adlaw", "speakText": "Mayo", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Mayo.wav", "whisper": "May. Month of the Flores de Mayo festivals in the Visayas."},
        {"id": "war_m6", "type": "month", "monthNum": 6, "glyph": "Hunyo", "phonetic": "[ˈhun.jo]", "gloss": "June • 30 adlaw", "speakText": "Hunyo", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Hunyo.wav", "whisper": "June. 'H' is pronounced breathy [h], followed by 'u' and palatal 'nyo'."},
        {"id": "war_m7", "type": "month", "monthNum": 7, "glyph": "Hulyo", "phonetic": "[ˈhul.jo]", "gloss": "July • 31 adlaw", "speakText": "Hulyo", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Hulyo.wav", "whisper": "July. Clear [l] and glide 'yo'."},
        {"id": "war_m8", "type": "month", "monthNum": 8, "glyph": "Agosto", "phonetic": "[a.ˈgos.to]", "gloss": "August • 31 adlaw", "speakText": "Agosto", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Agosto.wav", "whisper": "August. Samar Day is celebrated on Agosto 11!"},
        {"id": "war_m9", "type": "month", "monthNum": 9, "glyph": "Setyembre", "phonetic": "[sɛt.ˈjɛm.bɾɛ]", "gloss": "September • 30 adlaw", "speakText": "Setyembre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Setyembre.wav", "whisper": "September. Marks the beloved start of the Philippine Christmas season ('-ber months')!"},
        {"id": "war_m10", "type": "month", "monthNum": 10, "glyph": "Oktubre", "phonetic": "[ɔk.ˈtub.ɾɛ]", "gloss": "October • 31 adlaw", "speakText": "Oktubre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Oktubre.wav", "whisper": "October. Leyte Landing Day is commemorated every Oktubre 20 in MacArthur Landing Park."},
        {"id": "war_m11", "type": "month", "monthNum": 11, "glyph": "Nobyembre", "phonetic": "[nɔb.ˈjɛm.bɾɛ]", "gloss": "November • 30 adlaw", "speakText": "Nobyembre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Nobyembre.wav", "whisper": "November. Spelled with 'b' in modern Waray orthography (Nobyembre)."},
        {"id": "war_m12", "type": "month", "monthNum": 12, "glyph": "Disyembre", "phonetic": "[dɪs.ˈjɛm.bɾɛ]", "gloss": "December • 31 adlaw", "speakText": "Disyembre", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-Disyembre.wav", "whisper": "December. Month of Misa de Gallo and Christmas festivities."},
        {"id": "war_n11", "type": "date_num", "num": 11, "glyph": "11 — onse (napulo kag usa)", "phonetic": "[ˈon.sɛ] / [na.ˈpu.lo kag u.ˈsa]", "gloss": "Number 11", "speakText": "onse", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-onse.wav", "whisper": "For dates & clock time, speakers use Kinatsila 'onse' (e.g. 'onse de Agosto'); for counting items, native 'napulo kag usa'!"},
        {"id": "war_n12", "type": "date_num", "num": 12, "glyph": "12 — dose (napulo kag duha)", "phonetic": "[ˈdo.sɛ]", "gloss": "Number 12", "speakText": "dose", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-dose.wav", "whisper": "Twelve. Spanish-derived 'dose' for dates; 'napulo kag duha' for counting."},
        {"id": "war_n15", "type": "date_num", "num": 15, "glyph": "15 — kinse (napulo kag lima)", "phonetic": "[ˈkin.sɛ]", "gloss": "Number 15", "speakText": "kinse", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-kinse.wav", "whisper": "Fifteen. 'Ika-kinse hit Enero' = 15th of January."},
        {"id": "war_n20", "type": "date_num", "num": 20, "glyph": "20 — baynte (kaluhaan)", "phonetic": "[ˈbajn.tɛ]", "gloss": "Number 20", "speakText": "baynte", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-baynte.wav", "whisper": "Twenty. Kinatsila 'baynte'; native 'kaluhaan' (two tens)."},
        {"id": "war_n21", "type": "date_num", "num": 21, "glyph": "21 — baynte uno", "phonetic": "[ˈbajn.tɛ ˈu.no]", "gloss": "Number 21", "speakText": "baynte uno", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-baynte_uno.wav", "whisper": "Twenty-one. Notice Spanish loan 'uno' is paired with 'baynte' for calendar dates."},
        {"id": "war_n30", "type": "date_num", "num": 30, "glyph": "30 — trenta (katlu-an)", "phonetic": "[ˈtɾɛn.ta]", "gloss": "Number 30", "speakText": "trenta", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-trenta.wav", "whisper": "Thirty. Kinatsila 'trenta'; native Waray 'katlu-an' (three tens)."},
        {"id": "war_n31", "type": "date_num", "num": 31, "glyph": "31 — trenta y uno", "phonetic": "[ˈtɾɛn.ta i ˈu.no]", "gloss": "Number 31", "speakText": "trenta y uno", "audioUrl": "https://commons.wikimedia.org/wiki/Special:FilePath/LL-Q34279_(war)-trenta_y_uno.wav", "whisper": "Thirty-one. Final day of January, March, May, July, August, October, December."}
    ],
    "earGym": [
        {
            "prompt": "Listen to the audio. Which calendar date was spoken?",
            "speakAudio": "kinse de Enero",
            "options": ["January 15 (kinse de Enero)", "January 5 (singko de Enero)", "February 15 (kinse de Pebrero)"],
            "correct": 0,
            "explain": "'kinse de Enero' combines Kinatsila 'kinse' (15) + 'de' + 'Enero' (January)."
        },
        {
            "prompt": "Listen to the month name. Which month was pronounced?",
            "speakAudio": "Oktubre",
            "options": ["October (Oktubre)", "August (Agosto)", "September (Setyembre)"],
            "correct": 0,
            "explain": "'Oktubre' is the Waray spelling and pronunciation for October."
        },
        {
            "prompt": "Listen to the number. Is this 11 or 21?",
            "speakAudio": "onse",
            "options": ["11 (onse)", "21 (baynte uno)", "12 (dose)"],
            "correct": 0,
            "explain": "'onse' is the number 11 in Kinatsila."
        },
        {
            "prompt": "Listen to the question. What does Lolo Pedring ask?",
            "speakAudio": "Ika-pira hit bulan yana",
            "options": ["What is today's date? ('Ika-pira hit bulan yana?')", "What time is it?", "How many months are there?"],
            "correct": 0,
            "explain": "'Ika-pira hit bulan yana?' literally asks 'Which number of the month is today?'"
        }
    ],
    "sundial": [
        {
            "quest": "Santo Niño Festival (Tacloban City)",
            "clue": "Lolo Pedring: 'Set the calendar to January 15 (Ika-kinse de Enero)!'",
            "targetMonthIdx": 0,
            "targetDay": 15,
            "displayMonth": "Enero",
            "explain": "Enero 15 is the grand feast of the Santo Niño in Tacloban!"
        },
        {
            "quest": "Leyte Landing Commemoration",
            "clue": "Lolo Pedring: 'Mark October 20 (Ika-baynte de Oktubre) for the historic landing!'",
            "targetMonthIdx": 9,
            "targetDay": 20,
            "displayMonth": "Oktubre",
            "explain": "Oktubre 20 marks the historic 1944 return to Red Beach, Leyte."
        },
        {
            "quest": "Samar Province Foundation Day",
            "clue": "Lolo Pedring: 'Mark August 11 (Ika-onse de Agosto)!'",
            "targetMonthIdx": 7,
            "targetDay": 11,
            "displayMonth": "Agosto",
            "explain": "Agosto 11 is the official provincial foundation day of Samar."
        },
        {
            "quest": "Flores de Mayo (First of May)",
            "clue": "Lolo Pedring: 'Mark the first day of May (Primero de Mayo)!'",
            "targetMonthIdx": 4,
            "targetDay": 1,
            "displayMonth": "Mayo",
            "explain": "Primero de Mayo is the opening of May festivities across the islands."
        }
    ],
    "scribe": [
        {"clue": "Assemble the month of January:", "tiles": ["E", "N", "E", "R", "O", "P"], "answer": "ENERO", "gloss": "Enero (January)"},
        {"clue": "Assemble the date number 15 (Kinatsila):", "tiles": ["K", "I", "N", "S", "E", "O"], "answer": "KINSE", "gloss": "kinse (15)"},
        {"clue": "Assemble the month of December:", "tiles": ["D", "I", "S", "Y", "E", "M", "B", "R", "E"], "answer": "DISYEMBRE", "gloss": "Disyembre (December)"}
    ],
    "quiz": [
        {
            "q": "Why do Waray-Waray speakers use 'onse, dose, kinse' instead of 'napulo kag usa, napulo kag duha' when giving dates?",
            "options": [
                "Spanish loan numbers ('Kinatsila') are conventionally used for calendar dates and clock time, while native 'Ihap' counts objects!",
                "Native numbers cannot count past 10",
                "It depends purely on personal mood"
            ],
            "correct": 0,
            "explain": "Visayan languages typically maintain this functional duality: Kinatsila for dates/time and native Ihap for physical quantities."
        },
        {
            "q": "How do you ask 'What is today's date?' in Waray-Waray?",
            "options": ["Ika-pira hit bulan yana?", "Hain ka makadto?", "Hin-o it imo ngaran?"],
            "correct": 0,
            "explain": "'Ika-pira hit bulan yana?' means 'What date of the month is it today?'"
        },
        {
            "q": "Which prefix turns a number into an ordinal date in Waray (e.g. '15th')?",
            "options": ["ika- (e.g. ika-kinse, ika-lima)", "maka-", "taga-"],
            "correct": 0,
            "explain": "The prefix 'ika-' marks ordinal rank and dates: ika-kinse (15th), ika-duha (2nd)."
        },
        {
            "q": "What is the Waray name for the month of October?",
            "options": ["Oktubre", "Agosto", "Setyembre"],
            "correct": 0,
            "explain": "October is spelled 'Oktubre' in standard Waray orthography."
        },
        {
            "q": "How is 'January 15' spoken in everyday Visayan conversation?",
            "options": ["kinse de Enero (or ika-kinse hit Enero)", "tulo ka Enero", "napulo de Enero"],
            "correct": 0,
            "explain": "'kinse de Enero' is the most natural, widespread way to state January 15th."
        }
    ]
}

print("WARAY_STEP2 defined successfully.")

