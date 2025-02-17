#Day 86: Raspberry Pi project


#Use Python to control hardware (e.g., Raspberry Pi projects).

import os
import glob
import time
from gpiozero import LED, Button

# Initialize LED and Button
led = LED(17)      # LED on GPIO 17
button = Button(2) # Button on GPIO 2

# Set up the DS18B20 temperature sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
    """Reads temperature from the DS18B20 sensor"""
    with open(device_file, 'r') as f:
        lines = f.readlines()
    temp_string = lines[1].split("t=")[-1]
    temp_c = float(temp_string) / 1000.0
    return temp_c

# Button control for LED
button.when_pressed = led.on
button.when_released = led.off

# Main loop
try:
    while True:
        led.toggle()  # Blink LED every second
        temp = read_temp()
        print(f"Temperature: {temp:.2f}°C")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting program...")
    led.off()



#Run the script 
#python3 script.py

