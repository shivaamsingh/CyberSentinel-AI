def extract_features(flow):

    return {
        "duration": flow["duration"],
        "packets": flow["packets"],
        "bytes": flow["bytes"],
        "pps": flow["pps"],
        "bps": flow["bps"],
        "avg_packet_size": flow["avg_packet_size"]
    }