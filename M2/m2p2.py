# Filename: m2p2.py
# Author: Zachary Milne
# Course: ITSC203
# Details: Take a single CLI parameter and generate the output.
# Example Output:
    #File Name	: <filename>
    #File Path	: <absolute path of the file>
    #File Size	: 125 bytes
    #Inode		: 2356755
    #Last Mod	: Tues Jan 8 07:00:53	2019



import os
import time
import sys
workspace = " ".join(sys.argv[1:]) #I had to do this because I made a directory with a space in it, which seperates entries for argv
print("Printing file information for files in %s" % workspace) 
print("━"*len(workspace), "━"*70, sep='')
for path, dirs, files, in os.walk(workspace): #os.walk will go through everything in the directory
    for f in files:
        filePath = os.path.join(path, f)    #joining f to path for an absolute path
        fileStats= os.stat(filePath)        #give os.stat its own object to print inode
        timesinceEpoc = os.path.getmtime(filePath)
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timesinceEpoc)) # y/m/d format for time.
        print("filename:   ", f)
        print("File Path:  ", filePath)
        print("File Size:  ",fileStats.st_size, "Bytes")
        print("Inode:      ", fileStats.st_ino)
        print("Last Mod:   ", modificationTime)
        print("━"*len(workspace), "━"*70, sep='')