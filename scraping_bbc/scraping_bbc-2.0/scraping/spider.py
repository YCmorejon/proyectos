import requests
from bs4 import BeautifulSoup


#Hacer petición get y obtener el html
def obtener_html(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.content
    except :
        print("[ERROR] No se pudo obtener la página")
        return None

#Parsea el HTML y devuelve los primeros títulos encontrados
def extraer_titulos(html, cantidad=10):
    sopa = BeautifulSoup(html, "html.parser")
    elementos = sopa.find_all("div", {"class": "promo-text"})[:cantidad]
    titulos = [elem.get_text(strip=True) for elem in elementos]
    return titulos
