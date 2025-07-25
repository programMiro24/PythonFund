import re

email = 'webbersoft@gmail.'

pattern_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(pattern_email, email):
    print(f'{email} е валиден имейл адрес!')
else:
    print(f'{email} не е валиден имейл адрес!')
