import re

with open("tf2 website text.txt", "w") as file:
    final = re.sub("\.", ".\n")


def remove_doublespace(string):
    if '  ' not in string:
       return string
    return remove_doublespace(string.replace('  ',' '))
