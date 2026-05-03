import datetime

class MyDiary:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_entry(self):
        """Multi-line input loop as diary."""
        try:
            with open(self.filename, "a") as file:
                print(f"--- My Log Session: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ---")

                while True:
                    entry_line = input("Log your line: ")
                    file.write(entry_line + "\n")

                    choices = input("Are there more lines? y/n ").lower()
                    if choices != 'y':
                        print("My entry saved successfully.")
                        break
        except IOError as error:
            print(f"An error occured while writing the file: {error}")

if __name__ == "__main__":
    multiple_lines = MyDiary()
    multiple_lines.write_entry()
