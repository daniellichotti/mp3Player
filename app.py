from python_play.player import play_it
from pytube import YouTube
import pygame
import time
from pydub import AudioSegment
from pydub.playback import play


def baixar_video(url, caminho_saida):
    from pytube import YouTube

    # Criar uma instância do objeto YouTube
    yt = YouTube(url)

    # Obter a melhor qualidade de vídeo disponível
    video = yt.streams.get_highest_resolution()

    # Baixar o vídeo
    video.download(output_path=caminho_saida)

    print("Download de vídeo concluído!")


def baixar_audio(url, caminho_saida):
    try:
        # Criar uma instância do objeto YouTube
        yt = YouTube(url)

        # Obter a melhor qualidade de áudio disponível
        audio = yt.streams.filter(only_audio=True).first()

        # Baixar o áudio
        audio.download(output_path=caminho_saida)

        print("Download de áudio concluído!")

    except Exception as e:
        print(f"Erro: {str(e)}")


def tocar_audio(caminho_musica):
    play_it(caminho_musica)


def tocar_audio2(caminho_arquivo):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            # Aguardar até que a reprodução termine
            time.sleep(1)

    except Exception as e:
        print(f"Erro: {str(e)}")

    finally:
        pygame.mixer.quit()
        pygame.quit()


def tocar_audio_pydub(caminho_arquivo):
    audio = AudioSegment.from_file(caminho_arquivo, format="mp4")
    play(audio)


def converter_mp4_para_wav(caminho_entrada, caminho_saida):
    audio = AudioSegment.from_file(caminho_entrada, format="mp4")
    audio.export(caminho_saida, format="wav")
    return caminho_saida


def tocar_audio_pydub(caminho_arquivo):
    audio = AudioSegment.from_file(caminho_arquivo, format="wav")
    play(audio)


# Substitua 'https://www.youtube.com/watch?v=VIDEO_ID' pela URL real do vídeo do YouTube
# e 'caminho/do/seu/diretorio' pelo diretório onde você deseja salvar o áudio
url = 'https://www.youtube.com/watch?v=h0ffIJ7ZO4U'
caminho_saida = 'music/'
caminho_musica = 'music/Sultans Of Swing Video.mp4'


# Substitua 'caminho/do/seu/arquivo.mp4' pelo caminho real do seu arquivo MP4
caminho_arquivo_mp4 = 'music/Sultans Of Swing Video.mp4'
caminho_arquivo_wav = 'music/Sultans Of Swing Video.wav'

# Converter MP4 para WAV
converter_mp4_para_wav(caminho_arquivo_mp4, caminho_arquivo_wav)

# Tocar o áudio convertido
tocar_audio_pydub(caminho_arquivo_wav)
