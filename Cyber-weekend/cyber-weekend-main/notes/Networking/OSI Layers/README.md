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



## ⚠️ Attacks by Layer



###  1. Physical Layer (Layer 1)
Deals with hardware, cables, and signals.

**Attacks:**
- **Cable tapping** – Physically intercepting data from cables  
- **Device theft** – Stealing hardware to access data  
- **Signal jamming** – Blocking wireless communication  

---

###  2. Data Link Layer (Layer 2)
Handles MAC addresses and local network communication.

**Attacks:**
- **MAC spoofing** – Faking MAC address to impersonate devices  
- **ARP spoofing** – Redirecting traffic using fake ARP messages  
- **MAC flooding** – Overloading switch to capture traffic  

---

###  3. Network Layer (Layer 3)
Manages IP addresses and routing.

**Attacks:**
- **IP spoofing** – Using fake IP address  
- **Packet sniffing** – Capturing network data  
- **Routing attacks** – Manipulating traffic routes  
- **DDoS** – Flooding server to make it unavailable  

---

###  4. Transport Layer (Layer 4)
Ensures reliable data delivery (TCP/UDP).

**Attacks:**
- **SYN flood** – Sending many fake connection requests  
- **Session hijacking** – Taking over active connection  
- **Port scanning** – Finding open ports and vulnerabilities  

---

###  5. Session Layer (Layer 5)
Manages sessions between systems.

**Attacks:**
- **Session hijacking** – Stealing session ID  
- **Replay attack** – Resending captured data  

---

###  6. Presentation Layer (Layer 6)
Handles encryption and data formatting.

**Attacks:**
- **SSL/TLS attacks** – Exploiting encryption weaknesses  
- **Encryption breaking** – Cracking encrypted data  
- **Man-in-the-Middle (MITM)** – Intercepting communication  

---

###  7. Application Layer (Layer 7)
User-level applications like browsers and messaging apps.

**Attacks:**
- **Phishing** – Fake websites/emails to steal credentials  
- **Malware injection** – Installing malicious software  
- **SQL injection** – Attacking databases  
- **Cross-Site Scripting (XSS)** – Injecting scripts into websites  
- **Fake apps/websites** – Imitating real platforms  

---

## 📝 Notes

- Lower layers → Hardware & network-based attacks  
- Upper layers → Software & user-based attacks  




