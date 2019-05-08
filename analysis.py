# File writing
f = open("LyricsArchive.txt", mode='r', encoding='utf8')
fullText = f.read()
while "[" in fullText and "]" in fullText:
    fullText =