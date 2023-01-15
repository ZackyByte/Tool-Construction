#!/usr/bin/python3

# Filename: m2p1.py
# Author: Zachary Milne
# Course: ITSC203
# Details: generate sequence and find a substring
# Example Output:
    #Linux~$ Please enter a seq length and architecture: 45 4
    #Your generated sequence of length 45 is: 
    #Lajsdfpioqpeipqifposfadpqwierfasdfwepr1234
    #Please enter a substring: peip
    #Sub-sequence was found at offset: 10
    #Your pattern peip was not found anywhere else.

import string 
upper = string.ascii_uppercase
lower = string.ascii_lowercase
number = string.digits
sequence = ''
length, bytes = input("Enter a sequence length value between 100 to 1024 and either a 4 or 8 for byte length, seperated by a space: ").split()
while int(length) < 100 or int(length) > 1024:
    length = input("Please enter a value between 100 and 1024: ")
while not (int(bytes) == 4 or int(bytes) == 8):
    bytes = input(" Please enter either 4 or 8 for byte length: ")
    
print("you have chosen a sequence length of: \n", int(length))
print("You have chosen a byte length of: \n", int(bytes))
for cap in upper:
    for low in lower:
        for num in number:
            sequence = sequence + cap + low + num
for x in range(int(length)):
    print(sequence[x], end='')

if int(bytes) == 4:
    substr = input("\nplease enter a string of 4 characters from the sequence: ")
    while not((len(substr)) == 4):
        substr = input("enter 4 characters:")
        
if int(bytes) == 8:
    substr = input("\nplease enter a string of 8 characters from the sequence: ")
    while not((len(substr)) == 8):
        substr = input("enter 8 characters:")

offset = sequence.find(substr)
strcount = sequence.count(substr)

print("\nYour substring %s was found at offset %d and was counted %d times." % (substr, offset, strcount))
