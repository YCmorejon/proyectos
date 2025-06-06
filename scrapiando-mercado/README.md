# 🛒 Web Scraping: Precios en MercadoLibre Argentina

Este proyecto forma parte de mi serie de ejercicios prácticos para aprender **Web Scraping**. En este caso, extraigo información de productos desde el sitio [MercadoLibre Argentina](https://www.mercadolibre.com.ar/), simulando una búsqueda real.

## 📌 Objetivo

Realizar una búsqueda de un producto específico en MercadoLibre y obtener el **nombre y precio de los primeros 5 resultados**.

## ⚠️ Desafíos del scraping en este sitio

- MercadoLibre tiene una **estructura HTML dinámica y cambiante**.
- Hay medidas contra scraping como cambios frecuentes de clases y posibles bloqueos por IP.

Este proyecto incluye técnicas básicas para manejar estas dificultades.

## 🛠️ Herramientas utilizadas

- [`requests`](https://docs.python-requests.org/en/latest/): Para hacer la solicitud HTTP simulando un navegador.
- [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/): Para analizar y extraer la información del HTML de la página.

## 📂 Estructura del proyecto

"""

mercadolibre\_scraper/
├── main.py              # Script principal con la lógica de scraping
├── requirements.txt     # Librerías necesarias
└── README.md            # Este archivo

"""


## ▶️ Cómo ejecutar

1. Clona este repositorio:

   git clone https://github.com/tu_usuario/mercadolibre_scraper.git
   cd mercadolibre_scraper


2. Instala las dependencias:

   pip install -r requirements.txt


3. Ejecuta el script con un término de búsqueda (ejemplo: laptop):

   python main.py
   

## 📝 Notas adicionales

* Se recomienda incluir cabeceras (`headers`) para simular un navegador real y evitar bloqueos.
* El sitio puede cambiar con el tiempo. Si el script falla, probablemente haya que actualizar los selectores CSS.
* Este proyecto es con fines educativos y no debe usarse para scraping masivo.

## 🤝 Contribuciones

Si tienes mejoras que aportar, ¡no dudes en abrir un Pull Request!
También puedes copiar y reutilizar este código sin problema.


¡Gracias por visitar este proyecto! 🚀
