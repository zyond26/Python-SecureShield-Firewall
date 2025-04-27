# xây dựng chức năng phân tích gói tin 

from scapy.all import sniff

def packet_handler(packet):
    if packet[IP].src == "192.168.1.100":
        print(f"Blocked packet from {packet[IP].src}")
    else:
        print(f"Allowed packet: {packet.summary()}")

sniff(filter="ip", prn=packet_handler)