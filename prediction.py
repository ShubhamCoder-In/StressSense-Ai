# prediction.py
from gradio_client import Client

client = Client("https://ShubhamCoder01-stress-detector.hf.space")

def predict_stress(text: str):
    result = client.predict(
        text,
        api_name="/predict"
    )
    return result