import whisper
import google.generativeai as genai
import os
from dotenv import load_dotenv
from prompts import MOM_PROMPT

# Load env
load_dotenv()

# Gemini setup
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ STABLE MODEL
model = genai.GenerativeModel("gemini-2.5-flash")

# Load whisper ONCE
WHISPER_MODEL = whisper.load_model("base")

def process_meeting(audio_path: str):
    try:
        # 1️⃣ Transcription
        result = WHISPER_MODEL.transcribe(audio_path)
        transcript = result.get("text", "").strip()

        if not transcript:
            return "No speech detected.", "MoM could not be generated."

        return transcript, None
    finally:
        # Cleanup temp file
        if os.path.exists(audio_path):
            os.remove(audio_path)

def generate_mom_from_text(transcript: str):
    # MoM generation from text
    prompt = MOM_PROMPT.format(transcript=transcript)
    response = model.generate_content(prompt)
    mom = response.text.strip() if response and response.text else "MoM generation failed."
    return mom
