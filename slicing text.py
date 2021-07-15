import re
import io

web_lis = []

with io.open("tf2 website text.txt", "w", encoding="utf-8") as file:
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
