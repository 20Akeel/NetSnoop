from scapy.all import sniff
from utils.threat_detection import analyze_packet

def main():
    print("[*] Starting packet sniffer...")
    sniff(filter="ip", prn=analyze_packet, store=0)

if __name__ == "__main__":
    main()
