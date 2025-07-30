import re
text = 'Hello World'
result = re.findall(r'hello', text, re.IGNORECASE)
print(result)
