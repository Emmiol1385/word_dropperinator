
from george import g
from time import sleep
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

while True:
  print"yo"
  print"one  zigzag"
  print"two rain"
  print"three cross"
  dojo=input("so why are you here")
  if dojo==1:
    zig(  )
  if dojo==2:
    rain()
  if dojo==3:
    cross()
  if dojo==9:
    g.mr_python.cleanup()
    break
