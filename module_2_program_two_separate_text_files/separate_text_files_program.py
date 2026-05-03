import math

class IntegerSorter:
    def __init__(self, source_file="integers.txt"):
        self.source_file = source_file
        self.odd_file = "triple.txt"
        self.even_file = "double.txt"
    
    def number_sorter(self):
        """Program to read the integers and sort them based on parity."""
        try:
            with open(self.source_file, 'r') as source:
                integers = [int(line.strip()) for line in source if line.strip()]
            
            with open(self.odd_file, 'w') as odd, open(self.even_file, 'w') as even:
                for num in integers:
                    if num % 2 == 0:
                        sorted_number == num ** 2
                        even.write(f"{sorted_number}\n")
                    else:
                        sorted_number = num ** 3
                        odd.write(f"{sorted_number}\n")
            
            print(f"Sorting complete, check {self.odd_file} and {self.even_file}.")
            
        except FileNotFoundError:
            print(f"Error: {self.source_file} not found. Please create a '.txt' file first.")
        except ValueError:
            print("Error: The txt file contains non-integer data.")
        
        


