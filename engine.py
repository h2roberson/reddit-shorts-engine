import json
import os
from datetime import datetime
import random

# Create output directory if it doesn't exist
os.makedirs("generated", exist_ok=True)

MEMORY_FILE = "engine_memory.json"

# Load or initialize memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {"used_hooks": []}

hooks = [
    "This Reddit post ruined my night",
    "I shouldn’t have opened this thread",
    "This escalated way too fast",
    "Reddit wasn’t ready for this",
    "I wish I never read this story"
]

available = [h for h in hooks if h not in memory["used_hooks"]]

if not available:
    memory["used_hooks"] = []
    available = hooks

hook = random.choice(available)
memory["used_hooks"].append(hook)

output = {
    "hook": hook,
    "format": "Reddit Short",
    "background": "Subway Surfers or Minecraft",
    "voiceover": hook
}

filename = f"generated/{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, "w") as f:
    json.dump(output, f, indent=2)

with open(MEMORY_FILE, "w") as f:
    json.dump(memory, f, indent=2)

print("Generated:", filename)
