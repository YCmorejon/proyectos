import requests
from bs4 import BeautifulSoup
import logging

#Handlers
handlers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

#Extraer html
def extraer_html(URL):
    try:
        respuesta = requests.get(URL, headers=handlers)
        respuesta.raise_for_status()
        return respuesta.content
    except Exception as e:
        logging.error(f"Ha ocurrido un error {e}")

#Parsear el html y obtener los datos persistentes
def obtener_datos(html):
    try:
        sopa = BeautifulSoup(html,"html.parser")
        busqueda = sopa.find_all("div",{"class" : "promo-text"})
        articulos = ""
        return articulos
    except:
        pass