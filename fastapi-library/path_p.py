#Path Parameters
#for 1 specific thing'
#1. http://127.0.0.1:8000/customer/101
#2. http://127.0.0.1:8000/model/credit-risk-v1/customer/101

from fastapi import FastAPI

app = FastAPI()

customer_risk_profiles = {
    101: {"name": "Ravi Kumar" , "risk": "low" , "score": 0.12},
    102: {"name": "Priya Sharma" , "risk": "medium" , "score": 0.54},
    103: {"name": "Arjun Kapoor" , "risk": "high" , "score": 0.89},
}

@app.get("/customer/{customer_id}") #http://127.0.0.1:8000/customer/101
def get_customer(customer_id: int): 
    if customer_id not in customer_risk_profiles:
        return {"error": f"customer {customer_id} not found"}

    profile = customer_risk_profiles[customer_id]

    return {
        "customer_id": customer_id,
        "name": profile["name"],
        "risk_level": profile["risk"],
        "score": profile["score"]
    }

@app.get("/model/{model_name}/customer/{customer_id}") #http://127.0.0.1:8000/model/credit-risk-v1/customer/101
def get_model_prediction(model_name: str , customer_id: int):
    return {
        "model": model_name,
        "customer_id": customer_id,
        "prediction": "high risk"
    }

