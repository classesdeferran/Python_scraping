# Librerias necesarias
import requests
from bs4 import BeautifulSoup


for number in range(1, 11):
    url = f'https://books.toscrape.com/catalogue/page-{number}.html'
    print(url)
    # pagina = requests.get(url)

