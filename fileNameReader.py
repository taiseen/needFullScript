# 15 Aptil 2022

import os

fileNameRead = os.listdir('.')

jpg = '.jpg'
png = '.png'

fileNameContailer = []

for file in fileNameRead:
    
     if file.endswith( jpg ) :
     
        jpgFile = file.replace( jpg, '' ).replace( '-' , '' )
        
        fileNameContailer.append( jpgFile )
        outPut = "import {} from '../assets/{}'; ".format( jpgFile, file )
        print( outPut )
        
     elif file.endswith(png) :
     
        pngFile = file.replace( png , '' ).replace( '-' , '' )
        
        fileNameContailer.append( pngFile )
        outPut = "import {} from '../assets/{}'; ".format( pngFile, file )
        print( outPut )        


for fileName in fileNameContailer :
    print(fileName,',')

