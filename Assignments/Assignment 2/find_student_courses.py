import sys
from lxml import etree

def find_student_courses(student_id):
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        print("Error: Database not found.")
        return

    # Find the student with the given ID
    student = root.find(f".//student[@id='{student_id}']")
    if student is None:
        print(f"Student with ID '{student_id}' not found in the database.")
        return

    # Retrieve the student's name
    student_name = student.find("name").text

    # Retrieve the courses taken by the student
    courses = []
    enrollments = root.findall(".//enrollment")
    for enrollment in enrollments:
        enrollment_student_id = enrollment.find("student_id").text
        if enrollment_student_id == student_id:
            course_number = enrollment.find("course_number").text
            semester = enrollment.find("semester").text
            courses.append({"course_number": course_number, "semester": semester})

    # Create an XML document for the output
    output_root = etree.Element("student_courses")
    student_elem = etree.SubElement(output_root, "student")
    student_elem.set("id", student_id)
    student_name_elem = etree.SubElement(student_elem, "name")
    student_name_elem.text = student_name

    for course_info in courses:
        course_elem = etree.SubElement(student_elem, "course")
        course_number_elem = etree.SubElement(course_elem, "course_number")
        course_number_elem.text = course_info["course_number"]
        semester_elem = etree.SubElement(course_elem, "semester")
        semester_elem.text = course_info["semester"]

    # Print the XML output
    output_tree = etree.ElementTree(output_root)
    output_tree.write(sys.stdout.buffer, pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_student_courses.py <student_id>")
    else:
        student_id = sys.argv[1]
        find_student_courses(student_id)
