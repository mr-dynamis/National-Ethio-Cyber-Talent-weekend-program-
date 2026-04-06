from scapy.all import IP, TCP, sr1

def syn_scan(target, port, results):
    try:
        pkt = IP(dst=target) / TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)

        if resp and resp.haslayer(TCP):
            if resp[TCP].flags == 0x12:  # SYN-ACK
                results.append((port, "OPEN", "SYN"))
            elif resp[TCP].flags == 0x14:
                pass  # CLOSED
    except:
        pass
