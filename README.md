# Reset mining world in modded server

This repository contains a python script to reset a mining world in a modded Minecraft server. The script is designed to be run on a Linux server and requires Python.

It was designed for the Epicraft server which had a world barrier and the only generation was in the mining world. The script is not designed to be used on a server with a normal world generation, but it can be modified to do so.

The mining world is a separate dimension that is used for mining and resource gathering. I used [DimX](https://www.curseforge.com/minecraft/mc-mods/dimx-extra-overworld-dimension) to have overworld generation but any mod providing an overworld dimension should work.

Note:
My minecraft server is running on `screen -R Epicraft` to keep it running in the background. If you are using a different method to run your server, you will need to modify the script accordingly.

## Requirements

see [requirements.txt](requirements.txt) for the full list of requirements

- Python 3.6 or higher
- Linux server
- Python libraries:
    - `os`
    - `discord`
    - `nbtlib`
    - `dotenv`

## Usage

This script is running in a cron job once a day. You just have to run reset_minage.sh

## Script Steps

1. Stop the server
2. Modify the level.dat of the world
3. Tp players in the mining dimension to the overworld spawn
4. Remove the mining world
5. Send a discord message to the server
6. Start the server
7. Pregenerate chunks in the mining world

## External Server

You can run this script on an other machine than the one running the minecraft server. You can use main_external.py to do so. It will use the client in paramiko_client.py.
