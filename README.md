######### CIS-600 Internet of Things - Assignment 3 #########
A cloud-based IoT system for collecting data from virtual sensors using MQTT protocol and ThingSpeak as the cloud-based backend for data storage and visualization.

Steps used in developing the IOT system
1. Sensor Simulation: Created a Python program to simulate sensors that generate periodic and random CO2 pressure, humidity, and temperature measurements within predefined limits.
2. ThingSpeak Setup: ThingSpeak was chosen as the cloud-based backend, with its MQTT capabilities for data input and storage.
3. Configuration and Authentication: Set up the MQTT channel, client, and device with the appropriate parameters, such as channel ID, API key, Client ID, username, and password, for authentication with the ThinkSpeak Broker.
4. Data Monitoring and Analysis: Data was published to the ThingSpeak channel as payloads using the Paho MQTT library and MQTT Topic. Analyzed the data and tracked sensor readings to ensure proper data release.

Console output:
https://github.com/wadeshilpa/CIS600_IOT/blob/d2a386ae8e1451d9bcf10bfc776fe8484340234d/Console_output.png

ThingSpeak Dashboard - sensors data:
https://github.com/wadeshilpa/CIS600_IOT/blob/d2a386ae8e1451d9bcf10bfc776fe8484340234d/Temperature_sensor_data.png

https://github.com/wadeshilpa/CIS600_IOT/blob/d2a386ae8e1451d9bcf10bfc776fe8484340234d/Humidity_sensor_data.png

https://github.com/wadeshilpa/CIS600_IOT/blob/d2a386ae8e1451d9bcf10bfc776fe8484340234d/CO2_sensor_data.png
