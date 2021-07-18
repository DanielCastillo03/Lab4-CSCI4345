import socket
import os

SEPARATOR = "<SEPARATOR>"
#bytes that will be sent
BUFFER_SIZE = 4096 

# the ip address of my virtual Linux Machine
host = "192.168.1.9"
# the port that will be used
port = 5001
# the name of file that will be sent to the linux VM
filename = "shared"
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

#message to show that the two machines have connected
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        s.sendall(bytes_read)
        
# close the socket
s.close()

