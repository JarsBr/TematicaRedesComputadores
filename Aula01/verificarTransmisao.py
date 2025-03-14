import random

def transmit_with_error_noise(number):
    noise = random.randint(1, 255)  # Gera um número aleatório de 8 bits
    print(format(noise, 'b'))
    number_with_error = number ^ noise  # Aplica um XOR com ruído aleatório
    return number_with_error

def add_parity_bit(number):
    """
    Adiciona um bit de paridade ao número.
    Usa paridade par: se o número de bits 1 for ímpar, adiciona um bit 1; caso contrário, adiciona um bit 0.
    """
    bits = format(number, '08b')
    parity = '1' if bits.count('1') % 2 != 0 else '0'
    return int(bits + parity, 2)

def check_parity(number):
    """
    Verifica se o bit de paridade está correto.
    Conta os bits 1 e verifica se o total é par.
    """
    bits = format(number, '09b')  # 9 bits incluindo paridade
    return bits.count('1') % 2 == 0

def calculate_checksum(number):
    """
    Calcula o checksum do número.
    Retorna o valor do número módulo 256.
    """
    return number % 256

def check_checksum(number, received_checksum):
    """
    Verifica a integridade do checksum.
    Compara o checksum recebido com o recalculado a partir do número original.
    """
    return calculate_checksum(number) == received_checksum

def calculate_crc(number, divisor='1101'):
    """
    Calcula o CRC (Cyclic Redundancy Check) usando um divisor polinomial.
    Concatena zeros ao número original e aplica divisão binária XOR.
    Retorna o resto da divisão como código de verificação.
    """
    bits = format(number, '08b')
    dividend = bits + '0' * (len(divisor) - 1)
    divisor = int(divisor, 2)
    dividend = int(dividend, 2)
    
    while dividend.bit_length() >= divisor.bit_length():
        shift = dividend.bit_length() - divisor.bit_length()
        dividend ^= divisor << shift
    
    return format(dividend, f'0{divisor.bit_length() - 1}b')

def check_crc(number, received_crc, divisor='1101'):
    """
    Verifica a integridade do CRC.
    Calcula o CRC do número original e compara com o recebido.
    """
    return calculate_crc(number) == received_crc


original = 58545
corrupted = transmit_with_error_noise(original)

# Aplicação das verificações
parity_bits = add_parity_bit(original)
checksum = calculate_checksum(original)
crc = calculate_crc(original)

print(f"Original: {format(original, '08b')}, Com erro: {format(corrupted, '08b')}, Decimal com erro: {corrupted}")
print("Paridade válida?", check_parity(parity_bits))
print("Checksum válido?", check_checksum(original, checksum))
print("CRC válido?", check_crc(original, crc))