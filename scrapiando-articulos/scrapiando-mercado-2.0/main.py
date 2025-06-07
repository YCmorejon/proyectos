from spider import Scraper
import pandas as pd

def main():
    scraper = Scraper()
    articulos = scraper.extraer_datos()
    df = pd.DataFrame({"Articulos" : articulos})
    df.to_csv("articulos.csv",index=False)
    
if __name__ == "__main__":
    main()