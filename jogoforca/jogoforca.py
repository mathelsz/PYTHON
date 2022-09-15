import random


def bem_vindo():
    print('************************************************ JOGO DA FORCA ************************************************')

# define uma palavra secreta
def gera_palavra_secreta():
    palavras = ['arroz', 'feijao', 'banana', 'maca', 'hipopotamo']
    index = random.randint(0, len(palavras) - 1)
    return palavras[index]


# gerar uma palavra vazia
def gera_palavra_vazia(qntd_caracteres):
    palavra_vazia = []

    for i in range(qntd_caracteres):
        palavra_vazia.append('_')
    return palavra_vazia

def status(palavra, erros):
    print(palavra)
    print('Erros: ' + str(erros) + '\n')

if __name__ == '__main__':
    bem_vindo()

    palavra_secreta = gera_palavra_secreta()
    palavra_jogo = gera_palavra_vazia(len(palavra_secreta))



    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        status(palavra_jogo, erros)

        letra_chute = input("Qual letra?")
        if letra_chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if letra_chute == letra:
                    palavra_jogo[posicao] = letra

                posicao += 1
        else:
            erros += 1

        if erros == 6:
            enforcou = True
            print('Você perdeu ----------- ENFORCADO!')

        if '_' not in palavra_jogo:
            acertou = True
            print('Você ganhou!')
