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
    
    newCipher = ajeita_cifra(cipher)
    
    trigramas = {}
    tamanho_provavel= (-1, -1) #(tamanho_provavel, frequncia)
    tamanhos_possiveis ={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0}
    
    i = 0
    j = 3
    
    while j <= len(newCipher):
    
        if newCipher[i:j] in trigramas.keys():
            espaco = i - trigramas[newCipher[i:j]]
            
            t_possiveis = dividores_ate_20(espaco)
            
            for a in t_possiveis:
                tamanhos_possiveis[a] += 1
                if tamanhos_possiveis[a] > tamanho_provavel[1]:
                    tamanho_provavel = (a, tamanhos_possiveis[a])
        
        trigramas[newCipher[i:j]] = i
            
        i += 1
        j += 1
    
    for i in tamanhos_possiveis.keys():
        print(i, ":", tamanhos_possiveis[i])
    
    return tamanho_provavel


def found_key(cipher: str, key_len: int, language: str):

    newCipher = ajeita_cifra(cipher)
    
    key = ""
    
    for i in range(key_len):

        key += found_letter(newCipher, i, key_len, language)
    
    return key

def found_letter(cipher: str, indice: int, key_len: int, language: str):
    
    eng_probabilities = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    pt_probabilities = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]
    
    cipher_probabilities = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cipher_frequencia = []
    count_letters = 0
    ajuste = 0
    menor_diferenca = 1e9

    for i in range(indice, len(cipher), key_len):
        cipher_probabilities[ord(cipher[i]) - ord('A')] += 1
        count_letters += 1
    
    for i in range(26):
        cipher_frequencia.append((cipher_probabilities[i] / count_letters) * 100)
    
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
    #return (ajuste, menor_diferenca)
    
   
def shift_lista(lista):
    first_element = lista[0]
    return lista[1:len(lista)] + [first_element]



def dividores_ate_20(num: int):
    
    divisores = []
    i = 2
    
    while i <= 20:
        if num % i == 0:
            divisores.append(i)
        i += 1
    
    return divisores

def ajeita_cifra(cipher: str):
    newCipher = ""
    
    for letra in cipher:
        if letra in ALFABETO:
            newCipher += letra
    
    return newCipher
    

if __name__ == "__main__":
    # https://cryptii.com/pipes/vigenere-cipher
    # checador online ↑

    texto = "In a world filled with endless possibilities, the human spirit yearns for exploration and discovery. From the deepest reaches of the oceans to the farthest corners of the cosmos, our innate curiosity propels us forward into the unknown, seeking knowledge, adventure, and meaning. One of the most remarkable aspects of human nature is our insatiable thirst for knowledge. Throughout history, we have sought to unravel the mysteries of the universe, from understanding the mechanics of the stars to deciphering the complexities of the human mind. It is through this relentless pursuit of knowledge that we have made incredible advancements in science, technology, and culture. The written word has been one of our most powerful tools in this quest for understanding. From ancient scrolls and manuscripts to modern books and digital publications, we have preserved and shared the collective wisdom of humanity across generations. Literature, in all its forms, serves as a bridge between the past and the future, allowing us to learn from the experiences and insights of those who came before us. As we journey through life, we encounter countless stories that shape our perspectives and values. Fictional tales transport us to fantastical realms, sparking our imagination and offering new ways of thinking. Non-fiction works provide us with information, analysis, and guidance, helping us navigate the complexities of the world. Each book, each essay, each poem has the power to leave an indelible mark on our souls. Yet, our quest for knowledge extends beyond the written word. We are explorers of the physical world as well, venturing into uncharted territories, scaling towering mountains, and delving into the depths of the earth. The natural world, with its breathtaking landscapes and diverse ecosystems, is a source of wonder and inspiration. It reminds us of our responsibility to be stewards of the planet, preserving its beauty and biodiversity for future generations. In our pursuit of knowledge and adventure, we also find connection with one another. Through shared experiences and shared stories, we forge bonds that transcend borders and cultures. We discover the universal truths that unite us as human beings, regardless of our differences. In a world often divided by politics and ideology, our shared quest for understanding can serve as a unifying force. As we stand on the threshold of the future, our thirst for knowledge remains unquenchable. We are on the brink of new discoveries in science and technology, from the exploration of other planets to the development of artificial intelligence. These advancements bring both excitement and challenges, as we grapple with ethical dilemmas and the implications of our actions. In this ever-changing world, it is crucial that we never lose sight of our fundamental human drive to explore, learn, and connect. Whether through the written word, scientific exploration, or the simple act of listening to another person's story, we have the power to enrich our lives and make a positive impact on the world. So, let us continue to embrace our innate curiosity, to seek out knowledge and adventure, and to cherish the connections we make along the way. For in the vast tapestry of human existence, it is these pursuits that give our lives depth, meaning, and purpose."
    chave = "arararara"

    cifrado = vigenere_crypt(texto, chave)
    decifrado = vigenere_decrypt(cifrado, chave)

    print(cifrado)
    print("")
    print(decifrado)
    
    print(key_legth(cifrado))

    print(found_key(cifrado, 3, "EN"))
   