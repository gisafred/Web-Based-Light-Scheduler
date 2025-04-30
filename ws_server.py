import asyncio
import websockets
import json
import subprocess


async def handler(websocket, path):
    async for message in websocket:
        schedule= json.loads(message)
        on = schedule["on"]
        off= schedule["off"]
        mqtt_msg = f"{on},{off}"
        subprocess.run(["mosquitto_pub", "-t", "light/schedule","-m",mqtt_msg])
        print("Schedule sent to MQTT", mqtt_msg);

start_server= websockets.serve(handler, "localhost", 6789)
asyncio.get_event_loop().run_until_complete(start_server)
print("Websocket Server started at ws://localhost:6789")
asyncio.get_event_loop().run_forever()

