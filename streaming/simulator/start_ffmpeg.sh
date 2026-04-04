#!/bin/sh

# Rulează ffmpeg cu parametri din variabilele de mediu
exec ffmpeg \
  -re -stream_loop -1 -i /app/video.mp4 \
  -vf "scale=$RESOLUTION" \
  -c:v libx264 -preset "$PRESET" -tune "$TUNE" \
  -b:v "$BITRATE" -maxrate "$MAXBITRATE" -bufsize "$BUFFER_SIZE" \
  -c:a aac -ar 44100 -b:a "$BITRATE_AUDIO" \
  -f flv "$RTMP_SERVER"
