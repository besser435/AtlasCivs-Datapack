import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

"""
The files here are from the vanilla Minecraft datapack, but with
updated output quantities. Since there are many files, updating them manually would suck.
This automates the process.

When copying files from the Minecraft datapack, be sure to not include anything that is out of place.
Ex, iron trapdoors output 1, and have a different recipe pattern than wooden trapdoors, so you wouldn't 
want to change that.
"""

FILENAME_TO_MATCH = "_door.json"   # Match files that end with this. 
# ENSURE THERE IS AN UNDERSCORE!!!
# If you dont include an underscore, you might match other things. Ex, door.json would also match trapdoor.json
NEW_OUTPUT_QTY = 4                  # New output quantity
_MINECRAFT_OVERRIDE_PATH = r"../data/minecraft/recipe"

for root, dirs, files in os.walk(_MINECRAFT_OVERRIDE_PATH):
    for filename in files:
        if filename.endswith(FILENAME_TO_MATCH):
            filepath = os.path.join(root, filename)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)

                if isinstance(data.get("result"), dict):
                    old_count = data["result"].get("count", None)
                    data["result"]["count"] = NEW_OUTPUT_QTY

                    with open(filepath, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)

                    print(f"Updated {filepath}: {old_count} -> {NEW_OUTPUT_QTY}")
                else:
                    print(f"Skipped {filepath} (no result.count found)")

            except Exception as e:
                print(f"Error processing {filepath}: {e}")
