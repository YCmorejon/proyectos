import requests
from bs4 import BeautifulSoup

#Headers para realizar la petición get
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

#Obteniendo el html
def obtener_html(URL):
    try:
        respuesta = requests.get(URL,headers=headers)
        return respuesta.content
    except Exception as e:
        print(f"Error al obtener el html : {e}")
        

#Extraer datos pertinenetes(citas , autor y etiquetas)
def extraer_datos(html):
    #Html parseado
    sopa = BeautifulSoup(html,"html.parser")
    # Extracción madre y datos pertinentes
    try:
        busqueda = sopa.find_all("div", {"class": "quote"})
        citas = [item.find("span", {"class": "text"}).text for item in busqueda]
        autor = [item.find("small", {"class": "author"}).text for item in busqueda]
        etiquetas = [
            ", ".join([tag.text for tag in item.find_all("a", class_="tag")])
            for item in busqueda
        ]
        return citas, autor, etiquetas
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        return None
