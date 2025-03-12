import random as rd

def transmit_with_error(m:str): 
    """
    Simula um erro
    """
    random_number = rd.randint(0, len(m) - 1)
    bit_list = list(m)

    bit_list[random_number] = '0' if m[random_number] == '1' else '1'

    message_erro = "".join(bit_list) 
    return message_erro


def integer_to_binary(number):
    return format(int(number), 'b')
     

def binary_to_integer(number):
    return int(number, 2)

message = 20
print(f"Mesagem Original: {message} --- {integer_to_binary(message)}")

message_received = transmit_with_error(integer_to_binary(message))
print(f"Mesagem Recebida: {binary_to_integer(message_received)} --- {message_received}")