import sys
from lxml import etree

def add_student(student_id, student_name, program):
    # Load the XML database
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        # Create a new XML tree if the file doesn't exist
        root = etree.Element("database")

    # Check if the student already exists
    existing_student = root.find(f".//student[@id='{student_id}']")
    if existing_student is not None:
        print(f"Student with ID '{student_id}' already exists. Not adding a duplicate.")
        return

    # Create a new student element
    student = etree.Element("student")
    student.set("id", student_id)
    student.text=student_id
    
    name = etree.SubElement(student, "name")
    name.text = student_name
    
    program_elem = etree.SubElement(student, "program")
    program_elem.text = program

    # Append the new student to the root
    students_section = root.find("students")
    students_section.append(student)

    # Save the updated database
    tree = etree.ElementTree(root)
    tree.write("hw2.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_student.py <student_id> <student_name> <program>")
    else:
        student_id, student_name, program = sys.argv[1], sys.argv[2], sys.argv[3]
        add_student(student_id, student_name, program)
