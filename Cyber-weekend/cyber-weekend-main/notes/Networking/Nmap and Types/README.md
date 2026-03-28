# Nmap (Network Mapper)

## Definition
Nmap (Network Mapper) is an open-source network scanning and security auditing tool used to discover hosts, identify open ports, detect services, and determine operating systems on a network.

## Purpose
- Network discovery
- Port scanning
- Service and version detection
- Security auditing

## Key Features
- Fast and powerful scanning
- Supports multiple scan techniques
- OS and service detection
- Scriptable using NSE (Nmap Scripting Engine)

## Example Commands
- `nmap 192.168.1.1` → Scan a single host  
- `nmap -sn 192.168.1.0/24` → Discover live hosts  
- `nmap -A 192.168.1.1` → Aggressive scan  

## Note
> Nmap is widely used by network administrators and ethical hackers to analyze network security. Always use it with proper authorization.

# Types of Nmap Scans

Nmap provides different scan techniques to discover hosts, ports, and services.

## 1. TCP Connect Scan (-sT)
- Completes full TCP handshake
- Reliable but easily detected

## 2. SYN Scan (-sS)  [Stealth Scan]
- Half-open scan (does not complete handshake)
- Faster and less detectable

## 3. UDP Scan (-sU)
- Scans UDP ports
- Slower and less reliable than TCP scans

## 4. Ping Scan (-sn)
- Checks if hosts are alive
- Does not scan ports

## 5. FIN Scan (-sF)
- Sends FIN packets
- Used to bypass some firewalls

## 6. NULL Scan (-sN)
- Sends packets with no flags
- Useful for stealth scanning

## 7. Xmas Scan (-sX)
- Sends packets with FIN, PSH, URG flags
- Used to detect open ports stealthily

## 8. ACK Scan (-sA)
- Used to map firewall rules
- Determines if ports are filtered or unfiltered

## 9. Window Scan (-sW)
- Similar to ACK scan
- Uses TCP window size to detect open ports

## 10. Idle Scan (-sI)
- Very stealthy scan using a zombie host
- Hides attacker identity

---

## Summary
- TCP Connect → reliable but detectable  
- SYN Scan → fast and stealthy  
- UDP Scan → for UDP services  
- FIN/NULL/Xmas → stealth techniques  
- ACK/Window → firewall analysis  
- Idle → highly anonymous scan  
