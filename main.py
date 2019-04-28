#https://github.com/guoguo12/billboard-charts
import billboard
#https://pypi.org/project/PyLyrics/
from PyLyrics import *
#https://github.com/johnwmillr/LyricsGenius
import lyricsgenius
# Set api key
genius = lyricsgenius.Genius("0KOm32ykagdXVPBan93S4QMYRt80vo3j_VnJoRZaL4yS2hiQS53HwrD7eWnJCXdz")

# Get the songs from the top 100
chart = billboard.ChartData('hot-100')
successList = []
failureList = [] 
allLyrics = []
successCounter = 0
failureCounter = 0
# Run Lyric search through PyLyrics (lyrics.wiki)
for song in chart:
    try:
        parsedArtist = song.artist

        lyrics = PyLyrics.getLyrics(song.artist, song.title)
        allLyrics.append(lyrics)
        successList.append(song)
        successCounter += 1
    except:
        failureList.append(song)
        failureCounter += 1
# Number of Successes and Failures of PyLyrics
print("lyrics.wiki -> Successes: " + successCounter + "| Failures: " + failureCounter)
successCounter = 0
failureCounter = 0

# Run Failures through LyricsGenius (genius)
for song in failureList:
    try:
        foundSong = genius.search_song(song.title, song.artist)
        allLyrics.append(foundSong.lyrics)
        successCounter += 1
    except: 
        failureCounter += 1

# Number of Successes and Failures of Genius
print("genius -> Successes: " + successCounter + "| Failures: " + failureCounter)

# Check how many lyrics were actually fetched
print("Lyric Count: " + len(allLyrics))

# File writing
f = open("LyricsArchive.txt","w+")
for lyric in allLyrics:
    f.write(lyric + "\n==================================================================\n")
f.close()