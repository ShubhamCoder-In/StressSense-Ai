# prediction.py
from gradio_client import Client

client = Client("ShubhamCoder01/stress-detector")

def predict_stress(text: str):
    result = client.predict(
        text=text,
        api_name="/predict"
    )
    return result