###Author- Shambhavi Singh
###Date- 9th April 2020
###Description-
###This program that reads a CSV file with no column labels, and can compute a maximum, minimum or average of a column.
###It reads all of the values into a 2D list. You can loop through each line of the file, and split each line on ,.
###The list is then appended to another list which is then used
###The column on which the operation has to be performed and the operation to be performed is taken by the user
###It is composed of three functions- minimum, maximum and average to perform the corresponding operations

def minimum(num, column):
    '''
    num- list stores string versions of all the numbers in the file
    column- index of the column in the 2D list on which the operation has to performed
    num- list stores string versions of all the numbers in the file
    column- index of the column in the 2D list on which the operation has to performed
    The first elemnt of the column on which the operation has to be performed is stored in min_num
    The loop runs through all the numbers in that column and converts it to float type and compares it to the min_num.
    If the number is found to be smaller than the min_num then its value is stored in max_num as well
    After the loop runs through all the numbers the function returns min_num
    '''
    min_num = float(num[0][column])
    for i in range(0, len(num)):
        if min_num > float(num[i][column]):
            min_num = float(num[i][column])
    return min_num

def maximum(num, column):
    '''
    num- list stores string versions of all the numbers in the file
    column- index of the column in the 2D list on which the operation has to performed
    The first elemnt of the column on which the operation has to be performed is stored in max_num
    The loop runs through all the numbers in that column and converts it to float type and compares it to the max_num.
    If the number is found to be greater than the max_num then its value is stored in max_num as well
    After the loop runs through all the numbers the function returns max_num
    '''
    max_num = float(num[0][column])
    for i in range(0, len(num)):
        if max_num < float(num[i][column]):
            max_num = float(num[i][column])
    return max_num

def average(num, column):
    '''
    num- list stores string versions of all the numbers in the file
    column- index of the column in the 2D list on which the operation has to performed
    Calculates the sum of each element of the column by first converting it to float type.
    It then divides it by the length of the list num
    it returns the average of all the numbers in the column
    '''
    avg = 0
    for i in range(0, len(num)):
        avg += float(num[i][column])
    return (avg/len(num))

def main():
    '''
    The numbers list is empty at first but then it stores string versions of all the numbers in the file
    All the lines are read one by one and stored in a list lines
    All the elements of the string are stripped of the '\n' and are split on the ',' and stored in a 2D list numbers
    The column and the operation are asked from the user and are then used during the function call for the respective operator
    '''
    numbers=[]
    file_name = input("Enter CSV file name:\n")
    column_num = int(input("Enter column number:\n"))
    operation = input("Enter column operation:\n")
    inp = open(file_name, "r")
    for lines in inp:
        lines=lines.strip('\n')
        lines=lines.split(',')
        numbers.append(lines)
    if operation == "min":
        print("The minimum value in column",column_num,"is:", minimum(numbers, column_num-1))
    elif operation == "max":
        print("The maximum value in column",column_num,"is:", maximum(numbers, column_num-1))
    elif operation == "avg":
        print("The average for column",column_num,"is:", average(numbers, column_num-1))

main()

