import sys
import subprocess

note_defs = {
     -4 : "g5",
     -3 : "f5",
     -2 : "e5",
     -1 : "d5",
      0 : "c5",
      1 : "b4",
      2 : "a4",
      3 : "g4",
      4 : "f4",
      5 : "e4",
      6 : "d4",
      7 : "c4",
      8 : "b3",
      9 : "a3",
     10 : "g3",
     11 : "f3",
     12 : "e3",
     13 : "d3",
     14 : "c3",
     15 : "b2",
     16 : "a2",
     17 : "f2"
}
notes = note_defs.items()

# Compares the note given with the notes in the song. Returns the location of the note
def findnote(note, songdata, location):
    if note==songdata[location]:
        return ["Exact match",location]
    for notepair in notes:
        if notepair[1] == note:
            notekey=notepair[0]
            if songdata[location]==note_defs[notekey+1] or songdata[location]==note_defs[notekey-1]:
                return ["1 note offset",location]
    if note==songdata[location-1]:
        location+=-1
        return ["1 backwards",location]
    if location<len(songdata)-1 and note==songdata[location+1]:
        location+=1
        return ["1 forward",location]

    return("NO MATCH",location)
    
def open_file(path):
    cmd = {'linux':'eog', 'win32':'explorer', 'darwin':'open'}[sys.platform]
    subprocess.run([cmd, path])

if __name__ == "__main__":
    #Opening files
    song=open("Song data.txt","rU")
    songData1=song.readlines()
    songData=[]
    for note in songData1:
        songData.append(note.rstrip())
    music=open("Music data.txt","rU")
    musicData1=music.readlines()
    musicData=[]
    for note in musicData1:
        musicData.append(note.rstrip())
    
    open_file("2PageTest-0.jpg")
    location=0
    #Run loop through every note in the MusicData(the data from ListenNote.py) to simulate getting notes from real-time.
    for note in musicData:
            findnoteResults=findnote(note, songData,location)
            location=findnoteResults[1]
            print(findnoteResults[0])
            print(location)
            print(note)
            location+=1
            if location==355:
                open_file("2PageTest-1.jpg")