from flask import Flask, request, jsonify
from utils import download_audio
from transcribe import transcribe_audio
from summarize import summarize_text
import os

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    youtube_url = data.get("url")

    audio_path = download_audio(youtube_url)
    if not audio_path:
        return jsonify({"error": "Audio download failed"}), 500

    transcript = transcribe_audio(audio_path)
    summary = summarize_text(transcript)

    os.remove(audio_path)  # Clean up
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(port=5000)
