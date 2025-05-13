from microbit import*

# Ángulo actual del servo (0 o 90)
angulo = 0

# Función para mover el servo al ángulo indicado
def mover_servo(a):
    if a == 0:
        pin2.write_analog(26)  # 0 grados
    elif a == 90:
        pin2.write_analog(77)  # 90 grados

# Posición inicial del servo
mover_servo(angulo)

# Bucle principal
while True:
    if button_b.was_pressed():
        if angulo == 0:
            angulo = 90
        else:
            angulo = 0
        mover_servo(angulo)
        sleep(300)

