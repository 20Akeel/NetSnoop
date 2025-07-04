# NetSnoop: Lightweight Network Intrusion Detection System

## Overview
NetSnoop is a Python-based tool to sniff local network packets and flag suspicious activity such as brute-force or port scan attempts.

## Features
- Live packet capture using Scapy
- Threat detection based on port & frequency
- Real-time dashboard using Streamlit
- Logs saved to CSV

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
Start sniffer:
```bash
sudo python sniffer.py
```

Start dashboard:
```bash
streamlit run dashboard.py
```
