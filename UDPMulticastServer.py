# Basic UDP Multicasting server built in python

import socket
import time
import datetime

def UDPSendMultiCast(group, port):
    # Create UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    try:
        
        while True:
            time.sleep(1)
            
            date = datetime.datetime.now()
            msg = date.strftime("%Y-%m-%d %H:%M:%S")
            
            print "Elapsed 1 Second, Sending: [%s]" %(msg)    
            
            s.sendto(msg, (group, port))
            
            
    except KeyboardInterrupt:
        
        print 'Interrupted Server, Shutting Down.'
        s.close()
        
    except Exception, e:
        print "Error: %s, Shutting down."%(e)
        
    
    
if __name__ == '__main__':
    UDPSendMultiCast('224.1.1.1', 5007)
    