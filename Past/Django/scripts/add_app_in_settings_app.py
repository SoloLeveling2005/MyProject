import os

os.chdir("../")
os.chdir("../")
os.chdir("../")

line_to_replace = 17 #the line we want to remplace
my_file = 'myfile.txt'

with open(my_file, 'r') as file:
    lines = file.readlines()
#now we have an array of lines. If we want to edit the line 17...

if len(lines) > int(line_to_replace):
    lines[line_to_replace] = 'The text you want here'

with open(my_file, 'w') as file:
    file.writelines( lines )