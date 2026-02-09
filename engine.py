from pathlib import Path
import random
import json

# ----- PATHS -----
OUTPUT_DIR = Path("generated")
OUTPUT_DIR.mkdir(exist_ok=True)

STORY_FILE = OUTPUT_DIR / "reddit_story.txt"
MEMORY_FILE = Path("engine_memory.json")

# ----- LOAD OR INIT MEMORY -----
if MEMORY_FILE.exists():
    memory = json.loads(MEMORY_FILE.read_text())
else:
    memory = {"used_topics": []}

# ----- SAMPLE REDDIT-STYLE TOPICS -----
topics = [
    "What’s a secret you’ve never told anyone?",
    "What’s the creepiest thing that happened to you at night?",
    "What’s a mistake that changed your life forever?",
    "What’s the most awkward thing you’ve witnessed?",
    "What’s something that sounds fake but is 100% real?"
]

# Prevent repeats
available = [t for t in topics if t not in memory["used_topics"]]
if not available:
    memory["used_topics"] = []
    available = topics

topic = random.choice(available)
memory["used_topics"].append(topic)

# ----- GENERATE STORY TEXT -----
story = f"""
Reddit asked:

{topic}

Here’s what someone replied:

I never thought I’d share this, but one night everything changed.
What started as a normal day ended with a moment I still think about.
I learned something about myself that night — and I’ll never forget it.
"""

story = story.strip()

# ----- WRITE STORY FILE -----
STORY_FILE.write_text(story, encoding="utf-8")

# ----- SAVE MEMORY -----
MEMORY_FILE.write_text(json.dumps(memory, indent=2))

print(f"Story written to {STORY_FILE}")