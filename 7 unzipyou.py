import zipfile
import os
import re
'''
zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
zip_obj.extractall('The text file')
'''
# Reading the unzipped files
print(os.getcwd())

file_dir = 'D:\Gustav\Git\The text file'

for root,folder,file in os.walk(file_dir+'\\extracted_content'):
    print(root,folder,file)
    for fold in folder:
       
        for f in file:
     
            try:
                path_to_file = file_dir+'\\extracted_content'+'\\'+fold+'\\'+f
                print(os.listdir(path_to_file))
                print(path_to_file)
                with open(path_to_file+f,'r') as z:
                    x = re.search(r'\D{11}',z)
                    print(x)
            except FileNotFoundError:
                print(f"This file does not exist")
