import random

def transmit_with_error_noise(number):
    noise = random.randint(1, 255)  # Gera um número aleatório de 8 bits
    print(format(noise, 'b'))
    number_with_error = number ^ noise  # Aplica um XOR com ruído aleatório
    return number_with_error

def add_parity_bit(number):
    bits = format(number, '08b')
    parity = '1' if bits.count('1') % 2 != 0 else '0'
    return int(bits + parity, 2)

def check_parity(number):
    bits = format(number, '09b')  # 9 bits incluindo paridade
    return bits.count('1') % 2 == 0

def calculate_checksum(number):
    return number % 256

def check_checksum(number, received_checksum):
    return calculate_checksum(number) == received_checksum

def calculate_crc(number, divisor='1101'):
    bits = format(number, '08b')
    dividend = bits + '0' * (len(divisor) - 1)
    divisor = int(divisor, 2)
    dividend = int(dividend, 2)
    
    while dividend.bit_length() >= divisor.bit_length():
        shift = dividend.bit_length() - divisor.bit_length()
        dividend ^= divisor << shift
    
    return format(dividend, f'0{divisor.bit_length() - 1}b')

def check_crc(number, received_crc, divisor='1101'):
    return calculate_crc(number) == received_crc

original = 5
corrupted = transmit_with_error_noise(original)

# Aplicação das verificações
parity_bits = add_parity_bit(original)
checksum = calculate_checksum(original)
crc = calculate_crc(original)

print(f"Original: {format(original, '08b')}, Com erro: {format(corrupted, '08b')}, Decimal com erro: {corrupted}")
print("Paridade válida?", check_parity(parity_bits))
print("Checksum válido?", check_checksum(original, checksum))
print("CRC válido?", check_crc(original, crc))