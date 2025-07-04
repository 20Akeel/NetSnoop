# 🛡️ NetSnoop
> A lightweight real-time Network Intrusion Detection System (NIDS) built with Python and Streamlit.

NetSnoop passively monitors your local network traffic and detects suspicious activity such as brute-force login attempts, unauthorized port scans, and access to critical ports (22, 23, 3389). It’s built to be fast, educational, and beginner-friendly.

---

## 🚀 Features

- 🔍 Real-time packet sniffing using Scapy
- 🧠 Simple threat detection logic (port abuse, IP repetition)
- 📊 Interactive dashboard with Streamlit
- 📝 Logs suspicious events to a CSV file
- 📨 Optional: Email alerts for flagged threats
- 💡 Easy to extend with more detection rules

---

## ⚙️ Tech Stack

| Tool/Library  | Purpose                      |
|---------------|------------------------------|
| Python        | Core logic                   |
| Scapy         | Packet sniffing              |
| Streamlit     | Interactive web dashboard    |
| Pandas        | Log analysis and charts      |
| CSV           | Logging traffic & status     |

---

## 📸 Screenshot

> *[Insert dashboard screenshot or GIF here]*  
(*To add yours: Save a screenshot as `dashboard.png` and commit it to the repo.*)

---

## 🧑‍💻 How to Run

### 🔧 Setup
```bash
git clone https://github.com/20Akeel/NetSnoop.git
cd NetSnoop
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 📡 Start Sniffer
```bash
sudo python sniffer.py
```

### 📊 Launch Dashboard
```bash
streamlit run dashboard.py
```

---

## ✅ Detection Logic

- Ports monitored: `22 (SSH)`, `23 (Telnet)`, `3389 (RDP)`
- IPs flagged if repeated access attempts exceed threshold
- All packets logged in `logs/netsnoop_log.csv`

---

## 🤝 Contributing

Want to improve NetSnoop?
- Fork the repo
- Add your feature or detection logic
- Submit a pull request

---

## 📄 License

MIT License – see `LICENSE` file for details.

---

## 🙏 Acknowledgements

- Inspired by [TryHackMe](https://tryhackme.com/), [Wireshark](https://www.wireshark.org/), and beginner-friendly cybersecurity labs.
