import json

with open(
    r"C:\Projects\CyberSentinel-AI\frontend\src\samples.json"
) as f:
    data = json.load(f)

print(len(data["PortScan"]))

print({
    "features": data["PortScan"]
})