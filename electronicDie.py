from sense_hat import SenseHat
import time
from random import choice
import random
  
sense = SenseHat()
  
sense.clear()
loop_break = False 
b = (0, 0, 0) #black
g = (0, 255, 0) #green
r = (255, 0, 0) #red
p = (255,105, 180) #pink
B =(0, 0, 255) #blue

# Die number one
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
# Die number two
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
# Die number three
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
# Die number four
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
# Die number five 
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
# Die number six 
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
class emoJ:
    
    def __init__(self, loop_break):
        self.loop_break = loop_break
   # This method picks a random number between 1-6
    def roll_dice(self):
      r = random.randint(1,6) 
      p = r%6
      n = 0
       
      if p == 1:
          sense.set_pixels(ONE)
          n = 1
      elif p == 2:
          sense.set_pixels(TWO)
          n = 2
      elif p == 3:
          sense.set_pixels(THREE)
          n = 3
      elif p == 4:
          sense.set_pixels(FOUR)
          n = 4
      elif p == 5:
          sense.set_pixels(FIVE)
          n = 5
      elif p == 0:
          sense.set_pixels(SIX)
          n = 6
      return n
    #Check's for movement
    def check_for_movement(self):
      sense.show_message("Shake  ", scroll_speed=0.05)
      while True:
          x, y, z = sense.get_accelerometer_raw().values()

          x = abs(x)
          y = abs(y)
          z = abs(z)

          if x > 1.5 or y > 1.5 or z > 1.5:
              roll = dice.roll_dice() 
              time.sleep(1)
              if self.loop_break is True:
                  return roll
                  break

dice = emoJ(loop_break)
if __name__ == "__main__":
    dice.check_for_movement()
    dice.roll_dice()


