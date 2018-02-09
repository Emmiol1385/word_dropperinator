from time import sleep
from servosix import ServoSix 
kitty_ninja=ServoSix()
kitty_ninja.set_servo(1,40) 
sleep(0.1)
kitty_ninja.set_servo(1,0)
sleep(0.2)
kitty_ninja.cleanup()




#note to self,both sleep numbers,(0.1) and (0.2) both work (but for demo use (0.2) to be safe.