from spider import extraer_html, obtener_datos
import logging
from datetime import datetime
import sys
import os

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

class ScrapingController:
    def __init__(self):
        self.url = "https://www.bbc.com/mundo/topics/cyx5krnw38vt"
        
    def ejecutar_scraping(self):
        try:
            logging.info("Iniciando proceso de scraping")
            
            logging.info(f"Extrayendo HTML de {self.url}")
            html = extraer_html(self.url)
            
            if not html:
                logging.error("No se pudo obtener el HTML")
                return False
            
            logging.info("Extrayendo datos del HTML")
            datos = obtener_datos(html)
            
            if datos:
                logging.info(f"Se obtuvieron {len(datos) if isinstance(datos, list) else 1} registros")
                for dato in datos:
                    print(dato)
            else:
                logging.warning("No se encontraron datos para extraer")
                return False
                
        except Exception as e:
            logging.error(f"Error durante el scraping: {str(e)}")
            return False

def main():
    try:
        # Configurar logging
        setup_logging()
        
        # Iniciar el controlador
        controller = ScrapingController()
        
        # Ejecutar el scraping
        resultado = controller.ejecutar_scraping()
        
        if resultado:
            logging.info("Proceso completado exitosamente")
            print(resultado)
        else:
            logging.error("El proceso finalizó con errores")
            
    except Exception as e:
        logging.critical(f"Error crítico en la aplicación: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

