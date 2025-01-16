import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=c01419dc-d942-435b-95af-9bbb06d559bf"

r =requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)

# spans = soup.find("html")
# print(soup.spam)
# print(soup.find("span"))

data = {'title': [], 'price': []}
mobil_name = soup.find_all(class_="KzDlHZ")
mobil_price = soup.find_all(class_="Nx9bqj _4b5DiR")

for i in mobil_name:
    # print(i.string)
    data['title'].append(i.string)

for price in mobil_price:
    # print(price.string)
    data['price'].append(price.string[1:])



# create data.csv file of Mobil Name and Price.
# df = pd.DataFrame.from_dict(data)
# df.to_csv("web_scraping/data.csv",index=False)

