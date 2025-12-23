# AtlasCivs Datapack


# Custom Recipes and Recipe Tweaks
Custom recipes are located in [data/atlas_custom_recipes/recipe](data/atlas_custom_recipes/recipe). These are mainly QoL improvements and additional recipes.

The [scripts/create_give_recipes_mcfunction.py](scripts/create_give_recipes_mcfunction.py) python script will be ran on each build. It gives the players
all of the custom recipes, but not the Minecraft override ones. If you are building locally, make sure to run this script. 

> [!IMPORTANT]
> Once the datapack is on the server, the recipe giver needs to be started with `/function atlas_custom_recipes:give_all_recipes`. Afterwards
it will be ran every 60 seconds to give any new players the recipes.

### Minecraft recipe overrides
Minecraft recipe overrides are located in [data/minecraft/recipe](data/minecraft/recipe).
These are recipes that remain unchanged, but increase the number of items granted per craft.
They are vanilla recipes sourced from the default Minecraft datapack, but have been modified using a Python script. 
The python script is located at [data/minecraft/recipe/edit_output_qty.py](data/minecraft/recipe/edit_output_qty.py).

> [!IMPORTANT]
> As Minecraft gets updates, be sure to update this folder.

> [!IMPORTANT]
> When adding files to the minecraft folder, be sure to only add the files you actually need. If you use the Search feature
> in your file browser, you may accidentally add unnecessary files.
> Additionally, when using the Python script, make sure the replace file variable starts with an `_` so you don't replace the wrong files.
> There are more details in the Python script about this.

# Rarity Loot Rewards
By running a single command, we can give a targeted player either diamonds, an item of [uncommon rarity](https://minecraft.wiki/w/Rarity#Uncommon), or [rare rarity](https://minecraft.wiki/w/Rarity#Rare). 
This is programmed under [data/atlas_rarity_loot](data/atlas_rarity_loot)

This is meant to serve as a reward for voting or reffering new players. 

Before this works, we need to create a scoreboard objective with `/scoreboard objectives add rarity_roll dummy` (only needs to be done once per world).
Then we can run `execute as @p run function rarity_loot:roll` where @p is a player's username.

> [!IMPORTANT]
> As Minecraft gets updates, the rarity tags will need to be updated with the new items. They are in [data/atlas_rarity_loot/tags/item](/data/atlas_rarity_loot/tags/item)

# General Stuff
### Enabling
The datapack should be loaded after Minecraft in order to ensure the overrides work. Enable the datapack with `/datapack enable <file> after vanilla`

### Contributing
Get approval from the admin team, and ensure your additions follow the conventions in this repository. 

### Helpful Resources
[Datapack Contents](https://minecraft.wiki/w/Data_pack#Contents)

[List of tag types (Java Edition)](https://minecraft.wiki/w/Tag_(Java_Edition)#List_of_tag_types)

[Recipe](https://minecraft.wiki/w/Recipe) 
