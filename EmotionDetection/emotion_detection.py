import requests
import json


def emotion_detector(text_to_analyze):
    # initalize request vars
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=myobj).json()
    
    emotions_set = response.get("emotionPredictions", [])[0].get("emotion", {})

    dominant = {}
    for k,v in emotions_set.items():
        if v == max(emotions_set.values()):
            dominant.update({"dominant_emotion": k})
    emotions_set.update(dominant)
    
    return emotions_set