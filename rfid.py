#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_rfid(2,3) # Configures the LCD Screen pins

for _ in range(1, 10):
  sensed_card = eb.rfid_sensed_card()
  tag_number = eb.rfid_tag_number()
  print(f"Sensed Card: {sensed_card} | Tag: {tag_number}")  
  time.sleep(10)
  print("CONTINUE")
