from nio.block.base import Block
from nio.properties import VersionProperty

import time
import Adafruit_PCA9685

class AdafruitPWMServo(Block):

    def __init__(self):
            super().__init__()
            self.pwm = Adafruit_PCA9685.PCA9685()
            self.servo_min = 200
            self.servo_max = 550
            self.pwm.set_pwm_freq(60)

    def process_signals(self, signals):
        for signal in signals:
            self.pwm.set_pwm(0, 0, servo_min)
            time.sleep(1)
            self.pwm.set_pwm(0, 0, servo_max)
            time.sleep(1)
