from gwa_display_functionality import GwaSorter

def main_program():
    print("--- Top Student of the Class ---")
    sorter = GwaSorter("students.txt")
    top_student = sorter.highest_gwa()

    if top_student:
        print(f"The top student of the class is {top_student.name} with a General Weighted Average of {top_student.gwa}")

if __name__ == "__main__":
    main_program()