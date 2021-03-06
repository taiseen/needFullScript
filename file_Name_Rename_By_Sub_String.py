# 04 - March - 2021 

# python file_Name_Rename_By_Sub_String.py

import os

path = '.'
count = 0

file_formate = '.txt'

present_string = 'current_sub_string_name'

new_string = 'what_you_want_to_set'

for file in os.listdir(path) :

    if file.endswith(file_formate) :
    
        if file.find(present_string) > -1 :
        
            count+= 1
            
            os.rename(
            os.path.join(path, file), 
            os.path.join(path, file.replace(present_string, new_string)))

print("Total File :", count)


if count == 0 :
    print("No File has been Renamed...")


# END of Script
# Thank You! :)