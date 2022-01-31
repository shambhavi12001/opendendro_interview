import csv
'''
This python program takes in the file name from the user and prints the header
or the first line of any CSV file on the terminal

file_name- used for taking in the csv file's name as an input from the user
inp- to create a file object of the csv file
lines- reads all the lines of the CSV file and stores it as a list
outp- takes in 1 or 2 to print either the header or the first line
'''

file_name = input("Enter CSV file name:\n")
inp = open(file_name, "r") 
while True:
    outp = int(input("1. Header\n2. First Line\nEnter 1 to print the header or 2 to print the first line\n"))
    if not(outp == 1 or outp == 2):
        print("Wrong Input")
        continue
    else:
        break
lines  = inp.readlines()
if outp == 1:
    print(lines[0])
elif outp == 2:
    print(lines[1])

inp.close()


