from scraping.spider import obtener_html,extraer_datos
import time

#Función pricipal del programa
def main():
    for url_modificada in range(1, 11): 
        time.sleep(1) 
        html = obtener_html(f"https://quotes.toscrape.com/page/{url_modificada}/")
        if html:
            citas, autor, etiquetas = extraer_datos(html)
            for c, a, e in zip(citas, autor, etiquetas):
                print("Cita :", c)
                print("Autor :", a)
                print("Etiqueta :", e)
        else:
            print("Error al intentar mostrar los datos")

if __name__ == "__main__":
    main()