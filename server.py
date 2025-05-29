"""Flask server for emotion detection web application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle emotion detection requests and return formatted response or error message."""
    text_to_analyze = request.form.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    result = emotion_detector(text_to_analyze)
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    if result.get('error'):
        return f"Error: {result['error']}", 500
    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
