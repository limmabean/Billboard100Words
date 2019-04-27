#https://github.com/guoguo12/billboard-charts
import billboard
#https://pypi.org/project/PyLyrics/
from PyLyrics import *
#https://github.com/johnwmillr/LyricsGenius


# Get the songs from the top 100
chart = billboard.ChartData('hot-100')
successList = [];
failureList = [];
successCounter = 0;
failureCounter = 0;
for song in chart:
    try:
        lyrics = PyLyrics.getLyrics(song.artist, song.title)
        successList.append(song)
        successCounter += 1
    except:
        failureList.append(song)
        failureCounter += 1
