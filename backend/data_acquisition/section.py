import json
import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page_number, page in enumerate(reader.pages):
        page_text = page.extract_text() 
        text += page_text + "\n"  # Appends text from each page with a newline for separation
    return text

def parse_text_to_data(text):
    data = []
    current_subject_designator = ""
    current_subject_name = ""
    current_course_id = ""
    lines = text.split('\n')
    accumulated_text = ""

    for line in lines:
        # print(line)

        accumulated_text += line + "\n"  # Append the line and a newline character
        pattern = r'GPAAA BBB CC D F S UC RN P IN W N R O t h e r(?: Summary by Level)?\s+\d+\s+(\D.*)'
        abrv_subject_name_match = re.search(pattern, accumulated_text, re.DOTALL)
        # print(accumulated_text)
        if abrv_subject_name_match:
            abrv_subject_name = abrv_subject_name_match.group(1).strip() if abrv_subject_name_match.group(1) is not None else "No subject name found"
            current_subject_designator = abrv_subject_name
            print("CURRENT SUBJECT DESIGNATOR:"+current_subject_designator)
            accumulated_text = ""  # Reset accumulated text once a match is found

        # Get [266 COMPUTER SCIENCES]
        subject_match = re.match(r'^(\d{3})([A-Z\s&]+)\sSection\s#.*$', line)
        if subject_match:
            subject_name = subject_match.group(2).strip()  # eg. COMPUTER SCIENCES
            current_subject_name = subject_name
       
        course_id_match = re.search(r'(\d+)$', line)
        if course_id_match:
            # print(subject_designator_match.group(1).strip())
            current_course_id = course_id_match.group(1).strip() 

        course_total_match = re.match(r'^Course Total\s+(\d+(?:\s+\d+|\.\d+)*)(.*?)\s(\d+\.\d{3})\s+([A-Z].*)$', line)
        if course_total_match:
            numbers_str = course_total_match.group(1).strip()  
            average_gpa = float(course_total_match.group(3).strip())
            course_title = course_total_match.group(4).strip()
            print(course_title)
            grade_dists = [float(num) if num != '.' else None for num in numbers_str.split()]
            course_total = grade_dists.pop(0)
            
            course_data = {
                'Course Total': course_total,
                'Subject Designator': current_subject_designator,
                'Subject Name': current_subject_name,
                'Course ID': current_course_id,
                'Grades Dists': grade_dists,
                'Average GPA': average_gpa,  
                'Course Title': course_title
            }
            data.append(course_data)
    return data

#


def print_json_output(data):
    prefixes = ['A:', 'AB:', 'B:', 'BC:', 'C:', 'D:', 'E:', 'F:']
    
    for course in data:
        print(f"Course Title: {course['Course Title']}")
        print(f"Course ID: {course['Subject Designator']} {course['Course ID']}")
        print(f"Total Students: {course['Course Total']}")
        print(f"Average GPA: {course['Average GPA']}")

        
        if course['Grades Dists']:
            for idx in range(min(len(course['Grades Dists']), len(prefixes))):
                number = course['Grades Dists'][idx]
                if number is not None:  # Check if number is not None before printing
                    print(f"{prefixes[idx]} {number}")  # Print with the prefix
                else:
                    print(f"{prefixes[idx]} N/A")  # Print N/A if there is no number
        else:
            print("No number data available.")
        
        print()  # Print


def save_to_json(data, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    data = parse_text_to_data(text)
    # print_json_output(data)
    save_to_json(data, output_path)

if __name__ == "__main__":
    pdf_path = 'fall23_md.pdf'
    # pdf_path = 'fall23.pdf'
    output_path = 'simple.json'  # Update with your desired output path
    main(pdf_path, output_path)
