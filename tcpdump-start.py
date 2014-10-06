import socket
import subprocess
import sys


def activate(host , time = 60):
    print "starting tcpdump for ", host, "for ", time," seconds"
    if host == 'pgw':
        p1 = subprocess.Popen(["timeout",time,"sudo","tcpdump","-i","eth5","-w", "pgw-in-eth5-192.168.2.X.pcap"])
        p2 = subprocess.Popen(["timeout",time,"sudo","tcpdump","-i","eth3","-w", "pgw-in-eth3-192.168.1.X.pcap"])
        p1.wait()
        p2.wait()
        print "Files written"

    elif host == 'epc':
        p1 = subprocess.Popen(["timeout",time,"sudo","tcpdump","-i","eth3","-w", "epc-in-eth3-192.168.1.X.pcap"])
        p1.wait()
        print "Files written"
    
    elif host == 'sgw':
        p1 = subprocess.Popen(["timeout",time,"sudo","tcpdump","-i","eth5","-w", "sgw-in-eth5-192.168.4.X.pcap"])
        p2 = subprocess.Popen(["timeout",time,"sudo","tcpdump","-i","eth3","-w", "sgw-out-eth3-192.168.2.X.pcap"])
        p1.wait()
        p2.wait()
        pass
        print "Files written"
    else:
        print "Error in Host name"

def main():
    host = socket.gethostname().split('.')[0]
    activate(host, sys.argv[1])

   
if __name__ == "__main__":
    main()
