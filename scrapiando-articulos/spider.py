import requests
from bs4 import BeautifulSoup

handlers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
#Extrayendo el html
def extraer_html(URL):
    try:
        respuesta = requests.get(URL, headers=handlers)
        respuesta.raise_for_status()
        return respuesta.content
    except:
        return None
    
#Obtener datos 
def obtener_datos(html):
        sopa = BeautifulSoup(html,"html.parser")
        busqueda_datos = sopa.find_all("div",{"class" : "promo-text"})[0:10]
        datos =  [dato.get_text(strip=True) for dato in busqueda_datos]
        return datos