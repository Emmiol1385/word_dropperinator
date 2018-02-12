from time import sleep
from servosix import ServoSix 
kitty_ninja=ServoSix()
try:
  kitty_ninja.set_servo(2,20)
  sleep(.5)
  while True:
    kitty_ninja.set_servo(2,50) 
    sleep(0.15)
    kitty_ninja.set_servo(2,20)
    sleep(0.3)
finally:
  kitty_ninja.set_servo(2,20)
  sleep(.5)
  kitty_ninja.cleanup()




#note to self,both sleep numbers,(0.1) and (0.2) both work (but for demo use (0.2) to be safe.
