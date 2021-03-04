# 04 - March - 2021 

# python _File_Renam_Script_.py

import os

path = '.'
count = 0

file_formate = '.txt'
present_string = 'Text Document'
new_string = ''

for file in os.listdir(path):
    if file.endswith(file_formate):
        if file.find(present_string) > -1:
            count+= 1
            os.rename(
            os.path.join(path, file), 
            os.path.join(path, file.replace(present_string, new_string)))

print("Total File : ", count)


if count == 0:
    print("No file has been found")


# END of Script
# Thank You! :)