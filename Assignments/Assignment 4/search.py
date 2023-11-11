import sys
import csv

def search_records(filename, name):
    found_records = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == name:
                found_records.append(row)

    if found_records:
        print(f"Records with name '{name}':")
        for record in found_records:
            print(f"ID: {record[0]}, Name: {record[1]}, Gender: {record[2]}")
    else:
        print(f"No records found with name '{name}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 search.py <name>")
        sys.exit(1)

    filename = "person.csv"
    name = sys.argv[1]
    search_records(filename, name)
