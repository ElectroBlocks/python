#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations

eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_passive_buzzer(9)

for _ in range(1, 4):
    eb.play_passive_buzzer(9, 131)
    time.sleep(1)
    eb.play_passive_buzzer(9, 200)
    time.sleep(1)
    eb.turn_off_buzzer(9)
    time.sleep(1)