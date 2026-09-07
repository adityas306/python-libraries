from fastapi import FastAPI
from pydantic import BaseModel
#pydantic is used to dataType of given data and check range between given condition

app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    loan_amount: float
    employeement_years: int

@app.post("/predict")
def predict_loan(application: LoanApplication):

    #pretend this trained model
    if application.income > 5000 and application.employeement_years > 2:
        decision = "approved"
    else:
        decision = "rejected"

    return {
        "application_age":application.age,
        "decision":decision
    }

