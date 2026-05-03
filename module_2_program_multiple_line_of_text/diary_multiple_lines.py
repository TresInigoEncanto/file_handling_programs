import datetime

class MyDiary:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_entry(self):
        """Multi-line input loop as diary."""
        try:
            with open(self.filename, "a") as file:
                print(f"--- My Log Session: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ---")