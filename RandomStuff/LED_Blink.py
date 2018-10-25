from gpiozero import LED


def start():
    led = LED(2)
    while True:
        led.blink(2, 1)