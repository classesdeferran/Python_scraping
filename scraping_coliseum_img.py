import requests
from bs4 import BeautifulSoup

url = "https://www.centrocoliseum.com/"
pagina = requests.get(url)

sopa = BeautifulSoup(pagina.text, 'html.parser')

ruta_imatge = sopa.select(".size-large")[0]['src']
# print(imatge)

imatge_desc = requests.get(ruta_imatge)
# print(imatge_desc.text)
f = open("img/img-1.jpg", "wb")
f.write(imatge_desc.content)

f.close()