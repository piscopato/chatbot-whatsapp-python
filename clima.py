import requests


def clima_estado(city):
    try:
        API_KEY = "9f441d521e13bc0ee295186fedc05e19" # informe sua key de api do openweather
        cidade = city
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        print(link)

        requisicao = requests.get(link)
        print(requisicao.json())
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        print(descricao, f"{temperatura:.1f}ºC")

        return (f'O clima em {cidade}: {descricao} com uma temperatura de {temperatura:.1f}ºC')

    except:
        return ('Não foi possível localizar o clima desse local. ')


# clima_estado('Rio de janeiro')
