#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations
eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_led_matrix(10, 11, 12) # Echo and Trig

for _ in range(1, 4):
  for i in range(1, 9):
    eb.set_led_matrix_led(i, i, True)
    time.sleep(0.2)
    eb.set_led_matrix_led(i, i, False)

  for i in range(8, 2, -1):
    eb.set_led_matrix_led(i, i, True)
    time.sleep(0.2)
    eb.set_led_matrix_led(i, i, False)


for _ in range(1, 4):
  # START CODE TO DRAW BLOCK 0qnZ+JUE_N?s/r^0,nMq
  eb.set_led_matrix_led(1, 1, False)
  eb.set_led_matrix_led(1, 2, False)
  eb.set_led_matrix_led(1, 3, False)
  eb.set_led_matrix_led(1, 4, False)
  eb.set_led_matrix_led(1, 5, False)
  eb.set_led_matrix_led(1, 6, False)
  eb.set_led_matrix_led(1, 7, False)
  eb.set_led_matrix_led(1, 8, False)
  eb.set_led_matrix_led(2, 1, False)
  eb.set_led_matrix_led(2, 2, True)
  eb.set_led_matrix_led(2, 3, True)
  eb.set_led_matrix_led(2, 4, False)
  eb.set_led_matrix_led(2, 5, False)
  eb.set_led_matrix_led(2, 6, True)
  eb.set_led_matrix_led(2, 7, True)
  eb.set_led_matrix_led(2, 8, False)
  eb.set_led_matrix_led(3, 1, False)
  eb.set_led_matrix_led(3, 2, True)
  eb.set_led_matrix_led(3, 3, True)
  eb.set_led_matrix_led(3, 4, False)
  eb.set_led_matrix_led(3, 5, False)
  eb.set_led_matrix_led(3, 6, True)
  eb.set_led_matrix_led(3, 7, True)
  eb.set_led_matrix_led(3, 8, False)
  eb.set_led_matrix_led(4, 1, False)
  eb.set_led_matrix_led(4, 2, False)
  eb.set_led_matrix_led(4, 3, False)
  eb.set_led_matrix_led(4, 4, False)
  eb.set_led_matrix_led(4, 5, False)
  eb.set_led_matrix_led(4, 6, False)
  eb.set_led_matrix_led(4, 7, False)
  eb.set_led_matrix_led(4, 8, False)
  eb.set_led_matrix_led(5, 1, False)
  eb.set_led_matrix_led(5, 2, False)
  eb.set_led_matrix_led(5, 3, False)
  eb.set_led_matrix_led(5, 4, True)
  eb.set_led_matrix_led(5, 5, True)
  eb.set_led_matrix_led(5, 6, False)
  eb.set_led_matrix_led(5, 7, False)
  eb.set_led_matrix_led(5, 8, False)
  eb.set_led_matrix_led(6, 1, False)
  eb.set_led_matrix_led(6, 2, False)
  eb.set_led_matrix_led(6, 3, False)
  eb.set_led_matrix_led(6, 4, False)
  eb.set_led_matrix_led(6, 5, False)
  eb.set_led_matrix_led(6, 6, False)
  eb.set_led_matrix_led(6, 7, False)
  eb.set_led_matrix_led(6, 8, False)
  eb.set_led_matrix_led(7, 1, True)
  eb.set_led_matrix_led(7, 2, True)
  eb.set_led_matrix_led(7, 3, True)
  eb.set_led_matrix_led(7, 4, True)
  eb.set_led_matrix_led(7, 5, False)
  eb.set_led_matrix_led(7, 6, True)
  eb.set_led_matrix_led(7, 7, True)
  eb.set_led_matrix_led(7, 8, True)
  eb.set_led_matrix_led(8, 1, False)
  eb.set_led_matrix_led(8, 2, True)
  eb.set_led_matrix_led(8, 3, True)
  eb.set_led_matrix_led(8, 4, True)
  eb.set_led_matrix_led(8, 5, True)
  eb.set_led_matrix_led(8, 6, True)
  eb.set_led_matrix_led(8, 7, True)
  eb.set_led_matrix_led(8, 8, False)

  # FINISH CODE TO DRAW BLOCK 0qnZ+JUE_N?s/r^0,nMq
  time.sleep(2) # Wait for the given/defined seconds.
  eb.set_led_matrix_led(7, 5, True)
  time.sleep(2) # Wait for the given/defined seconds.

print("COMPLETE")