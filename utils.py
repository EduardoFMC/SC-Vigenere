import string
ALFABETO = list(string.ascii_uppercase)

#repete as letras da chave para caber o tamanho completo da mensagem
def check_key(message, password_key):

    new_key = ""
    i = 0

    for _ in message:
        new_key += password_key[i]
        i = (i + 1) % len(password_key)

    return new_key.upper()

#recebe uma lista e retorna a mesma lista, mas com o primeiro elemento sendo o último
def shift_lista(lista):
    first_element = lista[0]
    return lista[1:len(lista)] + [first_element]

#recebe um inteiro e retorna uma lista com os seus divisores de 2 até 20
def dividores_ate_20(num: int):
    
    divisores = []
    i = 2
    
    while i <= 20:
        if num % i == 0:
            divisores.append(i)
        i += 1
    
    return divisores

#recebe uma cifra e retorna a mesma cifra, porém sem os símbolos que não são estão no alfabeto
def ajeita_cifra(cipher: str):
    newCipher = ""
    text = cipher.upper()

    for letra in text:
        if letra.upper() in ALFABETO:
            newCipher += letra
    
    return newCipher