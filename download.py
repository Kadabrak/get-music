import yt_dlp
import json
URLS = ["https://www.youtube.com/playlist?list=PLNBoDqHGQDfhPNBaKLcB6O0qM6ppiBwwV"]

ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'outtmpl': '/var/www/html/Musique/%(uploader)s/%(playlist)s/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
	ydl.download(URLS)
