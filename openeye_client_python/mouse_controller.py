from pynput.mouse import Button, Controller
import math
import time
class MouseController:

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