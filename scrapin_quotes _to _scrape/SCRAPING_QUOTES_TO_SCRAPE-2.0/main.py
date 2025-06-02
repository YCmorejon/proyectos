from scraping.spider import obtener_html,extraer_datos
import time
import pandas as pd

#Función pricipal del programa
def main():
    lista = []
    for url_modificada in range(1, 11): 
        time.sleep(1) 
        html = obtener_html(f"https://quotes.toscrape.com/page/{url_modificada}/")
        if html:
            citas, autor, etiquetas = extraer_datos(html)
            for c, a, e in zip(citas, autor, etiquetas):
                diccionario = {  # Crear nuevo diccionario para cada iteración
                    "Citas": c,
                    "Autor": a,
                    "Etiquetas": e
                }
                lista.append(diccionario)  
        else:
            print("Error al intentar mostrar los datos")
    df = pd.DataFrame(lista)
    df.to_csv("quotes.csv")

if __name__ == "__main__":
    main()