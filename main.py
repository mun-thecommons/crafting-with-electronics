# Import the required libraries
from machine import Pin, PWM
import time
import random

# Set these variables to be whatever GPIO pins you're using
pin_1 = 0
pin_2 = 4
pin_3 = 22

# Create a Pin object for every GPIO pin used, store these in a list
led_pins = [Pin(pin_1), Pin(pin_2), Pin(pin_3)]

# Create a PWM object for every LED, store these in a list
led_PWM = [PWM(led) for led in led_pins]

# Set the frequency of every LED
for led in led_PWM:
    led.freq(1000)

# This is the function that causes the LEDs to "twinkle"
def twinkle(led):
    # Set the LED "brightness" to random value between 0 and 100
    led_brightness = random.randint(0, 100)
    led_speed = random.choice([-5,5])
    
    # Sets the duty cycle to be the the LED brightness times 500
    # A "duty cycle" refers to how long a signal is active
    # At 65535, it's on 100% of the time, and at 0, it's on 0% of the time
    led.duty_u16(int(led_brightness * 500))
    
    # Increment the brightness value by the speed value
    led_brightness += led_speed
    
    # If the brightness level is above 100, start decreasing
    if led_brightness >= 100:
        led_speed = -5
        time.sleep(0.1)
        
    # If the brightness level is below 0, start increasing
    elif led_brightness <= 0:
        led_speed = 5
        time.sleep(0.1)

# While the Raspberry Pi is powered, run the "twinkle" function on each LED
while True:
    for led in led_PWM:
        twinkle(led)
