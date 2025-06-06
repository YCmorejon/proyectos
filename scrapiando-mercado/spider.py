from bs4 import BeautifulSoup
import requests

#Extraer html
def extraer_html(URL):
    try:
        respuesta = requests.get(URL)
        respuesta.raise_for_status()
        return respuesta.content
    except Exception as e:
        print(f"Error al intentar realizar la petición : {e}")
        
#Parsear html y obtener datos
def obtener_html(html):
    sopa = BeautifulSoup(html,"html.parser")
    busqueda = sopa.find_all("div",{"class" : "poly-card__content"})[0:5]
    nombre =[dato.find("span",{"class" : "poly-component__brand"}) for dato in busqueda]
    precio = [dato.find("div",{"class" : "poly-price__current"}) for dato in busqueda]
    return nombre.text,precio.text