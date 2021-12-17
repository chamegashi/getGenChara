import requests
from bs4 import BeautifulSoup
import time

def getImage():
    url = 'https://wikiwiki.jp/genshinwiki/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_tags = soup.find_all("img")

    print(img_tags)

    for tag in img_tags:
        print(tag)

    # response = requests.get(img_tag['src'])
    # image = response.content

    # with open("img/" + name, "wb") as f:
    #     f.write(image)
    
    # print("saved: " + name)

    
# text-align:center; width:300px;

if __name__ == "__main__":
    getImage()
