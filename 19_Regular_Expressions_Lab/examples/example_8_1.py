import re

example_text = "Hello 123 world 456"

new_text = re.sub(r'\d+', 'NUM', example_text)

print(new_text)
