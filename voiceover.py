from gtts import gTTS
from pathlib import Path
import json

# Paths
TEXT_FILE = Path("generated/reddit_story.txt")
AUDIO_DIR = Path("audio")
AUDIO_DIR.mkdir(exist_ok=True)
OUTPUT_AUDIO = AUDIO_DIR / "voiceover.mp3"

# Validate input
if not TEXT_FILE.exists():
    raise FileNotFoundError("reddit_story.txt not found")

text = TEXT_FILE.read_text(encoding="utf-8").strip()

if not text:
    raise ValueError("Story text is empty")

# Generate audio
tts = gTTS(text=text, lang="en", slow=False)
tts.save(str(OUTPUT_AUDIO))

print(f"Voiceover generated: {OUTPUT_AUDIO}")