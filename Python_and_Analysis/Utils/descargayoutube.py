from multiprocessing.spawn import import_main_path
import pytube
opcion=int(input("Opcion:\n 1 video \n 2 audio: "))
if opcion==1:
    url=input("video url: ")
    path="D:\Descargar youtube"
    pytube.YouTube(url).streams.get_highest_resolution().download(path) ##VIDEOS
if opcion==2:
    url=input("video url: ")
    path="D:\Descargar youtube"
    pytube.YouTube(url).streams.get_by_itag("140").download(path) ##AUDIOS
