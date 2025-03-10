import random as rd

def trasmission_with_error(m):
    #simular um erro
    x = rd.randint(0, len(m) - 1)
    lista = list(m)
    if m[x] == '1':
        lista[x] = '0'
        final = "".join(lista) 
    elif m[x] == '0':
        lista[x] = '1'  
        final = "".join(lista) 
    print("Mensagem trasmitida")
    return final

def integer_to_binary(number):
    number_bin = format(int(number), 'b')
    return number_bin

def binary_to_integer(number):
    number_int = int(number, 2)
    return number_int

mesagem = 20
mesagem_final = trasmission_with_error(integer_to_binary(mesagem))

print("Mesagem Original INT:", mesagem)
print("Mesagem Original BIN:", integer_to_binary(mesagem))

print("Mesagem Original INT:", binary_to_integer(mesagem_final))
print("Mesagem Recebida: BIN", mesagem_final)