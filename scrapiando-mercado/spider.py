from bs4 import BeautifulSoup
import requests

#Datos necesarios para realizar la petición get
handlers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

#Extraer html
def extraer_html(URL):
    try:
        respuesta = requests.get(URL, headers=handlers)
        respuesta.raise_for_status()
        return respuesta.content
    except Exception as e:
        print(f"Error al intentar realizar la petición : {e}")
        
#Parsear html y obtener datos
def obtener_datos(html):
    sopa = BeautifulSoup(html,"html.parser")
    busqueda = sopa.find_all("div",{"class" : "poly-card__content"})[0:5]
    nombre =[dato.find("span",{"class" : "poly-component__brand"}) for dato in busqueda]
    precio = [dato.find("div",{"class" : "poly-price__current"}) for dato in busqueda]
    return nombre,precio