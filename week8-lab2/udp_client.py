import socket
from time import sleep
from env_data import get_environmental_data

#UDP Client configuration parameters
serverAddressPort = ("172.236.30.12", 41234)
deviceID = "device1"
interval = 5

# Create a UDP socket on device
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    #construct message to send to server
    msgFromClient = get_environmental_data(deviceID)
    bytesToSend = str(msgFromClient).encode()
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)      
    #Log to console
    print(f"Sent to server: {msgFromClient}")
    #Sleep for 5 seconds before transmitting again. 
    sleep(interval)