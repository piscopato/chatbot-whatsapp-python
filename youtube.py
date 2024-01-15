from pytube import YouTube
import os
import re

def baixar_mp4(link, pasta, nome):
    try:
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=pasta, filename=nome)

        print('download completo')
    except:
        print('erro ao baixar')


def baixar_mp3(link, pasta):
    try:
        video = YouTube(link)
        stream = video.streams.get_audio_only()
        name_audio = re.sub(r'[\\/*?:"<>|]', "", video.title) + '.mp3'
        if name_audio in os.listdir(pasta):
            print('arquivo já existe')
        else:
            stream.download(output_path=pasta, filename=name_audio)

            print('download completo')
        return name_audio
    except Exception as e:
        print(f'erro ao baixar{e}')


# baixar_mp3('https://youtu.be/6wkhYPgdxPA?si=ARtLUYiHJf_CsO0s', 'D:\\novochatbot\\videos')
