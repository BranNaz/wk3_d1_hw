### Regex project

# Use python to read the file regex_test.txt and print the last name on each line using 
# regular expressions and groups (return None for names with no first and last name, 
# or names that aren't properly capitalized)
##### Hint: use with open() and readlines()

import re

with open("files2/regex_test.txt")as f:
    data = f.readlines()


pattern_name = re.compile('([A-Z][a-zA-Za-z]+) ([A-Za-z]+)')

for name in data:
    match = pattern_name.search(name)
    if match:
        print(match.group())
    else:
        print(None)
        


f.close()
