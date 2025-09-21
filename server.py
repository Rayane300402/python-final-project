"""Flask web app for the Emotion Detection final project."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector"
)
@app.route("/emotionDetector")
def sent_detetctor():
    """HTTP GET endpoint that returns formatted emotion scores for a given text."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")

def main():
    """Run the Flask development server on localhost:5000."""
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
