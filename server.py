from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotDetector():
    # function takes in text to analyze, returns emotion scores
    text_to_analyze = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_analyze)
    
    output = "For the given statement, the system response is "
    i = 0
    for k,v in response.items():
        i += 1
        if i <=4:
            output = output + f"'{k}': {v}, "
        elif i == 5:
            output = output + f"'{k}': {v}."
        else:
            output = output + f" The dominant emotion is {v}."
    
    return output


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)