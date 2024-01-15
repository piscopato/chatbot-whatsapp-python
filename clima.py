import requests


emojis = {
"01d" : "☀️",
"01n" : "🌃",
"02d" : "🌤️",
"02n" : "🌌",
"03d" : "☁️",
"03n" : "☁️",
"04d" : "☁",
"04n" : "☁",
"09d" : "🌧️",
"09n" : "🌧️",
"10d" : "⛈️",
"10n" : "⛈️",
"11d" : "🌩️",
"11n" : "🌩️",
"13d" : "❄️",
"13n" : "❄️",
"50n" : "⛆",
"50d" : "⛆"
}


def clima_estado(city):
    try:
<<<<<<< HEAD
        API_KEY = "ab579498b7ef0e29244aadf8ddf129e5" # informe sua key de api do openweather
=======
        API_KEY = "" # informe sua key de api do openweather
>>>>>>> origin/main
        cidade = city
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        # print(link)

        requisicao = requests.get(link)
        # print(requisicao.json())
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        temperatura_maxima = requisicao_dic['main']['temp_max'] - 273.15
        temperatura_minima = requisicao_dic['main']['temp_min'] - 273.15
        sensa_term = requisicao_dic['main']['feels_like'] - 273.15
        umidade = requisicao_dic['main']['humidity']
        nuvem = requisicao_dic['clouds']['all']
        id_emoji = requisicao_dic['weather'][0]['icon']

        resposta = (f'''
cidade: {cidade.capitalize()}
clima:  {descricao}  
temperatura atual: {temperatura:.1f}ºC 
temperatura máxima: {temperatura_maxima:.1f}ºC 
temperatura minima: {temperatura_minima:.1f}ºC  
sensação térmica: {sensa_term:.1f}ºC   
umidadade: {umidade}%   
nebulosidade: {nuvem}% 
        ''')

        resposta_com_emoji = (f'''
cidade: {cidade.capitalize()}
clima: {emojis[id_emoji]} {descricao}  
temperatura atual:🌡️ {temperatura:.1f}ºC 
temperatura máxima: {temperatura_maxima:.1f}ºC 
temperatura minima: {temperatura_minima:.1f}ºC  
sensação térmica: 🥵 {sensa_term:.1f}ºC   
umidadade: 💧 {umidade}%   
nebulosidade: ☁ {nuvem}% 
''')

        return (resposta)

    except:
        return ('Não foi possível localizar o clima desse local. ')


print(clima_estado('Rio de janeiro'))
