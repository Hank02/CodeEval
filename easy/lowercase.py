# Read string from file and print in lowercase

import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# funtion to print in lowercase
def to_lower(instring):
    print(instring.lower())

if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        to_lower(row)
    # close file
    file.close()