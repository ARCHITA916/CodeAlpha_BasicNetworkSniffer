from scapy.all import IP, ICMP
packet = IP(dst="192.168.1.1")/ICMP()
packet.show()