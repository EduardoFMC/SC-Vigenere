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

#encontrar tamanho da chave
def key_legth(cipher: str):
    
    trigramas = {}
    tamanho_provavel= (-1, -1) #(tamanho_provavel, frequncia)
    tamanhos_possiveis ={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0}
    
    i = 0
    j = 2
    
    while j <= len(cipher):
        
        if cipher[i:j] in trigramas.keys():
            espaco = i - (trigramas[cipher[i:j]] + 1)
            
            t_possiveis = dividores_ate_20(espaco)
            
            for a in t_possiveis:
                tamanhos_possiveis[a] =+ 1
                if tamanhos_possiveis[a] > tamanho_provavel[1]:
                    tamanho_provavel = (a, tamanhos_possiveis[a])
            
        trigramas[cipher[i:j]] = j
        i += 1
        j += 1
    
    return tamanho_provavel[0]

def dividores_ate_20(num: int):
    
    divisores = []
    i = 2
    
    while i <= 20:
        if num % i == 0:
            divisores.append(i)
        i += 1
    
    return divisores
    

if __name__ == "__main__":
    # https://cryptii.com/pipes/vigenere-cipher
    # checador online ↑

    texto = "Heron de Alexandria no século primeiro inventou teatros automatizados que usavam programação análoga para controlar os fantoches, portas, luzes e efeitos de som.A mais antiga programadora de computadores que se conhece é Ada Lovelace, filha de Anabella e de Lord Byron (o poeta). Ao serviço do matemático Charles Babbage, traduziu e expandiu uma descrição da sua máquina analítica. Muito embora Babbage nunca tenha completado a construção de nenhuma das suas máquinas, o trabalho que ele e Ada desenvolveram sobre elas, garantiu a Ada o título de primeira programadora de computadores do mundo (veja as notas de Ada Byron sobre a máquina analítica).[2] A linguagem de programação Ada recebeu o seu nome em homenagem à Ada.[3] Um dos primeiros programadores que se tem notícia de ter completado todos os passos para a computação sem auxílio, incluindo a compilação e o teste, é Wallace J. Eckert. O trabalho deste homem antecede a ascensão das linguagens de computador, porque ele usou a linguagem da matemática para solucionar problemas astronômicos. No entanto, todos os ingredientes estavam lá: ele trabalhou um laboratório de computação para a Universidade de Colúmbia com equipamentos fornecidos pela IBM, completos com uma divisão de serviço de atendimento ao cliente, e consultores de engenharia para propósitos especiais, na cidade de Nova York, na década de 1930, usando cartões perfurados para armazenar os resultados intermediários de seus cálculos, e então formatando os cartões perfurados para controlar a impressão das respostas, igual ao trabalho para os censos décadas antes. Tinha técnicas de debug tais como códigos de cores, bases cruzadas, verificação e duplicação. Uma diferença entre Eckert e os programadores dos dias de hoje é que o exemplo do seu trabalho influenciou o projeto Manhattan. Seu trabalho foi reconhecido por astrônomos do Observatório da Universidade de Yale, Observatório da Universidade de Princeton, Observatório da Marinha dos EUA, Observatório da Faculdade Harvard, Observatório dos estudantes da Universidade da Califórnia, Observatório Ladd da Universidade de Brown e Observatório Sproul da Faculdade de Swarthmore. Alan Turing é frequentemente encarado como o pai da ciência de computadores e, por afinidade, da programação. Ele foi responsável por ajudar na elaboração e programação de um computador destinado a quebrar o código alemão ENIGMA durante a Segunda Guerra Mundial — ver Máquina Enigma."
    chave = "senhasecreta"

    cifrado = vigenere_crypt(texto, chave)
    decifrado = vigenere_decrypt(cifrado, chave)

    print(cifrado)
    print("")
    print(decifrado)
    
    print(key_legth(cifrado))
   