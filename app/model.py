# app/model.py

def predict_sentiment(text: str) -> str:
    """
    根據輸入的文字簡單分類情緒（模擬用，可替換為真正模型）。

    :param text: 使用者輸入的文字
    :return: "positive"、"negative" 或 "neutral"
    """
    positive_keywords = ["happy", "good", "great", "love", "fantastic"]
    negative_keywords = ["sad", "bad", "hate", "terrible", "angry"]

    text = text.lower()

    if any(word in text for word in positive_keywords):
        return "positive"
    elif any(word in text for word in negative_keywords):
        return "negative"
    else:
        return "neutral"