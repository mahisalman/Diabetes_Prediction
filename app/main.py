from fastapi import FastAPI
from .schemas import PatientData
import joblib
import numpy as np
import json
from fastapi.middleware.cors import CORSMiddleware
import os
import joblib
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# CORS for frontend JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(__file__)  # path to backend/
model_path = os.path.join(BASE_DIR, "diabetes_model.pkl")

model = joblib.load(model_path)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: PatientData):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,
                            data.SkinThickness, data.Insulin, data.BMI,
                            data.DiabetesPedigreeFunction, data.Age]])
    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data)[0].max()
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    return {
        "prediction": int(prediction),
        "result": result,
        "confidence": round(float(confidence), 2)
    }

@app.get("/metrics")
async def get_metrics():
    with open("metrics.json", "r") as f:
        return json.load(f)

# Serve static frontend files
BASE_DIR = os.path.dirname(__file__)
app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "static"), html=True), name="static")