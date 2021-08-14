
#Converting an IPv4 address to different formats
import socket
from binascii import hexlify
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print "IP Address: %s => Packed: %s, Unpacked: %s"\
   %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)
    
if __name__ == '__main__':
    convert_ip4_address()

#Finding a service name, given the port and protocol
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 21, 22, 23, 445, 110]:
        print "Port: %s => service name: %s" %(port, socket.
getservbyport(port, protocolname))
    print "Port: %s => service name: %s" %(53, socket.
getservbyport(53, 'udp'))
    
if __name__ == '__main__':
    find_service_name()