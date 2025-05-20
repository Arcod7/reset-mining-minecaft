import nbtlib
import random

def modify_seed(level_dat_path: str, new_seed: int):
    print("\n-- Modifying seed --")
    level_dat = nbtlib.load(level_dat_path)
    level_dat["Data"]["WorldGenSettings"]["seed"] = nbtlib.Long(new_seed)
    level_dat.save()

    print(level_dat["Data"]["WorldGenSettings"]["seed"])

def tp_player_if_in_dimx(player_dat_path: str):
    print("\n-- Tp player if he's in the mining dimension --")
    SPAWN_POS = nbtlib.List([
        nbtlib.Double(-133.5),
        nbtlib.Double(74.5),
        nbtlib.Double(-38.5)
    ])

    player_dat = nbtlib.load(player_dat_path)
    if player_dat["Dimension"] == "dim_x:dimx":
        print("Player is in the mining dimension, teleporting him to the overworld")
        player_dat["Dimension"] = nbtlib.String("minecraft:overworld")
        player_dat["Pos"] = SPAWN_POS
        player_dat.save()

        return True

    print(player_dat["Dimension"])
    print(player_dat["Pos"])

    return False

def randomize_player_pos_and_dim(player_dat_path: str):
    print("\n-- Randomizing player pos and dimension --")

    random_pos = nbtlib.List([
        nbtlib.Double(random.randint(-4000, 4000)),
        nbtlib.Double(random.randint(1, 300)),
        nbtlib.Double(random.randint(-4000, 4000))
    ])

    if random.randint(0, 1) == 0:
        dimension = nbtlib.String("minecraft:overworld")
    else:
        dimension = nbtlib.String("dim_x:dimx")

    player_dat = nbtlib.load(player_dat_path)
    player_dat["Dimension"] = dimension
    player_dat["Pos"] = random_pos
    player_dat.save()

    print(player_dat["Dimension"])
    print(player_dat["Pos"])

