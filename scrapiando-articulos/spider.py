import requests
from bs4 import BeautifulSoup

#Extrayendo el html
def extraer_html(URL):
    try:
        respuesta = requests.get(URL)
        respuesta.raise_for_status()
        return respuesta.content
    except:
        return None 
    

#Obtener datos 
def obtener_datos(html):
    if html:
        sopa = BeautifulSoup(html,"html.parser")
        busqueda = sopa.find_all("div",{"class" : "promo-text"})
        return busqueda