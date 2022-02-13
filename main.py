import json
import os
import shutil

MC_ASSETS = 'C:/Users/l1nt3x/AppData/Roaming/.tlauncher/legacy/Minecraft/files/assets'
MC_VERSION = os.listdir(MC_ASSETS + "/indexes")[-1]
OUTPUT_PATH = 'C:/Users/l1nt3x/Desktop/MC_Sounds/'
MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION}"
MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
MC_SOUNDS = 'C:/Users/l1nt3x/AppData/Roaming/.tlauncher/legacy/Minecraft/files/sounds'

with open(MC_OBJECT_INDEX, "r") as read_file:
    data = json.load(read_file)
    sounds = {k: v["hash"] for (k, v) in data["objects"].items() if k[-3:]=='ogg'}
    for fpath, fhash in sounds.items():
        src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
        dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/sounds/{fpath}")
        os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
        shutil.copyfile(src_fpath, dest_fpath)
