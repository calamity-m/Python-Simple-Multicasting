# Basic UDP Multicasting server built in python

import socket
import struct

def UDPReceiveMultiCast(group, port):
    # Create UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    
    mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)

    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    try:
        
        while True:
            print s.recv(10240)
    
    except KeyboardInterrupt :
        print 'Client Interrupted, Closing Socket'
        s.close()
    
    
if __name__ == '__main__':
    UDPReceiveMultiCast('224.1.1.1', 5007)
    