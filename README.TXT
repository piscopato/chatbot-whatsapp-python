Projeto feito por Eduardo Souza :D

Antes de iniciar é necessário baixar :
1- selenium
2- webdriver
3- lib openai
4- pynput

versão utilizada do python: 3.12

1- Após iniciar o código será exibida uma janela do webdriver do google chrome mas você pode alterar para o navegador que desejar.
2- Após o ler o Qr code basta apertar o enter que o código começará a ser executado.
3- O bot lê todas as suas últimas mensagens recebidas em loop:
    while True:
        try:
            msg = WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ler)))
            for e in msg:
             try:
                texto = e.text
        No trecho acima ele pega todas a box das últimas mensagens de cada conversa e põe na lista 'msg'
        a lista é iterada pela variável 'e' e a variável 'texto' recebe o text dentro da box.




4- Caso o text da variável texto 'a última mensagem de uma conversa' seja uma chave dentro dos if/elif um trecho de código será executado:
    função: abrir_conversa(e) - abre a conversar. Exemplo de uso:
       if texto == '!oi':
            print(texto)
            abrir_conversa(e)
            caixa_de_mensagem('Olá, como posso ajudar?')

    No trecho acima, assim que o bot identificou que a última mensagem da conversa foi a chave "oi", foi executada a função abrir_conversa(e) *(a variável 'e' é descrito no item 3)

5- função caixa_de_mensagem(a) abre a caixa de mensagem, escreve o que foi inserido na variável 'a' e envia. Exemplo de uso:
        caixa_de_mensagem('Olá, como posso ajudar?')

6- a função de criar figurinhas por enquanto só funciona com imagens devido a uma limitação do próprio whatsapp web.


