import requests
from bs4 import BeautifulSoup
import time

names = [
    "主人公",
    "アーロイ",
    "ジン",
    "アルベド",
    "ディルック",
    "エウルア",
    "クレー",
    "モナ",
    "ウェンティ",
    "刻晴",
    "七七",
    "胡桃",
    "ショウ",
    "鍾離",
    "甘雨",
    "楓原万葉",
    "神里綾華",
    "荒瀧一斗",
    "雷電将軍",
    "宵宮",
    "珊瑚宮心海",
    "タルタリヤ",
    "ベネット",
    "ガイア",
    "レザー",
    "ノエル",
    "ロサリア",
    "バーバラ",
    "スクロース",
    "リサ",
    "アンバー",
    "フィッシュル",
    "ディオナ",
    "行秋",
    "辛炎",
    "北斗",
    "重雲",
    "香菱",
    "煙緋",
    "凝光",
    "早柚",
    "トーマ",
    "九条裟羅",
    ]

def getImage(name):
    url = 'https://wikiwiki.jp/genshinwiki/' + name
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_tag = soup.find("img", height="500")
    name = ''.join(img_tag['alt'].split("500"))

    response = requests.get(img_tag['src'])
    image = response.content

    with open("img/" + name, "wb") as f:
        f.write(image)
    
    print("saved: " + name)

if __name__ == "__main__":
    for name in names:
        getImage(name)
        time.sleep(1)