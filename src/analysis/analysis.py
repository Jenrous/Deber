import pandas as pd  # Importa pandas para manejo de datos
import os # Importa os para manejo del sistema de archivos
from ..decorators.decorators import timeit, logit # importacion de los decoradores personalizados

@logit # decorador para anadir el login a la funcion
@timeit # decorador para meddir el tiempode ejecucion de la funcio n
def load_data(data_path):
    if data_path.endswith(".csv"): 
        df = pd.read_csv(data_path) # Lee datos desde un archivo CSV
    elif data_path.endswith("xlsx"):
       df = pd.read_excel(data_path) # Lee datos desde un archivo Excel
    else:
      raise ValueError("Unsupported file format")  # Lanza un error si el formato no es compatible
    print ("Data loaded successfully") # Imprime un mensaje indicando que los datos se cargaron correctamente

    return df  # Devuelve el DataFrame con los datos cargados


@logit # decorador para anadir el login a la funcion
@timeit # decorador para meddir el tiempode ejecucion de la funcio n    
def clean_data(df):
   # limpiamos los datos
   df ["price"]= df ["price"].replace(r"[\$,]", "", regex=True). astype(float) # Limpiamos los datos y conertimos la columna de precios a tipo float. es decir le quita la comad
   print("Data cleaned Successfully")
   return df



@logit # decorador para anadir el login a la funcion
@timeit # decorador para meddir el tiempode ejecucion de la funcio n
def analyze_data (df):
   
   print("Basic data analysis: ")
   print(df.describe())
   print ("\nProducts with highest prices: ")
   highestPrices= df.nlargest(5,"price")
   print(highestPrices)



@logit # decorador para anadir el login a la funcion
@timeit # decorador para meddir el tiempode ejecucion de la funcio n
def save_clean_data(df,outputh_path):
   df.to_csv(outputh_path,index=False)


if __name__ == "__main__": 
   data_patch = "data/raw/products.csv"
   outputh_path = "data/processed/cleaned_products.csv" 

   df =load_data (data_patch)
   df = clean_data(df)
   analyze_data(df)
   os.makedirs("data/processed", exist_ok=True)

   save_clean_data(df, outputh_path)


   