from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import csv
import json
import os

class Product(BaseModel):
    id:int
    product_name:str
    customer_average_rating:float


# Create FastAPI instance
app = FastAPI()

csvFilePath = '.\\data.csv'
jsonFilePath = '.\\products.json'
#csvFilePath = '.\data.mp3'


# [GET] route
@app.get("/")
async def main():
    return {"message": "Hello World"}


# [GET] route, Convert CSV file to JSON
@app.get("/topProduct")
async def top_product():

    # Split the path and Check the file type
    if os.path.splitext(csvFilePath)[1] != ".csv":
        raise HTTPException(status_code=415, detail="Unsupported Media Type")

    # Read the contents of a CSV file
    with open(csvFilePath, 'r', encoding='utf-8') as csvFile:

        csvReader = csv.reader(csvFile)

        # Skip first row of csv file (the header)
        next(csvReader)

        # Convert each row and add it to object variable
        data = {"allProduct": []}
        top_product = None
        for row in csvReader:  # o(n)
            # each row = [id,product_name,customer_average_rating]
            id = int(row[0])
            product = str(row[1])
            rating = float(row[2])

            newProduct = {"ID": id, "product": product, "rating": rating}

            if (top_product is None):
                top_product = {
                    "top_product": product,
                    "product_rating": rating}
            elif (rating > top_product["product_rating"]):
                top_product = {
                    "top_product": product,
                    "product_rating": rating}

            data["allProduct"].append(newProduct)

    # Open a JSON writer, and Return top_product as JSON
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        json.dump(top_product, jsonFile, indent=2)
        return top_product

# try and catch


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
