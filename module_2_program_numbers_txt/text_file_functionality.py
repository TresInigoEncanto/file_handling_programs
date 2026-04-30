class OddEvenSorter:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.even_filename = "even.txt"
        self.odd_filename = "odd.txt"
    
    def process_files(self):
        try:
            with open(self.input_filename, 'r') as source_file:
                numbers = [int(line.strip()) for line in source_file if line.strip()]
            
            with open(self.even_filename, 'w') as even_output, \
                 open(self.odd_filename, 'w') as odd_output:

                for num in numbers:
                    if num % 2 == 0:
                        even_output.write(f"{num}\n")
                    else:
                        odd_output.write(f"{num}\n")

            return True

        except FileNotFoundError:
             print(f"Could not find the file '{self.input_filename}'.")
             return False

        except ValueError:
            print("The file contains non-numeric data.")
            return False