from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

print("Listening... Press Ctrl+C to stop.")

sniff(
    prn=process_packet,
    store=False
)