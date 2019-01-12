from rectangle import Rectangle

note_step = 0.0625

note_defs = {
     -4 : ("G5", 79),
     -3 : ("F5", 77),
     -2 : ("E5", 76),
     -1 : ("D5", 74),
      0 : ("C5", 72),
      1 : ("B4", 71),
      2 : ("A4", 69),
      3 : ("G4", 67),
      4 : ("F4", 65),
      5 : ("E4", 64),
      6 : ("D4", 62),
      7 : ("C4", 60),
      8 : ("B3", 59),
      9 : ("A3", 57),
     10 : ("G3", 55),
     11 : ("F3", 53),
     12 : ("E3", 52),
     13 : ("D3", 50),
     14 : ("C3", 48),
     15 : ("B2", 47),
     16 : ("A2", 45),
     17 : ("F2", 53),
}

class Note(object):
    def __init__(self, rec, sym, staff_rec, sharp_notes = [], flat_notes = []):
        self.rec = rec
        self.sym = sym

        middle = rec.y + (rec.h / 2.0)
        height = (middle - staff_rec.y) / staff_rec.h
        note_def = note_defs[int(height/note_step + 0.5)]
        self.note = note_def[0]
        self.pitch = note_def[1]
        if any(n for n in sharp_notes if n.note[0] == self.note[0]):
            #self.note += "#"
            self.pitch += 1
        if any(n for n in flat_notes if n.note[0] == self.note[0]):
            #self.note += "b"
            self.pitch -= 1


