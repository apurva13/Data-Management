import sys
from lxml import etree

def find_instructor_courses(instructor_id):
    try:
        tree = etree.parse("hw2.xml")
        root = tree.getroot()
    except FileNotFoundError:
        print("Error: Database not found.")
        return

    # Find the instructor with the given ID
    instructor = root.find(f".//instructor[@id='{instructor_id}']")
    if instructor is None:
        print(f"Instructor with ID '{instructor_id}' not found in the database.")
        return

    # Retrieve the instructor's name
    instructor_name = instructor.find("name").text

    # Retrieve the courses taught by the instructor
    courses = []
    schedule = root.findall(".//teach")
    for teach in schedule:
        teaching_instructor_id = teach.find("instructor_id").text
        if teaching_instructor_id == instructor_id:
            course_number = teach.find("course_number").text
            semester = teach.find("semester").text
            courses.append({"course_number": course_number, "semester": semester})

    # Create an XML document for the output
    output_root = etree.Element("instructor_courses")
    instructor_elem = etree.SubElement(output_root, "instructor")
    instructor_elem.set("id", instructor_id)
    instructor_name_elem = etree.SubElement(instructor_elem, "name")
    instructor_name_elem.text = instructor_name

    for course_info in courses:
        course_elem = etree.SubElement(instructor_elem, "course")
        course_number_elem = etree.SubElement(course_elem, "course_number")
        course_number_elem.text = course_info["course_number"]
        semester_elem = etree.SubElement(course_elem, "semester")
        semester_elem.text = course_info["semester"]

    # Print the XML output
    output_tree = etree.ElementTree(output_root)
    output_tree.write(sys.stdout.buffer, pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_instructor_courses.py <instructor_id>")
    else:
        instructor_id = sys.argv[1]
        find_instructor_courses(instructor_id)
