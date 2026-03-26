import paho.mqtt.client as mqtt
import time
import random
import argparse
import os

# cmd line args
parser = argparse.ArgumentParser(description="IoT sensor simulator")
parser.add_argument("--broker", type=str, default="mqtt-service.iot-slice.svc.cluster.local", help="MQTT broker address")
parser.add_argument("--port", type=int, default=1883, help="MQTT broker port")
parser.add_argument("--topic", type=str, default="iot/sensors/temperature", help="MQTT topic where sensor will send messages")
parser.add_argument("--sensor_id", type=str, default="sensor-1", help="sensor ID")
parser.add_argument("--interval", type=float, default=5.0, help="Delay [ in seconds ] between mesages")
args = parser.parse_args()

# connection function
def on_connect(client, userdata, flags, rc):
    print(f"Sensor {args.sensor_id} has been connected to the broker")

# MQTT client creation
client = mqtt.Client(args.sensor_id)
client.on_connect = on_connect
client.connect(args.broker, args.port, 60)
client.loop_start()

try:
    while True:
        temperature = random.uniform(20.0, 30.0)  # generate a random number between 20.0 and 30.0 - temperature
        client.publish(args.topic, f"{args.sensor_id}: {temperature:.2f}°C")
        print(f"[{args.sensor_id}] sent: {temperature:.2f}°C")
        time.sleep(args.interval)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    print(f"[{args.sensor_id}] shutdown")

