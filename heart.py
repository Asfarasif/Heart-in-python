
import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2 * k) - 2 * \
           math.cos(3 * k) - \
           math.cos(4 * k)

speed(0)
bgcolor('black')
penup()
goto(0, 0)
pendown()
color('red')

# tracer(0)  # Turn off automatic screen updates

scale_factor = 0.1  # Initial scale factor

for i in range(1000):
    k = i * 50
    goto(hearta(k) * scale_factor, heartb(k) * scale_factor)
    scale_factor += 0.01  # Gradually increase the scale factor

# update()  # Update the screen all at once
done()
