from sense_hat import SenseHat
from time import sleep
from random import choice
import random

sense = SenseHat()

sense.clear()

sense.show_message("Shake  ")

b = (0, 0, 0)
g = (0, 255, 0)
r = (255, 0, 0)
p = (255,105, 180)
B =(0, 0, 255)

ONE = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,r,r,r,r,b,b,
b,b,r,r,r,r,b,b,
b,b,r,r,r,r,b,b,
b,b,r,r,r,r,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

TWO = [
b,b,b,b,b,b,b,b,
b,p,p,p,b,b,b,b,
b,p,p,p,b,b,b,b,
b,p,p,p,b,b,b,b,
b,b,b,b,p,p,p,b,
b,b,b,b,p,p,p,b,
b,b,b,b,p,p,p,b,
b,b,b,b,b,b,b,b,
]

THREE = [
g,g,b,b,b,b,b,b,
g,g,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,g,g,
b,b,b,b,b,b,g,g,
]

FOUR = [
b,b,b,b,b,b,b,b,
b,B,B,b,b,B,B,b,
b,B,B,b,b,B,B,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,B,B,b,b,B,B,b,
b,B,B,b,b,B,B,b,
b,b,b,b,b,b,b,b,
]

FIVE = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]

SIX = [
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
]

def roll_dice():
    r = random.randint(1,6) 
    p= r1%6
     
    if p == 1:
        sense.set_pixels(ONE)
    elif p == 2:
        sense.set_pixels(TWO)
    elif p == 3:
        sense.set_pixels(THREE)
    elif p == 4:
        sense.set_pixels(FOUR)
    elif p == 5:
        sense.set_pixels(FIVE)
    elif p == 0:
        sense.set_pixels(SIX)

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1.5 or y > 1.5 or z > 1.5:
        roll_dice() 
        time.sleep(1)