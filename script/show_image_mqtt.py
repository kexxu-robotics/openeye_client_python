from openeye_client_python.client_mqtt_openeye import ClientMqttOpeneye
from openeye_client_python.client_mqtt_openeye import ListenerPrint
from openeye_client_python.client_mqtt_openeye import ListenerShowImageOpencv
from openeye_client_python.client_mqtt_openeye import ListenerWriteImage

topic_prefix = "devices/openeye-alpha1-7-ve8gs4veFW7McSCZX7mA/"
client = ClientMqttOpeneye()
# client.add_listener(ListenerShowImageOpencv(topic_prefix + "image_eyecam", "image_eyecam"))
# client.add_listener(ListenerShowImageOpencv(topic_prefix + "image_eyecamcrop", "image_eyecamcrop"))
# client.add_listener(ListenerShowImageOpencv(topic_prefix + "image_scenecam", "image_scenecam"))
#client.add_listener(ListenerShowImageOpencv(topic_prefix + "image_overlay", "image_overlay"))
client.add_listener(ListenerWriteImage(topic_prefix + "image_overlay", "C:\\project\\kexxu\\data\\instancegroup\\ig-record"))
client.connect()
client.loop_forever()