import random

### IMPORTANTE ###
# nao funcionando, nao sei pq, nao sei como, nao sei quem, so sei q nada sei
# ass: Jars

def string_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_string(binary_message, block_size=8):
    chars = [binary_message[i:i+block_size] for i in range(0, len(binary_message), block_size)]
    return ''.join(chr(int(char, 2)) for char in chars)

def transmit_with_error_noise(binary_message, error_rate=0.05):
    corrupted_bits = ""
    for bit in binary_message:
        if random.random() < error_rate:
            corrupted_bits += "0" if bit == "1" else "1"
        else:
            corrupted_bits += bit
    return corrupted_bits

def hamming_encode(data):
    while len(data) < 4:
        data += '0'  # Preenchendo com zeros se necessário
    d = [int(bit) for bit in data]
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}"

def hamming_decode(data):
    d = [int(bit) for bit in data]
    p1 = d[0] ^ d[2] ^ d[4] ^ d[6]
    p2 = d[1] ^ d[2] ^ d[5] ^ d[6]
    p3 = d[3] ^ d[4] ^ d[5] ^ d[6]
    error_position = p1 * 1 + p2 * 2 + p3 * 4
    if error_position:
        d[error_position - 1] ^= 1  # Corrige o erro na posição identificada
    return f"{d[2]}{d[4]}{d[5]}{d[6]}"

def crc_remainder(data, divisor="1101"):
    data += '0' * (len(divisor) - 1)
    data = list(data)
    divisor = list(divisor)
    
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':
            for j in range(len(divisor)):
                data[i + j] = str(int(data[i + j]) ^ int(divisor[j]))
    return ''.join(data[-(len(divisor) - 1):])

def crc_encode(data, divisor="1101"):
    remainder = crc_remainder(data, divisor)
    return data + remainder

def crc_check(data, divisor="1101"):
    return crc_remainder(data, divisor) == '0' * (len(divisor) - 1)

def pad_to_multiple(data, block_size):
    while len(data) % block_size != 0:
        data += '0'
    return data

def simulate_transmission(original_message, iterations, error_rate):
    total_errors = 0
    corrected_errors = 0
    no_errors = 0
    successfully_corrected = 0
    undetected_errors = 0
    
    for _ in range(iterations):
        binary_message = string_to_binary(original_message)
        crc_encoded_message = crc_encode(binary_message)
        crc_encoded_message = pad_to_multiple(crc_encoded_message, 4)  # Garante múltiplo de 4 bits
        hamming_encoded_message = ''.join(hamming_encode(crc_encoded_message[i:i+4]) for i in range(0, len(crc_encoded_message), 4))
        corrupted_message = transmit_with_error_noise(hamming_encoded_message, error_rate)
        decoded_corrected_bits = ''.join(hamming_decode(corrupted_message[i:i+7]) for i in range(0, len(corrupted_message), 7))
        
        if crc_check(decoded_corrected_bits):
            decoded_message = binary_to_string(decoded_corrected_bits[:-3])  # Remove bits CRC
            if decoded_message == original_message:
                no_errors += 1
            else:
                successfully_corrected += 1
        else:
            total_errors += 1
            decoded_message = binary_to_string(decoded_corrected_bits[:-3])
            if decoded_message == original_message:
                corrected_errors += 1
            else:
                undetected_errors += 1
    
    print(f"Total de execuções: {iterations}, Mensagem: {original_message}, Chance de erro: {error_rate}")
    print(f"Mensagens sem erro: {no_errors}")
    print(f"Mensagens com erro detectado: {total_errors}")
    print(f"Mensagens corrigidas com sucesso: {successfully_corrected}")
    print(f"Mensagens com erro não detectado: {undetected_errors}")

# Exemplo de uso:
simulate_transmission("A", iterations=1000, error_rate=0.05)
