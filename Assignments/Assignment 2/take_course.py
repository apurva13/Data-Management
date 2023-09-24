import sys
from lxml import etree

def is_valid_input(student_id, course_number, semester, root):
    # Check if the student exists in the database
    student = root.find(f".//student[@id='{student_id}']")
    if student is None:
        return False, f"Student with ID '{student_id}' not found in the database."

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

def take_course(student_id, course_number, semester):
    # Load the XML database
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        print("Error: Database not found.")
        return

    # Check if the 'enrollments' section exists; if not, create it
    enrollments_section = root.find("enrollments")
    if enrollments_section is None:
        enrollments_section = etree.Element("enrollments")
        root.append(enrollments_section)

    # Check the validity of the input
    is_valid, error_message = is_valid_input(student_id, course_number, semester, root)
    if not is_valid:
        print(f"Error: {error_message}")
        return

    # Create a new enrollment element
    enrollment = etree.Element("enrollment")
    
    student_id_elem = etree.SubElement(enrollment, "student_id")
    student_id_elem.text = student_id
    
    course_number_elem = etree.SubElement(enrollment, "course_number")
    course_number_elem.text = course_number
    
    enrollment_semester_elem = etree.SubElement(enrollment, "semester")
    enrollment_semester_elem.text = semester

    # Append the enrollment to the 'enrollments' section
    enrollments_section.append(enrollment)

    # Save the updated database
    tree = etree.ElementTree(root)
    tree.write("hw2.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 take_course.py <student_id> <course_number> <semester>")
    else:
        student_id, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        take_course(student_id, course_number, semester)
