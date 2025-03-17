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

def transmit_with_error_noise(binary_message, error_rate = 0.1):
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

def calculate_checksum(binary_message):
    """
    Calcula o checksum somando os valores inteiros de cada byte e aplicando módulo 256.
    """
    checksum = sum(int(binary_message[i:i+8], 2) for i in range(0, len(binary_message), 8)) % 256
    return format(checksum, '08b')

def check_checksum(binary_message, received_checksum):
    """
    Verifica se o checksum recalculado bate com o recebido.
    """
    return calculate_checksum(binary_message) == received_checksum

def calculate_crc(binary_message, divisor='1101'):
    """
    Calcula o CRC (Cyclic Redundancy Check) da mensagem.
    """
    divisor_len = len(divisor) - 1
    dividend = binary_message + '0' * divisor_len
    divisor = int(divisor, 2)
    dividend = int(dividend, 2)
    
    while dividend.bit_length() >= divisor.bit_length():
        shift = dividend.bit_length() - divisor.bit_length()
        dividend ^= divisor << shift
    
    return format(dividend, f'0{divisor_len}b')

def check_crc(binary_message, received_crc, divisor='1101'):
    """
    Verifica a integridade do CRC comparando o recebido com o recalculado.
    """
    return calculate_crc(binary_message, divisor) == received_crc



# # TESTE TAXA DE DETECCAO
# original_message = "Oi, tudo bem?"
# binary_message = string_to_binary(original_message)

# # Número de testes
# num_tests = 10

# detections_parity = 0
# detections_checksum = 0
# detections_crc = 0

# for x in range(num_tests):
#     print(f"{x}")
#     original_message = "Hello"
#     binary_message = string_to_binary(original_message)
    
#     # Calcula valores antes da transmissão
#     original_parity = add_parity_bit(binary_message)
#     original_checksum = calculate_checksum(binary_message)
#     original_crc = calculate_crc(binary_message)
    
#     # Simula transmissão com erro
#     corrupted_message = transmit_with_error_noise(binary_message)
    
#     # Recalcula valores após a transmissão
#     corrupted_parity = add_parity_bit(corrupted_message)
#     corrupted_checksum = calculate_checksum(corrupted_message)
#     corrupted_crc = calculate_crc(corrupted_message)
    
#     if not check_parity(corrupted_parity):
#         detections_parity += 1
#     if not check_checksum(corrupted_message, original_checksum):
#         detections_checksum += 1
#     if not check_crc(corrupted_message, original_crc):
#         detections_crc += 1

# # Calcula porcentagens de detecção
# parity_rate = (detections_parity / num_tests) * 100
# checksum_rate = (detections_checksum / num_tests) * 100
# crc_rate = (detections_crc / num_tests) * 100

# print(f"Taxa de detecção por Paridade: {parity_rate:.2f}%")
# print(f"Taxa de detecção por Checksum: {checksum_rate:.2f}%")
# print(f"Taxa de detecção por CRC: {crc_rate:.2f}%")



# TESTE UNICO

original_message = "AAA"
binary_message = string_to_binary(original_message)

# Calcula valores antes da transmissão
original_parity = add_parity_bit(binary_message)
original_checksum = calculate_checksum(binary_message)
original_crc = calculate_crc(binary_message)

# Simula transmissão com erro
corrupted_message = transmit_with_error_noise(binary_message)
corrupted_message_parity = transmit_with_error_noise(original_parity)

# Recalcula valores após a transmissão
# corrupted_parity = add_parity_bit(corrupted_message)
corrupted_checksum = calculate_checksum(corrupted_message)
corrupted_crc = calculate_crc(corrupted_message)

print(f"Mensagem original: {original_message}")
print(f"Mensagem binária original: {binary_message}")
print(f"Mensagem binária com erro: {corrupted_message}")
print(f"Mensagem recebida: {binary_to_string(corrupted_message)}")
print("Mensagem binária com erro:",corrupted_message_parity)
print("Paridade detectou erro?", check_parity(corrupted_message_parity))
# print("Checksum detectou erro?", not check_checksum(corrupted_message, original_checksum))
# print("CRC detectou erro?", not check_crc(corrupted_message, original_crc))