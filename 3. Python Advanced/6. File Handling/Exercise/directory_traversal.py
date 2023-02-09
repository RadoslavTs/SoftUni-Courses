import os

directory = input() # Should be just 'Example'
file_list = os.listdir(directory)

files_dict = {}
subfolder_list = []

for file in file_list:
    file_name = file.split('.')
    if len(file_name) == 1:
        subfolder_list.append(file_name[0])

if subfolder_list:
    items = []
    for folder in subfolder_list:
        items = os.listdir(f'{directory}/{folder}')
        file_list.remove(folder)
    for item in items:
        file_list.append(item)

for file in file_list:
    file_name = file.split('.')
    file_extension = []
    if len(file_name) > 1:
        file_extension = file.split('.')[1]
    else:
        subfolder_list.append(file_name)

    if file_extension not in files_dict.keys():
        files_dict[file_extension] = []
        files_dict[file_extension].append(file_name[0])
    else:
        files_dict[file_extension].append(file_name[0])

result = []

for key, value in sorted(files_dict.items(), key=lambda x: (x[0], x[1])):
    result.append(f'.{key}')
    for item in sorted(value):
        result.append(f'- - - {item}.{key}')

with open('report.txt', 'w') as file:
    file.write('\n'.join(result))