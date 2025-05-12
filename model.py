# app/model.py
def predict_sentiment(text: str) -> str:
    """簡易情緒分類（模擬用，可換成真正模型）"""
    positive_keywords = ["happy", "good", "great", "love", "fantastic"]
    negative_keywords = ["sad", "bad", "hate", "terrible", "angry"]

    text = text.lower()
    if any(word in text for word in positive_keywords):
        return "positive"
    elif any(word in text for word in negative_keywords):
        return "negative"
    else:
        return "neutral"