from scapy.all import IP, ICMP, sr1

def detect_os(target):
    try:
        pkt = IP(dst=target) / ICMP()
        resp = sr1(pkt, timeout=1, verbose=0)

        if resp:
            ttl = resp.ttl

            if ttl <= 64:
                return "Linux/Unix"
            elif ttl <= 128:
                return "Windows"
            else:
                return "Unknown"
    except:
        return "Unknown"
