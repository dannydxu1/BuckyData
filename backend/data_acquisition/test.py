import re

other_txt = """GradesAve
GPAAA BBB CC D F S UC RN P IN W N R O t h e r Summary by Level
266 COMP SCI
Freshmen 855 48.1 20.9 17.2 6.1 3.2 2.0 1.5 .  .  1.1 .  .  .  .  .  .  3.410"""

# Define the pattern to match the subject name following the specified sequence
# This pattern allows for optional digits followed by optional spaces before the subject name
pattern = r'GPAAA BBB CC D F S UC RN P IN W N R O t h e r Summary by Level\s*(\d*\s*\w+\s*\w*)'

# Perform the matching
match = re.search(pattern, other_txt, re.DOTALL)

# Check if a match is found
if match:
    # Extract the part after 'Summary by Level', which may include the course code
    following_text = match.group(1).strip()
    # Further split to separate the course code if it's there
    parts = following_text.split()
    # If there's a course code, it should be the first part, and the rest is the subject name
    if parts[0].isdigit():
        course_code = parts[0]
        subject_name = ' '.join(parts[1:])
    else:
        subject_name = following_text
else:
    subject_name = "No match found"

print(subject_name)  # Should print 'COMP SCI' or '266 COMP SCI' as appropriate
