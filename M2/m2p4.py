#!/usr/bin/python3
# Filename: m2p2.py
# Author: Zachary Milne
# Course: ITSC203
# Details: Write code that will generate a list of all possible IP Address (including the subnet network address and subnet broadcast address).
# Do not use third party modules. IP's: 10.110.16.128/26, 10.110.17.128/26. 
# The output should have the following format:
    #Subnet Network Address: 10.110.XX.XX
    #Subnet First Address: 10.110.XX.XX
    #Subnet Last Address: 10.110.XX.XX

import sys


addr = [0, 0, 0, 0]
mask = [0, 0, 0, 0]
cidr = 0
    
if len(sys.argv) == 2:
    (addr, cidr) = sys.argv[1].split('/')    #split slash notation
    addr = [int(x) for x in addr.split(".")] #split and int, or splint, the octets
    cidr = int(cidr)                         
    mask = [( ((1<<32)-1) << (32-cidr) >> i ) & 255 for i in reversed(range(0, 32, 8))]  #make all 1's, shift with bit length of cidr, shift with position i to AND 255. 
                                                                                         #generate octets for mask
netw = [addr[i] & mask[i] for i in range(4)]                                            
bcas = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]                                     
hnum = (2**(32 - cidr)) 

counter = 1
for ip in range(hnum): #printing Ip's in range breaks if you go below /25, number of hosts will still calculate correctly for lower slash notations.
    print("{0}".format('.'.join(map(str, addr))), end="\t")
    (addr[3]) += 1
    if counter == 1:
        first = format('.'.join(map(str, addr)))
    if counter % 8 == 0:            
        print("")      
    if counter %2 == 1:
        last = format('.'.join(map(str, addr)))
    counter += 1

print("\nAddress:     {0}".format('.'.join(map(str, addr))))
print("Mask:      {0}".format('.'.join(map(str, mask))))
print("Cidr:                   {0}".format(cidr))
print("Network:     {0}".format('.'.join(map(str, netw))))
print("Broadcast:   {0}".format('.'.join(map(str, bcas)))) 
print("First IP:   ", first)
print("Last IP:    ", last)
print("Number of Hosts: {0}".format(int(hnum)-2))




