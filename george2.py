from time import sleep
from servosix import ServoSix

class George():

  def make_kitty(self,n):
    servo = n
    home = self.clear[n] - 20
    move = self.clear[n] + 5
    return Kitty(self.mr_python, servo, home, move)

  def __init__(self, mr_python):
    self.mr_python =mr_python
    #all the other methods can talk to the servosix board by saying self.mr_python.set_servo
    self.delay=0.1
    self.clear = {
      1: 61,
      2: 40,
      3: 59,
      4: 64,
      5: 73
    }
    self.kitties=[
      self.make_kitty(1),
      self.make_kitty(2),
      self.make_kitty(3),
      self.make_kitty(4),
      self.make_kitty(5)
    ]
    for kitty in self.kitties:
      kitty.attention()

  def home_all(self):
    for k in self.kitties:
      k.attention()

  def inc_all(self, amt):
    for k in self.kitties:
      k.home += amt
      k.zero()
      k.attention()
      print(str(k.servo) + ": " + str(k.home))
      
  def calibrate(self):
    self.home_all()
    for kitty_number in [0,1,2,3,4]:
      guess = input("guess>")
      k = self.kitties[kitty_number]
      k.go_to(guess)
      current = guess
      while True:
        shift = input("shift (0 for next servo) > ")
        if(shift == 0):
          break
        current = current + shift
        k.go_to(current)
        print(str(current))

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
    self.cur=None

  def go_to(self, dest):
    self.ss.set_servo(self.servo, dest)
    self.cur = dest

  def report(self):
    print(str(self.cur))

  def attention(self):
    self.go_to(self.home)
    
  def walk(self):
    self.go_to(self.move)

  def zero(self):
    self.go_to(0)


g = George(ServoSix())

def a():
  s=.2
  sleep(1)
  g.drop([1,5])
  sleep(s)
  g.drop([1,5])
  sleep(s)
  g.drop([1,2,3,4,5])
  sleep(.1)
  g.drop([2,4])
  sleep(.1)
  g.drop([3])
  sleep(s)

def zig():
  sleep(1)
  dir = 1
  cur = 1
  while True:
    g.drop([cur])
    if (cur == 5) and (dir == 1):
      dir *= -1
    if (cur == 1) and (dir == -1):
      dir *= -1
    cur = cur + dir

def cross():
  while True: 
    g.drop([5,1])
    g.drop([4,2])
    g.drop([3,3])
    g.drop([2,4])
    g.drop([1,5])

def rain():
  while True:
    import random   
    ninja=([random.randint(1,5)])
    g.drop(ninja)