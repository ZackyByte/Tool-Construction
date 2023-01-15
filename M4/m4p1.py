#!/usr/bin/python3
# Filename: m3p1.py
# Author: Zachary Milne
# Course: ITSC203
# Details: Read and parse contents of Linux /proc using a class. use atleast one getter and one setter method. must have printData method for the following:
#            name:           m04p01.py
#             pid:                2345 
#            ppid:                 340 
#             rss:    0xfffffffffffffL 
#          rsslim: 0xffffffffffffffffL 
#      start_code:            0x400000 
#        end_code:            0x6bb0f4 
#     start_stack:      0x7fffdd658190 
#      start_data:            0x8bbdc0 
#        end_data:            0x9303f4 
#       start_brk:           0x2872000 
#       arg_start:      0x7fffdd658661 
#         arg_end:      0x7fffdd65867d 
#       env_start:      0x7fffdd65867d 
#         env_end:      0x7fffdd658fec 

class LinuxProcess():
    def __init__(self,pid):                     #initialize class
        self.stat = '/proc/' + pid + '/stat'    # set path to stat
        self.status = '/proc/' + pid + '/status' #set path to status
        self.pid = pid                           #store pid entered.
    def get_Name(self):                          #name was in the status file, getter function to get name
        file = open(self.status, 'r')               
        procname = file.readline()
        procname = procname.split()
        self.name = procname[1]                 #open status for reading and store name which is on the first line
        file.close()
        return self.name                        
    def readfile(self):                         #reads and stores stat file into list, each attribute is pulled from an offset 
        file = open(self.stat, 'r')
        filetxt = file.read()
        filetxt = filetxt.split()
        self.ppid = filetxt[3]
        self.rss = filetxt[23]
        self.rsslim = filetxt[24]
        self.startcode = filetxt[25]
        self.endcode = filetxt[26]
        self.startstack = filetxt[27]  
        self.startdata =filetxt[44]
        self.enddata = filetxt[45]
        self.startbrk = filetxt[46]
        self.argstart = filetxt[47]
        self.argend = filetxt[48]
        self.envstart = filetxt[49]
        self.envend = filetxt[50]
    def printData(self):                        #prints hex data if required otherwise decimal.
        print(f"name:               {self.name}")
        print(f"pid:                {self.pid}")
        print(f"ppid:               {self.ppid}")
        print(f"rss:                {hex(int(self.rss))}")
        print(f"rsslim:             {hex(int(self.rsslim))}")
        print(f"start_code:         {hex(int(self.startcode))}")        
        print(f"end_code:           {hex(int(self.endcode))}")      
        print(f"start_stack:        {hex(int(self.startstack))}")    
        print(f"start_data:         {hex(int(self.startdata))}")       
        print(f"end_data:           {hex(int(self.enddata))}")     
        print(f"start_brk:          {hex(int(self.startbrk))}")     
        print(f"arg_start:          {hex(int(self.argstart))}")
        print(f"arg_end:            {hex(int(self.argend))}")
        print(f"env_start:          {hex(int(self.envstart))}")
        print(f"env_end:            {hex(int(self.envend))}")

pid = input("please enter a pid: ")                 #ask for pid
object = LinuxProcess(pid)                          #create object based on pid and class
LinuxProcess.get_Name(object)                       #run object through get_Name function
LinuxProcess.readfile(object)                       #run object through readfile function
LinuxProcess.printData(object)                      #Run object through printData function


