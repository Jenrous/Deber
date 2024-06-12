import requests # modulo requests para hacer  solicitudes HTTP
from bs4 import BeautifulSoup #  BeautifulSoup para analizar  documentos HTML
import pandas as pd #  pandas para manejar datos en los DataFrames 


def fetch_page(url):

    response = requests.get(url)
    if response.status_code == 200: # se compara el estado de respuesta en este si es exitoso

        return response.content # retorna el contenido de la pagina en caso de que la solicitud haya sido exitosa
    else:
        raise Exception(f"Failed to fetch page: {url}") # Lanza (raise una excepcion)  si la solicitud falla
    


def parse_product(product):

    title= product.find("a", class_="title").text.strip()
    desciption = product.find("p", class_="description").text.strip()
    price = product.find("h4", class_="price").text.strip()
    return {
        "title": title,
        "description": desciption,
        "price": price,
    }

def scrape(url):
    page_content= fetch_page(url)
    soup = BeautifulSoup(page_content, "html.parser")

    print(soup)

    products = soup.find_all("div", class_="thumbnail")

    products_data=[]

    for product in products:
        product_info = parse_product(product)
        products_data.append(product_info)

    print (products_data)
    return pd.DataFrame(products_data)


base_url= "https://webscraper.io/test-sites/e-commerce/allinone" # Definnimos el URL base para el Scraping.
    
    # Llamamos a la funcion scrape para obtener los datos de los productos 
df = scrape(base_url)

    # Imprimos el DF resultante

print(df)
    # Guardamos los datos en un archivo CSV sin incluir el indice.

df.to_csv('data/raw/products.csv', index=False)