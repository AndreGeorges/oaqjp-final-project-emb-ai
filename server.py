'''import from flask and EmotionDetection'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''bring in our variables'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid input! try again"
    return {
        f"For the given statement, the system response is \
        'anger': {anger}, \
        'disgust': {disgust},\
        'fear': {fear}, \
        'joy': {joy} and \
        'sadness': {sadness}.\
        The dominant emotion is {dominant_emotion}."
    }

@app.route("/")
def render_index_page():
    '''render the page user will see'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    