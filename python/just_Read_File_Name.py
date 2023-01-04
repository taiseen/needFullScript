# 06 - March - 2021

# python just_Read_File_Name.py

import os

#allFile = os.scandir('.')

allFile = os.listdir('.')

for fileName in allFile:
    
    indexNumber = fileName.find("s")    
    
    print("File Name :",fileName , "& find index is :", indexNumber)