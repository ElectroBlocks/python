#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations

eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_stepper_motor(11, 10, 9, 8, 200, 10)

for _ in range(1, 20):
    eb.move_stepper_motor(30)
    time.sleep(0.1)


print("COMPLETE")
