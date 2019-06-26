# Page-Flipper
A python application that automatically flips a score page according to the music being played

Before running requirments.txt, portaudio needs to be installed. The instructions for installation can be found at https://people.csail.mit.edu/hubert/pyaudio/

Install with pip install -r requirements.txt

This repository contains 4 programs: SheetVision, ListenNote.py, Music comparasion.py, and Prototype.py.

SheetVision is a program from GitHub that reads Sheet Music and converts it into Midi files. It can be found at https://github.com/cal-pratt/SheetVision. It has been modified to output a list of notes into the terminal. This program requires a .jpg file as its input. To run the program, download the files and run the program with one of the two .jpg files as an argument. The two .jpg files are the first and second pages of the test music scores. After running the program, the notes outputted are printed into SongData.txt. You can run the program on any .jpg file using the following terminal command:        
py main.py Any_File.jpg

ListenNote.py uses a package called aubio to listen to the data coming from the microphone and convert it to notes. Running the file in the terminal immediately activates the program. The program prints the data to the file called MusicData.txt, as well as outputs the notes into the terminal. However, this program is sometimes inaccurate, and makes many mistakes.

Music comparasion.py uses SongData.txt and MusicData.txt as its inputs, and attempts to sync them together. It simulates receiving the notes real-time, by running through every note from MusicData.txt, and attempts to locate the locations of every note.

Prototype.py combines ListenNote.py with Music comparasion.py. It listens to the realtime data and convert it into notes, which are used to track the location on the page. When this location reaches the end of the page, it opens up the second page of the music scores.

To run ListenNote.py, Music comparation.py, or Prototype.py, go to the appropriate directory and enter:

py ProgramName.py
