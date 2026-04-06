# Mini Nmap - Python Network Scanner

**Mini Nmap** is a Python-based network scanning tool inspired by the popular Nmap utility.
It is designed for **learning, experimentation, and red-team practice**, allowing users to scan hosts, detect open ports, perform basic OS fingerprinting, and run service-specific plugins.

This project demonstrates how real-world scanners work internally, including:

* TCP connect scanning
* Stealth SYN scanning
* Asynchronous scanning with `asyncio`
* Plugin-based service detection

---

## Features

* **TCP Connect Scan**
  Performs full TCP handshake to determine open/closed ports

* **Stealth SYN Scan**
  Fast, half-open scanning for stealthy enumeration

* **OS Fingerprinting**
  Basic OS detection using TCP/IP characteristics

* **Plugin System**

  * HTTP Title extraction
  * SSH banner/version detection

* **Async Scanning**
  Uses Python `asyncio` for high-speed concurrent scans

* **Extensible Architecture**
  Easily add new scanners or plugins

---

## Project Structure

| Module                   | Role                   |
| ------------------------ | ---------------------- |
| `core/engine.py`         | Orchestrates all scans |
| `scanner/tcp_connect.py` | Full TCP connect scan  |
| `scanner/syn_scan.py`    | Stealth SYN scan       |
| `core/fingerprint.py`    | OS detection           |
| `plugins/http_title.py`  | HTTP title plugin      |
| `plugins/ssh_version.py` | SSH banner plugin      |
| `utils/resolver.py`      | DNS resolution         |
| `main.py`                | CLI entry point        |

---

## ⚙️ Installation

```bash
git clone https://github.com/mr-dynamis/National-Ethio-Cyber-Talent-weekend-program-.git
cd Cyber-weekend/cyber-weekend-main/tasks/mini_nmap
```

(Optional virtual environment)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

##  How It Works

Mini Nmap uses **asynchronous programming (`asyncio`)** to scan multiple ports simultaneously.

Instead of scanning ports one-by-one (slow), it:

* Launches many scan tasks at once
* Waits for responses efficiently
* Reduces scan time significantly

---

## Plugins

### HTTP Title Plugin

* Sends HTTP request
* Extracts `<title>` from HTML
* Helps identify web applications

### SSH Version Plugin

* Connects to port 22
* Reads SSH banner
* Detects version (e.g., OpenSSH)

---

## Usage

Basic scan:

```bash
python main.py scanme.nmap.org -p 20-100
```

Verbose scan (recommended):

```bash
python main.py scanme.nmap.org -p 20-100 -v
```

### Arguments

| Flag | Description               |
| ---- | ------------------------- |
| `-p` | Port range (e.g., 20-100) |
| `-v` | Verbose output            |

---

## 🌐 Example Scan

### Command

```bash
python main.py scanme.nmap.org -p 20-100 -v
```

### Example Output

```text
[+] Target: scanme.nmap.org (45.33.32.156)

PORT     STATE    SERVICE
22/tcp   OPEN     SSH
80/tcp   OPEN     HTTP
25/tcp   CLOSED   SMTP
53/tcp   FILTERED DNS

[+] OS Detection:
Likely Linux (TTL=64)

[+] Service Detection:

[HTTP] Port 80:
Title: Example Domain

[SSH] Port 22:
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13

[+] Scan completed successfully
```

---

## Async Advantage

| Method | Behavior               |
| ------ | ---------------------- |
| Sync   | One port at a time     |
| Async  | Multiple ports at once |

 Result: **Much faster scanning**

---

---

## Disclaimer

This tool is intended for:

*  Learning
*  Ethical hacking practice
*  Authorized security testing

> Do NOT scan systems without permission.

---

Open-source project for educational purposes.

---

##  Author

Developed by **mr-dynamis**
 

---

##  Final Note

Mini Nmap is not meant to replace professional tools but to help you understand:

> “How network scanners actually work under the hood.”

---

