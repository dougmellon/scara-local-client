import socket
import serial
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8080
board = serial.Serial(port='/dev/tty.usbserial-A6008eiv', baudrate=115200, timeout=.1)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("Connection established on port 8080")
def write_read(x):
    board.write(x)
data2 = board.readline() return data2
while True:
data, addr = serverSock.recvfrom(1024) value = write_read(data)
print(value)
