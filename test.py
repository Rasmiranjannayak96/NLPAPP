import requests

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


# Example usage
if __name__ == "__main__":
    analyzer = EmotionPredictor()
    text = "I love using Hugging Face models!"
    result = analyzer.query(text)
    y=[]
    for i in result:
        for j in i:
            y.append(j['score'])
            if max(y)==j['score']:
                result2=(j['label'])
    print(result2)
