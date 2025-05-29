
import requests


def emotion_detector(text_to_analyze):
    api_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(api_url, headers=headers, json=json)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
