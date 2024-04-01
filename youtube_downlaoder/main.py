import pytube


url=input("Lütfen indirmek istediğiniz video linkini yazınız:")
path=""
video=pytube.YouTube(url).streams.get_highest_resolution().download(path)