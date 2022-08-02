from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(f"INFO:\n{yt.title} By: {yt.author}, Views: {yt.views}\n{yt.description}")

video = yt.streams.get_highest_resolution()
print(f"\n\nDownloading Video: {yt.title}")
video.download(argv[2])