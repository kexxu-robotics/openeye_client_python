import sys
import json
import paho.mqtt.client as mqtt
import numpy as np
import imageio
import cv2

class ListenerPrint:

    def __init__(self, topic):
        super(ListenerPrint, self).__init__()
        self.topic = topic
    
    def message(self, bytearray_json):
        print(self.topic + " " + str(len(bytearray_json)))
        print(bytearray_json)
        sys.stdout.flush()


class ListenerShowImageOpencv:

    def __init__(self, topic, name_image):
        super(ListenerShowImageOpencv, self).__init__()
        self.topic = topic
        self.name_image = name_image
    
    def message(self, bytearray_image):
        print(self.topic + " " + str(len(bytearray_image)))
        sys.stdout.flush()

        image = imageio.imread(bytearray_image)
        # get uint8 mode (float16 is default)
        array_image = np.asarray(image, dtype=np.uint8)
        # swap channels
        temp = array_image[:,:,2]
        array_image[:,:,2] = array_image[:,:,0]
        array_image[:,:,0] = temp
        array_image = cv2.resize(array_image, dsize=(320, 240), interpolation=cv2.INTER_CUBIC)
        cv2.imshow(self.name_image, array_image)
        cv2.waitKey(1)

class ClientMqttOpeneye:

    def __init__(self):
        super(ClientMqttOpeneye, self).__init__()
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.dict_listener = {}

    def add_listener(self, listener):
        self.dict_listener[listener.topic] = listener

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected with result code " + str(rc))
            sys.stdout.flush()
            # client.subscribe("$SYS/#")
            client.subscribe("#")
        else:
            raise RuntimeError('error while connection')

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if msg.topic in self.dict_listener:
            self.dict_listener[msg.topic].message(msg.payload)

    def connect(self):
        self.client.connect("raspberrypi.local", 1883, 60)

    def loop(self):
        self.client.loop()

    def loop_forever(self):
        self.client.loop_forever()

    def send_json(self, topic, json_message):
        self.client.publish(topic, json.dumps(json_message))
