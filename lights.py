import os
from time import sleep
import graphics

os.system(r'pip install graphics.py')


class TrafficLight:

    def __init__(self):
        self.__colors = {0: ('red', 7), 1: ('gold', 3), 2: ('green', 10)}
        self.lights = [
            graphics.Circle(graphics.Point(200, 130), 25),
            graphics.Circle(graphics.Point(200, 190), 25),
            graphics.Circle(graphics.Point(200, 250), 25),
        ]
        self.msg = graphics.Text(graphics.Point(200, 70), "")

    def draw(self):
        win = graphics.GraphWin('window', 400, 400)
        box = graphics.Rectangle(graphics.Point(160, 30), graphics.Point(240, 300))
        box.setFill('darkgrey')
        box.draw(win)
        for i in range(0, 3):
            self.lights[i].draw(win)
            self.lights[i].setWidth(2)
            self.lights[i].setFill('white')
        self.msg.setSize(30)
        self.msg.setStyle('bold')
        self.msg.draw(win)

    def running(self):
        TrafficLight.draw(self)
        while True:
            for color, count in self.__colors.items():
                i = 1
                count_ = count[1]
                self.lights[color].setFill(count[0])
                self.msg.setTextColor(count[0])
                while i <= count_:
                    self.msg.setText(f'{count_}')
                    sleep(1)
                    count_ -= 1
                self.lights[color].setFill('white')


light = TrafficLight()
light.running()
