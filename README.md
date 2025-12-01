# 🛡️ Python Network Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Network](https://img.shields.io/badge/Network-Socket-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-success?style=for-the-badge)

A multi-threaded, command-line network scanner built with Python. This tool is designed to scan open ports on a target server using raw sockets.

> **Note:** The script is currently configured to scan `scanme.nmap.org`, a service provided by the Nmap Security Scanner project specifically for authorized scanning and testing.

---

## 📖 Project Overview

This script demonstrates the fundamentals of **Network Programming** and **Ethical Hacking** using Python's standard `socket` library. It performs a TCP handshake scan on the first 100 ports of the target to determine if services are running.

[Image of TCP handshake diagram]

### Key Features

- **Target:** Pre-configured to scan `scanme.nmap.org` (Safe testing environment).
- **Port Range:** Scans commonly used system ports (1-100).
- **Safety Mechanisms:** Includes a 1-second timeout per socket to prevent hanging on filtered ports.
- **Error Handling:** Gracefully manages `KeyboardInterrupt` and connection errors.

---

## 💻 Code Structure

The script uses `socket.connect_ex()` which returns an error indicator rather than raising an exception, allowing for cleaner flow control:

```python
# Returns 0 if the connection is successful (Port is OPEN)
result = s.connect_ex((target, port))
```
