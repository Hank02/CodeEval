# Read string from file and print in lowercase

import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# sum constituent digits of a positive int
def is_even(instring):
    # convert string into int
    number = int(instring)
    # determine of number is even
    if number % 2 == 0:
        print(1)
    else:
        print(0)
    

if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        is_even(row)
    # close file
    file.close()