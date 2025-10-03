#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration

# Initialise the program settings and configurations
eb = ElectroBlocks(verbose=True) # Create an instance of the ElectroBlocks class
eb.config_joystick("A1", "A3", 9) # Configures the LCD Screen pins

for _ in range(1, 10):
  button_pressed = eb.is_joystick_button_pressed()
  angle = eb.joystick_angle()
  is_engaged = eb.is_joystick_engaged()
  print(f"Engaged: {is_engaged} | Angle: {angle} | Button Pressed: {button_pressed}")  
  time.sleep(2)
  print("CONTINUE")
