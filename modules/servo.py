# servo.py
from machine import Pin, PWM

class Servo:
    def __init__(self, pin, min_duty=1802, max_duty=7864, min_angle=0, max_angle=180):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(50)  # servo standard 50Hz
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.min_angle = min_angle
        self.max_angle = max_angle

    def angle(self, a):
        if a < self.min_angle: a = self.min_angle
        if a > self.max_angle: a = self.max_angle
        # linear mapping
        duty = int( (a - self.min_angle) / (self.max_angle - self.min_angle) * (self.max_duty - self.min_duty) + self.min_duty )
        self.pwm.duty_u16(duty)

    def deinit(self):
        self.pwm.deinit()
