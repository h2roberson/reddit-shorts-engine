from pathlib import Path
from gtts import gTTS

# ----- FILE PATHS -----
TEXT_FILE = Path("generated/reddit_story.txt")
AUDIO_DIR = Path("audio")
OUTPUT_AUDIO = AUDIO_DIR / "voiceover.mp3"

# ----- VALIDATE STORY FILE -----
if not TEXT_FILE.exists():
    raise FileNotFoundError("generated/reddit_story.txt not found")

text = TEXT_FILE.read_text(encoding="utf-8").strip()

if not text:
    raise ValueError("Story text is empty")

# ----- CREATE AUDIO DIRECTORY -----
AUDIO_DIR.mkdir(exist_ok=True)

# ----- GENERATE VOICEOVER -----
tts = gTTS(text=text, lang="en", slow=False)
tts.save(str(OUTPUT_AUDIO))

print(f"Voiceover generated successfully: {OUTPUT_AUDIO}")