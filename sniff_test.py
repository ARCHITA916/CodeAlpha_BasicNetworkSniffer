from scapy.all import sniff, IP,TCP, UDP
packets = sniff(count=1, timeout=15)
print("Packet captured!")
packets[0].show()