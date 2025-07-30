import re
n = int(input())
barcode_pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
for barcode_number in range(n):
    barcode = input()
    match = re.match(barcode_pattern, barcode)
    if match:
        product_group = re.findall(r'\d', barcode)
        if not product_group:
            product_group = '00'
        print(f"Product group: {''.join(product_group)}")
    else:
        print(f"Invalid barcode")
