from openeye_client_python.client_mqtt_openeye import ClientMqttOpeneye

client = ClientMqttOpeneye()
client.connect()
client.loop_forever()