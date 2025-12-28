from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration
i = 0


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_servo(9) # Configures the servo motor on pin 8
eb.config_servo(11) # Configures the servo motor on pin 7



while True:
  for i in range(0, 91, 5):
    eb.move_servo(9, i) # Rotate servo position to i degrees
    eb.move_servo(11, (180 - i)) # Rotate servo position to (180 - i) degrees
    time.sleep(0.05) # Wait for the given/defined seconds.
  for i in range(90, -1, -5):
    eb.move_servo(9, i) # Rotate servo position to i degrees
    eb.move_servo(11, (180 - i)) # Rotate servo position to (180 - i) degrees
    time.sleep(0.05) # Wait for the given/defined seconds.
