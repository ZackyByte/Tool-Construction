#!/usr/bin/python3
# Filename: m3p1.py
# Author: Zachary Milne
# Course: ITSC203
# Scenario: You have encountered an executable file (strange.exe). There are multiple users this program will ask you to log in as.
# Each user has a uniqe password.
# there are 5 messages for success and 5 for failure after a password attempt.
# You MUST use the pexpect module.
# Program must determine how many users are available to log in.
# Program must print the message about access strings presented by the strange program.
# Determine if other passwords will gain access.
# Keep track of user and password combinations used. 
import pexpect
import random
import string
jtru = 'jtru.txt'
boba = 'boba.txt'
rgin = 'rgin.txt'

names = []
messages =[]
for x in range(50):                        #this runs 50 times to populate names and messages. no passwords are sent. 
    child = pexpect.spawn("/bin/bash")          
    child.sendline("./strange")
    child.expect('\r')
    child.sendline('')
    child.expect('password')
    output= ''
    output = child.before.decode()          #this helps us split but child.readline is easier. 
    output = output.split(' ')              #split so we can get a list of users
    child.expect('\r')
    message = (child.readline())  
    print(message)                          #this prints the message for fun
    messages.append(message)                #append current message to list
    names.append(output[3])                 #append current name to list
    print(output[3])                        
    while True:
        try:
            names.remove('enter')              #sometimes output split in a way that 'enter' is added to names.
        except ValueError:
            break                           
users = set(names)                             #set to print only unique items
messagecheck= set(messages)
print(users)
print(messagecheck)

while True:                                     #runs til the end of days.
    child = pexpect.spawn("/bin/bash")          #some code repeated for convenience. 
    child.sendline("./strange")
    child.expect('\r')
    child.sendline('')
    child.expect('password')
    output= ''
    output = child.before.decode()
    output = output.split(' ')
    length=random.randint(3,20)         #assuming pass atleast 3 characters and less than 20
    password = (''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    if "bobama's" == output[3]:
        file = open(boba, "r+")
        contents = file.read()
        if password in contents:
            break      
        else:
            child.sendline(password)
            file.write(password+'\n')            
        file.close()
    elif "rbginsburg's" == output[3]:  #write passwords to files and check if duplicate
        file = open(rgin, "r+")
        contents = file.read()
        if password in contents:
            break      
        else:
            child.sendline(password)
            file.write(password+'\n')            
        file.close()
    elif "jtrudeau's" == output[3]:
        file = open(jtru, "r+")
        contents = file.read()
        if password in contents:
            break      
        else:
            child.sendline(password)
            file.write(password+'\n')            
        file.close()
    child.expect('\r')
    message = (child.readline())
    if message not in messagecheck:   #since we have populated messages earlier, we can check if a success message was found against
        print(message)                #the messages for failure
        input = print("There was a new message found, likely indicating a successful log in. print to success.txt?: y/n? ")
        while input == 'y':
            file = open('success.txt', 'w') #theoretically writes name and pass to file success.txt if found.
            file.write(output[3] + password)
            file.close()
        while not input == 'y':
            break                    
    messages.append(message)
    names.append(output[3])
    print(output[3])
    print(password)
 




# with open("filename", "r+") as file:
#     for line in file:
#         if needle in line:
#            break
#     else: # not found, we are at the eof
#         file.write(needle) # append missing data

