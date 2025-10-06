#Import ElectroBlocks library
from electroblocks import ElectroBlocks
import time # imports the time library


# Variable Declaration


# Initialise the program settings and configurations

eb = ElectroBlocks() # Create an instance of the ElectroBlocks class
eb.config_dht_temp(4, "DHT11")

for _ in range(1, 4):
    temp = eb.dht_temp_celcius()
    humidity = eb.dht_temp_humidity()
    print(f"Temp: {temp} & Humidity: {humidity}")
    time.sleep(1)


print("COMPLETE")