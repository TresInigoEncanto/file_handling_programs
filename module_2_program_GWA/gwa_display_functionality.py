class StudentName:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

class GwaSorter:
    def __init__(self, filename):
        self.filename = filename

    def highest_gwa(self):
        highest_student = None

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    #The format is: Name, GWA
                    if line.strip():
                        parts = line.strip().split(',')
                        if len(parts) == 2:
                            name = parts[0].strip()
                            gwa = parts[1].strip()

                            current_student = StudentName(name, gwa)

                            if highest_student is None or current_student.gwa < highest_student.gwa:
                                highest_student = current_student
            
            return highest_student

