import json
import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page_number, page in enumerate(reader.pages):
        page_text = page.extract_text() 
        # print(f"--- Start of Page {page_number + 1} ---")  # Print the start of a new page
        # for line in page_text.split('\n'):
            # print(line)  # Print each line extracted from the page
        text += page_text + "\n"  # Appends text from each page with a newline for separation
        # print(f"--- End of Page {page_number + 1} ---\n")  # Print the end of the current page
    return text

def parse_text_to_data(text):
    data = []
    current_subject_designator = ""
    lines = text.split('\n')
    for line in lines:
        # print(line)
        # This regex separates the course total numbers, GPA-like number, and course title
        match = re.match(r'^Course Total\s+(\d+(?:\s+\d+|\.\d+)*)(.*?)\s(\d+\.\d{3})\s+([A-Z].*)$', line)
        if match:
            numbers_str = match.group(1).strip()  # Capture the numbers as a string
            # The ignored sequence of dots and numbers (if any are present)
            dots_and_numbers = match.group(2).strip()
            # Capture the GPA-like number
            average_gpa = float(match.group(3).strip())
            # Capture the course title, which starts with a capital letter
            course_title = match.group(4).strip()
            
            # The rest of the parsing remains unchanged...
            numbers = [float(num) if num != '.' else None for num in numbers_str.split()]
            course_total = numbers.pop(0)
            
            course_data = {
                'Course Total': course_total,
                'Numbers': numbers,
                'Average GPA': average_gpa,  # New field for Average GPA
                'Course Title': course_title
            }
            data.append(course_data)
    return data

#


def print_json_output(data):
    # Define the prefix list for the Numbers. There are only 7 letters so it assumes there will be at most 7 numbers.
    prefixes = ['A:', 'AB:', 'B:', 'BC:', 'C:', 'D:', 'E:', 'F:']
    
    for course in data:
        print(f"Course Title: {course['Course Title']}")
        print(f"Total Students: {course['Course Total']}")
        print(f"Average GPA: {course['Average GPA']}")

        
        if course['Numbers']:
            for idx in range(min(len(course['Numbers']), len(prefixes))):
                number = course['Numbers'][idx]
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
    print_json_output(data)
    save_to_json(data, output_path)

if __name__ == "__main__":
    pdf_path = 'fall23.pdf'
    # pdf_path = 'fall23.pdf'
    output_path = 'simple.json'  # Update with your desired output path
    main(pdf_path, output_path)
