from pytube import YouTube

def baixar_video(url, extension):
    youtube = YouTube(url)
    youtube.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first().download()
    print('Video Baixado com sucesso')
