import socket
import psutil

def get_ip_and_subnet():
    interfaces = psutil.net_if_addrs()
    for interface, addresses in interfaces.items():
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print(f"Interface: {interface}")
                print(f"Endereço IP: {addr.address}")
                print(f"Máscara de Sub-rede: {addr.netmask}")
                print("-" * 30)

get_ip_and_subnet()
