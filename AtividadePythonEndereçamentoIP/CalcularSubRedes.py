import ipaddress
from tabulate import tabulate

def dividir_rede(rede_str, num_subredes):
    rede = ipaddress.ip_network(rede_str, strict=False)
    subredes = list(rede.subnets(new_prefix=rede.prefixlen + (num_subredes - 1).bit_length()))
    return subredes[:num_subredes]

def info_subrede(subrede):
    hosts = list(subrede.hosts())
    return {
        'Rede': str(subrede.network_address),
        'Broadcast': str(subrede.broadcast_address),
        'Primeiro IP útil': str(hosts[0]) if hosts else 'N/A',
        'Último IP útil': str(hosts[-1]) if hosts else 'N/A',
        'Qtd Hosts': len(hosts)
    }

def ip_pertence(ip_str, subredes):
    ip = ipaddress.ip_address(ip_str)
    for i, subrede in enumerate(subredes):
        if ip in subrede:
            return i
    return None

def desenhar_subrede(subrede):
    hosts = list(subrede.hosts())
    linhas = []
    for i, ip in enumerate(hosts[:10]):
        linhas.append(f"| {i+1:2d} | {str(ip):15} |")
    return "\n".join(linhas)

def simular_roteamento(ip_origem, ip_destino, subredes):
    origem_idx = ip_pertence(ip_origem, subredes)
    destino_idx = ip_pertence(ip_destino, subredes)
    
    if origem_idx is None or destino_idx is None:
        return "Um dos IPs não pertence a nenhuma sub-rede."
    if origem_idx == destino_idx:
        return f"Pacote enviado diretamente dentro da sub-rede {origem_idx + 1}."
    else:
        return f"Pacote roteado da sub-rede {origem_idx + 1} para a sub-rede {destino_idx + 1} via gateway."

def main():
    subredes = []
    while True:
        print("\n===== MENU INTERATIVO =====")
        print("1. Gerar Sub-redes")
        print("2. Mostrar Informações das Sub-redes")
        print("3. Mostrar IPs das Sub-redes (até 10)")
        print("4. Verificar a qual Sub-rede um IP pertence")
        print("5. Simular Roteamento entre dois IPs")
        print("0. Sair")
        print("===== =====")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            rede_str = input("Digite a rede (ex: 192.168.0.0/24): ")
            num_subredes = int(input("Quantas sub-redes você quer gerar? "))
            subredes = dividir_rede(rede_str, num_subredes)
            print("Sub-redes geradas com sucesso.")

        elif opcao == "2":
            if not subredes:
                print("Você precisa gerar as sub-redes primeiro (opção 1).")
            else:
                print("\n===== Informações das Sub-redes =====")
                tabela = [info_subrede(sr) for sr in subredes]
                print(tabulate(tabela, headers="keys", tablefmt="grid"))

        elif opcao == "3":
            if not subredes:
                print("Você precisa gerar as sub-redes primeiro (opção 1).")
            else:
                print("\n===== IPs das Sub-redes (até 10 IPs úteis) =====")
                for i, sub in enumerate(subredes):
                    print(f"\nSub-rede {i+1}: {sub}")
                    print(desenhar_subrede(sub))

        elif opcao == "4":
            if not subredes:
                print("Você precisa gerar as sub-redes primeiro (opção 1).")
            else:
                ip_verificar = input("Digite um IP para verificar: ")
                idx = ip_pertence(ip_verificar, subredes)
                if idx is not None:
                    print(f"O IP {ip_verificar} pertence à sub-rede {idx + 1}: {subredes[idx]}")
                else:
                    print("O IP não pertence a nenhuma das sub-redes.")

        elif opcao == "5":
            if not subredes:
                print("Você precisa gerar as sub-redes primeiro (opção 1).")
            else:
                ip_origem = input("Digite o IP de origem: ")
                ip_destino = input("Digite o IP de destino: ")
                resultado = simular_roteamento(ip_origem, ip_destino, subredes)
                print(resultado)

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
