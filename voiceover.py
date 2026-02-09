import json
import os
import subprocess

GENERATED_DIR = "generated"
AUDIO_DIR = "audio"

os.makedirs(AUDIO_DIR, exist_ok=True)

latest_file = sorted(
    [f for f in os.listdir(GENERATED_DIR) if f.endswith(".json")]
)[-1]

with open(os.path.join(GENERATED_DIR, latest_file), "r") as f:
    data = json.load(f)

text = data["narration"]

output_audio = os.path.join(
    AUDIO_DIR, latest_file.replace(".json", ".mp3")
)

command = [
    "edge-tts",
    "--voice", "en-US-GuyNeural",
    "--text", text,
    "--write-media", output_audio
]

subprocess.run(command, check=True)

print("Voiceover generated:", output_audio)