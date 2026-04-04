# Folosește imaginea oficială cu FFmpeg preinstalat
FROM jrottenberg/ffmpeg:latest

# Director de lucru
WORKDIR /app

# Copiază fișierul video
COPY video.mp4 /app

# Rulează comanda FFmpeg direct (fără Python)
CMD ["-re", "-stream_loop", "-1", "-i", "/app/video.mp4", "-vf", "scale=1280:720", "-c:v", "libx264", "-preset", "ultrafast", "-tune", "zerolatency", "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "4000k", "-c:a", "aac", "-ar", "44100", "-b:a", "128k", "-f", "flv", "rtmp://nginx-service.streaming-slice.svc.cluster.local:1935/live/stream1"]
