#This program was first written to help me sort the tiny tower floors in ascending order in terms of level 10 stock.
import bs4, requests, logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def getLvlTenStock(floorName) :
    #get the level ten stock number of a particular floor given the floor name
    logging.debug("Start of getLvlTenStock")
    url = makeUrl(floorName)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select("div.tabbertab:nth-child(10) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3)")

    if len(elems[0]) > 1:
        element = elems[0].text.strip()
    else:
        element = elems[0].text
    logging.debug(element)
    return(element)

def makeUrl(shopName) :
    #returns url of particular floor on wiki when given the floor name
    logging.debug("Start of makeUrl")
    shopName = list(shopName.split())
    shop = shopName[0].capitalize()
    if len(shop) > 1 :
        for word in shopName[1:] :
            logging.debug(shop)
            shop += '_' + word.capitalize()
    logging.debug("makeUrl : https://tinytower.fandom.com/wiki/" + shop + "#Level_10")
    return("https://tinytower.fandom.com/wiki/" + shop + "#Level_10")

print("Product stock is " + getLvlTenStock("donut shop"))



