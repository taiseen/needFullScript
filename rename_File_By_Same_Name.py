# 06 - March - 2021 

# python rename_File_By_Same_Name.py 

import os

count = 0

file_formate = '.txt'

present_txt = 'ALL_READY_HAVE'
blank_spase = ' '

you_want = 'WHAT_YOU_WANT' + blank_spase


for idx, file in enumerate(os.listdir(".")) :

    if file.endswith(file_formate) :
    
        if file.find(present_txt) > -1 :
        
            count += 1
            idx += 1
            
            if( idx < 10) :
                os.rename( file , f"{you_want}0{idx} " + file_formate )
            else :
                os.rename( file , f"{you_want}{idx} " + file_formate )


print("\nTotal File :" , count)

if count == 0 :
    print("\nNo File has been Renamed...")


# End Of Script
# Thank You! :)