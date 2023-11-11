import sys
import csv

def insert_record(filename, id, name, gender):
    # Check if the primary key already exists
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0 and row[0] == id:
                print(f"Record with id {id} already exists. Insertion failed.")
                return
            if len(name) > 20:
                print(f"Length of name with id {id} is more than 20. Insertion failed.")
                return
            if len(gender) > 1:
                print(f"Length of gender with id {id} is more than 1. Insertion failed.")
                return

    # Insert the new record
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, gender])
    print("Record inserted successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 insert.py <id> <name> <gender>")
        sys.exit(1)

    filename = "person.csv"
    id, name, gender = sys.argv[1], sys.argv[2], sys.argv[3]
    insert_record(filename, id, name, gender)



