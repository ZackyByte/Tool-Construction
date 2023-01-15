#!/usr/bin/python3
# Filename: m3p1.py
# Author: Zachary Milne
# Course: ITSC203
# Details: Run createfiles.exe in a directory. Your program should enumerate the entire folder, present in a way that visualizes the structure. Create hashes of all the files in folders
# and subfolders. Create a folder for each type of extension found. Copy files to folder based on extension and rename as their hash value. Do not alter the original files.
import os
import hashlib
import shutil
copypath = '/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/Lab3Hashes'
BLOCK_SIZE = 65536
workspace = "/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/lab3/folder04e/"
for root, dirs, files in os.walk(workspace):                    #os.walk will go through everything in the directory
    path = root.split(os.sep)                                   #split up path
    length=len(path)                                            #length variable to print tree
    print('SUB',(length - 8) * '---', os.path.basename(root))   #print sub folders
    for file in files:
        filePath = os.path.join(root,file)                      #get path of file
        file_hash = hashlib.sha512()                            #create hash object
        with open(filePath, 'rb') as f:                         #open file             
            fb=f.read(BLOCK_SIZE)                               #read blocks at a time
            while len(fb) > 0:                                  
                file_hash.update(fb)                            #keep file_hash updated
                fb= f.read(BLOCK_SIZE)                          # read next block
            copyfname = file_hash.hexdigest()                   #create variable of hash
            fext = filePath.split('.')                          #split file extension
            fext = fext[1]                                      #updates fext to string
            copyfname = (copyfname + '.'+fext)                  #add ext back to filename            
            if os.path.isdir(copypath) == False:                #create dirs
                os.mkdir(copypath)
            copyfolder = (copypath +'/'+ fext +'/')             
            if os.path.isdir(copyfolder) == False:
                os.mkdir(copyfolder)
            if fext == fext:                                    #avoids making a bunch of IF statements based on EXT for files.
                shutil.copyfile(filePath,copyfolder+copyfname)  #copy file in filepath to destination
        print((length-9)* '---', file,'Hash:', file_hash.hexdigest())

#  'Hash:', file_hash.hexdigest()
# copypath = '/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/Lab3Hashes'

#print((len(path)-9 )* '---', file)
# file = ".\myfile.txt" # Location of the file (can be set a different way)
# BLOCK_SIZE = 65536 # The size of each read from the file
# file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
# with open(file, 'rb') as f: # Open the file to read it's bytes
#     fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
#     while len(fb) > 0: # While there is still data being read from the file
#         file_hash.update(fb) # Update the hash
#         fb = f.read(BLOCK_SIZE) # Read the next block from the file

# print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash