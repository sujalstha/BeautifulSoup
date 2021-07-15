import re

web_lis = []

with open("tf2 website text.txt", "r+") as file:
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        web_lis.append(line_list)

    file.close()

print(web_lis)


def remove_doublespace(string):
    if '  ' not in string:
        return string
    return remove_doublespace(string.replace('  ', ' '))
