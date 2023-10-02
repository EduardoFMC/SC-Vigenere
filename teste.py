import string

ALFABETO = list(string.ascii_uppercase)

def ajeita_cifra(cipher: str):
    newCipher = ""
    
    for letra in cipher:
        if letra.upper() in ALFABETO:
            newCipher += letra.upper()
    
    return newCipher
