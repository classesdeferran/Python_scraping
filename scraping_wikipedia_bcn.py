# Instalación de las librerias
# pip install requests
# pip install beautifulsoup4
# pip install pandas
# pip install lxml

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://es.wikipedia.org/wiki/Barcelona"

pagina = requests.get(url)

sopa = BeautifulSoup(pagina.text, 'html.parser' )
# print(sopa)

tablas = sopa.select(".collapsible")[0]
meteo_bcn = pd.read_html(str(tablas))[0]
export_csv = meteo_bcn.to_csv(r"csv/meteo-bcn.csv", index=None, header=True )