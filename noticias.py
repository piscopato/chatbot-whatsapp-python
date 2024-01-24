from bs4 import BeautifulSoup
import requests

def noticias_G1():
    site = requests.get('https://g1.globo.com/rj/rio-de-janeiro/ultimas-noticias/')
    soup = BeautifulSoup(site.text, 'html.parser')
    noticias = soup.find_all("a", "feed-post-link gui-color-primary gui-color-hover")
    novas = []
    for n in range(0, 5):
        # print(noticias[n])
        # print(f'Noticia : {noticias[n].text}')
        # print(f'Fonte : {noticias[n]['href']}')
        # print(' ')
        novas.append(f'Noticia : {noticias[n].text}\nFonte : {noticias[n]['href']}\n\n')
    novas = ''.join(novas)
    return novas


# print(noticias_G1())
