import random

def transmit_with_error_noise(number):
    noise = random.randint(1, 255)  # Gera um número aleatório de 8 bits
    print(format(noise, 'b'))
    number_with_error = number ^ noise  # Aplica um XOR com ruído aleatório
    return number_with_error

original = 5
corrupted = transmit_with_error_noise(original)
print(f"Original: {format(original, '08b')}, Com erro: {format(corrupted, '08b')}, Decimal com erro: {corrupted}")