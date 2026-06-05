def extract_features(flow):

    return [
        flow["duration"],
        flow["pps"],
        flow["bps"],
        flow["avg_packet_size"]
    ]