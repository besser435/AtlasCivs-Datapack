execute store result score @s atlas_rarity_roll run random value 1..100


execute if score @s atlas_rarity_roll matches 1..5 run function atlas_rarity_loot:give_rare
execute if score @s atlas_rarity_roll matches 6..30 run function atlas_rarity_loot:give_uncommon
execute if score @s atlas_rarity_roll matches 31..100 run function atlas_rarity_loot:give_diamonds
