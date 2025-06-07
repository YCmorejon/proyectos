import requests
from bs4 import BeautifulSoup
import logging

class SimpleScraper:
    """Scraper simple para extraer artículos de BBC Mundo"""
    
    def __init__(self):
        self.url = "https://www.bbc.com/mundo/topics/cyx5krnw38vt"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def obtener_articulos(self):
        """Método único que maneja todo el proceso de scraping"""
        try:
            # Obtener HTML
            respuesta = requests.get(self.url, headers=self.headers)
            respuesta.raise_for_status()
            
            # Parsear contenido
            sopa = BeautifulSoup(respuesta.content, "html.parser")
            articulos = sopa.find_all("div", {"class": "promo-text"})[0:10]
            
            # Extraer texto
            return [articulo.get_text(strip=True) for articulo in articulos]
            
        except Exception as e:
            logging.error(f"Error durante el scraping: {e}")
            return []



