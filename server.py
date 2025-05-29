from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text_to_analyze = request.form.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No text provided.", 400
    result = emotion_detector(text_to_analyze)
    if result.get('error'):
        return f"Error: {result['error']}", 500
    response = (f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}.")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
