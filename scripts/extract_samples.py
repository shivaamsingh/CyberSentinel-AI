import pandas as pd
import json

df = pd.read_csv("data/processed/multiclass_balanced.csv")

samples = {}

for attack in [
    "BENIGN",
    "PortScan",
    "DDoS",
    "BruteForce",
    "Bot",
    "WebAttack",
    "DoS"
]:
    row = df[df["AttackFamily"] == attack].iloc[0]

    features = (
        row.drop(
            ["Label", "AttackFamily", "Target"]
        )
        .astype(float)      # <-- important
        .tolist()
    )

    samples[attack] = features

with open("samples.json", "w") as f:
    json.dump(samples, f, indent=2)

print("samples.json created")