from flask import Flask, request, jsonify
from utils import download_audio
from transcribe import transcribe_audio
from summarize import summarize_text
import os

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    audio_path = download_audio(url)
    if not audio_path:
        return jsonify({"error": "Audio download failed"}), 500

    transcript = transcribe_audio(audio_path)
    summary = summarize_text(transcript)

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(port=5000)
