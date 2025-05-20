from paramiko_client import Client
import edit_dat
import random
from discord import SyncWebhook
from dotenv import load_dotenv
import os

load_dotenv()

# Credentials
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
PORT = int(os.getenv('PORT'))
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

client = Client(HOST, USERNAME, PASSWORD, PORT)

client.ftp.get("world/level.dat", "temp/level.dat")
player_dat_list = [file for file in client.ftp.listdir("world/playerdata") if file.endswith('.dat')]
for player_dat in player_dat_list:
    client.ftp.get(f"world/playerdata/{player_dat}", f"temp/{player_dat}")

seed = random.randint(-3000000000, 3000000000)
edit_dat.modify_seed("temp/level.dat", seed)
for player_dat in player_dat_list:
    edit_dat.tp_player_if_in_dimx(f"temp/{player_dat}")

client.ftp.put("temp/level.dat", "world/level.dat")
for player_dat in player_dat_list:
    client.ftp.put(f"temp/{player_dat}", f"world/playerdata/{player_dat}")

client.ftp.rmdir("world/dimensions/dim_x")
client.ftp.rmdir("dynmap/web/tiles/dim_x_dimx")
webhook = SyncWebhook.from_url(DISCORD_WEBHOOK_URL)
webhook.send("Venez découvrir la nouvelle map minage (seed " + str(seed) + "). Profitez en, elle ne dure que 23h42 ! :wink:")

