data_dict = {}
with open("majors.txt", 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 3:
            key = parts[0]
            value = " ".join(parts[1:3])
            data_dict[key] = [value]
