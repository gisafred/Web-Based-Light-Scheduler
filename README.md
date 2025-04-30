# Web-Based Light Scheduler

A web-based system for scheduling light controls using WebSocket, MQTT, and serial communication with Arduino.

## Overview

This project implements a light scheduling system with the following components:
- Web interface for setting ON/OFF times
- WebSocket server for real-time communication
- MQTT broker for message handling
- Serial communication with Arduino for light control

## System Architecture

```
[Web Interface] <-> [WebSocket Server] <-> [MQTT Broker] <-> [Serial Bridge] <-> [Arduino]
```

## Components

1. **Web Interface** (`index.html`)
   - Modern, responsive design
   - Time input fields for scheduling
   - WebSocket client for real-time updates

2. **WebSocket Server** (`ws_server.py`)
   - Handles web client connections
   - Converts WebSocket messages to MQTT format
   - Runs on port 6789

3. **MQTT to Serial Bridge** (`mqtt_to_serial.py`)
   - Subscribes to MQTT topics
   - Manages scheduling logic
   - Controls Arduino via serial connection

## Prerequisites

- Python 3.x
- MQTT Broker (e.g., Mosquitto)
- Arduino board
- Required Python packages:
  - `paho-mqtt`
  - `pyserial`
  - `websockets`
  - `asyncio`

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install paho-mqtt pyserial websockets asyncio
   ```

2. **Configure MQTT Broker**
   - Install Mosquitto MQTT broker
   - Ensure it's running on localhost:1883

3. **Arduino Setup**
   - Connect Arduino to USB port
   - Note the COM port number (Windows) or device path (Linux)
   - Update serial port in `mqtt_to_serial.py` if needed

4. **Start the System**
   ```bash
   # Start WebSocket server
   python ws_server.py

   # Start MQTT to Serial bridge
   python mqtt_to_serial.py
   ```

5. **Access Web Interface**
   - Open `index.html` in a web browser
   - Default address: `http://localhost`

## Usage

1. Open the web interface
2. Set desired ON and OFF times
3. Click Submit to save the schedule
4. The system will automatically control the lights at scheduled times

## Configuration

### Serial Port Settings
- Windows: Default COM3
- Linux: Default /dev/ttyUSB0
- Baud Rate: 9600

### WebSocket Settings
- Host: localhost
- Port: 6789

### MQTT Settings
- Broker: localhost
- Port: 1883
- Topic: light/schedule

## Troubleshooting

1. **Serial Connection Issues**
   - Verify correct COM port
   - Check Arduino connection
   - Ensure proper permissions

2. **MQTT Connection Issues**
   - Verify MQTT broker is running
   - Check broker address and port
   - Confirm topic subscription

3. **WebSocket Issues**
   - Ensure server is running
   - Check browser console for errors
   - Verify port availability

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 