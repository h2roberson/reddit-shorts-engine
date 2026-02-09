import json
import os
import random
from datetime import datetime

os.makedirs("generated", exist_ok=True)

MEMORY_FILE = "engine_memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {"used_topics": []}

topics = [
    "roommate horror story",
    "relationship betrayal",
    "family secret",
    "workplace nightmare",
    "creepy coincidence"
]

available_topics = [t for t in topics if t not in memory["used_topics"]]

if not available_topics:
    memory["used_topics"] = []
    available_topics = topics

topic = random.choice(available_topics)
memory["used_topics"].append(topic)

hooks = {
    "roommate horror story": "I thought my roommate was normal until this happened",
    "relationship betrayal": "I ignored the red flags and it cost me everything",
    "family secret": "I found out something about my family I wish I didn’t know",
    "workplace nightmare": "I should’ve quit my job when this happened",
    "creepy coincidence": "This coincidence still doesn’t make sense"
}

story_templates = {
    "roommate horror story": [
        "I moved in with my roommate because rent was cheap and everything seemed fine at first.",
        "About a month in, I started noticing small things going missing. At first, I blamed myself.",
        "One night, I came home early and saw something I was never meant to see.",
        "I moved out the next morning without telling them why."
    ],
    "relationship betrayal": [
        "We had been together for years and I trusted them completely.",
        "People warned me about the signs but I ignored them.",
        "One night, I accidentally saw a message that wasn’t meant for me.",
        "That was the moment everything fell apart."
    ],
    "family secret": [
        "Growing up, there was always something my family refused to talk about.",
        "I didn’t think much of it until I found a box hidden in the attic.",
        "Inside were documents that explained everything.",
        "I’ve never looked at my family the same since."
    ],
    "workplace nightmare": [
        "My job started out perfect and the pay was decent.",
        "Then management changed and things became uncomfortable fast.",
        "What finally happened crossed a line I didn’t know existed.",
        "HR told me it was best to stay quiet."
    ],
    "creepy coincidence": [
        "I don’t believe in coincidences, but this made me question everything.",
        "It started with something small that I brushed off.",
        "Then it happened again in a way I couldn’t ignore.",
        "I still can’t explain how this was possible."
    ]
}

hook = hooks[topic]
story_paragraphs = story_templates[topic]

output = {
    "hook": hook,
    "story": story_paragraphs,
    "cta": "Follow for more real Reddit stories",
    "background_style": "Subway Surfers or Minecraft parkour",
    "estimated_duration_seconds": 50
}

filename = f"generated/{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, "w") as f:
    json.dump(output, f, indent=2)

with open(MEMORY_FILE, "w") as f:
    json.dump(memory, f, indent=2)

print("Generated story:", filename)