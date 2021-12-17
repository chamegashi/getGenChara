import requests
from bs4 import BeautifulSoup
import time

def getImage():
    url = 'https://pampulte.com/procecacharacter/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_tags = soup.find_all("img", width="768")

    for tag in img_tags:
        response = requests.get(tag['src'])
        image = response.content

        with open("proImage/" + tag["alt"] + ".jpg", "wb") as f:
            f.write(image)
        
        print("saved: " + tag["alt"])
        time.sleep(1)

if __name__ == "__main__":
    getImage()
