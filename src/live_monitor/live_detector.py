def detect(flow):

    duration = flow["duration"]
    pps = flow["pps"]
    packets = flow["packets"]
    bytes_count = flow["bytes"]

    # Ignore very new flows
    if duration < 2:
        return "BENIGN"

    # Port Scan
    if (
        packets > 100
        and pps > 100
        and bytes_count < 100000
    ):
        return "PortScan"

    # DDoS
    if (
        packets > 1000
        and pps > 500
        and bytes_count > 5000000
    ):
        return "Possible DDoS"

    return "BENIGN"