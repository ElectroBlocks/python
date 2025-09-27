#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_rgb_strip("A0", 30, "GRB", 10)

for i in range(0, 29):
  eb.rgb_strip_set_color(i, 100, 0, 100)

eb.rgb_strip_show_all()
time.sleep(4)

print("COMPLETE")
