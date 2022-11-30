import re

search_term = r'www\.[a-zA-Z0-9-\.]+\.[a-z]+'

sites_list = []
text = input()
while text:
    result = re.search(search_term, text)
    if result:
        sites_list.append(result.group(0))
    text = input()

for site in sites_list:
    print(site)