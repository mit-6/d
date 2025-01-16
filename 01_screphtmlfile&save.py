import requests

def fatchandsave(url, path):
    r = requests.get(url)      # get url
    with open(path, 'w') as file:
        file.write(r.text)    # to write text in to saved filr

url = "https://ahduni.edu.in/"

fatchandsave(url, "web_scraping/Ahmedabad_university.html")