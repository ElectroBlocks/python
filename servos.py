from electroblocks import ElectroBlocks
import time
eb = ElectroBlocks()
eb.config_servo(6)

while True:
    # Move servo to 0 degrees
    eb.set_servo(6, 0)
    # Wait for 1 second
    time.sleep(1)
    # Move servo to 90 degrees
    eb.set_servo(6, 90)
    # Wait for 1 second
    time.sleep(1)
    # Move servo to 180 degrees
    eb.set_servo(6, 180)
    # Wait for 1 second
    time.sleep(1)