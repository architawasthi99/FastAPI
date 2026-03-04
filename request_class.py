from fastapi import FastAPI,Request #here we are importing FASTAPI class to create WebAPI application
from mockData import product


app=FastAPI() #creating object

#CREATING 1ST ENDPOINT
@app.get("/") #decorator send data from backend to frontend through api #converting to route
def home():
    return "WELCOME TO THE FASTAPI SEIES!"

#2nd ENDPOINT
@app.get("/contact") #converting to route
def contact():
    return "YOU HAVE REACHED THE 2nd ENDPOINT!"

#to access this 2nd endpoint write "http://127.0.0.1:8000/contact" on any web browser


#PATH AND QUERY PARAMETERS IN FASTAPI
@app.get("/product")
def get_product():
    return product

#PATH PARAMS
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    #if product availab;e with the id return product else return error

    for oneproduct in product:
        if oneproduct.get("id")==product_id:
            return oneproduct
    return{
        "error":"value not found"
    }

#QUERY PARAMS {when we want to pass n number of parameters}
@app.get("/greet")
def greet_user(name:str, age:int):
    return{
        "greet":f"Hello {name} age is {age}, Hows You"
    }
#for o/p  http://127.0.0.1:8000/greet?name=Archit&age=21 

#WHEN WE HAVE N NUMBER OF PARAMETERS IN KEY VALUE PAIRS FORM 

@app.get("/greet2")
def greet_one(request:Request):
    query_params=dict(request.query_params)
    print(query_params)
    return{
        "greet2": f"hello {query_params.get('name')}, your age is {query_params.get('age')}"
}
 
