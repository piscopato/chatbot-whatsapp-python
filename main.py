import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from chatgptfinal import *
import clima
import lotobot
from pynput.keyboard import Key, Controller
import os
from selenium.webdriver.chrome.options import Options
import conselhos
import youtube as yt


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Adiciona a opção de download
prefs = {"download.prompt_for_download": True}
chrome_options.add_experimental_option("prefs", prefs)

drive = webdriver.Chrome(options=chrome_options)
drive.get('https://web.whatsapp.com/')
texto = 'vazio'
num_imagem = 0
video_yt = 0

# seletores e classes:
ler = '.ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr'
box_msg = '.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt'
enviar = '.tvf2evcx.oq44ahr5.lb5m6g5c.svlsagor.p2rjqpw5.epia9gcq'
img = '.jciay5ix.tvf2evcx.oq44ahr5.lb5m6g5c.osz0hll6.nq7eualt.em5jvqoa.a21kwdn3'
menugeral = '.bo8jc6qi.p4t1lx4y.brjalhku'
itens_do_menu = '.bugiwsl0.fooq7fky'
itens_de_imagens = '._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1'


# menu de ajuda:
ajuda = '''Menu de ajuda do chatbot:
!q - respondo qualquer pergunta que você quiser 
!oi - respondo com (Olá, como posso ajudar?)
!hora - respondo com dia e a hora exata
!clima cidade - respondo com algumas informações sobre o clima
!loto Escolha APENAS 1 (LOTOFÁCIL) OU 2(MEGASENA) / Quantidade de jogos (exemplo !loto 5 2) - sorteios números para sua aposta
!discord - informo meu discord oficial 
!sticker - transforma *IMAGENS* em figurinhas
!mp4 link - baixa qualquer video do youtube na maior qualidade
!mp3 link - baixa somente o audio de qualquer video do youtube
!conselho - te da um conselho aleatório

E é só isso mesmo que eu faço'''

# confirma com o usuário se a página carregou:
input("Pressione enter após a leitura do Qr code ")


# cria uma pasta para salvas as imagens que serão usadas para salvar as figurinhas

def criar_pasta(pasta):
    try:
        diretorio_atual = os.getcwd()
        path = os.path.join(diretorio_atual, pasta)
        os.mkdir(path)
        print('pasta criada')

    except:
        pass


# aperta na caixa de mensagem / escreve a mensagem / envia a mensagem (parâmetro 'a' deve receber a mensagem a ser enviada)
def caixa_de_mensagem(a):
    try:
        digitar = WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, box_msg)))
        for caixas in digitar:
            if caixas.get_attribute("title") == "Digite uma mensagem":
                lines = a.split('\n')
                for line in lines:
                    caixas.send_keys(line)
                    ActionChains(drive).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                        Keys.ENTER).perform()
                    time.sleep(0.1)

                caixas.send_keys(Keys.ENTER)
    except Exception as es:
        print('erro ao enviar', es)
    # confirmar = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, enviar)))
    # confirmar.click()


# abre a conversa
def abrir_conversa(e):
    while True:
        try:
            e.click()
            break
        except:
            continue


criar_pasta('imagens para fig')
criar_pasta('videos')



# verifica constantemente as últimas mensagens recebidas e caso a mensagem seja uma das chaves definidas uma ação será executada
while True:
    try:
        msg = WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ler)))
        for e in msg:
            try:
                texto = e.text
                # time.sleep(0.1)
                # print(texto)

                # interação de oi
                if texto == '!oi':
                    print(texto)
                    abrir_conversa(e)
                    time.sleep(2)
                    caixa_de_mensagem('Olá, como posso ajudar?')

                # interage com o chatgpt da lib chatgptfinal
                elif texto[0: 2] == '!q':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(gerar_resposta(texto))

                # envia o menu de ajuda
                elif texto[0: 5] == '!help':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(ajuda)

                # envia o dia e a hora
                elif texto[0: 5] == '!hora':
                    data_e_hora_atuais = datetime.now()
                    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M'")
                    print(data_e_hora_atuais.strftime("Hoje é dia %d/%m/%Y e são: %H:%M' "))
                    abrir_conversa(e)
                    caixa_de_mensagem(data_e_hora_atuais.strftime("Hoje é dia %d/%m/%Y e são: %H:%M' "))

                # envia o clima conforme lib clima
                elif texto[0: 6] == '!clima':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(clima.clima_estado(texto[7:]))

                # envia o discord oficial
                elif texto[0: 8] == '!discord':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem('Nosso discord oficial é https://discord.gg/G9mqwq9E')

                # sorteia números para jogos da telesena
                elif texto[0: 5] == '!loto':
                    print(texto)
                    abrir_conversa(e)
                    if len(texto) == 9:
                        print(texto[6])
                        print(texto[8])
                        if texto[6].isnumeric():
                            if texto[8].isnumeric():
                                sorteio = lotobot.sortear(int(texto[6]), int(texto[8]))
                                print(sorteio)
                                caixa_de_mensagem(sorteio)
                            else:
                                caixa_de_mensagem('Escreva conforme exemplo: !loto 5 2) Usando somente números')
                        else:
                            caixa_de_mensagem('Escreva conforme exemplo: !loto 6 2) Usando somente números')
                    else:
                        caixa_de_mensagem('Escreva conforme exemplo: !loto 7 2) Usando somente números')


                elif texto[0:9] == '!conselho':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(conselhos.conselho())


                elif texto[0:5] == '!mp4 ':
                    abrir_conversa(e)
                    pasta = 'D:\\novochatbot\\videos'
                    nome_mp4 = f'video_yt{video_yt}.mp4'

                    yt.baixar_mp4(texto[5:], pasta, nome_mp4)

                    seletor = WebDriverWait(drive, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, menugeral)))
                    seletor.click()  # abre o menu de envio de arquivos da conversa
                    time.sleep(1)
                    opcao_do_seletor = WebDriverWait(drive, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             itens_do_menu)))  # retorna uma lista com todas os itens do menu de envio de arquivos na conversa

                    if os.path.getsize(f"D:\\novochatbot\\videos\\video_yt{video_yt}.mp4") > 67108864:
                        opcao = opcao_do_seletor[1]  # vai para o último item da lista que é o item para gerar figurinhas
                    else:
                        opcao = opcao_do_seletor[2]
                    opcao.click()
                    time.sleep(1.5)
                    keyboard = Controller()
                    keyboard.type(f"D:\\novochatbot\\videos\\video_yt{video_yt}.mp4")  # abre o local com nome onde foi salva a imagem
                    time.sleep(1.5)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time.sleep(10)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)  # envia a figurinha
                    video_yt += 1


                elif texto[0:5] == '!mp3 ':
                    abrir_conversa(e)
                    pasta = 'D:\\novochatbot\\videos'
                    musica = yt.baixar_mp3(texto[5:], pasta)

                    seletor = WebDriverWait(drive, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, menugeral)))
                    seletor.click()  # abre o menu de envio de arquivos da conversa
                    time.sleep(1)
                    opcao_do_seletor = WebDriverWait(drive, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             itens_do_menu)))  # retorna uma lista com todas os itens do menu de envio de arquivos na conversa

                    if os.path.getsize(f"D:\\novochatbot\\videos\\{musica}") > 67108864:
                        opcao = opcao_do_seletor[
                            1]  # vai para o último item da lista que é o item para gerar figurinhas
                    else:
                        opcao = opcao_do_seletor[2]
                    opcao.click()
                    time.sleep(1.5)
                    keyboard = Controller()
                    keyboard.type(
                        f"D:\\novochatbot\\videos\\{musica}")  # abre o local com nome onde foi salva a imagem
                    time.sleep(1.5)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time.sleep(10)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)  # envia a figurinha
                    video_yt += 1


                # transforma imagens em figurinhas
                elif texto[0:8] == '!sticker':
                    print(texto)
                    abrir_conversa(e)
                    time.sleep(2.5)
                    try:
                        imagens = WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, img)))
                        if len(imagens) == 0:
                            print('imagens não encontradas')
                        time.sleep(1)
                        c = imagens[-1]  # retorna a última imagem na conversa
                        tag = c.get_attribute('alt')
                        src = c.get_attribute('src')  # retorna o blob da imagem na página
                        try:
                            if tag == texto:
                                caixa_de_mensagem('⏳Um momento⏳')

                                c.click()  # abre a última mensagem na conversa com a tag alt='!sticker'
                                num_imagem += 1
                                opcao_da_imagem = WebDriverWait(drive, 10).until(
                                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, itens_de_imagens)))  # retorna uma lista com todas os itens do menu da imagem aberta
                                for i_d_m in opcao_da_imagem:
                                    if i_d_m.get_attribute('title') == 'Baixar':  # itera essa lista e retorna o item com a tag title='baixar'
                                        i_d_m.click()  # baixa a imagem
                                        time.sleep(1.5)  # delay para abrir o confirmador de download
                                        keyboard = Controller()
                                        keyboard.type(f"D:\\novochatbot\\imagens para fig\\imagem{num_imagem}.png")  # define um local e nome para salvar a imagem
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        time.sleep(1.5)  # delay para baixar a imagem
                                        for i_d_m in opcao_da_imagem:
                                            if i_d_m.get_attribute('title') == 'Fechar':  # itera essa lista e retorna o item com a tag title='fechar'
                                                i_d_m.click()  # fecha a imagem
                                        print('salvo')
                                        # time.sleep(1)
                                        seletor = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, menugeral)))
                                        seletor.click()  # abre o menu de envio de arquivos da conversa
                                        time.sleep(1)
                                        opcao_do_seletor = WebDriverWait(drive, 10).until(
                                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, itens_do_menu)))  # retorna uma lista com todas os itens do menu de envio de arquivos na conversa
                                        opcao = opcao_do_seletor[-1]  # vai para o último item da lista que é o item para gerar figurinhas
                                        opcao.click()
                                        time.sleep(1.5)
                                        keyboard = Controller()
                                        keyboard.type(f"D:\\novochatbot\\imagens para fig\\imagem{num_imagem}.png")  # abre o local com nome onde foi salva a imagem
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)  # envia a figurinha

                        except:
                            print('não foi possível concluir')

                    except:
                        print('não foi possível obter')

            except:
                continue
    except:
        print("Elemento não encontrado. Continuando...")
        continue
