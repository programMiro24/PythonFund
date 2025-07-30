import re

example_text = "Hello 123 world 456"

match = re.search(r'\d+', example_text)
print(match.group())
