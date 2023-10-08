import yt_dlp
import json

ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'outtmpl': '/var/www/html/Musique/%(uploader)s/%(playlist)s/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

#with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#	ydl.download(URLS)
with open("playlist.txt",'r') as file:
	for i in file.readlines():
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download(i.strip())
