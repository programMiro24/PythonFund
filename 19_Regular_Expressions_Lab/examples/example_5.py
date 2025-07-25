import re

text = "The ball is red and big"
pattern = r'(red|blue) and (big|small)'
result = re.findall(pattern, text)

print(result)
