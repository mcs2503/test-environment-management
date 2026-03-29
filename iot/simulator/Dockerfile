FROM python:3.9-slim
WORKDIR /app
COPY iot_sensor.py .
RUN pip install paho-mqtt==1.6.1
CMD ["python", "iot_sensor.py", "--broker", "mqtt-service.iot-slice.sv.cluster.local", "--port", "1883", "--topic", "iot/sensors/temperature", "--sensor_id", "temp-sensor-1", "--interval", "0.1"]
