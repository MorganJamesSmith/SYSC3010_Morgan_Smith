import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# from pynput.keyboard import Key, Controller

# GPIO code modified from: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
# keyboard code modified from: https://nitratine.net/blog/post/simulate-keypresses-in-python/

# This script waits for pin 1 and pin 3 to be shorted. When that
# occurs, it prints out a little message

# I wanted it to type out a little message but that would require a
# running X server

# keyboard = Controller()


def button_callback(channel):
    print("Button was pushed!")
    #keyboard.type('Button was pushed!')

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(3,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

while True:
    try:
        continue
    except KeyboardInterrupt:
        GPIO.cleanup() # Clean up
        exit()
