filename = 'movies_line_by_line'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())