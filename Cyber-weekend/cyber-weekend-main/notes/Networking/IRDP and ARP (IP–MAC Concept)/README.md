# 1. IRDP (ICMP Router Discovery Protocol)
> Definition:
- IRDP is a protocol that helps a host (computer) automatically discover the default router (gateway) in a network using ICMP messages.
Purpose:
- To find the router’s IP address without manual configuration

- Helps devices know where to send data outside their network
> How it Works:
 - Router Advertisement
    - Router broadcasts: “I am available as a gateway”
  - Router Solicitation
    - Host requests: “Is there any router available?”

> Layer:
- Network Layer (uses ICMP)

> Example:
- When you connect to Wi-Fi, your device finds the router automatically using IRDP.
   ## ICMP (Internet Control Message Protocol) Notes

**Layer:** OSI Layer 3 (Network Layer)

**Purpose:**  
- Reports errors in IP communication  
- Tests network connectivity  

**Functions:**  
1. Error reporting (e.g., host/network unreachable)  
2. Network diagnostics (e.g., ping, traceroute)  

**Common ICMP Types:**  
| Type | Function |
|------|---------|
| Echo Request / Echo Reply | Check if a host is reachable (`ping`) |
| Destination Unreachable | Host or network cannot be reached |
| Time Exceeded | TTL expired (used in `traceroute`) |
| Redirect | Suggests a better route to a host |

**Security:**  
- Can be exploited in attacks like **Ping Flood** or **Smurf attack**  
- Often filtered for security  

**Analogy:**  
> ICMP is like a network “messenger” that reports problems or confirms reachability—it does **not** carry normal user data.
# 2. ARP (Address Resolution Protocol)
> Definition:
- ARP is used to find the MAC address of a device when its IP address is known.
> Purpose:
- To map IP address → MAC address
Enables communication inside a local network (LAN)
> How it Works:
- Device sends ARP request:
  - “Who has IP 192.168.1.1?”
- Target replies:
  - “I have it, my MAC is XX:XX:XX:XX:XX”
> Layer:
- Link Layer (between Network & Data Link)
> Example:
- Before sending data, your computer must know the MAC address of the destination device.
