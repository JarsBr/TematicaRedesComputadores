import psutil
import socket

def get_default_gateway():
    gateways = psutil.net_if_addrs()
    
    for interface, addresses in gateways.items():
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print(f"Gateway Padrão: {addr.address}")
                return

get_default_gateway()
