# Add the digits of an int

import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# sum constituent digits of a positive int
def sum_digits(instring):
    # convert string into list of chars
    inlist = list(instring)
    # eliminate \n from last element
    inlist.pop()
    # convert digits to ints
    inlist = [int(i) for i in inlist]
    # sum and print
    print(sum(inlist))

if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        sum_digits(row)
    # close file
    file.close()