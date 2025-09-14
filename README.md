# AtlasCivs Datapack

## Enabling
The datapack should be loaded after Minecraft in order to ensure the overrides work. Enable the datapack with `/datapack enable <file> after vanilla`

## Custom recipes
Custom recipes are located in [data/atlas_custom/recipe](data/atlas_custom/recipe). These are mainly QoL improvements and additional recipes.

## Minecraft recipe overrides
Minecraft recipe overrices are located in [data/minecraft/recipe](data/minecraft/recipe).
These are recipes that remain unchanged, but increase the number of items granted per craft.
They are vanilla recipes sourced from the default Minecraft datapack, but have been modified using a Python script. 
The python script is located at [data/minecraft/recipe/edit_output_qty.py](data/minecraft/recipe/edit_output_qty.py).
As Minecraft gets updates, be sure to update this folder.

> [!IMPORTANT]
> When adding files to the minecraft folder, be sure to only add the files you actually need. If you use the Search feature
> in your file browser, you may accidentally add uncessicary files.
> Aditionally, when using the Python script, make sure the replace file variable starts with an `_` so you don't replace the wrong files.
> There are more details in the Python script about this.

## Contribuing
Get approval from bca, and ensure your additions follow the conventions in this repository. 

### Helpful Resources
[Datapack Contents](https://minecraft.wiki/w/Data_pack#Contents) 
[List of tag types (Java Edition)](https://minecraft.wiki/w/Tag_(Java_Edition)#List_of_tag_types)
