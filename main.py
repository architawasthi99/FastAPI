from fastapi import FastAPI #here we are importing FASTAPI class to create WebAPI application

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