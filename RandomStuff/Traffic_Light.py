from gpiozero import LED
from time import sleep


class TrafficLight:
    __RED__ = int
    __YELLOW__ = int
    __GREEN__ = int

    def __init__(self, pin_red: int, pin_yellow: int, pin_green: int):
        self.__RED__ = pin_red
        self.__YELLOW__ = pin_yellow
        self.__GREEN__ = pin_green

    def start_traffic_light(self, value: bool):
        red = LED(self.__RED__)
        yellow = LED(self.__YELLOW__)
        green = LED(self.__GREEN__)
        while value:
            red.off()
            yellow.off()
            green.off()
            # now the traffic starts
            red.on()
            sleep(20)
            yellow.on()
            sleep(10)
            red.off()
            yellow.off()
            green.on()
            sleep(7)
            green.off()
            sleep(2)
            yellow.on()
            sleep(5)
            yellow.off()