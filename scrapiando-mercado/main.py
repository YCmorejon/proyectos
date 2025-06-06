from spider import extraer_html,obtener_datos
import logging
import os
from datetime import datetime
import sys

# Configuración del logging
def setup_logging():
    # Crear directorio de logs si no existe
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configurar el formato y el archivo de log
    log_file = f'logs/scraping_{datetime.now().strftime("%Y%m%d")}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
#Datos necesarios para el programa
URL = "https://listado.mercadolibre.com.ar/laptops#D[A:laptops]"

def main():
    setup_logging()
    
    html = extraer_html(URL)
    if html:
        logging.info("Empezando a extraer los datos")
        nombres,precios = obtener_datos(html)
        for name , price in zip(nombres,precios):
            print(f"Nombre : {name.text}\nPrecio : {price.text}")
    else:
        logging.error("Error al empezar extraer los datos")

if __name__ == "__main__":
    main()