import paho.mqtt.publish as publish
import random
import time

THING_SPEAK_CHANNEL_ID = '2488598'
MQTT_HOST = 'mqtt3.thingspeak.com'
MQTT_CLIENT_ID = "DjwsITgoCzAFKTEEIDc6Oy0"
MQTT_USERNAME  = "DjwsITgoCzAFKTEEIDc6Oy0"
MQTT_PASSWORD  = "Y2HvTDh77A8/y0v+TdUygnMr"
TRANSPORT = "websockets"
PORT = 80

def generate_sensor_data():
    return {
        'temperature': random.uniform(-50, 50)  # Temperature in Celsius
        ,'humidity': random.uniform(0, 100)      # Humidity in %
        ,'co2': random.uniform(300, 2000)         # CO2 in ppm
    }

def publish_data(sensor_data):
    payload = "field1=" + str(sensor_data['temperature']) + "&field2=" + str(sensor_data['humidity']) + "&field3=" + str(sensor_data['co2'])
    try:
        publish.single(topic = "channels/" + THING_SPEAK_CHANNEL_ID + "/publish",
                       payload=payload,
                       hostname=MQTT_HOST,
                       transport=TRANSPORT,
                       port=PORT,
                       client_id=MQTT_CLIENT_ID,
                       auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD})

        print("Data published successfully.")
    except Exception as e:
        print(f"Failed to publish data: {e}")

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        print(f"Publishing data: {sensor_data}")
        publish_data(sensor_data)
        time.sleep(5)