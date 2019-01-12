
import pyaudio
import numpy as np
import aubio
import time


# define pyaudio callback
def process_frame(data, frame_count, time_info, status_flag):
    signal = np.frombuffer(data, dtype=np.float32)
    new_note = notes_o(signal)
    
    if (new_note[0] != 0):
        note=aubio.midi2note(int(new_note[0]))
        if(len(note)==2):
            note=note
        else:
            note=note[0]+note[2]
        Musicdata=open("Music data.txt","a")
        Musicdata.write(note+"\n")
        print(note)
        Musicdata.close()
    return ( data , pyaudio.paContinue)
    

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
                stream_callback=process_frame
                )



# setup pitch
win_s = 2048 # fft size
hop_s = buffer_size # hop size=buffer_size

notes_o = aubio.notes("default", win_s, hop_s, samplerate)
#The avaliable methods are those for onset detection: energy, hfc (default), complex, phase, wphase, specdiff, kl, mkl,specflux
# The notes output is a vector of length 3 containing: the midi note value, or 0 if no note was found, the note velocity, the midi note to turn off
notes_o.set_silence(-40)           #set notes detection silence threshold, in dB (default: -70)
notes_o.set_minioi_ms(10)         # set notes detection minimum inter-onset interval, in millisecond. The shortest interval between two consecutive onsets (default: 30ms?)
#notes_o.set_release_drop       set notes detection release drop level, in dB. If the level drops more than this amount since the last note started, the note will be turned off (default: 10).

# start pyaudio stream
stream.start_stream()

while stream.is_active() and not input():
    time.sleep(0.001)

stream.stop_stream()
stream.close()
p.terminate()
