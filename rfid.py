#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_rfid(2,3) # Configures the LCD Screen pins

for _ in range(1, 10):
  tag_number = eb.rfid_tag_number()
  card_number = eb.rfid_card_number()
  print(f"Tag: {tag_number} | Card: {card_number}")  
  time.sleep(10)
  print("CONTINUE")
