#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_button(7) # Configures the LCD Screen pins

for _ in range(1, 4):
  if eb.is_button_pressed(7):
    print("BUTTON PRESSED 7")
  else:
    print("BUTTON NOT PRESSED")
  
  time.sleep(5)
  print("CONTINUE")
