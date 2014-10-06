import socket
import sys

PORT = 9999
HOST = sys.argv[1]
#data = " ".join(sys.argv[1:])
max_packets = int(sys.argv[2])
# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
for i in range(1,max_packets+1):
    sock.sendto(str(i), (HOST, PORT))
    print "Sent:     {}".format(str(i))
    received = sock.recv(1024)
    print "Received: {}".format(received)
