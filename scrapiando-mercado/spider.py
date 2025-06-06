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