# CyberSentinel-AI

AI-Powered Cyber Threat Intelligence and Intrusion Detection Platform

---

## Overview

CyberSentinel-AI is an advanced cybersecurity platform that combines Machine Learning, Anomaly Detection, Explainable AI (XAI), Threat Intelligence, Interactive Security Dashboards, and Local Large Language Models (LLMs) to detect, classify, explain, and investigate cyber threats.

Built using the CICIDS2017 dataset, the platform provides both supervised and unsupervised threat detection capabilities alongside real-world threat intelligence integration and AI-powered cybersecurity assistance.

---

## Project Highlights

* 99.93% Multi-Class Intrusion Detection Accuracy
* Isolation Forest Anomaly Detection
* SHAP Explainable AI Integration
* AbuseIPDB Threat Intelligence Lookup
* React Security Operations Dashboard
* FastAPI Backend APIs
* Local Llama 3 Security Copilot
* Ollama Integration
* Versioned Development Lifecycle (v0.1 → v1.1)

---

## Features

### Multi-Class Intrusion Detection System (IDS)

Detects and classifies:

* BENIGN
* DDoS
* DoS
* PortScan
* BruteForce
* Bot
* WebAttack

**Model:** XGBoost

**Accuracy:** 99.93%

---

### Anomaly Detection Engine

Identifies suspicious network behavior that deviates from normal traffic patterns.

**Model:** Isolation Forest

**Accuracy:** 67.9%

**Attack Recall:** 78%

---

### Explainable AI (SHAP)

The platform uses SHAP (SHapley Additive exPlanations) to understand and explain model predictions.

Capabilities:

* Feature Importance Analysis
* Model Interpretability
* Threat Attribution
* Transparent Decision Making

---

### Threat Intelligence Integration

Integrated with AbuseIPDB for real-world IP reputation analysis.

Capabilities:

* IP Reputation Lookup
* Abuse Confidence Score
* Country Information
* Report Statistics
* Threat Level Assessment

Example Response:

```json
{
  "ip": "8.8.8.8",
  "risk_score": 0,
  "country": "US",
  "reports": 117,
  "threat_level": "LOW"
}
```

---

### AI Security Copilot

Powered by Llama 3 running locally through Ollama.

Capabilities:

* Threat Explanation
* Security Recommendations
* Vulnerability Education
* Incident Investigation Support
* Cybersecurity Question Answering

Example Questions:

* What is ransomware?
* Explain SQL Injection.
* How can I prevent brute force attacks?
* Explain Port Scanning.
* What is a zero-day vulnerability?

Example Response:

```text
User:
What is ransomware?

Copilot:
Ransomware is a type of malicious software that encrypts a victim's files and demands payment for restoration access.
```

---

### Security Operations Dashboard

Built using React and TailwindCSS.

Features:

* Real-Time Threat Analysis
* Threat History Tracking
* Threat Intelligence Lookup
* Risk Visualization
* AI Security Copilot
* Interactive Dashboard Interface

---

### REST APIs

#### Health Check

```http
GET /health
```

#### Threat Prediction

```http
POST /predict
```

#### Threat Intelligence Lookup

```http
GET /threat-intel/{ip}
```

#### AI Security Copilot

```http
POST /copilot
```

Request:

```json
{
  "question": "What is ransomware?"
}
```

---

## Project Structure

```text
CyberSentinel-AI
│
├── data
│   ├── raw
│   └── processed
│
├── docs
│
├── frontend
│
├── models
│
├── notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_binary_ddos_detection.ipynb
│   ├── 03_feature_importance.ipynb
│   ├── 04_multiclass_attack_detection.ipynb
│   ├── 05_anomaly_detection.ipynb
│   ├── 06_autoencoder_anomaly_detection.ipynb
│   └── 07_model_explainability.ipynb
│
├── src
│   ├── api
│   │   ├── main.py
│   │   ├── threat_intel.py
│   │   └── copilot.py
│   │
│   ├── models
│   ├── features
│   └── utils
│
├── tests
│
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Machine Learning

* Python
* Scikit-Learn
* XGBoost
* Isolation Forest
* SHAP

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* React
* TailwindCSS
* Axios
* Vite

### Threat Intelligence

* AbuseIPDB API

### Local AI

* Ollama
* Llama 3

### Visualization

* Matplotlib
* SHAP

### Development Tools

* Git
* GitHub
* VS Code

---

## Results

### Multi-Class Attack Classification

| Metric   | Value      |
| -------- | ---------- |
| Accuracy | 99.93%     |
| Classes  | 7          |
| Dataset  | CICIDS2017 |

### Anomaly Detection

| Metric        | Value |
| ------------- | ----- |
| Accuracy      | 67.9% |
| Attack Recall | 78%   |

---

## Version History

### v0.1

* Binary DDoS Detection
* FastAPI Setup

### v0.2

* Multi-Class Attack Classification
* Feature Importance Analysis

### v0.3

* Isolation Forest Anomaly Detection

### v0.4

* Production Prediction API
* Model Integration

### v0.5

* React Security Dashboard

### v0.6

* Threat History Dashboard
* System Status Monitoring

### v0.7

* Explainable AI using SHAP

### v0.8

* Threat Intelligence Integration
* AbuseIPDB Lookup
* Threat Level Assessment

### v0.9

* Enhanced Security Operations Dashboard
* Live Threat Intelligence Display
* Improved User Experience

### v1.0

* Rule-Based AI Security Copilot
* Natural Language Threat Explanations
* Interactive Security Assistant

### v1.1

* Local LLM Integration using Ollama
* Llama 3 Powered Security Copilot
* Dynamic Cybersecurity Question Answering
* AI Security Assistant

---

## Roadmap

### v1.2

* Incident Report Generator
* Threat Severity Assessment
* Automated Mitigation Recommendations
* PDF Report Export

### Future Enhancements

* RAG-Based Cybersecurity Knowledge Base
* SOC Analyst Assistant
* Malware Analysis Agent
* Threat Hunting Module
* SIEM Integration
* Real-Time Packet Monitoring
* Cloud Deployment

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shivaamsingh/CyberSentinel-AI.git

cd CyberSentinel-AI
```

### Create Virtual Environment

```bash
python -m venv venv

venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama:

https://ollama.com

Pull Llama 3:

```bash
ollama pull llama3
```

### Start Backend

```bash
python -m uvicorn src.api.main:app --reload
```

### Start Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Author

**Shivam Singh**

B.Tech CSE (AI/ML)

Cybersecurity • Artificial Intelligence • Machine Learning

GitHub: https://github.com/shivaamsingh
