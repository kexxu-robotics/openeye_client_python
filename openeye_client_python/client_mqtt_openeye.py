import sys
import paho.mqtt.client as mqtt

class ClientMqttOpeneye:

    def __init__(self):
        super(ClientMqttOpeneye, self).__init__()
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected with result code " + str(rc))
            sys.stdout.flush()
            #client.subscribe("$SYS/#")
            client.subscribe("#")
        else:
            raise RuntimeError('error while connection')

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        sys.stdout.flush()

    def connect(self):
        self.client.connect("raspberrypi.local", 1883, 60)

    def loop(self):
        self.client.loop()

    def loop_forever(self):
        self.client.loop_forever()
