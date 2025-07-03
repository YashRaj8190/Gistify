import subprocess
import os
import uuid

def download_audio(youtube_url):
    temp_folder = "temp"
    os.makedirs(temp_folder, exist_ok=True)
    filename = f"{uuid.uuid4()}.m4a"
    filepath = os.path.join(temp_folder, filename)

    command = [
        "yt-dlp",
        "-f", "140",
        "-o", filepath,
        youtube_url
    ]

    try:
        subprocess.run(command, check=True)
        return filepath
    except subprocess.CalledProcessError:
        return None
