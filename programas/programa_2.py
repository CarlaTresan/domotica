"""Programa que acende o neopixel se a temperatura super os 28º
Autora: Carla Tresandí Otero
Data: 05/05/2025"""

from microbit import *

led = pin14
while True:
    luz = pin1.read_analog      #leer valor de luz de LDR
    
    if luz < 300: 
        led.write_digital(1)    # Encender LED noche
    else:
        led.write_digital(0)    #apagar LED día
        
    sleep(1000)
