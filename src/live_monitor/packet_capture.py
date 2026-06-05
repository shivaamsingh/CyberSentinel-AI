from scapy.all import sniff
from flow_tracker import update_flow
from live_detector import detect
from ml_detector import predict

import requests


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

    # Rule-based Detection
    alert = detect(flow)

    if alert != "BENIGN":
        print(
            f"[ALERT] {alert}"
        )

    # ML Detection
    ml_result = predict(flow)

    print(
        f"ML:{ml_result}"
    )

    # Send anomalies to FastAPI
    if (
        ml_result == "ANOMALY"
        and flow["duration"] > 2
        and flow["pps"] > 2
        
        ):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/push-alert",
                json={
                    "alert": "ML_ANOMALY",
                    "pps": float(flow["pps"]),
                    "bps": float(flow["bps"])
                }
            )

            print(
                f"Alert sent: {response.status_code}"
            )

        except Exception as e:

            print(
                f"API Error: {e}"
            )


print("Listening...")

sniff(
    prn=process_packet,
    store=False
)