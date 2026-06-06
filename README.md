# CyberSentinel-AI

AI-Powered Cyber Threat Intelligence, Intrusion Detection, SOC Investigation, and Security Operations Platform

---

## Overview

CyberSentinel-AI is a full-stack cybersecurity platform that combines Machine Learning, Explainable AI (XAI), Threat Intelligence, Retrieval-Augmented Generation (RAG), MITRE ATT&CK Mapping, Live Network Monitoring, and Large Language Models (LLMs) to detect, explain, investigate, and respond to cyber threats.

Built using the CICIDS2017 dataset, CyberSentinel-AI provides both supervised and unsupervised threat detection alongside AI-powered SOC analyst workflows and real-time traffic monitoring.

---

## Key Highlights

* 99.93% Multi-Class Intrusion Detection Accuracy
* XGBoost Attack Detection Engine
* Isolation Forest Anomaly Detection
* SHAP Explainable AI
* AbuseIPDB Threat Intelligence Integration
* Local Llama 3 Security Copilot
* AI Incident Report Generation
* Cybersecurity RAG Knowledge Base
* MITRE ATT&CK Mapping
* SOC Analyst Assistant
* Live Packet Monitoring
* Live ML-Based Anomaly Detection
* Real-Time SOC Alert Feed
* Dockerized AI Stack
* Ollama + Llama 3 Integration
* FastAPI + React Architecture

---

## Architecture

Frontend (React + TailwindCSS)

↓

FastAPI Backend

↓

Machine Learning Layer

* XGBoost IDS
* Isolation Forest

↓

AI Layer

* Ollama
* Llama 3
* LangChain
* ChromaDB

↓

Threat Intelligence Layer

* AbuseIPDB

↓

Live Monitoring Layer

* Scapy Packet Capture
* Flow Statistics Engine
* Real-Time Detection

---

## Core Features

### Intrusion Detection System (IDS)

Detects:

* BENIGN
* PortScan
* BruteForce
* DDoS
* DoS
* Bot
* WebAttack

Model:

* XGBoost

Performance:

* 99.93% Accuracy

---

### Anomaly Detection

Model:

* Isolation Forest

Capabilities:

* Unknown Threat Detection
* Outlier Detection
* Suspicious Traffic Analysis
* Live Anomaly Monitoring

---

### Explainable AI

Powered by:

* SHAP

Capabilities:

* Feature Importance Analysis
* Prediction Explainability
* Threat Attribution
* Model Transparency

---

### Threat Intelligence

Powered by:

* AbuseIPDB

Capabilities:

* IP Reputation Lookup
* Threat Scoring
* Country Information
* Report Statistics
* Threat Classification

Endpoint:

GET /threat-intel/{ip}

---

### AI Security Copilot

Powered by:

* Ollama
* Llama 3

Capabilities:

* Cybersecurity Q&A
* Security Recommendations
* Attack Explanations
* Security Awareness Training

Endpoint:

POST /copilot

---

### AI Incident Report Generator

Capabilities:

* Executive Summary
* Threat Assessment
* Potential Impact Analysis
* Recommended Actions
* SOC-Style Reporting

Endpoint:

POST /generate-report

---

### Cybersecurity RAG System

Built Using:

* LangChain
* ChromaDB
* HuggingFace Embeddings

Knowledge Base Topics:

* SQL Injection
* DDoS
* Port Scanning
* Brute Force
* Web Attacks

Endpoint:

POST /rag-chat

---

### AI Threat Investigation Engine

Capabilities:

* MITRE ATT&CK Mapping
* Attacker Goal Analysis
* Impact Assessment
* Security Recommendations
* Executive Investigation Reports

Endpoint:

POST /investigate

---

### SOC Analyst Assistant

Capabilities:

* AI Threat Analysis
* MITRE ATT&CK Correlation
* RAG-Augmented Context
* Security Recommendations
* Incident Response Guidance

Endpoint:

POST /analyze-threat

---

### Live Packet Monitoring

Powered by:

* Scapy

Features:

* Real-Time Packet Capture
* Flow Tracking
* Traffic Statistics
* Live Detection Pipeline

---

### Live ML Detection

Powered by:

* Isolation Forest

Features:

* Real-Time Flow Analysis
* Live Anomaly Detection
* SOC Alert Generation
* Continuous Monitoring

---

### Live SOC Alert Feed

Capabilities:

* Real-Time Alerts
* PortScan Detection
* ML Anomaly Alerts
* Dashboard Visualization
* Alert History

---

## Security Operations Dashboard

Built Using:

* React
* TailwindCSS
* Axios
* Vite

Dashboard Features:

* Threat Detection
* Threat Intelligence Lookup
* Incident Reports
* Threat Investigation
* SHAP Explainability
* Security Copilot
* MITRE Mapping
* Live SOC Feed
* Live ML Alerts

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
| POST   | /investigate       | Threat Investigation       |
| POST   | /analyze-threat    | SOC Analyst Assistant      |
| GET    | /alerts            | Alert Feed                 |

---

## Docker Deployment

### Start Entire Platform

```bash
docker compose up --build
```

### Services

* FastAPI Backend
* Ollama
* Llama 3
* RAG Knowledge Base

### Verify

```bash
http://localhost:8000/docs
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

### AI

* Ollama
* Llama 3
* LangChain
* ChromaDB
* HuggingFace Embeddings

### Threat Intelligence

* AbuseIPDB

### Monitoring

* Scapy
* Custom Flow Engine

### DevOps

* Docker
* Docker Compose
* Git
* GitHub

---

## Version History

### v1.8

* Live Traffic Monitoring
* Flow Statistics Engine

### v1.9

* Live ML Detection
* SOC Alert Feed

### v2.0

* Dockerized Backend
* Ollama Integration
* Containerized AI Stack

### v2.1

* Docker Compose Deployment
* Full Llama 3 Container Integration
* Production-Ready Architecture

---

## Author

Shivam Singh

B.Tech CSE (AI/ML)

Artificial Intelligence • Machine Learning • Cybersecurity

GitHub:
https://github.com/shivaamsingh
