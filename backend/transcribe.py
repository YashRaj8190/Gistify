import whisper

model = whisper.load_model("base")  # You can use "small" or "medium" if needed

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
