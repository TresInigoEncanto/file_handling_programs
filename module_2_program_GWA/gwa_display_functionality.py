class StudentName:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

class GwaSorter:
    def __init__(self, filename):
        self.filename = filename

    def highest_gwa(self):
        highest_student = None