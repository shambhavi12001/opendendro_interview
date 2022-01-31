#read a csv file
import csv
file_name = input("Enter CSV file name:\n")
inp = open(file_name, "r")
csvreader = csv.reader(inp)
header = []
header = next(csvreader)
print(header)


