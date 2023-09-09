import os

path = os.getcwd()

full_list = os.listdir()

file_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]

types = set(i.split('.')[1].upper() for i in file_list)

for file_type in types:
    os.mkdir(file_type)

for file in file_list:
    from_path = os.path.join(path, file)
    to_path = os.path.join(path, file.split('.')[1], file)
    os.replace(from_path, to_path)
