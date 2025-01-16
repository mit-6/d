import requests
from bs4 import BeautifulSoup

with open('web_scraping/sample.html', 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find("h2"))

# print(soup.prettify()) # Display all document
# print(soup.title, type(soup.title))  # Show title of document and also show type of title
# print(soup.title.string) # See only title name not show tags

# print(soup.div) # to show first div tag
# print(soup.find_all("div")) # to show all div in document.

# for link in soup.find_all("a"):
#     # print(link) # to show all link in doc.
#     print(link.get("href")) # Get only links don't show tags
#     print(link.get_text()) # return text from anker tag.

# print(soup.find(id="link2")) # return given id content

## Modifing code
# cont = soup.find(class_="cont")
# cont.name = "spam"  # to change tag name div to spam
# cont['class'] = "new_cont" # to change class name
# cont['id'] = "new_ID" # to change id name
# cont.string = "Modifing new text in this tag using scraping(Beautiful Soup)."
# print(cont)


## create new tag
# ultag = soup.new_tag("ul") # to create new tag is ul

# litag = soup.new_tag('li')
# litag.string = "Home" # add string in li tag
# ultag.append(litag) # to appned litage content in ul tag

# litag = soup.new_tag('li')
# litag.string = "About" # add string in li tag
# ultag.append(litag) # to appned litage content in ul tag

# soup.html.body.insert(2, ultag) # give possion to add this new tag
# print(soup)


## To return if attribute is in or not in that tag.
# print(soup.find('div').has_attr("class")) 
# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# result = soup.find_all(has_class_but_not_id)
# for i in result:
#     print(i, "\n\n")



