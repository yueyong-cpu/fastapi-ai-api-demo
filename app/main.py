# app/main.py
from fastapi import FastAPI
from model import predict_sentiment
from schemas import TextInput, PredictionResult

app = FastAPI()

@app.post("/predict", response_model=PredictionResult)
def predict(input_data: TextInput):
    result = predict_sentiment(input_data.text)
    return {"sentiment": result}