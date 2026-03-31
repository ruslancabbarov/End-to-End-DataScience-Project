from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title="Credit Card Fraud Detection API")
try:
    with open('xgboost_fraud_model.pkl','rb') as f:
        model = pickle.load(f)
    print(" Model loaded successfully")
except Exception as e:
    print(" ERROR LOADING MODEL:", e)


class FraudInput(BaseModel):
    merchant: int
    amt: float
    city_pop: int
    job: int
    age: int
    distance_km: float
    is_online: int
    trans_hour: int
    trans_day: int
    trans_month: int
    is_night: int
    category_food_dining: int
    category_gas_transport: int
    category_grocery_net: int
    category_grocery_pos: int
    category_health_fitness: int
    category_home: int
    category_kids_pets: int
    category_misc_net: int
    category_misc_pos: int
    category_personal_care: int
    category_shopping_net: int
    category_shopping_pos: int
    category_travel: int
    gender_M: int

    class Config:
        json_schema_extra = {
            "example": {
                "merchant": 123,
                "amt": 45.5,
                "city_pop": 50000,
                "job": 15,
                "age": 30,
                "distance_km": 12.4,
                "is_online": 0,
                "trans_hour": 14,
                "trans_day": 5,
                "trans_month": 3,
                "is_night": 0,
                "category_food_dining": 0,
                "category_gas_transport": 1,
                "category_grocery_net": 0,
                "category_grocery_pos": 0,
                "category_health_fitness": 0,
                "category_home": 0,
                "category_kids_pets": 0,
                "category_misc_net": 0,
                "category_misc_pos": 0,
                "category_personal_care": 0,
                "category_shopping_net": 0,
                "category_shopping_pos": 0,
                "category_travel": 0,
                "gender_M": 1
            }
        }


@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!", "status": "Ready"}

@app.post("/predict")
def predict_fraud(data:FraudInput):
    input_df = pd.DataFrame([data.dict()])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return {
        "is_fraud": int(prediction),
        "fraud_probability": round(float(probability), 4),
        "verdict": "HIGH RISK (Fraud suspected)" if prediction == 1 else "SAFE (Normal transaction)"
    }