## 7 Layers of the OSI Model (Top → Bottom)
### 7. Application Layer
- Closest to the user
- Provides network services to applications
-      Examples: Web browsing, email
      Protocols: HTTP, FTP, SMTP
### 6. Presentation Layer
- Formats and translates data
- Handles encryption, compression
- Makes sure sender and receiver understand data
### 5. Session Layer
- Manages communication sessions
- Starts, maintains, and ends connections
### 4. Transport Layer
- Ensures reliable data delivery
- Breaks data into segments
- Handles error checking
Protocols: TCP (reliable), UDP (fast)
### 3. Network Layer
- Determines the best path for data
- Uses IP addressing
- Devices: Routers
### 2. Data Link Layer
- Transfers data between devices on the same network
- Uses MAC addresses
- Detects errors
### 1. Physical Layer
- Sends raw bits (0s and 1s)
- Deals with cables, signals, hardware

 1. Physical Layer (Layer 1)
   - Deals with cables, signals, hardware
> Attacks:
- Cable tapping (physically intercepting data)
- Device theft
- Signal jamming (blocking Wi-Fi signals)
2. Data Link Layer (Layer 2)
   - Works with MAC addresses and local network
> Attacks:
- MAC spoofing (fake MAC address)
- ARP spoofing (redirecting traffic)
- Switch attacks (like MAC flooding)
3. Network Layer (Layer 3)
   - Handles IP addresses and routing
> Attacks:
- IP spoofing (fake IP address)
- Packet sniffing
- Routing attacks
- DDoS (Distributed Denial of Service)
4. Transport Layer (Layer 4)
   - Ensures delivery (TCP/UDP)
> Attacks:
- SYN flood attack (overloading server)
- Session hijacking
- Port scanning
5. Session Layer (Layer 5)
   - Manages connections/sessions
> Attacks:
- Session hijacking (stealing login session)
- Replay attacks (resending captured data)
6. Presentation Layer (Layer 6)
   - Encryption and data formatting
> Attacks:
- SSL/TLS attacks
- Encryption breaking
- Man-in-the-middle (MITM)
7. Application Layer (Layer 7)
   - User-level apps like Telegram, browsers
> Attacks:
- Phishing attacks
- Malware injection
- SQL injection
- Cross-site scripting (XSS)
- Fake apps/websites


