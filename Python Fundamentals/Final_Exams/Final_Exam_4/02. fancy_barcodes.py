import re

count_of_barcodes = int(input())

pattern = r'(@[#]+)([A-Z][a-z0-9]{4,}[A-Z]{1}\b)'
# pattern = r"@[#]+(?P<found_text>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+"
resulting_barcode = ""

for sequence in range(count_of_barcodes):
    barcode_to_check = input()
    barcode = re.search(pattern, barcode_to_check)
    print(barcode)
    # if barcode:
    #     resulting_barcode = barcode.group(2)
    # print(barcode)
    # if barcode_check:
    #     for digit in barcode_check:
    #         if




# for product_input in range(number_products):
#     bar_code = input()
#     find_result = re.finditer(pattern, bar_code)
#     found = False
#     for show in find_result:
#         found = True
#         result_print = ''.join(x for x in show["found_text"] if x.isdigit())
#         if result_print:
#             print(f"Product group: {result_print}")
#         else:
#             print(f"Product group: 00")
#     if not found:
#         print("Invalid barcode")