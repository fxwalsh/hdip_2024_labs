import BlynkLib
from time import sleep
from sense_hat import SenseHat

BLYNK_AUTH = "YOUR BLINK TOKEN"
# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)
#initialise SenseHAT
sense = SenseHat()
sense.clear()


# Register handler for virtual pin V1 write event
@blynk.on("V0")
def handle_v0_write(value):
    button_value = value[0]
    print(f'Current button value: {button_value}')
    if button_value=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()

while True:
    blynk.run()  # Process Blynk events
    #blynk.virtual_write(1, sense.temperature)
    sleep(1)
