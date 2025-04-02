import os
import re

def get_mac_address(ip_address):
    output = os.popen("arp -a").read()
    
    pattern = rf"{ip_address}.*?([0-9A-Fa-f-]{{17}})"
    match = re.search(pattern, output)

    if match:
        return match.group(1)
    else:
        return "Endereço MAC não encontrado."

ip_alvo = "10.10.132.58"  # IP Flavio
mac_address = get_mac_address(ip_alvo)
print(f"Endereço MAC do IP (Flavio) {ip_alvo}: {mac_address} foi encontrado")

ip_alvo = "10.10.132.40"  # IP Diego
mac_address = get_mac_address(ip_alvo)
print(f"Endereço MAC do IP (Diego) {ip_alvo}: {mac_address}")
