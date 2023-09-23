import re
import string
from utils import *

# Referencias: https://www.geeksforgeeks.org/vigenere-cipher/

# Alfabeto em uppercase
ALFABETO = list(string.ascii_uppercase)

# Cifrar a message de acordo com a password_key
def vigenere_crypt(message: str, password_key: str):

    # Convert message to uppercase
    message = message.upper()

    # TODO: checar se a password_key é válida: se for maior que a message, se contém caracteres não alfabéticos, etc
    # TODO: Tudo deve ser em uppercase?

    resultado = ""
    
   
    k = check_key(message, password_key)
    i = 0
    
    for letra in message:
        if letra in ALFABETO:

            # ci = (pi + k[(i−1) mod l]+1) mod 26
            resultado += ALFABETO[((ord(letra) + ord(k[i])) % 26)]
            i += 1
        else:
            resultado += letra
       

    return resultado

# Decifrar a message de acordo com a password_key
def vigenere_decrypt(message: str, password_key: str):

    message = message.upper()
    resultado = ""

    k = check_key(message, password_key)
    i = 0

    for letra in message:
        if letra in ALFABETO:
            resultado += ALFABETO[(ord(letra) - ord(k[i]) % 26 + 26) % 26]
            i += 1
        else:
            resultado += letra
        
    return resultado

if __name__ == "__main__":
    # https://cryptii.com/pipes/vigenere-cipher
    # checador online ↑

    texto = "Suga e mama, chupa e engole"
    chave = "rola"

    cifrado = vigenere_crypt(texto, chave)
    decifrado = vigenere_decrypt(cifrado, chave)

    print(cifrado)
    print("")
    print(decifrado)
   