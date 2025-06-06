import requests
from bs4 import BeautifulSoup
import logging

handlers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

def extraer_html(URL):
    try:
        respuesta = requests.get(URL, headers=handlers)
        respuesta.raise_for_status()
        return respuesta.content
    except requests.RequestException as e:
        logging.error(f"Error al realizar la petición: {e}")
        return None

def obtener_datos(html):
    try:
        sopa = BeautifulSoup(html, "html.parser")
        busqueda = sopa.find_all("div", {"class": "poly-card__content"})[0:5]
        nombre = [dato.find("span", {"class": "poly-component__brand"}) for dato in busqueda]
        precio = [dato.find("div", {"class": "poly-price__current"}) for dato in busqueda]
        
        # Validar que se encontraron datos
        if not nombre or not precio:
            logging.warning("No se encontraron algunos elementos en la página")
            return None, None
            
        return nombre, precio
    except Exception as e:
        logging.error(f"Error al parsear HTML: {e}")
        return None, None