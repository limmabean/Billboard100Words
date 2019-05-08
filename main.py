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
stringParseIndex = 0

# Parse song titles and song artists for better search
for song in chart:
    # Artist Parse
    if " Featuring " in song.artist:
        # Find index of Featuring and subString out the main artist
        stringParseIndex = song.artist.find("Featuring")
        song.artist = song.artist[0:stringParseIndex-1]
        print("Is artist " + song.artist + " correct? F")
    if " X " in song.artist or " x " in song.artist:
        # Find index of the X or x
        stringParseIndex = song.artist.find(" X ")
        if stringParseIndex == -1:
            stringParseIndex = song.artist.find(" x ")
        # subString the main artist out.
        song.artist = song.artist[0:stringParseIndex]
        print("Is artist " + song.artist + " correct? X")
    # Title Parse
    if " (" in song.title and ")" in song.title:
        stringParseIndex = song.title.find(" (")
        song.title = song.title[0:stringParseIndex]
        print("Is title " + song.title + " correct? ()")

# Run Songs through LyricsGenius (genius)
for song in chart:
    try:
        foundSong = genius.search_song(song.title, song.artist)
        allLyrics.append("{{" + song.title + " by " + song.artist + "}}" + "\n" + foundSong.lyrics)
        successCounter += 1
    except:
        failureCounter += 1

# TEST 10 VALUES
# for x in range(10):
#     song = chart[x]
#     try:
#         foundSong = genius.search_song(song.title, song.artist)
#         allLyrics.append(song.title + " by " + song.artist + "\n" + foundSong.lyrics)
#         successCounter += 1
#     except:
#         failureCounter += 1

#Number of Successes and Failures of Genius
print("genius -> Successes: " + str(successCounter) + " | Failures: " + str(failureCounter))

# Run Lyric search through PyLyrics (lyrics.wiki)
# for song in chart:
    # try:
        # parsedArtist = song.artist
        # if "Featuring" in song.artist:
            # Find index of Featuring
            # stringParseIndex = song.artist.find("Featuring")
            # Find the substring that only has the main artist
            # newArtistStr = song.artist[0:stringParseIndex-1]
            # lyrics = PyLyrics.getLyrics(song.artist, song.title)
        # elif "X" in song.artist:
            # Find index of Featuring
            # stringParseIndex = song.artist.find("Featuring")
            # Find the substring that only has the main artist
            # newArtistStr = song.artist[0:stringParseIndex - 1]
            # song.artist.find("X")
            # print(song.artist)
        # else:
        #     lyrics = PyLyrics.getLyrics(song.artist, song.title)
        # allLyrics.append(lyrics)
        # successList.append(song)
        # successCounter += 1
    # except:
    #     failureList.append(song)
    #     failureCounter += 1
# Number of Successes and Failures of PyLyrics
# print("lyrics.wiki -> Successes: " + str(successCounter) + " | Failures: " + str(failureCounter))
# successCounter = 0
# failureCounter = 0



# Check how many lyrics were actually fetched

# Print how many lyrics are in the Lyric List
print("Lyric Count: " + str(len(allLyrics)))

# File writing
f = open("LyricsArchive.txt", mode='w+', encoding='utf8')
for lyric in allLyrics:
    f.write(lyric + "\n")
f.close()