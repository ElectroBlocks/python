#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_led_matrix(10, 11, 12, False) # Echo and Trig

for i in range(1, 9):
  eb.set_led_matrix_led(i, i, True)
  time.sleep(0.2)
  eb.set_led_matrix_led(i, i, False)

for i in range(8, 0, -1):
  eb.set_led_matrix_led(i, i, True)
  time.sleep(0.2)
  eb.set_led_matrix_led(i, i, False)


for _ in range(1, 4):
  eb.draw_led_matrix([
    "B00000000",
    "B01100110",
    "B01100110",
    "B00000000",
    "B00011000",
    "B00000000",
    "B11111111",
    "B01111110"
  ])
  time.sleep(1)
  eb.draw_led_matrix([
    "B00000000",
    "B01100000",
    "B01100110",
    "B00000000",
    "B00011000",
    "B00000000",
    "B11111111",
    "B01111110"
  ]) 
  time.sleep(1) 
print("COMPLETE")