import re

phone = '+359876292882'
pattern_phone = r'^08[7-9]\d{7}'

if re.match(pattern_phone, phone):
    print(f"{phone} е валиден телефонен номер")
else:
    print(f"{phone} не е валиден телефонен номер")
