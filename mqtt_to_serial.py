import paho.mqtt.client as mqtt
import serial
import time
import platform
from datetime import datetime

# Auto-select serial port based on OS
if platform.system() == 'Windows':
    serial_port = 'COM3'  # Change if using a different COM port
else:
    serial_port = '/dev/ttyUSB0'  # Change if using another USB port

# Initialize serial connection to Arduino
try:
    ser = serial.Serial(serial_port, 9600)
    print(f"Serial connected on {serial_port}")
except Exception as e:
    print(f"Failed to connect to serial port {serial_port}: {e}")
    exit(1)

# Dictionary to hold the on/off schedule
schedule = {}

# MQTT message callback
def on_message(client, userdata, msg):
    global schedule
    payload = msg.payload.decode()
    try:
        # Expecting format "HH:MM,HH:MM"
        on_time, off_time = payload.split(',')
        schedule['on'] = on_time.strip()
        schedule['off'] = off_time.strip()
        print(f"New schedule received: ON at {schedule['on']}, OFF at {schedule['off']}")
    except Exception as e:
        print("Error parsing message:", e)

# Configure MQTT client
client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("light/schedule")
client.on_message = on_message
client.loop_start()

# Main loop to check schedule and send commands
try:
    while True:
        now = datetime.now().strftime("%H:%M")

        if 'on' in schedule and now == schedule['on']:
            ser.write(b'1')
            print("Sent ON command")

        elif 'off' in schedule and now == schedule['off']:
            ser.write(b'0')
            print("Sent OFF command")

        time.sleep(30)

except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    ser.close()
