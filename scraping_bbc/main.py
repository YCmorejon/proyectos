from src.spider import obtener_html , extraer_titulos

URL = "https://www.bbc.com/mundo/topics/cyx5krnw38vt"

def main():
    html = obtener_html(URL)
    if html:
        titulos = extraer_titulos(html)
        print("\n📰 Títulos extraídos:")
        for i, titulo in enumerate(titulos, 1):
            print(f"{i}. {titulo}")
    else:
        print("[ERROR] No se pudo obtener el HTML.")

main()