------------- CIS-600 Internet of Things - Assignment 3 -----------

A cloud-based IoT system for collecting data from virtual sensors using MQTT protocol and ThingSpeak as the cloud-based backend for data storage and visualization.

-----------------------------------------------------------------------------------------------------

Steps used in developing the IOT system
1. Sensor Simulation: Created a Python program to simulate sensors that generate periodic and random CO2 pressure, humidity, and temperature measurements within predefined limits.
2. ThingSpeak Setup: ThingSpeak was chosen as the cloud-based backend, with its MQTT capabilities for data input and storage.
3. Configuration and Authentication: Set up the MQTT channel, client, and device with the appropriate parameters, such as channel ID, API key, Client ID, username, and password, for authentication with the ThinkSpeak Broker.
4. Data Monitoring and Analysis: Data was published to the ThingSpeak channel as payloads using the Paho MQTT library and MQTT Topic. Analyzed the data and tracked sensor readings to ensure proper data release.
   
-----------------------------------------------------------------------------------------------------
Console output:

<img width="946" alt="Console_output" src="https://github.com/wadeshilpa/CIS600_IOT/assets/160187057/d66d9f65-4b3f-4e69-95d0-962b63f998e8">

-----------------------------------------------------------------------------------------------------

ThingSpeak Dashboard - sensors data:

![Temperature_sensor_data](https://github.com/wadeshilpa/CIS600_IOT/assets/160187057/181e591a-823c-48fb-9c52-6ce84774a038)

![Humidity_sensor_data](https://github.com/wadeshilpa/CIS600_IOT/assets/160187057/d12a70df-5258-4b36-9a2a-36dac55a2653)

![CO2_sensor_data](https://github.com/wadeshilpa/CIS600_IOT/assets/160187057/1f2824e8-80c4-4821-acf6-02f4daec6f8d)

-----------------------------------------------------------------------------------------------------
