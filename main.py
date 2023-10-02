import re
import string
from utils import *

# Referencias: https://www.geeksforgeeks.org/vigenere-cipher/

# Alfabeto em uppercase
ALFABETO = list(string.ascii_uppercase)

# Cifrar a message de acordo com a password_key
def vigenere_crypt(message: str, password_key: str):
    message = message.upper()

    resultado = ""
    
   
    k = check_key(message, password_key)
    i = 0
    
    for letra in message:
        if letra in ALFABETO:

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

#mostra os três tamanhos mais possíveis de serem a chave
def key_length(cipher: str):
    
    newCipher = ajeita_cifra(cipher)
    maiorFator = (-1,-1)
    trigramas = {}
    tamanhos_possiveis ={2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0,
                        10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0,
                        17:0, 18:0, 19:0, 20:0}
    
    i = 0
    j = 3
    
    while j <= len(newCipher):
    
        if newCipher[i:j] in trigramas.keys():
            espaco = i - trigramas[newCipher[i:j]]
            
            t_possiveis = dividores_ate_20(espaco)
            
            for a in t_possiveis:
                tamanhos_possiveis[a] += 1
                #if 5 <= a <= 8 and tamanhos_possiveis[a] > maiorFator[1]:
                #    maiorFator = (a, tamanhos_possiveis[a])

        trigramas[newCipher[i:j]] = i
            
        i += 1
        j += 1
    
    tamanhos_possiveis = dict(sorted(tamanhos_possiveis.items(), key=lambda item: item[1], reverse=True))

    print("Os tamanhos mais prováveis encontrados foram:")

    i = 1   
    for tamanho in tamanhos_possiveis.keys():
        print("Tamanho:", tamanho, "--", "Fator:", tamanhos_possiveis[tamanho])
        if i == 3:
            break
        i += 1
    


#encontra a chave
def found_key(cipher: str, key_len: int, language: str):

    newCipher = ajeita_cifra(cipher)
    
    key = ""
    
    for i in range(key_len):

        key += found_letter(newCipher, i, key_len, language)
    
    return key

#encontra a letra de um determinado indice da chave
def found_letter(cipher: str, indice: int, key_len: int, language: str):
    eng_probabilities = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015,
                        6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507,
                        1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 
                        0.150, 1.974, 0.074]
    pt_probabilities = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18,
                        0.40, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 
                        7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]
    
    cipher_probabilities = {}
    cipher_frequencia = []
    count_letters = 0
    ajuste = 0
    menor_diferenca = 1e9

    for i in range(indice, len(cipher), key_len):
        cipher_probabilities[cipher[i]] = cipher_probabilities.get(cipher[i], 0) + 1
        count_letters += 1
    
    for i in ALFABETO:
        cipher_frequencia.append((cipher_probabilities.get(i, 0) / count_letters) * 100)
    
    for i in range(26):
        diferenca = 0
        for j in range(26):
            if language == "EN":
                diferenca += abs(eng_probabilities[j] - cipher_frequencia[j])
            else:
                diferenca += abs(pt_probabilities[j] - cipher_frequencia[j])
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            ajuste = i
        
        cipher_frequencia = shift_lista(cipher_frequencia)
        
    return chr(ord('A') + ajuste)
    

if __name__ == "__main__":
    # https://cryptii.com/pipes/vigenere-cipher
    # checador online ↑
    acao = ""

    print("Bem vindo ao cifrador e decifrador de Vigenere\n")

    while True:
        print("(1): Cifrar")
        print("(2): Decidrar")
        print("(3): Quebrar uma cifra")
        print("(4): Sair\n")
        print("Escolha a sua ação:", end="")
        acao = input()
        print()

        if acao == "1":
            mensagem = input("Digite a mensagem que será cifrada: ")
            chave = input("Digite a chave que será usada para cifrar: ")

            cifra = vigenere_crypt(mensagem, chave)
            print("\nMensagem cifrada:\n")
            print(cifra, "\n")
        
        elif acao == "2":
            cifra = input("Digite a cifra que será decifrada: ")
            chave = input("Digite a chave que será usada para decifrar: ")

            mensagem = vigenere_decrypt(cifra, chave)
            print("\nMensagem cifrada:")
            print(mensagem, "\n")
        
        elif acao == "3":
            cifra = input("Digite a cifra que será quebrada:")

            key_length(cifra)

            lingua = input("Qual lingua será utilizada para decifrar? (PT/EN) ")
            print()
            resposta = "s"
            while resposta == "s":
                tamanho = int(input("Qual tamanho de chave você deseja utilizar para quebrar a chave? "))
                print()
                chave_encontrada = found_key(cifra, tamanho, lingua)
                print("Chave encontrada:", chave_encontrada, "\n")

                mensagem_encontrada = vigenere_decrypt(cifra, chave_encontrada)
                print("Mensagem decifrada com a chave encontrada:\n")
                print(mensagem_encontrada, "\n")

                resposta = input("Deseja tentar de novo com um tamanho diferente? (s/n)")
                print()
        elif acao == "4":
            break

        input()
    
    print("EXIT")
    
    