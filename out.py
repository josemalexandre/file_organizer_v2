import os

path = os.getcwd()

folders = [i for i in os.listdir(path) if os.path.isdir(i)]

for i in folders:
    for j in os.listdir(i):
        from_path = os.path.join(path, i, j)
        to_path = os.path.join(path, j)
        os.rename(from_path, to_path)
    os.rmdir(i)
