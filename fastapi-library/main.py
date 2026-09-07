from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"my first API is working"}

@app.get("/about")
def about():
    return {"project" : "loan risk model" , "version" : "1.0"}

@app.get("/customer") #http://127.0.0.1:8000/customer?customer_id=101&city=delhi
def get_customer(customer_id: int , city:str):
    return {
        "customer_id": customer_id,
        "name":"Aditya",
        "status": "active",
        "city": city
    }