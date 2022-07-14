### Regex project

# Use python to read the file regex_test.txt and print the last name on each line using 
# regular expressions and groups (return None for names with no first and last name, 
# or names that aren't properly capitalized)
##### Hint: use with open() and readlines()

import re

f = open("files2/regex_test.txt")
data = f.read()


pattern_name = re.compile('([A-Z][a-zA-Za-z]+) ([A-Z][A-Za-z]+)')

found_names = pattern_name.findall(data)

for name in data.split(','):
    match = pattern_name.search(name)
    if match:
        print(match.group())
        


# print(found_names)

f.close()
