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

def init_major_dict(filename):
    major_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')  # Split columns by tab and remove leading/trailing spaces
            if len(parts) >= 3:
                key = parts[0].strip()
                major_abbrev = parts[1].strip()
                major_name = parts[2].strip()
                major_dict[key] = [major_abbrev, major_name]
    print(major_dict)
    return major_dict



def parse_text_to_data(text):
    data = []
    current_subject_designator = ""
    current_subject_name = ""
    current_course_id = ""
    lines = text.split('\n')
    line_num = 0
    major_dict = init_major_dict("majors.txt")
    section_dict = {}

    for line in lines:
        # print(line)
        line_num += 1
        # print(line_num)


        # Get [266 COMPUTER SCIENCES]
        subject_match = re.match(r'^(\d{3})([A-Z\s&]+)\sSection\s#.*$', line)
        if subject_match:
            major_id = subject_match.group(1).strip()
            major_abbrev = major_dict[major_id][0]
            current_subject_designator=major_abbrev
            subject_name = subject_match.group(2).strip()  # eg. COMPUTER SCIENCES
            current_subject_name = subject_name
       
        # Get COMP SCI [400]
        course_id_match = re.search(r'(\d+)$', line)
        if course_id_match:
            # Line looks like [001 190 3.384 36.3 19.5 36.8 3.7 1.6 2.1 .   .   .   .   .   .   .   .   .   .   400]
            temp_course_id = course_id_match.group(1).strip()
            current_course_id = temp_course_id
            # print(current_course_id)

        section_pattern = r'^(\d+)\s+(\d+)\s+(\d+\.\d{3})\s+([\d\s.]+)\s*(\d{3})\s*$'
        section_patt_match = re.match(section_pattern, line)
        if section_patt_match:
            section_id = section_patt_match.group(1).strip()
            section_num_enrolled = section_patt_match.group(2).strip()
            section_avg_gpa = float(section_patt_match.group(3).strip())
            grade_dists_str = section_patt_match.group(4).strip()
            temp_course_id = section_patt_match.group(5)
            grade_dists_list = grade_dists_str.split()[:-1]
            section_grade_dist = [float(num) if num != '.' else None for num in grade_dists_list]
            curr_section = {
                'Section ID': section_id,
                'Section Total': section_num_enrolled,
                'Average GPA': section_avg_gpa,  
                'Section Grade Dist': section_grade_dist,
            }
            key = (current_subject_designator, temp_course_id) # eg. (COMP SCI, 400)
            print(key)
            if key in section_dict:
                section_dict[key].append(curr_section)
            else:
                section_dict[key] = [curr_section]

        # Get [Course Total 654 32.4 25.7 29.1 7.2 2.1 2.8 0.6 .  .  .  .  .  .  .  .  0.2 3.322 Programming III]
        course_total_match = re.match(r'^Course Total\s+(\d+(?:\s+\d+|\.\d+)*)(.*?)\s(\d+\.\d{3})\s+([A-Z].*)$', line)
        if course_total_match:
            numbers_str = course_total_match.group(1).strip()  
            average_gpa = float(course_total_match.group(3).strip())
            course_title = course_total_match.group(4).strip()
            grade_dists = [float(num) if num != '.' else None for num in numbers_str.split()]
            course_total = grade_dists.pop(0)
            print((current_subject_designator, current_course_id))
            section_objects = section_dict.get((current_subject_designator, current_course_id), [])
            print(section_objects)
            course_data = {
                'Course Total': course_total,
                'Subject Designator': current_subject_designator,
                'Subject Name': current_subject_name,
                'Course ID': current_course_id,
                'Grades Dists': grade_dists,
                'Average GPA': average_gpa,  
                'Course Title': course_title,
                'Sections': section_objects,
                'Number of Sections': len(section_objects)
            }
            data.append(course_data)
            section_dict = {}
    return data

#


def print_json_output(data):
    print()
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
    output_path = 'sections.json'  # Update with your desired output path
    main(pdf_path, output_path)
