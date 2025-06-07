from spider import SimpleScraper
import pandas as pd

def main():
    # Obtener artículos
    articulos = SimpleScraper().obtener_articulos()
    
    # Guardar en CSV si hay artículos
    if articulos:
        pd.DataFrame({"Articulos": articulos}).to_csv("articulos.csv", index=False)
        print(f"Se guardaron {len(articulos)} artículos en articulos.csv")
    else:
        print("No se pudieron obtener artículos")

if __name__ == "__main__":
    main()