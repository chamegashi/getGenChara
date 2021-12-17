import requests
from bs4 import BeautifulSoup
import time

def getImage(num):
    url = "https://s3.ap-northeast-1.amazonaws.com/gamewith/article_tools/apexlegends/gacha/weapon_" + str(num) + ".png"
    response = requests.get(url)
    image = response.content

    with open("weaponImg/" + str(num) + ".png", "wb") as f:
        f.write(image)

    print("saved: " + str(num) + ".png")


# text-align:center; width:300px;

if __name__ == "__main__":
    for index in range(28):
        getImage(index+1)
        time.sleep(1)