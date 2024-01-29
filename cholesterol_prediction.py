from fastapi import APIRouter, HTTPException
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

router = APIRouter()

# Load the trained model
model = joblib.load('xgb_regressor_cholesterol.pkl')

class InputData(BaseModel):
    Age: int
    Gender: str
    ChestPainType: str
    RestingBloodPressure: int
    FastingBloodSugar: bool
    RestingECG: str
    MaxHeartRate: int
    ExerciseInducedAngina: str
    STDepression: float
    Slope: str
    NumMajorVessels: int
    Thalassemia: str
    HeartDisease: int

@router.post("/predict-cholesterol")
async def predict_cholesterol_endpoint(data: InputData):
    try:
        # Convert data to dictionary
        data_dict = data.dict()

        # Predict cholesterol using the cholesterol prediction function
        predicted_cholesterol = predict_cholesterol(data_dict)

        return {"predicted_cholesterol": predicted_cholesterol}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def predict_cholesterol(data):
    # Create a DataFrame from the new data
    new_data_df = pd.DataFrame(data, index=[0])

    # Encode categorical variables just like in the training process
    categorical_features = ['Gender', 'ChestPainType', 'FastingBloodSugar', 'RestingECG', 'ExerciseInducedAngina', 'Slope', 'Thalassemia']
    for col in categorical_features:
        new_data_df[col] = LabelEncoder().fit_transform(new_data_df[col])

    # Predict the cholesterol level with the trained model
    predicted_cholesterol = model.predict(new_data_df)
    
    return float(predicted_cholesterol[0])
