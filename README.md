# CyberSentinel-AI

AI-Powered Cyber Threat Intelligence and Intrusion Detection Platform

## Overview

CyberSentinel-AI is an advanced cybersecurity platform that combines Machine Learning, Anomaly Detection, Threat Intelligence, and AI-powered analysis to detect, classify, and investigate cyber threats.

The project is built using the CICIDS2017 dataset and currently supports both supervised and unsupervised threat detection techniques.

---

## Current Capabilities

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

**Attack Recall:** 78%

**Accuracy:** 67.9%

---

### FastAPI Backend

Provides a foundation for serving machine learning models through REST APIs.

---

## Project Structure

```text
CyberSentinel-AI
│
├── data
├── docs
├── models
├── notebooks
├── src
│   └── api
├── frontend
└── tests
```

---

## Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* XGBoost
* TensorFlow

### Backend

* FastAPI
* Uvicorn

### Frontend (Planned)

* React
* TailwindCSS

### Databases (Planned)

* PostgreSQL
* ChromaDB
* Neo4j

### AI & Threat Intelligence (Planned)

* Transformers
* RAG
* LLM Agents

---

## Results

### Multi-Class Classification

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

## Roadmap

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

* Explainable AI (SHAP)

### v0.7

* Threat Intelligence Retrieval System

### v1.0

* AI Security Copilot
* Incident Report Generation
* RAG-Based Cyber Knowledge Base

---

## Author

Shivam Singh

B.Tech CSE (AI/ML)

Cybersecurity & Artificial Intelligence Enthusiast
