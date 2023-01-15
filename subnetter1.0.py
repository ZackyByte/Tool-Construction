#!/usr/bin/python3

# Filename: labx_px.py
# Author: Zachary Milne
# Course: ITSC203
 #IP subnetter that I wasn't allowed to submit because of the module. 


from ipaddress import IPv4Network

net = IPv4Network("10.110.16.128/26")
counter = 1                          # 0 caused problems with formatting
for addr in net:
    print(addr, end="\t")
    if counter % 8 == 0:             #formats 8x8 nicely
        print("")                   #newline
    broadaddr = addr                #broadcast addr is the last addr. when loop is done broadaddr will be the last addr.
    if counter == 1:
        subnetaddr = addr           #Network address is the first address. 
    if counter == 2:
        firstaddr = addr            #firstaddr is the first assignable IP/second address in range.
    if counter % 2 == 1:
        lastaddr = addr             #similar to broadaddr, will be the last assignable IP when loop is done
    counter += 1
print("\nNetwork Address:     ", subnetaddr, "\nFirst Usable Address:", firstaddr, "\nLast Usable Address: ", lastaddr, "\nBroadcast Address:   ", broadaddr)       
print('─'*125)
net = IPv4Network("10.110.17.128/26")  
counter = 1 
for addr in net:                          # A loop so nice, I did it twice.
    print(addr, end="\t")
    if counter % 8 == 0 and counter != 0:
        print("")
    broadaddr = addr
    if counter == 1:
        subnetaddr = addr
    if counter == 2:
        firstaddr = addr
    if counter % 2 == 1:
        lastaddr = addr
    counter += 1
print("\nNetwork Address:     ", subnetaddr, "\nFirst Usable Address:", firstaddr, "\nLast Usable Address: ", lastaddr, "\nBroadcast Address:   ", broadaddr)
print('─'*125)