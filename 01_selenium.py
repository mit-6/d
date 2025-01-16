from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# quary = input("Enter Product which you find: ")

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome()

# Go to the Flipkart search page
quary = 'laptop'
url = f"https://www.flipkart.com/search?q={quary}&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=c01419dc-d942-435b-95af-9bbb06d559bf"
driver.get(url)
print(url)

# Wait a bit for the page to load (you can also use WebDriverWait for more control)
driver.implicitly_wait(5)

data = {'title': [], 'price': [], 'link':[]}
product = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
price = driver.find_elements(By.CLASS_NAME, "Nx9bqj._4b5DiR")
link = driver.find_elements(By.CLASS_NAME, 'CGtC98')

# print(product.text)
# print(len(elems))
# print(elem.get_attribute("outerHTML"))

for i in product:
    # print(i.text)
    data['title'].append(i.text)
    
for i in price:
    # print(i.text)
    data['price'].append(i.text[1::])

for i in link:
    # print(i.get_attribute("href"))
    data['link'].append(i.get_attribute("href"))


# create data.csv file of Mobil Name and Price.
df = pd.DataFrame.from_dict(data)
df.to_csv("web_scraping/data_from_selenium.csv",index=False)
# Close the browser
driver.quit()
