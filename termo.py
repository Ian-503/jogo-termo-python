import random
import requests
import emoji

url = "https://api.datamuse.com/words?ml=livro&v=pt"

try:
    resposta = requests.get(url, timeout=10)
    lista_de_palavras = resposta.json()    
    while True:
        item = random.choice(lista_de_palavras)

        palavra = item["word"].lower()
        palavra = palavra.replace("á", "a").replace("é", "e").replace("ã", "a").replace("ç", "c")
        if len(palavra) == 6:
            break
except Exception as e:
    print(f"\n❌ Erro de conexão: {e}")
A,B,C,D,E,F=list(palavra)
senha=[A,B,C,D,E,F]

print("====================================")
print("  BEM-VINDO AO MEU TERMO!  ")
print("====================================")

while True:
    mostrar=[]
    tentativa=input("qual voce acha que é a palavra de 6 letras:\n").lower()
    if len(tentativa)!=6:
        print("coloque uma palavra de 6 letras")
        continue

    if tentativa==palavra:
        print("VOCE ACERTOU, A PALAVRA ERA: "+palavra)
        break

    G,H,I,J,K,L=list(tentativa)
    jogada=[G,H,I,J,K,L]

    
    for i in range(6):
            if jogada[i] == senha[i]:
                mostrar.append(emoji.emojize(":green_circle:"))   
            elif jogada[i] in senha:
                mostrar.append(emoji.emojize(":yellow_circle:"))  
            else:
                mostrar.append(emoji.emojize(":red_circle:"))
    print(" ".join(mostrar))