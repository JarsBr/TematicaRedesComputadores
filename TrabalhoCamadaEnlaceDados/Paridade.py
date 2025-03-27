import random

def string_to_binary(message):
    """
    Converte uma string para sua representação binária.
    """
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_string(binary_message):
    """
    Converte uma representação binária de volta para string.
    """
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message) -1, 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def transmit_with_error_noise(binary_message, error_rate):
    """
    Introduz um erro aleatório na mensagem binária.
    """
    corrupted_bits = ""
    for bit in binary_message:
        if random.random() < error_rate:
            corrupted_bits += "0" if bit == "1" else "1"
        else:
            corrupted_bits +=bit
    return corrupted_bits

def add_parity_bit(binary_message):
    """
    Adiciona um bit de paridade par à mensagem binária.
    """
    parity = '1' if binary_message.count('1') % 2 != 0 else '0'
    return binary_message + parity

def check_parity(binary_message):
    """
    Verifica a paridade da mensagem binária.
    """
    return not binary_message.count('1') % 2 == 0


# original_message = input("Digite sua mensagem:")
original_message = "Temática em Redes de Computadores"
error_rate = 0.06
binary_message = string_to_binary(original_message)

print(f'Método de verificação: Paridade \nMessage: {original_message} \nError Rate: {error_rate}')

count_message_with_erro = 0
count_parity_detected_erro = 0
loop_row = 100

for x in range(loop_row):
    # Calcula valores antes da transmissão
    original_parity = add_parity_bit(binary_message)

    # Simula transmissão com erro
    corrupted_message_parity = transmit_with_error_noise(original_parity, error_rate)

    # print(f"Mensagem original: {original_message}")
    # print(f"Mensagem recebida: {binary_to_string(corrupted_message_parity)}")
    # print(f"Mensagem binária original: {binary_message}")
    # print(f"Paridade binária original: {original_parity}")
    # print(f"Paridade binária com erro:",corrupted_message_parity)
    # print("Paridade detectou erro:", check_parity(corrupted_message_parity))

    if original_parity != corrupted_message_parity:
        count_message_with_erro += 1

    if check_parity(corrupted_message_parity):
        count_parity_detected_erro += 1

print(f"De {loop_row} mensagens enviadas com {count_message_with_erro} mensagens com erro, Paridade detectou erro em {count_parity_detected_erro}")

