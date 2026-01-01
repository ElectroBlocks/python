#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations

eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_digital_display(10, 11)

for _ in range(1, 4):
    eb.set_digital_display(True, "1234")
    time.sleep(1)
    eb.set_digital_display(False, "")
    time.sleep(1)
    eb.set_digital_display(False, "Hi88")
    time.sleep(1)
