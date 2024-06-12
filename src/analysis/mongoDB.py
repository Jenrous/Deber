# import pandas as pd # se importa pnadas
# from pymongo import MongoClient # se importa de la biblioteca pymongo mongoclient



# # funcion para conectar a mongoDB

# def connect_mongodb (url, products):
#     client = MongoClient(url)
#     return client [products] # nombre de la base de datos


# # funcion qu einserta el documento en la coleccion de mongoDB (products_analysis)

# def insert_document (db, products_analysis, docuement):
#     collection = db[products_analysis]
#     result = collection.insert_one(docuement)
#     return result.inserted_id



# # funcion para analizar los datos y almacenar los resultados en MongoDB

# def analyze_data(df):
#     print("Basic data analysis: ")
#     analysis = df.describe()
#     print(analysis)
        
#     print("\nProducts with highest prices: ")
#     highestPrices = df.nlargest(5, "price")
#     print(highestPrices)
    
    



# # coneccion a mongoDB 
# url = 'mongodb://localhost:27017/'
# name_data_base = 'products'
# db = connect_mongodb (url, name_data_base)


# #preparar datos para ingresar a mnogoDB

# analyze_data.to_dict() # lo intenté profe :( 
# # highest_prices_data = highestPrices.to_dict(orient='records')

# #insertar analisia basico en mongoDB
# id_analysis = insert_document(db, 'high_prices', {'type': 'basic_analysis', 'data': analyze_data })
# print (f'Basic analysis document inserted with Id: {id_analysis}')


# #insertar productos con precios mas altos en mongoDB
# def highest_prices_data (db):
#     for product in highest_prices_data:
#      id_high_price = insert_document(db, 'high_prices', product)
#      print (f'Product with high price document iseerted with Id: {id_analysis}')



    
#     # analiza los datos y los almacena en mongoDB
#     analyze_data(db)

    