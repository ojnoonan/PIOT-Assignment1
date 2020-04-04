from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
P = (255,105, 180)

def smileyFace():
    
    Smface = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, G, G, Y, Y, G, G, Y,
    Y, G, G, Y, Y, G, G, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, B, B, B, B, B, B, Y,
    Y, Y, B, B, B, B, Y, Y,
    Y, Y, Y, B, B, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    ]
    return Smface

def  sadFace():
   
    Sface = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, P, P, Y, Y, P, P, Y,
    Y, P, P, Y, Y, P, P, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, R, R, Y, Y, Y,
    Y, Y, R, R, R, R, Y, Y,
    Y, R, R, R, R, R, R, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    ]
    return Sface
 

def funnyFace():
    
    Fface = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, W, W, Y, W, W, W, Y,
    Y, W, W, Y, W, W, W, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, G, G, G, G, G, G, Y,
    Y, G, G, G, R, R, R, Y,
    Y, Y, Y, Y, R, R, R, Y,
    Y, Y, Y, Y, R, R, R, Y,
    ]
    return  Fface

FACES = [smileyFace,sadFace,funnyFace]
count = 0

while True: 
     
    s.set_pixels(FACES[count % len(FACES)]())
    time.sleep(3)
    count += 1  