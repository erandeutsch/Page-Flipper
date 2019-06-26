import sys
import pyaudio
import numpy as np
import aubio
import time
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

song=open("Song data.txt","rU")
songData1=song.readlines()
songData=[]
for note in songData1:
    songData.append(note.rstrip())

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

# define pyaudio callback
def process_frame(data, frame_count, time_info, status_flag, loc):
    signal = np.frombuffer(data, dtype=np.float32)
    new_note = notes_o(signal)
    if (new_note[0] != 0):
        note=aubio.midi2note(int(new_note[0]))
        if(len(note)==2):
            note=note
        else:
            note=note[0]+note[2]
        Musicdata=open("Music data.txt","a")
        #Musicdata.write(note+"\n")
        print(note)
        Musicdata.close()

        findnoteResults=findnote(note, songData,loc[0])
        loc[0]=findnoteResults[1]
        print(findnoteResults[0])
        print(loc[0])
        print(note)
        loc[0]+=1
        if loc[0]==289:#355:
            open_file("2PageTest2-1.jpg")
    return (data , pyaudio.paContinue)
# print(location)
# global locationObject
# locationObject=location
# return process_frame
    
location = [0]

# initialise pyaudio
p = pyaudio.PyAudio()
# open stream
buffer_size = 256
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 22050
stream = p.open(format=pyaudio.paFloat32,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size,
                stream_callback=lambda a,b,c,d: process_frame(a,b,c,d,location)
                )

# setup pitch
win_s = 2048 # fft size
hop_s = buffer_size # hop size=buffer_size
notes_o = aubio.notes("default", win_s, hop_s, samplerate)

notes_o.set_silence(-40)           
notes_o.set_minioi_ms(10)         

# start pyaudio stream
stream.start_stream()


open_file("2PageTest2-0.jpg")
while stream.is_active() and not input():
    time.sleep(0.001)



stream.stop_stream()
stream.close()
p.terminate()
