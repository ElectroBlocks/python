#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.analog_config(6)

for i in range(1, 200):
  eb.analog_write(6, i)
  time.sleep(0.2)

print("COMPLETE")