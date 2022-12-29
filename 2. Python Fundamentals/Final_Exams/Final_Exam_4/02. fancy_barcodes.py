import re

count_of_barcodes = int(input())
pattern = r'[\@][\#]+([A-Z][A-Za-z0-9]{4,}[A-Z])[\@][\#]+'
digit_pattern = r'\d'
for sequence in range(count_of_barcodes):
    barcode_to_check = input()
    result = re.search(pattern, barcode_to_check)
    if result:
        resulting_barcode = result.group(1)
        digits = re.findall(digit_pattern, resulting_barcode)
        product_group = ""
        if digits:
            for digit in digits:
                product_group += digit
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
