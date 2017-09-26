from nio.block.base import Block
from nio.properties import VersionProperty, IntProperty

import Adafruit_PCA9685

class AdafruitPWMServo(Block):

    pulse_length = IntProperty(title="Pulse Length", default=0)
    frequency = IntProperty(title="Frequency", default=60)
    servo_channel = IntProperty(title="Servo Channel", defalut=0)

    def __init__(self):
            super().__init__()
            self.pwm = Adafruit_PCA9685.PCA9685()

    def start(self):
            self.pwm.set_pwm_freq(self.frequency())

    def process_signals(self, signals):
        for signal in signals:
            self.pwm.set_pwm(self.servo_channel(), 0, self.pulse_length())
