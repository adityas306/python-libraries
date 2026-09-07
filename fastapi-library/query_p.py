# Query Parameter 
#Used when filtering , sorting , customise
#we must set limit by which our system does not crash
#limit:int = 10
# http://127.0.0.1:8000/customers?city=bengaluru&risk=low

from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id":101, "name": "Ravi" , "city":"bengaluru" , "risk" : "low"},
    {"id":102, "name": "Om" , "city":"mumbai" , "risk" : "high"},
    {"id":103, "name": "Prakash" , "city":"mumbai" , "risk" : "high"},
    {"id":104, "name": "Yash" , "city":"bengaluru" , "risk" : "meadium"},
    {"id":105, "name": "Gopal" , "city":"delhi" , "risk" : "meadium"} 
]

@app.get("/customers") #http://127.0.0.1:8000/customers?city=bengaluru&risk=low
def get_customers(city:str , risk:str):
    filtered =  [
        c for c in all_customers
        if c["city"] == city and c["risk"] == risk
    ]

    return {
        "city": city,
        "risk": risk,
        "count" : len(filtered),
        "results" : filtered,
    }
