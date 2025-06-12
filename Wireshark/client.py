import socket
import threading
import time
from cryptography.fernet import Fernet

# Gera ou define a chave de criptografia (deve ser igual à do servidor)
key = Fernet.generate_key()
fernet = Fernet(key)

# Função que cada cliente executa
def start_cliente(id_cliente):
    HOST = '127.0.0.1'  # IP do servidor
    PORT = 12345        # Porta do servidor

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print(f"[CLIENTE {id_cliente}] Conectado ao servidor")

        def receber():
            while True:
                try:
                    msg = client.recv(1024)
                    if msg:
                        decrypted_msg = fernet.decrypt(msg).decode()
                        print(f"[CLIENTE {id_cliente}] Servidor: {decrypted_msg}")
                except Exception as e:
                    print(f"[CLIENTE {id_cliente}] Erro ao receber: {e}")
                    break

        threading.Thread(target=receber, daemon=True).start()

        # Envia mensagens automaticamente
        for i in range(5):
            mensagem = f"Olá do cliente {id_cliente} - msg {i}"
            encrypted = fernet.encrypt(mensagem.encode())
            client.send(encrypted)
            time.sleep(1)

        client.close()
        print(f"[CLIENTE {id_cliente}] Desconectado")

    except Exception as e:
        print(f"[CLIENTE {id_cliente}] Falha na conexão: {e}")

# Cria múltiplas conexões
def criar_multiplas_conexoes(qtd):
    for i in range(qtd):
        threading.Thread(target=start_cliente, args=(i,), daemon=True).start()
        time.sleep(0.5)  # Pequeno delay entre conexões

if __name__ == "__main__":
    criar_multiplas_conexoes(100)  # Altere o número de conexões aqui
    time.sleep(5)  # Espera para todas as mensagens serem trocadas
