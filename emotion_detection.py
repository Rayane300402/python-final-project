import requests
import json

def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    anger   = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear    = emotions.get("fear", 0)
    joy     = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores