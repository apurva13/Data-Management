import sys
from lxml import etree

def is_valid_input(instructor_id, course_number, semester, root):
    # Check if the instructor exists in the database
    instructor = root.find(f".//instructor[@id='{instructor_id}']")
    if instructor is None:
        return False, f"Instructor with ID '{instructor_id}' not found in the database."

    # Check if the course exists in the database for the specified semester
    courses = root.find("courses")
    course_exists = False
    for course in courses.findall("course"):
        number = course.find("number").text
        semesters = [s.text for s in course.findall("semester")]
        
        if number == course_number and semester in semesters:
            course_exists = True
            break

    if not course_exists:
        return False, f"Course '{course_number}' for semester '{semester}' not found in the database."

    return True, ""

def teach_course(instructor_id, course_number, semester):
    # Load the XML database
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        print("Error: Database not found.")
        return

    # Check if the 'schedule' section exists; if not, create it
    teachings_section = root.find("schedule")
    if teachings_section is None:
        teachings_section = etree.Element("schedule")
        root.append(teachings_section)

    # Check the validity of the input
    is_valid, error_message = is_valid_input(instructor_id, course_number, semester, root)
    if not is_valid:
        print(f"Error: {error_message}")
        return

    # Create a new teach element
    teach = etree.Element("teach")
    
    instructor_id_elem = etree.SubElement(teach, "instructor_id")
    instructor_id_elem.text = instructor_id
    
    course_number_elem = etree.SubElement(teach, "course_number")
    course_number_elem.text = course_number
    
    teaching_semester_elem = etree.SubElement(teach, "semester")
    teaching_semester_elem.text = semester

    # Append the teach to the 'schedule' section
    teachings_section.append(teach)

    # Save the updated database
    tree = etree.ElementTree(root)
    tree.write("hw2.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 teach_course.py <instructor_id> <course_number> <semester>")
    else:
        instructor_id, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        teach_course(instructor_id, course_number, semester)
