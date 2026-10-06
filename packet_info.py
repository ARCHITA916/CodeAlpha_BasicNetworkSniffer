from scapy.all import sniff, IP, TCP, UDP,Raw
from datetime import datetime

def analyze_packet(packet):
    if IP in packet:
        timestamp = datetime.now().strftime("%H:%M:%S")
        source = packet[IP].src
        destination = packet[IP].dst
        protocol = packet[IP].proto

        if protocol ==6:
            protocol = "TCP"
        elif protocol ==17:
            protocol = "UDP"
        elif protocol ==1:
            protocol = "ICMP"
        else:
            protocol = str(protocol) 

        if TCP in packet:
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport
        elif UDP in packet:
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport
        else:
            source_port = "-"
            destination_port = "-"
        if Raw in packet:
            payload_size = len(packet[Raw].load)
        else:
            payload_size = 0

        print("_"*50)
        print(f"Time: {timestamp}")
        print(f"{source}->{destination}")
        print(f"Protocol: {protocol}")
        print(f"Source Port: {source_port}")
        print(f"Destination Port: {destination_port}")
        print(f"Payload Size: {payload_size} bytes")

sniff(count=20,prn=analyze_packet,store=False)
