# api.py - API functions for News Sentiment TTS App

from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiment, generate_tts

app = Flask(__name__)

@app.route("/news", methods=["GET"])
def get_news():
    """API endpoint to fetch news for a given company."""
    company = request.args.get("company")
    if not company:
        return jsonify({"error": "Company name is required"}), 400
    
    news = fetch_news(company)
    return jsonify(news)

@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    """API endpoint to perform sentiment analysis."""
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Text field is required"}), 400
    
    sentiment = analyze_sentiment(data["text"])
    return jsonify({"sentiment": sentiment})

@app.route("/tts", methods=["POST"])
def get_tts():
    """API endpoint to generate Hindi TTS."""
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Text field is required"}), 400
    
    file_path = generate_tts(data["text"])
    return jsonify({"audio_file": file_path})

if __name__ == "__main__":
    app.run(debug=True)
