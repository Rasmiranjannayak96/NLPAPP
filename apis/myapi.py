
import requests

class SentimentAnalyzer:
    def __init__(self, model="distilbert-base-uncased-finetuned-sst-2-english"):
        self.api_key = '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' 
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query(self, text):
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        try:
            response.raise_for_status()  
            data = response.json()

            
            print(f"Response: {data}")

            
            if 'error' in data:
                print(f"Error: {data['error']}")
                if 'estimated_time' in data:
                    print(f"Estimated time: {data['estimated_time']}")
            return data

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None



class LanguageDetector:
    def __init__(self, model="papluca/xlm-roberta-base-language-detection"):
        self.api_key = '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'  
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query(self, text):
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        try:
            response.raise_for_status()  
            data = response.json()

            # Print the response for debugging
            print(f"Response: {data}")

            # Check if there is an error in the response
            if 'error' in data:
                print(f"Error: {data['error']}")
                if 'estimated_time' in data:
                    print(f"Estimated time: {data['estimated_time']}")
            return data

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None


class EmotionPredictor:
    def __init__(self, model="j-hartmann/emotion-english-distilroberta-base"):
        self.api_key = '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'  # Replace with your new API key
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query(self, text):
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        try:
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

            # Print the response for debugging
            print(f"Response: {data}")

            # Check if there is an error in the response
            if 'error' in data:
                print(f"Error: {data['error']}")
                if 'estimated_time' in data:
                    print(f"Estimated time: {data['estimated_time']}")
            return data

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None
