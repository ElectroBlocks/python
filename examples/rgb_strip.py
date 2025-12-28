#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration
n_leds = 30

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_rgb_strip("A0", 30, "GRB", 10)

# Scarier colors (darker, less toy-like)
PUMPKIN_ORANGE = (255, 35, 0)     # deep orange
WITCH_PURPLE   = (90, 0, 130)     # dark purple


for j in range(4):
  colors = []
  first_color = PUMPKIN_ORANGE if j % 2 == 0 else WITCH_PURPLE
  second_color = PUMPKIN_ORANGE if j % 2 != 0 else WITCH_PURPLE
  for i in range(n_leds):
    if i % 2 == 0:
        colors.append(first_color)
    else:
        colors.append(second_color)
    
  # Send frame and show
  eb.rgb_strip_set_all_colors(colors)
  eb.rgb_strip_show_all()
  time.sleep(2)

# Test setting all color individually
for i in range(n_leds):
   eb.rgb_strip_set_color(i, 0, 200, 0)

eb.rgb_strip_show_all()
time.sleep(2)



print("COMPLETE")
