# Librerias necesarias
import requests
from bs4 import BeautifulSoup

# ruta a scrapear
url = "https://www.centrocoliseum.com/"
# descargamos el código, que quedará como string
pagina = requests.get(url)

# lo reconvertimos a html
sopa = BeautifulSoup(pagina.text, 'html.parser')

'''
# Ejemplo de descarga de una sola imagen
ruta_imatges = sopa.select(".size-large")[0]['src']
# Se descarga código binario
# print(ruta_imatges)
imatge_desc = requests.get(ruta_imatges)
# print(imatge_desc.text)
f = open("img/img-1.jpg", "wb")
f.write(imatge_desc.content)
'''

ruta_imatges = sopa.select(".size-large")
indice = 1
for img in ruta_imatges:
    ruta_imatge = img['src']
    imatge_desc = requests.get(ruta_imatge)
    f = open("img/imagen-" + str(indice) + ".jpg", "wb")
    f.write(imatge_desc.content)
    indice += 1
    f.close()












etiquetes_imatges = sopa.select(".size-large")
contador = 1
for etiqueta_imatge in etiquetes_imatges:
    ruta_imatge = etiqueta_imatge['src']
    imatge_desc = requests.get(ruta_imatge)
    f = open("img/img-" + str(contador) + ".jpg", "wb")
    f.write(imatge_desc.content)
    contador += 1

f.close()