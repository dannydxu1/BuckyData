import re

line = "002 206 3.155 21.4 22.3 37.4 11.7 4.9 1.0 1.5 .   .   .   .   .   .   .   .   .   354"

# Define the regex pattern
section_pattern = r'^(\d+)\s+(\d+)\s+(\d+\.\d{3})\s+([\d\s.]+)\s*\d+\s*$'
section_patt_match = re.match(section_pattern, line)

if section_patt_match:
    course_number = section_patt_match.group(1).strip()
    enrolled_students = section_patt_match.group(2).strip()
    average_gpa = float(section_patt_match.group(3).strip())
    grade_dists_str = section_patt_match.group(4).strip()

    # Remove the last element (400) from the space-separated grade distributions
    grade_dists_list = grade_dists_str.split()[:-1]

    # Convert the remaining grade distributions to a list
    grade_dists = [float(num) if num != '.' else None for num in grade_dists_list]

    print("Course Number:", course_number)
    print("Enrolled Students:", enrolled_students)
    print("Average GPA:", average_gpa)
    print("Grade Distributions:", grade_dists)
