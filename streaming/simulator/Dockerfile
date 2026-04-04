FROM jrottenberg/ffmpeg:latest

WORKDIR /app

COPY video.mp4 /app
COPY start_ffmpeg.sh /app/start_ffmpeg.sh

RUN chmod +x /app/start_ffmpeg.sh

ENTRYPOINT []

ENTRYPOINT ["/app/start_ffmpeg.sh"]
