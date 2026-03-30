# Folosește imaginea oficială cu FFmpeg preinstalat
FROM jrottenberg/ffmpeg:latest

# Director de lucru
WORKDIR /app

# Copiază fișierul video
COPY video.mp4 /app

# Rulează comanda FFmpeg direct (fără Python)
CMD ["-re", "-stream_loop", "-1", "-i", "/app/video.mp4", "-c:v", "libx264", "-preset", "veryfast", "-c:a", "aac", "-f", "flv", "rtmp://nginx-service.streaming-slice.svc.cluster.local:1935/live/stream1"]
