# FastAPI AI 情緒分析 API

這是一個使用 Python + FastAPI 開發的 AI Web API 範例，可針對輸入的文字回傳情緒分類（正向 / 負向 / 中性）。

## 🚀 功能特色
- 建立 POST /predict API
- 自動產生 Swagger UI 測試介面
- 模型邏輯可替換成任意 AI 模型

## 🛠 技術
- FastAPI
- Uvicorn
- Python 3.10+
- Pydantic

## ▶️ 使用方式

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload