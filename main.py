from fastapi import FastAPI, HTTPException
import csv
import json
import os

# Create FastAPI instance
app = FastAPI()

csvFilePath = '.\data.csv'
jsonFilePath = '.\products.json'
#csvFilePath = '.\data.mp3'

# [GET] route
@app.get("/")
def main():
    return {"message": "Hello World"}

# [GET] route, Convert CSV file to JSON
@app.get("/topProduct")
def top_product():

    if os.path.splitext(csvFilePath)[1] != ".csv":
        raise HTTPException(status_code=415, detail="Unsupported Media Type")
    
    # Read the contents of a CSV file
    with open (csvFilePath, 'r', encoding='utf-8') as csvFile:
        
        csvReader = csv.reader(csvFile)
        
        # Skip first row of csv file (the header)
        next(csvReader)

        # Save the data in object variable
        data = {"allProduct":[]}
        top_product = None

        for row in csvReader: # o(n)
            # each row = [id,product_name,customer_average_rating]
            id = int(row[0])
            product = str(row[1])
            rating = float(row[2])

            newProduct = {"ID":id,"product":product,"rating":rating}

            if (top_product is None):
                top_product = {"top_product": product, "product_rating": rating}
            elif (rating > top_product["product_rating"]):
                top_product = {"top_product": product, "product_rating": rating}

            data["allProduct"].append(newProduct)

    with open (jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        json.dump(top_product, jsonFile, indent=2)
        return top_product

# try and catch
