"""Programa que acende o neopixel se a temperatura super os 28º
Autora: Carla Tresandí Otero
Data: 05/05/2025"""


from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 1)
rele = pin16 

while True:
    temp = temperature()

    if temp > 28:
        np[0] = (0, 255, 0)
        rele.write_digital(1)
    else:
        np[0] = (0, 0, 0)
        rele.write_digital(0)

np.show()
sleep(1000)
