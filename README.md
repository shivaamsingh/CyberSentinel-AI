# CyberSentinel-AI

AI-Powered Cyber Threat Intelligence, Intrusion Detection, and SOC Investigation Platform

---

## Overview

CyberSentinel-AI is an advanced cybersecurity platform that combines Machine Learning, Explainable AI (XAI), Threat Intelligence, Retrieval-Augmented Generation (RAG), MITRE ATT&CK Mapping, and Local Large Language Models (LLMs) to detect, explain, investigate, and report cyber threats.

Built using the CICIDS2017 dataset, the platform provides both supervised and unsupervised threat detection capabilities alongside AI-powered SOC analyst workflows.

---

## Project Highlights

* 99.93% Multi-Class Intrusion Detection Accuracy
* Isolation Forest Anomaly Detection
* SHAP Explainable AI
* AbuseIPDB Threat Intelligence Integration
* Local Llama 3 Security Copilot
* AI Incident Report Generator
* Cybersecurity RAG Knowledge Base
* MITRE ATT&CK Mapping
* AI Threat Investigation Engine
* React Security Operations Dashboard
* FastAPI Backend APIs

---

## Core Features

### Intrusion Detection System (IDS)

Detects:

* BENIGN
* DDoS
* DoS
* PortScan
* BruteForce
* Bot
* WebAttack

Model:

* XGBoost

Accuracy:

* 99.93%

---

### Anomaly Detection

Model:

* Isolation Forest

Capabilities:

* Unknown threat detection
* Outlier detection
* Suspicious traffic identification

---

### Explainable AI (SHAP)

Capabilities:

* Feature Importance Analysis
* Model Explainability
* Threat Attribution
* Transparent Predictions

---

### Threat Intelligence Integration

Powered by AbuseIPDB.

Capabilities:

* IP Reputation Lookup
* Risk Scoring
* Country Information
* Report Statistics
* Threat Level Classification

Endpoint:

GET /threat-intel/{ip}

---

### AI Security Copilot

Powered by:

* Ollama
* Llama 3

Capabilities:

* Cybersecurity Question Answering
* Attack Explanations
* Security Recommendations
* Vulnerability Education

Endpoint:

POST /copilot

---

### AI Incident Report Generator

Automatically creates SOC-style incident reports.

Capabilities:

* Executive Summary
* Threat Assessment
* Potential Impact Analysis
* Recommended Actions
* Professional Incident Documentation

Endpoint:

POST /generate-report

---

### Cybersecurity RAG Knowledge Base

Retrieval-Augmented Generation system built using:

* ChromaDB
* HuggingFace Embeddings
* LangChain

Knowledge Base Topics:

* SQL Injection
* Port Scanning
* Brute Force
* DDoS

Capabilities:

* Context-Aware Cybersecurity Answers
* Knowledge Retrieval
* Threat Explanation

Endpoint:

POST /rag-chat

---

### AI Threat Investigation Engine

Combines:

* MITRE ATT&CK Mapping
* Llama 3 Analysis
* RAG Context

Capabilities:

* Executive Summary
* Likely Attacker Goal
* Impact Analysis
* MITRE ATT&CK Mapping
* Recommended Actions

Supported MITRE Techniques:

| Attack Type | Technique |
| ----------- | --------- |
| PortScan    | T1046     |
| BruteForce  | T1110     |
| DDoS        | T1498     |
| Bot         | T1071     |
| WebAttack   | T1190     |

Endpoint:

POST /investigate

---

### Security Operations Dashboard

Built using:

* React
* TailwindCSS
* Axios
* Vite

Dashboard Features:

* Threat Analysis
* Threat History
* Threat Intelligence Lookup
* Incident Reports
* Threat Investigation
* AI Security Copilot
* MITRE Mapping Visualization

---

## API Endpoints

| Method | Endpoint           | Description                |
| ------ | ------------------ | -------------------------- |
| GET    | /health            | Health Check               |
| POST   | /predict           | Threat Prediction          |
| GET    | /threat-intel/{ip} | Threat Intelligence        |
| POST   | /copilot           | AI Security Copilot        |
| POST   | /generate-report   | Incident Report Generation |
| POST   | /rag-chat          | Cybersecurity RAG Chat     |
| POST   | /investigate       | AI Threat Investigation    |

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

* AbuseIPDB

### AI

* Ollama
* Llama 3
* LangChain
* ChromaDB
* HuggingFace Embeddings

### Development

* Git
* GitHub
* VS Code

---

## Version History

### v1.0

* AI Security Copilot

### v1.1

* Local Llama 3 Integration

### v1.2

* AI Incident Report Generator

### v1.3

* Cybersecurity RAG Knowledge Base

### v1.4

* AI Threat Investigation Engine
* MITRE ATT&CK Mapping
* RAG-Powered Investigation
* SOC Analyst Workflow

---

## Roadmap

### v1.5

* SOC Analyst Assistant
* Unified Threat Analysis Pipeline
* Automated Threat Intelligence Correlation
* Combined Investigation + Report Generation

### Future

* Malware Analysis Agent
* Threat Hunting Module
* SIEM Integration
* Docker Deployment
* Real-Time Packet Monitoring
* Cloud Deployment

---

## Author

Shivam Singh

B.Tech CSE (AI/ML)

Cybersecurity • Artificial Intelligence • Machine Learning

GitHub:
https://github.com/shivaamsingh
