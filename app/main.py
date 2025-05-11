# app/main.py
from fastapi import FastAPI
from model import predict_sentiment
from schemas import TextInput, PredictionResult

app = FastAPI()

@app.post("/predict", response_model=PredictionResult)
def predict(input_data: TextInput):
    result = predict_sentiment(input_data.text)
    return {"sentiment": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
