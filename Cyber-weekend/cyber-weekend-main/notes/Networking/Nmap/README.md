---
# Nmap (Network Mapper)

Nmap is a powerful open-source tool used for **network discovery, security auditing, and penetration testing**. It helps identify live hosts, open ports, services, and operating systems on a network.

---

# Basic Nmap Commands

## 1. Basic Scan

```bash
nmap <target-ip>
```

Example:

```bash
nmap 192.168.1.1
```

 Scans top 1000 ports of the target

---

## 2. Scan Multiple Hosts

```bash
nmap 192.168.1.1 192.168.1.2
```

Or:

```bash
nmap 192.168.1.0/24
```

---

## 3. Ping Scan (Host Discovery Only)

```bash
nmap -sn 192.168.1.0/24
```

 Shows which devices are online (no port scan)

---

## 4. Port Specification

```bash
nmap -p 80 192.168.1.1
```

Scan multiple ports:

```bash
nmap -p 22,80,443 192.168.1.1
```

Scan all ports:

```bash
nmap -p- 192.168.1.1
```

---

##  5. Service Version Detection

```bash
nmap -sV 192.168.1.1
```

Detects service versions (Apache, SSH, etc.)

---

##  6. OS Detection

```bash
nmap -O 192.168.1.1
```

Identifies operating system

---

## 7. Aggressive Scan

```bash
nmap -A 192.168.1.1
```

 Combines OS detection, version detection, script scan, and traceroute

---

##  8. Fast Scan

```bash
nmap -F 192.168.1.1
```

 Scans fewer common ports quickly

---

##  9. Save Output Formats

```bash
nmap -oN scan.txt 192.168.1.1
```

 Normal output

```bash
nmap -oX scan.xml 192.168.1.1
```

 XML output

```bash
nmap -oG scan.grep 192.168.1.1
```

 Grepable output

```bash
nmap -oA scan_all 192.168.1.1
```

 Saves all formats at once

---

##  10. Stealth SYN Scan

```bash
nmap -sS 192.168.1.1
```

 Fast and less detectable scan

---

##  11. UDP Scan

```bash
nmap -sU 192.168.1.1
```

---

##  12. Script Scan (Vulnerability Check)

```bash
nmap --script vuln 192.168.1.1
```

---

# Nmap Flags

| Flag | Meaning                   |
| ---- | ------------------------- |
| -sn  | Ping scan                 |
| -sS  | SYN scan                  |
| -sV  | Service version detection |
| -O   | OS detection              |
| -A   | Aggressive scan           |
| -p   | Port selection            |
| -F   | Fast scan                 |
| -oN  | Normal output             |
| -oX  | XML output                |
| -oG  | Grep output               |
| -oA  | All formats               |

---
