import re

example_text = "cat mat bat example"
x = re.finditer("\\b\w{3}\\b", example_text)

for match in x:
    print(f'{match.group()} found at {match.start()} - {match.end()}')
