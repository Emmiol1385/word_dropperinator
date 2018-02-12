from time import sleep

class George():

  def __init__(self, mr_python):
    self.mr_python =mr_python
    #all the other methods can talk to the servosix board by saying self.mr_python.set_servo
    self.delay=0.15
    self.kitties=[
      Kitty(mr_python,1,40,70),
      Kitty(mr_python,2,20,50),
      Kitty(mr_python,3,40,70),
      Kitty(mr_python,4,45,75),
      Kitty(mr_python,5,50,85)
    ]
    for kitty in self.kitties:
      kitty.attention()

  def drop_all(self):
    for kitty in self.kitties:
      kitty.walk()
    sleep(self.delay)
    for kitty in self.kitties:
      kitty.attention()
    sleep(self.delay)

  def drop(servo, move, home, delay):
    self.mr_python.set_servo(servo,move)
    sleep(delay) 
    self.mr_python.set_servo(servo,home)
    sleep(delay)



class Kitty():
  def __init__(self,ss,servo,home,move):
    self.servo=servo
    self.home=home
    self.ss=ss
    self.move=move

  def attention(self):
    self.ss.set_servo (self.servo,self.home)
    
  def walk(self):
    self.ss.set_servo(self.servo,self.move)
