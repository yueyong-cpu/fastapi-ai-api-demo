from fastapi import FastAPI
from app.model import predict_sentiment
from app.schemas import TextInput, PredictionResult

app = FastAPI()

# 新增首頁 route，避免 GET / 出現 502 錯誤
@app.get("/")
def root():
    return {"message": "FastAPI sentiment API is running!"}

@app.post("/predict", response_model=PredictionResult)
def predict(input_data: TextInput):
    print("Received text:", input_data.text)  #這行用於debug
    try:
        result = predict_sentiment(input_data.text)
        return {"sentiment": result}
    except Exception as e:
        print("Error:", str(e))  # 這行會顯示在 Deploy Logs 中
        return {"sentiment": "error"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)