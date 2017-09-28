import Adafruit_PCA9685

# Initialise the servo
pwm = Adafruit_PCA9685.PCA9685()

# Configure pulse length, frequency, and channel
pulse_length = 150
frequency = 60
servo_channel = 0

# Set the frequency
pwm.set_pwm_freq(frequency)

# Move the servo
pwm.set_pwm(servo_channel, 0, pulse_length)
