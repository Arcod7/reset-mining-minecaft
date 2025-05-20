import os
import shutil
import random
from discord import SyncWebhook
import edit_dat
from dotenv import load_dotenv

load_dotenv()

MINECRAFT_SERVER_PATH = os.getenv('MINECRAFT_SERVER_PATH')

# Paths
base_dir = os.path.expanduser(MINECRAFT_SERVER_PATH)
world_dir = os.path.join(base_dir, "world")
temp_dir = os.path.join(base_dir, "reset_minage", "temp")

# Ensure temp directory exists
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

# Copy level.dat and playerdata files to temp
shutil.copy(os.path.join(world_dir, "level.dat"), os.path.join(temp_dir, "level.dat"))
player_dat_list = [f for f in os.listdir(os.path.join(world_dir, "playerdata")) if f.endswith('.dat')]

for player_dat in player_dat_list:
    shutil.copy(os.path.join(world_dir, "playerdata", player_dat), os.path.join(temp_dir, player_dat))

# Modify seed and player data
seed = random.randint(-3000000000, 3000000000)
edit_dat.modify_seed(os.path.join(temp_dir, "level.dat"), seed)

for player_dat in player_dat_list:
    edit_dat.tp_player_if_in_dimx(os.path.join(temp_dir, player_dat))

# Move modified files back to world directory
shutil.copy(os.path.join(temp_dir, "level.dat"), os.path.join(world_dir, "level.dat"))
for player_dat in player_dat_list:
    shutil.copy(os.path.join(temp_dir, player_dat), os.path.join(world_dir, "playerdata", player_dat))

# Remove dimension and dynmap files
shutil.rmtree(os.path.join(world_dir, "dimensions", "dim_x"), ignore_errors=True)
shutil.rmtree(os.path.join(base_dir, "dynmap", "web", "tiles", "dim_x_dimx"), ignore_errors=True)

# Send Discord notification
webhook = SyncWebhook.from_url(DISCORD_WEBHOOK_URL)
webhook.send(f"Venez découvrir la nouvelle map minage (seed {seed}). Profitez en, elle ne dure que 23h42 ! :wink:")
