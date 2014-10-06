import socket
import subprocess
import sys


def activate(host , time = 60):
    print "starting tcpdump for ", host, "for ", time," seconds"
    if host == 'pgw':
        p1 = subprocess.call(["timeout",time,"sudo","tcpdump","-i","eth5","-w", "pgw-in-eth5-192.168.2.X.pcap"])
        p1 = subprocess.call(["timeout",time,"sudo","tcpdump","-i","eth3","-w", "pgw-in-eth3-192.168.1.X.pcap"])
        p1.wait()
        p2.wait()
        print "Files written"

        print gw
    elif host == 'epc':
        pass
        print "Files written"
    elif host == 'sgw':
        pass
        print "Files written"
    else:
        print "Error in Host name"

def main():
    host = socket.gethostname().split('.')[0]
    activate(host, sys.argv[1])

   
if __name__ == "__main__":
    main()
