from collections import defaultdict
import time



flows = defaultdict(
    lambda: {
        "packets": 0,
        "bytes": 0,
        "start_time": time.time(),
        "last_seen": time.time(),
        "pps": 0,
        "bps": 0,
        "avg_pkt_size": 0,
        "duration": 0
    }
)

def update_flow(packet):

    if not packet.haslayer("IP"):
        return

    src = packet["IP"].src
    dst = packet["IP"].dst

    if packet.haslayer("TCP"):
        sport = packet["TCP"].sport
        dport = packet["TCP"].dport
    elif packet.haslayer("UDP"):
        sport = packet["UDP"].sport
        dport = packet["UDP"].dport
    else:
        sport = 0
        dport = 0

    key = (src, dst, sport, dport)

    flows[key]["packets"] += 1
    flows[key]["bytes"] += len(packet)
    flows[key]["avg_packet_size"] = (
    flows[key]["bytes"]
    / flows[key]["packets"]
    )
    flows[key]["last_seen"] = time.time()
    
    flows[key]["duration"] = (
        flows[key]["last_seen"]
        - flows[key]["start_time"]
    )

    duration = flows[key]["duration"]

    if duration <= 0.001:
        duration = 0.001

    flows[key]["pps"] = (
        flows[key]["packets"]
        / duration
)

    flows[key]["bps"] = (
        flows[key]["bytes"]
        / duration
)

    return flows[key]