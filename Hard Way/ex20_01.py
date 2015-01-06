from sys import argv

script, file_name = argv

def print_a_line(line):
    print line.readline()

file_open = open(file_name)

print_a_line(file_open)
print_a_line(file_open)
print file_open.readline(6)

