
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("titanic_model.pkl")

# Define input model for API
class Passenger(BaseModel):
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Sex_male: int   
    Embarked_Q: int 
    Embarked_S: int 

@app.get("/")
def root():
    return {"message": "Titanic Survival Prediction API"}

@app.post("/predict")
def predict_survival(passenger: Passenger):
    # Convert input to DataFrame
    df = pd.DataFrame([passenger.dict()])
    
    # Make prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][prediction]
    if prediction==0:
        return {"prediction": 0, "probability": probability*100}
    else:
        return {"prediction": 1, "probability": (probability)*100}
