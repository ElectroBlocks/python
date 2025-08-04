#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_digital_read(7) # Configures the LCD Screen pins

for _ in range(1, 4):
  if eb.digital_read(7):
    print("ON")
  else:
    print("OFF")
  
  time.sleep(5)
  print("CONTINUE")
