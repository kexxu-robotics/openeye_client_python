from openeye_client_python.client_mqtt_openeye import ClientMqttOpeneye
from openeye_client_python.client_mqtt_openeye import ListenerPrint
from openeye_client_python.client_mqtt_openeye import ListenerShowImageOpencv

topic = "devices/openeye-alpha1-7-ve8gs4veFW7McSCZX7mA/json_marker_qr"
ssid = 'CasadeDante4'
password = 'Cuevano1983'
#password = 'Cuevano1983XXXX'

# T	WPA	Authentication type; can be WEP or WPA, or leave empty for no password.
# S	MyNetworkName	Network SSID. Required.
# P	ThisIsMyPassword	Password, ignored if T is left blank.
# H	true	Optional. True if the network SSID is hidden.


data = 'WIFI:S:' + ssid + ';T:WPA;P:' + password + ';;'
client = ClientMqttOpeneye()
client.add_listener(ListenerPrint(topic))

client.connect()
json_qr = {}
json_qr['list_marker'] = []
json_qr['list_marker'].append({
    'type':'qrcode',
    'data':data
})

client.send_json(topic, json_qr)
client.loop_forever()