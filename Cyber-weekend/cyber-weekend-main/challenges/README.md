# challenges
# Network Forensics Challenge (Wireshark CTF)

## Overview
This repository contains 5 beginner-to-intermediate network forensics challenges. Each challenge focuses on extracting hidden information from network traffic using tools like Wireshark, packet inspection, and decoding techniques.

## Tools Used
- Wireshark
- tcpdump (optional)
- CyberChef
- Base64 Decoder
- Hex / ASCII tools

# Challenge 1: Unencrypted Browser Traffic

### Hint
Sometimes secrets travel unencrypted. Inspect the messages your browser asks for.

### Objective
Find hidden data inside unencrypted HTTP traffic.

### Solution
1. Open the `.pcap` file in Wireshark  
2. Apply filter:
   ```
   http
3. Look at HTTP GET/POST requests  
4. Right-click packet → Follow → HTTP Stream  
5. Inspect response body for the flag  

### Key Idea
HTTP traffic is unencrypted and can expose sensitive data.

### Flag Format
FLAG{...}

# Challenge 2: Hidden Queries in System Requests

### Hint
Even small questions can carry hidden messages. Check what your system is asking the internet.

### Objective
Analyze DNS queries for hidden data.

### Solution
1. Apply filter:
   ```
   dns
2. Look at query names  
3. Identify unusual or encoded subdomains  
4. Decode using Base64 or Hex if needed  

### Key Idea
DNS queries can be used for data hiding (DNS tunneling).

### Flag Format


# Challenge 3: Split Across Packets

### Hint
The answer might be broken into pieces across multiple packets. Reassemble to see the whole picture.

### Objective
Reconstruct fragmented data from multiple packets.

### Solution
1. Apply filter:
   ```
   tcp
2. Right-click → Follow TCP Stream  
3. Check full reconstructed data  
4. Export stream if needed  
5. Reassemble hidden content  

### Key Idea
TCP splits data into segments; reassembly reveals hidden content.

### Flag Format
FLAG{...}

# Challenge 4: Encoded Payloads

### Hint
Some messages arrive encoded. The transport might reveal patterns in the body rather than headers.

### Objective
Decode hidden encoded payloads.

### Solution
1. Filter:
   ```
   tcp / http
2. Inspect packet payloads  
3. Look for encoding patterns such as:
- Base64
- Hex
- URL encoding  
4. Decode using CyberChef or terminal tools  

### Key Idea
Attackers often encode data to avoid detection.

### Flag Format
FLAG{...}


# Challenge 5: Secret Inside Ping (ICMP)

### Hint
Even simple pings can carry secrets inside them. Don’t just look at the summary—peek at the payload.

### Objective
Extract hidden data from ICMP packets.

### Solution
1. Apply filter:
   ```
   icmp

2. Open ICMP Echo Request/Reply packets  
3. Inspect packet data section  
4. Extract payload bytes  
5. Decode ASCII / Hex data  

### Key Idea
ICMP packets can carry hidden payloads inside echo requests.

### Flag Format
