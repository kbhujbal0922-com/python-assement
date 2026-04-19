import csv

# Base class for CSV handling
class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        """Reads CSV file and returns data as a list of dictionaries"""
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def write_csv(self, fieldnames, data):
        """Writes data (list of dicts) to CSV file"""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


# Derived class with extra functionality
class StudentCSV(CSVHandler):
    def __init__(self, filename):
        super().__init__(filename)

    def get_students_with_high_marks(self, threshold=80):
        """Return students scoring above threshold"""
        data = self.read_csv()
        return [student for student in data if int(student['Marks']) > threshold]


# Example usage
if __name__ == "__main__":
    # Writing sample data
    students = [
        {"Name": "Alice", "Marks": 85},
        {"Name": "Bob", "Marks": 72},
        {"Name": "Charlie", "Marks": 90}
    ]
    fieldnames = ["Name", "Marks"]

    handler = StudentCSV("students.csv")
    handler.write_csv(fieldnames, students)

    # Reading and filtering
    high_scorers = handler.get_students_with_high_marks(80)
    print("Students with marks above 80:")
    for student in high_scorers:
        print(student["Name"], "-", student["Marks"])
