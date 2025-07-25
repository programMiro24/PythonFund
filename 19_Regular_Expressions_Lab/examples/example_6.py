import re

text = "The time is 56:45"
pattern = r'[0-5][0-9]'
result = re.findall(pattern, text)

print(result)
