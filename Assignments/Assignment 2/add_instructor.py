import sys
from lxml import etree

def add_instructor(instructor_id, instructor_name, department):
    # Load the XML database
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        # Create a new XML tree if the file doesn't exist
        root = etree.Element("database")

    # Check if the student already exists
    existing_student = root.find(f".//instructor[@id='{instructor_id}']")
    if existing_student is not None:
        print(f"Instructor with ID '{instructor_id}' already exists. Not adding a duplicate.")
        return

    # Create a new student element
    instructor = etree.Element("instructor")
    instructor.set("id", instructor_id)
    instructor.text = instructor_id
    
    name = etree.SubElement(instructor, "name")
    name.text = instructor_name
    
    program_elem = etree.SubElement(instructor, "department")
    program_elem.text = department

    # Append the new student to the root
    students_section = root.find("instructors")
    students_section.append(instructor)

    # Save the updated database
    tree = etree.ElementTree(root)
    tree.write("hw2.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_instructor.py <instructor_id> <instructor_name> <department>")
    else:
        instructor_id, instructor_name, department = sys.argv[1], sys.argv[2], sys.argv[3]
        add_instructor(instructor_id, instructor_name, department)
