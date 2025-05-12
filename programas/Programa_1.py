


from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 1)
rele = pin16 

while True:
    temp = temperature()

    if temp > 24:
        np[0] = (0, 255, 0)
        rele.write_digital(1)
    else:
        np[0] = (255, 0, 0)
        rele.write_digital(0)

np.show()
sleep(1000)
