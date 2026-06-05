def detect(flow):

    if (
        flow["pps"] > 500
        and flow["bytes"] < 100000
    ):
        return "PortScan"

    if (
        flow["pps"] > 1000
        and flow["bytes"] > 5000000
    ):
        return "Possible DDoS"

    return "BENIGN"