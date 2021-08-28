from fastapi import FastAPI, HTTPException, Path, File, UploadFile
from pydantic import BaseModel
import pandas as pd
import json
import os

class Product(BaseModel):
    id:int
    product_name:str
    customer_average_rating:float


# Create FastAPI instance
app = FastAPI()

jsonFilePath = '.\\products.json'


# [POST] route, Convert CSV file to JSON
@app.post("/topProduct")
async def top_product(csv_file: UploadFile = File(...)):
    
    # Split the path and Check the file type
    if os.path.splitext(csv_file.filename)[1] != ".csv":
        raise HTTPException(status_code=415, detail="Unsupported Media Type")

    # read the csv file, Using (pandas mudeol)
    dataframe = pd.read_csv(csv_file.filename)
    # Sort the csv file, from highest value to lowest value according to the ["customer_average_rating"] column
    sortedData = dataframe.sort_values(by="customer_average_rating", ascending=False)
    # [0] => index for the first value
    firstRow = sortedData.iloc[0]
    top_product = {"top_product":firstRow["product_name"],"product_rating":firstRow["customer_average_rating"]}

    # top_product  = firstRow.to_json(orient="index")

    # Open a JSON writer, and Return top_product as JSON
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        json.dump(top_product, jsonFile, indent=2)
        return top_product


data = {"allProduct":[
                    {"id":132,"product_name":"Massoub gift card","customer_average_rating":5.0},
                    {"id":154,"product_name":"Kebdah gift card","customer_average_rating":3.2},
                    {"id":12,"product_name":"Fatayer gift card","customer_average_rating":1.8},
                    {"id":55,"product_name":"ice cream card","customer_average_rating":5.1}
                    ]}

# [GET] route (Return all Product)
@app.get("/product")
async def all_prodect():
    return data["allProduct"]


# [GET] route (Return one Product)
@app.get("/product/{id}")
async def one_product(id: int):
    allProductArr = data["allProduct"]
    for product in allProductArr:
        if (product["id"] == id):
            return product
    return {"message" : "Product not found"}


# [POST] route
@app.post("/createProduct")
async def create_product(product: Product):
    allProductArr = data["allProduct"]
    for oneProd in allProductArr:
        if (oneProd["id"] == product.id):
            return {"message": "product already Exist"}
    newProduct = {"id":product.id,"product_name":product.product_name,"customer_average_rating":product.customer_average_rating}
    allProductArr.append(newProduct)
    return allProductArr
    

# [PUT] route
@app.put("/updateProduct/{id}")
async def update_product(id: int, product: Product):
    allProductArr = data["allProduct"]
    product_to_update = None

    for oneProd in allProductArr:  
        if (oneProd["id"] == id):
            product_to_update = oneProd
    if product_to_update is not None:
        oneProd["id"] =  product.id
        oneProd["product_name"] = product.product_name
        oneProd["customer_average_rating"] = product.customer_average_rating
        return allProductArr       
    return {"message": "The product was not found"}

# [Delete] route
@app.delete("/deleteProduct/{id}")
async def delete_product(id: int):
    allProductArr = data["allProduct"]
    product_to_delete = None
    for oneProd in allProductArr:
        if (oneProd["id"] == id):
            product_to_delete = oneProd

    if product_to_delete is not None:
        allProductArr.remove(product_to_delete)
        return allProductArr
    return {"message":"Product not found"}