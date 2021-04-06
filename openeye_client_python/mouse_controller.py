import math
import time

from pynput.mouse import Button, Controller
from screeninfo import get_monitors

class MouseController:

    STATE_RUNNING = 1
    STATE_CALIBRATE_PRE = 2
    STATE_CALIBRATE_TOP_LEFT = 3
    STATE_CALIBRATE_TOP_RIGHT = 4
    STATE_CALIBRATE_BOTTOM_RIGHT = 5
    STATE_CALIBRATE_BOTTOM_LEFT = 6
    STATE_CALIBRATE_CENTRE = 7

    def __init__(self, mqtt_listenerer, index_monitor=0,):
        super(MouseController, self).__init__()
        self.mqtt_listenerer = mqtt_listenerer
        self.mqtt_listenerer.subscribe('event_move', self.move)
        self.mqtt_listenerer.subscribe('event_blink', self.blink)

    @staticmethod
    def calibrate():
        list_top_left = []
        list_top_right = []
        list_bottom_right = []
        list_bottom_left = []
        list_bottom_centre = []

        for m in get_monitors():
            print(str(m))

        print('calabrating for monitor')

    @staticmethod
    def circle():
        mouse = Controller()

        circle_length = 100
        circle_size = 200
        circle_offset = 500
        sleep = 0.01
        for i in range(circle_length):
            x = math.sin(i/circle_length * 2 * math.pi) * circle_size
            y = math.cos(i/circle_length * 2 * math.pi) * circle_size
            mouse.position = (x + circle_offset, y + circle_offset)
            time.sleep(sleep)    

    @staticmethod
    def test():
        mouse = Controller()

        # Read pointer position
        print('The current pointer position is {0}'.format(mouse.position))

        # Set pointer position
        mouse.position = (10, 20)
        print('Now we have moved it to {0}'.format(mouse.position))

        # Move pointer relative to current position
        mouse.move(5, -5)

        # Press and release
        mouse.press(Button.left)
        mouse.release(Button.left)

        # Double click; this is different from pressing and releasing
        # twice on Mac OSX
        mouse.click(Button.left, 2)

        # Scroll two steps down
        mouse.scroll(0, 2)