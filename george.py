from time import sleep

class George():

  def __init__(self, mr_python):
    self.mr_python =mr_python
    #all the other methods can talk to the servosix board by saying self.mr_python.set_servo
    self.delay=0.1
    self.kitties=[
      Kitty(mr_python,1,41,66),
      Kitty(mr_python,2,20,45),
      Kitty(mr_python,3,39,64),
      Kitty(mr_python,4,44,69),
      Kitty(mr_python,5,53,78)
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


  def drop(self,kitty_numbers):
    for n in kitty_numbers:
      self.kitties[n-1].walk()
    sleep(self.delay)
    for n in kitty_numbers:
      self.kitties[n-1].attention()
    sleep(self.delay)



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
