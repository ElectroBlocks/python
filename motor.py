#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations

eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_motor(11, 10, 9, 3, 4, 5)

for _ in range(1, 4):
    eb.move_motor(1, 200, "clockwise")
    time.sleep(1)
    eb.stop_motor(1)
    eb.move_motor(2, 200, "clockwise")
    time.sleep(1)
    eb.stop_motor(2)
    time.sleep(1)
    eb.move_motor(1, 200, "anticlockwise")
    time.sleep(1)
    eb.stop_motor(1)
    eb.move_motor(2, 200, "anticlockwise")
    time.sleep(1)
    eb.stop_motor(2)
    time.sleep(1)
