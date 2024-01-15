# Importando as bibliotecas necessárias
import requests
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='en', target='pt')


def obter_informacoes_pokemon(nome_pokemon):
    # URL da API
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"

    # Fazendo a requisição para a API
    resposta = requests.get(url)

    # Verificando se a requisição foi bem sucedida
    if resposta.status_code == 200:
        # Convertendo a resposta para JSON
        dados_pokemon = resposta.json()

        # Extraindo as informações desejadas
        id_pokemon = dados_pokemon['id']
        nome_pokemon = dados_pokemon['name']
        altura_pokemon = dados_pokemon['height']
        peso_pokemon = dados_pokemon['weight']

        # Extraindo as habilidades do Pokémon
        habilidades = [habilidade['ability']['name'] for habilidade in dados_pokemon['abilities']]
        habilidades_pt = tradutor.translate(habilidades)

        # Extraindo os tipos do Pokémon
        tipos = [tipo['type']['name'] for tipo in dados_pokemon['types']]

        # Extraindo as estatísticas do Pokémon
        estatisticas = {estatistica['stat']['name']: estatistica['base_stat'] for estatistica in dados_pokemon['stats']}

        # Extraindo as informações das evoluções do Pokémon
        url_evolucoes = dados_pokemon['species']['url']
        resposta_evolucoes = requests.get(url_evolucoes)
        dados_evolucoes = resposta_evolucoes.json()
        url_cadeia_evolucoes = dados_evolucoes['evolution_chain']['url']
        resposta_cadeia_evolucoes = requests.get(url_cadeia_evolucoes)
        cadeia_evolucoes = resposta_cadeia_evolucoes.json()

        # Imprimindo as informações
        print(f"ID: {id_pokemon}")
        print(f"Nome: {nome_pokemon}")
        print(f"Altura: {altura_pokemon}")
        print(f"Peso: {peso_pokemon}")
        print(f"Habilidades: {', '.join(habilidades_pt)}")
        print(f"Tipos: {', '.join(tipos)}")

    else:
        return (f"Não foi possível obter informações sobre o Pokémon {nome_pokemon}.")

# Testando a função
obter_informacoes_pokemon('pikachu')
