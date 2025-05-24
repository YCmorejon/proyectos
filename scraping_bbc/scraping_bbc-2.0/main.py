from scraping.spider import obtener_html,extraer_titulos
import pandas as pd
import logging

#Dirección de donde se extraen los artículos
URL = "https://www.bbc.com/mundo/topics/cyx5krnw38vt"
OUTPUT_FILE = "titulos.csv"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    html = obtener_html(URL)
    if html:
        titulos = extraer_titulos(html)
        df = pd.DataFrame(titulos, columns=['titulo'])
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
        logger.info("Títulos guardados exitosamente")
    else:
        logger.error("No se pudieron obtener los títulos")

if __name__ == "__main__":
    main()