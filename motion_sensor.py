#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_motion_sensor(10, 11) # Echo and Trig

for _ in range(1, 4):
  cm = eb.motion_distance_cm()
  print(f"Distance: {cm} centimeters")
  time.sleep(1)
  print("CONTINUE")
