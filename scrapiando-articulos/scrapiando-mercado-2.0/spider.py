from bs4 import BeautifulSoup
import requests
import logging

class Scraper:
    def __init__(self, url=None):
        self.url = url or "https://www.bbc.com/mundo/topics/cyx5krnw38vt"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
        }

    def extraer_html(self):
        try:
            respuesta = requests.get(self.url, headers=self.headers)
            respuesta.raise_for_status()
            return respuesta.content
        except requests.RequestException as e:
            logging.error(f"Error al extraer HTML: {e}")
            return None

    def extraer_datos(self):
        try:
            html = self.extraer_html()
            if not html:
                return None

            sopa = BeautifulSoup(html, "html.parser")
            articulos = sopa.find_all("div", {"class": "promo-text"})[0:10]
            return [articulo.get_text(strip=True).text for articulo in articulos]
        except Exception as e:
            logging.error(f"Error al extraer datos: {e}")
            return None



