from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask App!"


if __name__ == '__main__':
    app.run(debug=True)
