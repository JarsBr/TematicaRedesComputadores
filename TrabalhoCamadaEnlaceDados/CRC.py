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

def xor(a, b):
    """
    Realiza a operação XOR entre duas sequências de bits.
    """
    result = ""
    b = b.ljust(len(a), '0')  # Garante que b tenha o mesmo tamanho de a
    for i in range(len(a)):
        result += "0" if a[i] == b[i] else "1"
    return result

def mod2div(dividend, divisor):
    """
    Executa a divisão módulo 2.
    """
    pick = len(divisor)
    tmp = dividend[:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor)[1:] + dividend[pick]
        else:
            tmp = xor(tmp, '0' * pick)[1:] + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(tmp, divisor)[1:]
    else:
        tmp = xor(tmp, '0' * pick)[1:]
    return tmp

def encode_crc(binary_message, generator="1101"):
    """
    Codifica a mensagem com CRC usando um gerador polinomial.
    """
    appended_message = binary_message + "0" * (len(generator) - 1)
    remainder = mod2div(appended_message, generator)
    return binary_message + remainder

def check_crc(received_message, generator="1101"):
    """
    Verifica a integridade da mensagem usando CRC.
    """
    remainder = mod2div(received_message, generator)
    return int(remainder, 2) == 0

# original_message = input("Digite sua mensagem:")
original_message = "Temática em Redes de Computadores"
error_rate = 0.06
binary_message = string_to_binary(original_message)

count_message_with_erro = 0
count_crc_detected_error = 0
loop_row = 100

print(f'Método de verificação: CRC \nMessage: {original_message} \nError Rate: {error_rate}')

for x in range(loop_row):
    # Calcula CRC antes da transmissão
    crc_encoded_message = encode_crc(binary_message)

    # Simula transmissão com erro
    corrupted_message_crc = transmit_with_error_noise(crc_encoded_message, error_rate)

    # Verifica o CRC
    if not check_crc(corrupted_message_crc):
        count_crc_detected_error += 1

    if corrupted_message_crc != crc_encoded_message:
        count_message_with_erro += 1

print(f"De {loop_row} mensagens enviadas com {count_message_with_erro} mensagens com erro, CRC detectou erro em {count_crc_detected_error} ")