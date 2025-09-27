#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_ir_remote(2) # Configures the LCD Screen pins

for _ in range(1, 10):
  sensed_code = eb.ir_remote_has_sensed_code()
  code = eb.ir_remote_get_code()
  print(f"Sensed Code: {sensed_code} | Code: {code}")  
  time.sleep(10)
  print("CONTINUE")
