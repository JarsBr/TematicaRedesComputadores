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
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
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
            corrupted_bits += bit
    return corrupted_bits

def calculate_checksum(binary_message, chunk_size=8):
    """
    Calcula o checksum da mensagem binária.
    """
    checksum = 0
    for i in range(0, len(binary_message), chunk_size):
        chunk = binary_message[i:i + chunk_size]
        checksum += int(chunk, 2) if len(chunk) == chunk_size else 0
    checksum = (~checksum) & 0xFF  # Inverte os bits (Complemento de 1)
    return format(checksum, '08b')

def verify_checksum(binary_message, received_checksum, chunk_size=8):
    """
    Verifica o checksum da mensagem recebida.
    """
    checksum = 0
    for i in range(0, len(binary_message), chunk_size):
        chunk = binary_message[i:i + chunk_size]
        checksum += int(chunk, 2) if len(chunk) == chunk_size else 0
    checksum += int(received_checksum, 2)
    return (checksum & 0xFF) == 0xFF  # Se a soma com o checksum for 0xFF, está correto

# original_message = input("Digite sua mensagem:")
original_message = "Temática em Redes de Computadores"
error_rate = 0.06
binary_message = string_to_binary(original_message)

count_message_with_erro = 0
count_checksum_detected_error = 0
loop_row = 100

print(f'Método de verificação: Checksum \nMessage: {original_message} \nError Rate: {error_rate}')

for x in range(loop_row):
    # Calcula checksum antes da transmissão
    checksum = calculate_checksum(binary_message)
    message_with_checksum = binary_message + checksum

    # Simula transmissão com erro
    corrupted_message_with_checksum = transmit_with_error_noise(message_with_checksum, error_rate)
    corrupted_binary_message = corrupted_message_with_checksum[:-8]
    received_checksum = corrupted_message_with_checksum[-8:]

    if message_with_checksum != corrupted_message_with_checksum:
        count_message_with_erro += 1

    # Verifica o checksum
    if not verify_checksum(corrupted_binary_message, received_checksum):
        count_checksum_detected_error += 1

print(f"De {loop_row} mensagens enviadas com {count_message_with_erro} mensagens com erro, Checksum detectou erro em {count_checksum_detected_error}")
