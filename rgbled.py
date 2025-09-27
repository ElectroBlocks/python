#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_rgbled(9,10,11) # Configures the LCD Screen pins

for _ in range(1, 10):
  eb.set_color_rgbled(100, 0, 0)
  time.sleep(1)
  eb.set_color_rgbled(0, 100, 0)
  time.sleep(1)
  eb.set_color_rgbled(0, 0, 100)
  time.sleep(1)

print("COMPLETE")
