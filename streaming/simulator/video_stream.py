import subprocess
import sys

# Calea către fișierul video
video_path = "/app/video.mp4"

# Comanda ffmpeg (ca string pentru a fi executată direct în shell)
ffmpeg_command = (
    "ffmpeg -re -stream_loop -1 -i /app/video.mp4 "
    "-c:v libx264 -preset veryfast -c:a aac -f flv "
    "rtmp://nginx-service.streaming-slice.svc.cluster.local:1935/live/stream1"
)

# Rulează comanda direct în shell
try:
    subprocess.run(ffmpeg_command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Eroare la rularea ffmpeg: {e}")
    sys.exit(1)
except FileNotFoundError:
    print("Eroare: FFmpeg nu este instalat în container!")
    sys.exit(1)
