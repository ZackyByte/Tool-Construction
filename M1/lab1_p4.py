#!/usr/bin/python3

# Filename: lab1_p4.py
# Author: Zachary Milne
# Course: ITSC203
# Details: making a table

users = [['kenny rogers', '/home/users/KRogers'],['tony robbins', '/home/TRobbins'] , ['johnny cash', '/home/users/JCash'],['tito jackson', '/home/hut/TJackson'],['tim tzuyu', '/home/users/TTzuyu'], ['kareena kapoor', '/home/users2/KKapoor']]

length_name = len(users[5][0])
length_path = len(users[5][1])

print("+","-"*(length_name)," + ","-"*(length_path),"+")
for x in range(6):
    print("|", users[x][0].title(), " "*(length_name - len(users[x][0])), "|", (users[x][1].lower()), " "*(length_path -len(users[x][1])), "|")
    
print("+", "-"*(length_name), " + ", "-"*(length_path), "+")

