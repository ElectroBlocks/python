
  
#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_lcd(4, 20, 63) # Configures the LCD Screen pins



for _ in range(1, 3):
  eb.lcd_toggle_backlight(False) # Turn off the LCD backlight
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_toggle_backlight(True) # Turn on the LCD backlight
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_clear() # Clear the LCD screen
  eb.lcd_print(0, 0, "HELLO") # Print the first row text on the LCD screen
  eb.lcd_print(1, 0, "WORLD") # Print the second row text on the LCD screen
  time.sleep(3) # Pause / Wait
  eb.lcd_scrollright()
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_scrollleft()
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_blink_curor(0, 0, True) # Turn on the blink.
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_blink_curor(0, 0, False) # Turn off the blink.
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_print_all_4(". HELLO", "  WORLD. .", "Talk", "  Test Testing ! !!. *")
  time.sleep(2) # Wait for the given/defined seconds.
  eb.lcd_clear()
  time.sleep(2) # Wait for the given/defined seconds.
print("COMPLETE")