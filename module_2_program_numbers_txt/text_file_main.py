from text_file_functionality import OddEvenSorter

def program_proper():
    print("--- Odd Even Sorter Program ---")

    sorter = OddEvenSorter("numbers.txt")

    success = sorter.process_files()

    if success:
        print("The numbers have been sorted into odd.txt and even.txt files.")

if __name__ == "__main__":
    program_proper()