import requests
from bs4 import BeautifulSoup
import ArticleFinder
from ArticleFinder import Finder

f1 = Finder()
lists = f1.findArticle("bitcoin")
for i in lists:
    print(i)
print("\nTOTAL AMOUNT OF sites: " + str(len(lists)))
