import openai
from datetime import datetime




# openai.api_key = ''  # informe sua key de api do chatgpt



def gerar_resposta(question):
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M'")
    mensagens = [{"role": "system", "content": "Você é um assistente gente boa."}]
    mensagens.append({"role": "user", "content": str(f'{question}')})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=mensagens,
        temperature=0.5
    )
    return response.choices[0].message.content

# Exemplo de uso:
# question = "Qual é a capital do Brasil?"
# answer = gerar_resposta(question)
# print("User:", question)
# print("ChatGPT:", answer)


print(gerar_resposta('que dia é hoje?'))
