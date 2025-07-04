suspicious_ips = {}

def analyze_packet(packet):
    if packet.haslayer("IP") and packet.haslayer("TCP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        dport = packet["TCP"].dport

        status = "OK"
        if dport in [22, 23, 3389]:  # suspicious ports
            suspicious_ips[ip_src] = suspicious_ips.get(ip_src, 0) + 1
            if suspicious_ips[ip_src] > 10:
                status = "THREAT"

        log_to_csv(ip_src, ip_dst, dport, status)

def log_to_csv(src, dst, port, status):
    with open("logs/netsnoop_log.csv", "a") as f:
        f.write(f"{src},{dst},{port},{status}\n")
