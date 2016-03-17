# Given numbers x and n, where n is a power of 2, 
# print out the smallest multiple of n which is greater than or equal to x. 
# Do not use division or modulo operator.

import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# find lowest multiple of x greater than n
def multiple(instring):
    # convert string of comma-separated str into list of ints
    inlist = [int(each) for each in instring.split(",")]
    result = inlist[1]
    while(result < inlist[0]):
        result += inlist[1]
    print(result)

if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        multiple(row)
    # close file
    file.close()