from pytube import YouTube
from sys import argv
# import os

yt = YouTube('https://www.youtube.com/watch?v=Zd_Wsjq2ljc')
title = yt.title
artists = yt.
print(title)


link = argv[1]


yt = YouTube(link)


print("Title: ", yt.title)
print("Views: ", yt.views)


# yd = yt.streams.get_highest_resolution()

# yd.download("/home/kalimax/Music/MusicDownloads")
