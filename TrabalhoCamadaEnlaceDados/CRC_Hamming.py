import random

def string_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_string(binary_message, block_size=8):
    # Agora usamos block_size para dividir corretamente em 7 bits (Hamming)
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

original_message = "rede"
binary_message = string_to_binary(original_message)

# Codificação com Hamming
hamming_encoded_message = ''.join(hamming_encode(binary_message[i:i+4]) for i in range(0, len(binary_message), 4))

# Introdução de erro
corrupted_message_hamming = transmit_with_error_noise(hamming_encoded_message)

# Decodificação e correção de erros
decoded_corrected_bits = ''.join(hamming_decode(corrupted_message_hamming[i:i+7]) for i in range(0, len(corrupted_message_hamming), 7))

# Verificação se houve erro detectado e corrigido
error_detected = decoded_corrected_bits != binary_message

# Impressão da mensagem com erro e corrigida
print(f"Mensagem original (binário): {binary_message}")
print(f"Mensagem original (texto): {original_message}\n")
print(f"Mensagem com erro (binário): {corrupted_message_hamming}")
print(f"Mensagem com erro (texto): {binary_to_string(corrupted_message_hamming, block_size=7)}")  # Usando block_size=7 para Hamming
print(f"Erro detectado: {error_detected}\n")
print(f"Mensagem corrigida (binário): {decoded_corrected_bits}")
print(f"Mensagem corrigida (texto): {binary_to_string(decoded_corrected_bits)}")
