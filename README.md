Jogo Termo (Clone) em Python

Este é um clone do famoso jogo **Termo** (ou *Wordle*), desenvolvido para rodar diretamente no terminal. 

O projeto consome uma API real para sortear dinamicamente palavras em português e utiliza a biblioteca de emojis para dar o feedback visual das tentativas do jogador!

----------------------------------------------------------

Tecnologias Utilizadas

*   **Python 3**
*   **API Datamuse** (Requisições HTTP para busca de palavras)
*   **Biblioteca `requests`** (Para comunicação com a API)
*   **Biblioteca `emoji`** (Para renderizar as bolinhas coloridas no terminal)

-----------------------------------------------------------

Como Rodar o Jogo

Se quiser testar o jogo na sua máquina, siga os passos abaixo:

 1. Clonar o repositório ou baixar o arquivo
Baixe o arquivo `termo.py` para a sua máquina.

 2. Instalar as dependências
Abra o seu terminal e instale as bibliotecas necessárias rodando:
bash
pip install requests emoji

------------------------------------------------------------
Como Jogar
O objetivo é adivinhar uma palavra secreta de 6 letras:

🟢 Bolinha Verde: A letra está correta e na posição certa!

🟡 Bolinha Amarela: A letra existe na palavra, mas está na posição errada.

🔴 Bolinha Vermelha: A letra não faz parte da palavra secreta.
