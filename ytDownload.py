from pytube import YouTube

# URL do vídeo do YouTube
url = "https://www.youtube.com/watch?v=auLBLk4ibAk"

# Criar uma instância do objeto YouTube
yt = YouTube(url)

# Obter a melhor qualidade de vídeo disponível
video = yt.streams.get_highest_resolution()

# Baixar o vídeo
video.download(output_path="music/")

print("Download concluído!")
