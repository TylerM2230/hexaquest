#!/usr/bin/env python3
"""
Meta MMS (Massively Multilingual Speech) Audio Generator for HexaQuest
---------------------------------------------------------------------
Generates natural neural audio .wav files for Waray-Waray, Latin, and other
low-resource languages using Meta's VITS checkpoints from Hugging Face.

Requirements:
    pip install transformers accelerate torch scipy

Usage:
    python3 generate_mms_audio.py --lang war --output-dir ./audio/waray
"""

import os
import argparse

# Language checkpoints on Hugging Face (Meta MMS-TTS)
MMS_MODELS = {
    "war": "facebook/mms-tts-war",   # Waray-Waray
    "lat": "facebook/mms-tts-lat",   # Latin
    "heb": "facebook/mms-tts-heb",   # Hebrew
    "cmn": "facebook/mms-tts-cmn",   # Mandarin Chinese
    "fra": "facebook/mms-tts-fra",   # French
    "deu": "facebook/mms-tts-deu",   # German
}

VOCAB_STEP_1 = {
    "war": {
        "num_0": "waray",
        "num_1": "usa",
        "num_2": "duha",
        "num_3": "tulo",
        "num_4": "upat",
        "num_5": "lima",
        "num_6": "unom",
        "num_7": "pito",
        "num_8": "walo",
        "num_9": "siyam",
        "num_10": "napulo",
        "glottal_stop": "may-ada",
        "ng_consonant": "ngaran",
        "greeting": "maupay nga adlaw"
    },
    "lat": {
        "num_0": "nihil",
        "num_1": "unus",
        "num_2": "duo",
        "num_3": "tres",
        "num_4": "quattuor",
        "num_5": "quinque",
        "num_6": "sex",
        "num_7": "septem",
        "num_8": "octo",
        "num_9": "novem",
        "num_10": "decem"
    }
}

VOCAB_STEP_2 = {
    "war": {
        "m_enero": "Enero", "m_pebrero": "Pebrero", "m_marso": "Marso",
        "m_abril": "Abril", "m_mayo": "Mayo", "m_hunyo": "Hunyo",
        "m_hulyo": "Hulyo", "m_agosto": "Agosto", "m_setyembre": "Setyembre",
        "m_oktubre": "Oktubre", "m_nobyembre": "Nobyembre", "m_disyembre": "Disyembre",
        "num_11": "onse", "num_12": "dose", "num_15": "kinse",
        "num_20": "baynte", "num_21": "baynte uno", "num_30": "trenta", "num_31": "trenta y uno",
        "date_phrase_1": "kinse de Enero", "date_phrase_2": "Ika-pira hit bulan yana"
    },
    "lat": {
        "m_ianuarius": "Ianuarius", "m_februarius": "Februarius", "m_martius": "Martius",
        "m_aprilis": "Aprilis", "m_maius": "Maius", "m_iunius": "Iunius",
        "m_iulius": "Iulius", "m_augustus": "Augustus", "m_september": "September",
        "m_october": "October", "m_november": "November", "m_december": "December",
        "num_11": "undecim", "num_12": "duodecim", "num_15": "quindecim",
        "num_18": "duodeviginti", "num_19": "undeviginti", "num_20": "viginti",
        "date_phrase_1": "Idus Martiae", "date_phrase_2": "Kalendae Ianuariae"
    }
}

def generate_audio(lang: str, output_dir: str, step: int = 1):
    try:
        from transformers import VitsModel, AutoTokenizer
        import torch
        import scipy.io.wavfile
    except ImportError:
        print("Missing dependencies! Please run:")
        print("  pip install transformers accelerate torch scipy")
        return

    model_id = MMS_MODELS.get(lang)
    if not model_id:
        print(f"Language '{lang}' not in supported MMS models list: {list(MMS_MODELS.keys())}")
        return

    print(f"Loading Meta MMS checkpoint: {model_id}...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = VitsModel.from_pretrained(model_id)

    os.makedirs(output_dir, exist_ok=True)
    vocab = VOCAB_STEP_1.get(lang, {}) if step == 1 else VOCAB_STEP_2.get(lang, {})
    if not vocab:
        print(f"No preset vocabulary for '{lang}' in Step {step}.")
        return

    torch.manual_seed(42)  # For reproducible duration prediction
    print(f"Synthesizing Step {step} ({len(vocab)} audio assets) to '{output_dir}'...")

    for key, text in vocab.items():
        print(f"  Generating [{key}] -> '{text}'...")
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            output = model(**inputs).waveform

        waveform = output.squeeze().cpu().numpy()
        filepath = os.path.join(output_dir, f"{key}.wav")
        scipy.io.wavfile.write(filepath, rate=model.config.sampling_rate, data=waveform)

    print(f"Synthesis complete! All Step {step} audio files generated successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Meta MMS Audio for HexaQuest")
    parser.add_argument("--lang", default="war", choices=list(MMS_MODELS.keys()), help="Target language code")
    parser.add_argument("--output-dir", default="./audio/waray", help="Destination folder for .wav files")
    parser.add_argument("--step", type=int, default=1, choices=[1, 2], help="Curriculum step (1 or 2)")
    args = parser.parse_args()
    generate_audio(args.lang, args.output_dir, step=args.step)

