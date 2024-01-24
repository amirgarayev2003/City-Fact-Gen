import requests
from bs4 import BeautifulSoup

wiki_page = requests.get('https://en.wikipedia.org/wiki/Reading,_Berkshire')


# HTML parser 
wiki_page = BeautifulSoup(wiki_page.content, 'html.parser')


# Find p tags inside wiki body containers 

wiki_page_body = wiki_page.find(id="bodyContent").find_all("p")

print(wiki_page_body)