import re

regex = r'\w+'
test_str = "any word character \n"
matches = re.finditer(regex, test_str)

for match in matches:
    print(match.group())
