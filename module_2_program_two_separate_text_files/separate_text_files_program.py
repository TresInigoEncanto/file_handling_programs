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
                

