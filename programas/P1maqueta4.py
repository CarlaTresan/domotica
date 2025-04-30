from microbit import *
import machine

servo = machine.PWM(machine.Pin(2))
servo.freq(50)

def mover_servo(grado):
    duty = int((grado / 180) * 75 + 25)
    servo.duty(duty)

angulo = 0
mover_servo(angulo)

while True:
  if button_b.was_pressed():
    if
