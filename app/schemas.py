# app/schemas.py

from pydantic import BaseModel

# 用於接收請求資料（POST /predict）
class TextInput(BaseModel):
    text: str

# 用於回傳預測結果（response_model）
class PredictionResult(BaseModel):
    sentiment: str