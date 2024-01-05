import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from chatgptfinal import *
import clima
import lotobot
from PIL import Image
import io
from pynput.keyboard import Key, Controller
import urllib.request






drive = webdriver.Chrome()

# seletores e classes:
ler = '.ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr'
box_msg = '.selectable-text.copyable-text.iq0m558w.g0rxnol2'
enviar = '.tvf2evcx.oq44ahr5.lb5m6g5c.svlsagor.p2rjqpw5.epia9gcq'
img = '.jciay5ix.tvf2evcx.oq44ahr5.lb5m6g5c.osz0hll6.nq7eualt.em5jvqoa.a21kwdn3'
menugeral = '.bo8jc6qi.p4t1lx4y.brjalhku'
itens_do_menu = '.bugiwsl0.fooq7fky'
itens_de_imagens = '._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1'


drive.get('https://web.whatsapp.com/')
texto = 'vazio'
num_imagem = 0

# menu de ajuda:
ajuda = '''Menu de ajuda do chatbot:
!q respondo qualquer pergunta que você quiser 
!oi respondo com (Olá, como posso ajudar?)
!hora respondo com a hora exata
!loto Escolha APENAS 1 (LOTOFÁCIL) OU 2(MEGASENA) / Quantidade de jogos (exemplo !loto 5 2)
E é só isso mesmo que eu faço'''

# confirma com o usuário se a página carregou:
input("Leu o Qr Code? (y/n) ")

# aperta na caixa de mensagem / escreve a mensagem / envia a mensagem (parâmetro 'a' deve receber a mensagem a ser enviada
def caixa_de_mensagem(a):
    digitar = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, box_msg)))
    digitar.send_keys(a)
    digitar.send_keys('''
    ''')
    # confirmar = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, enviar)))
    # confirmar.click()

def abrir_conversa(e):
    e = e
    while True:
        try:
            e.click()
            break
        except:
            continue


def get_blob_content(driver, blob_url):
    result = driver.execute_async_script("""
        var blob_url = arguments[0];
        var callback = arguments[1];
        var xhr = new XMLHttpRequest();
        xhr.open('GET', blob_url, true);
        xhr.responseType = 'blob';
        xhr.onload = function(e) {
            if (this.status == 200) {
                var blob = this.response;
                var reader = new FileReader();
                reader.onload = function() {
                    callback(reader.result);
                };
                reader.readAsDataURL(blob);
            }
        };
        xhr.send();
    """, blob_url)
    return result



# verifica constantemente as últimas mensagens recebidas e caso a mensagem seja uma das chaves definidas uma ação será executada
while True:
    try:
        msg = WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ler)))
        for e in msg:
            try:
                texto = e.text
                # time.sleep(0.1)
                # print(texto)

                if texto == '!oi':
                    print(texto)
                    abrir_conversa(e)
                    time.sleep(2)
                    caixa_de_mensagem('Olá, como posso ajudar?')

                elif texto[0: 2] == '!q':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(gerar_resposta(texto))

                elif texto[0: 5] == '!help':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(ajuda)

                elif texto[0: 5] == '!hora':
                    data_e_hora_atuais = datetime.now()
                    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M'")
                    print(data_e_hora_atuais.strftime("Hoje é dia %d/%m/%Y e são: %H:%M' "))
                    abrir_conversa(e)
                    caixa_de_mensagem(data_e_hora_atuais.strftime("Hoje é dia %d/%m/%Y e são: %H:%M' "))

                elif texto[0: 6] == '!clima':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem(clima.clima_estado(texto[7:]))

                elif texto[0: 8] == '!discord':
                    print(texto)
                    abrir_conversa(e)
                    caixa_de_mensagem('Nosso discord oficial é https://discord.gg/G9mqwq9E')

                elif texto[0: 5] == '!loto':
                    print(texto)
                    abrir_conversa(e)
                    if len(texto) == 9:
                        print(texto[6])
                        print(texto[8])
                        if texto[6].isnumeric():
                            if texto[8].isnumeric():
                                caixa_de_mensagem(lotobot.sortear(int(texto[6]), int(texto[8])))
                            else:
                                caixa_de_mensagem('Escreva conforme exemplo: !loto 5 2) Usando somente números')
                        else:
                            caixa_de_mensagem('Escreva conforme exemplo: !loto 6 2) Usando somente números')
                    else:
                        caixa_de_mensagem('Escreva conforme exemplo: !loto 7 2) Usando somente números')

                elif texto[0:8] == '!sticker':
                    print(texto)
                    abrir_conversa(e)
                    time.sleep(2.5)
                    try:
                        imagens = WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, img)))
                        time.sleep(1)

                        #for c in imagens:
                            # Obter o valor de um atributo
                            #try:
                                #tag = c.get_attribute('alt')
                                #print(tag)
                                #src = c.get_attribute('src')
                              #  print(f'SRC: {src}')
                        c = imagens[-1]
                        tag = c.get_attribute('alt')
                        src = c.get_attribute('src')
                        try:
                            if tag == texto:
                                caixa_de_mensagem('⏳Um momento⏳')

                                c.click()
                                num_imagem += 1
                                # png = c.screenshot_as_png
                                # imgem = Image.open(io.BytesIO(png))
                                # imgem.save(f'imagens para fig/imagem{num_imagem}.png')
                                opçao_da_imagem = WebDriverWait(drive, 10).until(
                                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, itens_de_imagens)))
                                for i_d_m in opçao_da_imagem:
                                    if i_d_m.get_attribute('title') == 'Baixar':
                                        i_d_m.click()
                                        time.sleep(1.5)
                                        keyboard = Controller()
                                        keyboard.type(f"D:\\novochatbot\\imagens para fig\\imagem{num_imagem}.png")
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        time.sleep(1.5)
                                        for i_d_m in opçao_da_imagem:
                                            if i_d_m.get_attribute('title') == 'Fechar':
                                                i_d_m.click()

                                        # urllib.request.urlretrieve(src, f"nome_da_imagem{num_imagem}.png")
                                        print('salvo')
                                        # time.sleep(1)
                                        seletor = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, menugeral)))
                                        seletor.click()
                                        time.sleep(1)
                                        opçao_do_seletor = WebDriverWait(drive, 10).until(
                                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, itens_do_menu)))
                                        opcao = opçao_do_seletor[-1]

                                        opcao.click()
                                        time.sleep(1.5)
                                        keyboard = Controller()
                                        keyboard.type(f"D:\\novochatbot\\imagens para fig\\imagem{num_imagem}.png")
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)
                                        time.sleep(1.5)
                                        keyboard.press(Key.enter)
                                        keyboard.release(Key.enter)

                        except:
                            print('não foi possível concluir')




                    except:
                        print('não foi possível obter')


                    if len(imagens) == 0:
                        print('imagens não encontradas')



            except StaleElementReferenceException:
                continue
    except NoSuchElementException:
        print("Elemento não encontrado. Continuando...")
        continue
