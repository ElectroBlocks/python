#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.digital_write_config(13)
for _ in range(1, 10):
  eb.digital_write(13, 1)
  time.sleep(1)
  eb.digital_write(13, 0)
  time.sleep(1)

print("COMPLETE")