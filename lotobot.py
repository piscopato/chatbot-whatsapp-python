from random import randint
from time import sleep


def sortear(apostas, quantidade):
    jogos = list()
    jogo = list()
    aposta = apostas
    t = 0
    n = 0
    # print(20 * "-", "LOTO", 20 * "-")
    if aposta not in (1, 2):
        return ('Escolha APENAS 1 (LOTOFÁCIL) OU 2 (MEGASENA)')
    else:

        tent = quantidade
        if aposta == 1:
            aposta = 25
            numb = 15
        elif aposta == 2:
            aposta = 60
            numb = 6

        # print("sorteando...")
        # sleep(1)
        for t in range(0, tent):
            for n in range(0, numb):
                a = randint(1, aposta)
                if a in jogo:
                    while True:
                        a = randint(1, aposta)
                        if a not in jogo:
                            break
                jogo.append(a)
            jogo = sorted(jogo)
            jogos.append(jogo)
            jogo = []

        # print(17 * "-", "RESULTADOS", 17 * "-", '\n')
        resultado = list()
        for count, j in enumerate(jogos):
            resultado.append(f'''jogo {count + 1} : {j}
''')
        return (resultado)
        # print(46 * "-")





