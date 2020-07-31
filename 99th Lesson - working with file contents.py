filename = 'movies_line_by_line'

with open(filename) as file_object:
    lines = file_object.readlines() #takes each line in file and puts it in list

for line in lines: #takes each line from 'lines' list
    print(line.strip())

print("\n------------------------------------------------\n")

popped_movie = lines.pop()

for line in lines:
    print(line.strip())

print("\n------------------------------------------------\n")

sorted_list = lines.sort()

for line in lines:
    print(line.strip())