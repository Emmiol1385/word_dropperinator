from time import sleep


class ServoSet:
    def __init__(self, ss):
        self.ss = ss
        self.delay=0.1

        def make_dropper(n):
            servo = n
            home = self.clear_positions[n] - 20
            move = self.clear_positions[n] + 5
            return Dropper(self.ss, servo, home, move)

        self.clear_positions = {
            1: 61,
            2: 40,
            3: 59,
            4: 64,
            5: 73
        }
        self.droppers = map(make_dropper, range(1, 5))
        self.home()

    def home(self):
        for d in self.droppers:
            d.to_base()

    def calibrate(self):
        self.home()
        for servo in self.droppers:
            guess = input("guess? ")
            servo.to(guess)
            current = guess
            while True:
                shift = input("shift? (0 for next servo) ")
                if shift == 0:
                    break
                current += shift
                servo.to(current)
                servo.report()

    def drop(self, columns):
        for d in self.droppers:
            if d.servo in columns:
                d.to_offset()
        sleep(self.delay)
        for d in self.droppers:
            if d.servo in columns:
                d.to_base()
        sleep(self.delay)

    def drop_all(self):
        self.drop([s.servo for s in self.droppers])


class Servo:
    def __init__(self, ss, servo):
        self.ss=ss
        self.servo=servo
        self.cur=None

    def to(self, dest):
        self.ss.set_servo(self.servo, dest)
        self.cur = dest

    def report(self):
        print(str(self.servo) + ": " + str(self.cur))

    def zero(self):
        self.to(0)


class Dropper(Servo):
    def __init__(self, ss, servo, base, offset):
        Servo.__init__(self, ss, servo)
        self.base=base
        self.offset=offset
        self.cur=None

    def to_base(self):
        self.to(self.base)

    def to_offset(self):
        self.to(self.offset)
