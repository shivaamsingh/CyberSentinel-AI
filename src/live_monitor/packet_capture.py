from scapy.all import sniff
from flow_tracker import update_flow
from live_detector import detect


def process_packet(packet):

    flow = update_flow(packet)

    if not flow:
        return

    print(
    f"PPS={flow['pps']:.2f} | "
    f"BPS={flow['bps']:.2f} | "
    f"Duration={flow['duration']:.2f}s | "
    f"AvgPkt={flow['avg_packet_size']:.2f}"
)

    alert = detect(flow)

    if alert != "BENIGN":
        print(f"[ALERT] {alert}")


print("Listening...")

sniff(
    prn=process_packet,
    store=False
)