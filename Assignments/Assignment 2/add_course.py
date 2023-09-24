import sys
from lxml import etree

def course_exists(course_number, semester, root):
    # Check if the course already exists with the same course number and semester
    courses = root.find("courses")
    for course in courses.findall("course"):
        number = course.find("number").text
        semesters = [semester.text for semester in course.findall("semester")]
        
        if number == course_number and semester in semesters:
            return True

    return False

def add_course(course_number, course_title, semester):
    # Load the XML database
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        # Create a new XML tree if the file doesn't exist
        root = etree.Element("database")

    # Check if the course already exists with the same course number and semester
    if course_exists(course_number, semester, root):
        print(f"Error: Course {course_number} for semester {semester} already exists. Skipping.")
        return

    # Create a new course element
    course = etree.Element("course")
    
    number = etree.SubElement(course, "number")
    number.text = course_number
    
    title = etree.SubElement(course, "title")
    title.text = course_title
    
    semester_elem = etree.SubElement(course, "semester")
    semester_elem.text = semester

    # Append the new course to the root
    courses_section = root.find("courses")
    courses_section.append(course)

    # Save the updated database
    tree = etree.ElementTree(root)
    tree.write("hw2.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_course.py <course_number> <course_title> <semester>")
    else:
        course_number, course_title, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        add_course(course_number, course_title, semester)
