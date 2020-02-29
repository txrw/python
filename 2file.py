#!/usr/bin/pytyhon
# conding=utf8
import re
new_file = []

file1 = open("file1.txt","r")
for x in file1:
    if x not in new_file:
        new_file.append(x)
    else:
        print(x)

file2 = open("file2.txt","r")
for y in file2:
    if y not in new_file:
        new_file.append(y)
    else:
        print(y)

f = open('2file_repeate_result.txt', 'a+')
f.writelines(new_file)
f.close()
file1.close()
file2.close()
