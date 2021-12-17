import os
import json

def makeCharaJsonData():
    name_list = os.listdir("./img")
    ret_data = []
    for name in name_list:
        ret_data.append({
            "name": name[:-4],
            "file": name
        })
    return ret_data

def makeWeaponJsonData():
    name_list = os.listdir("./weaponImg")
    ret_data = []
    for name in name_list:
        ret_data.append({
            "name": name[:-4],
            "file": name
        })
    return ret_data

def makeProJsonData():
    name_list = os.listdir("./proImage")
    ret_data = []
    for name in name_list:
        ret_data.append({
            "name": name[:-4],
            "file": name
        })
    return ret_data

def makeJson(json_data, filename):
    with open('./' + filename + '.json', 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    makeJson(makeCharaJsonData(), "genshin")
    makeJson(makeWeaponJsonData(), "weapon")
    makeJson(makeProJsonData(), "proseka")
