from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import download_audio
from transcribe import transcribe_audio
from summarize import summarize_text
import os

app = Flask(__name__)
CORS(app) 

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
    # print("=== RAW TRANSCRIPT ===")
    # print(transcript[:1000])
    # print("=== END ===")
    summary = summarize_text(transcript)

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(port=5000)
