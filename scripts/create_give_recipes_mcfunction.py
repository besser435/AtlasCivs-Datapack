import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# === CONFIG ===
DATAPACK_PATH = os.path.join("..")
NAMESPACE = "atlas_custom_recipes"

# Output function file path
OUTPUT_FUNCTION = os.path.join(
    DATAPACK_PATH,
    "data",
    NAMESPACE,
    "function",
    "give_all_recipes.mcfunction"
)


# === SCRIPT ===
recipe_dir = os.path.join(DATAPACK_PATH, "data", NAMESPACE, "recipe")

print(f"Looking for recipes in: {recipe_dir}")

if not os.path.isdir(recipe_dir):
    raise FileNotFoundError(f"Could not find recipe folder: {recipe_dir}")

recipes = []

# Recursively walk through all subfolders
for root, _, files in os.walk(recipe_dir):
    for file in files:
        if file.endswith(".json"):
            # path relative to the recipes folder, without ".json"
            rel_path = os.path.relpath(os.path.join(root, file), recipe_dir)
            recipe_id = f"{NAMESPACE}:{rel_path[:-5].replace(os.sep, '/')}"
            recipes.append(recipe_id)

# Write the mcfunction file
os.makedirs(os.path.dirname(OUTPUT_FUNCTION), exist_ok=True)
with open(OUTPUT_FUNCTION, "w", encoding="utf-8") as f:
    for recipe in sorted(recipes):  # sort for consistency
        f.write(f"recipe give @a {recipe}\n")

    # Run again to ensure any new players that joined have the recipes
    f.write("schedule function atlas_custom_recipes:give_all_recipes 60s")

print(f"Generated {OUTPUT_FUNCTION} with {len(recipes)} recipes.")
