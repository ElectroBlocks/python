#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations

eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_thermistor("A0")

for _ in range(1, 4):
    celcius = eb.thermistor_celsius()
    fahrenheit = eb.thermistor_fahrenheit()
    print(f'Celcius: {celcius} Fahrenheit: {fahrenheit}')
    time.sleep(1)
