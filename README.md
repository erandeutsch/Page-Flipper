# Page-Flipper
A python application that automatically flips a score page according to the music being played

This repository contains 4 programs: SheetVision, ListenNote.py, Music comparasion.py, and Prototype.py.

SheetVision is a program from GitHub that reads Sheet Music and converts it into Midi files. It has been modified to also output a list of notes into the terminal. This program requires a .jpg file as its input. To run the program, download the files and run the program with one of the two .jpg files as an argument. The two .jpg files are the first and second pages of the test music scores. After running the program, the notes outputted are printed into SongData.txt. You can run the program on any .jpg file using the following terminal command:        
py main.py Any_File.jpg


ListenNote.py uses a package called aubio to listen to the data coming from the microphone and convert it to notes. Running the file in the terminal immediately activates the program. The program prints the data to the file called Music Data, as well as outputs the notes into the terminal. However, this program is very inaccurate, and constantly makes many mistakes.

Music comparasion.py uses SongData.txt and MusicData.txt as its inputs, and attempts to sync them together. It simulates receiving the notes real-time, by running through every note from MusicData.txt, and attempts to locate the locations of every note. This program has mostly worked when both files are similar, yet it cannot comprehend the irregularities of ListenNote.py. When given data from 
ListenNote.py, it usually loses track of the position and gives up.

Prototype.py attempts to combine ListenNote.py with Music comparasion.py. It attempts to listen to the realtime data and convert it into notes, which are used to track the location on the page. When this location reaches the end of the page, it opens up the second page of the music scores. However, it is not currently functioning, due to the function process_frame not recognising the location variable. This will hopefully be fixed in the next commits.
