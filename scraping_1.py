# Instalación de las librerias
# pip install requests
# pip install beautifulsoup4
# pip install pandas
# pip install lxml

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.worldometers.info/world-population/population-by-country/"

pagina = requests.get(url)
# print(pagina.text)

sopa = BeautifulSoup(pagina.text )
# print(sopa)

# h1 = sopa.find("h1").getText()
# print(h1)

tabla = sopa.find("table")
# print(tabla)


df_poblacion = pd.read_html(str(tabla))[0]
# print(df_poblacion)
# df_poblacion.head()
# print(type(df_poblacion))

export_csv = df_poblacion.to_csv(r"csv/poblacion-mundial-2023.csv", index=None, header=True )