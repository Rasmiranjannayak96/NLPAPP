
import requests

class SentimentAnalyzer:
    def __init__(self, model="distilbert-base-uncased-finetuned-sst-2-english"):
        self.api_key='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'
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query(self, text):
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        return response.json()