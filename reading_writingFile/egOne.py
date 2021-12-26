import os
files_name = []

files_name.append(os.listdir())


for i in range(len(files_name)):
    filePath = os.getcwd()
    name = files_name[i]
    print(files_name[i])

