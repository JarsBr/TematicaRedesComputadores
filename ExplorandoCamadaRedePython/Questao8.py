import psutil

def get_mac_addresses():
    mac_addresses = {}
    interfaces = psutil.net_if_addrs()
    
    for interface, addresses in interfaces.items():
        for addr in addresses:
            if addr.family == psutil.AF_LINK:  # Verifica se é um endereço MAC
                mac_addresses[interface] = addr.address
    
    return mac_addresses

macs = get_mac_addresses()
for interface, mac in macs.items():
    print(f"Interface: {interface}, MAC: {mac}")
