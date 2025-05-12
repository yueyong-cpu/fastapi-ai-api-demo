from fastapi import FastAPI
from app.model import predict_sentiment
from app.schemas import TextInput, PredictionResult

app = FastAPI()

# 提供首頁 GET，避免直接訪問 / 時報錯
@app.get("/")
def root():
    return {"message": "FastAPI sentiment API is running!"}

@app.post("/predict", response_model=PredictionResult)
def predict(input_data: TextInput):
    print("Received text:", input_data.text)  # Debug log
    try:
        result = predict_sentiment(input_data.text)
        return {"sentiment": result}
    except Exception as e:
        print("Error:", str(e))  # 顯示在 Railway Deploy Logs 中
        return {"sentiment": "error"}