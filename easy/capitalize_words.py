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
def cap_first(instring):
    # convert string into list by splitting words into elements
    as_list = instring.split()
    # iterate over each word
    for i in range(len(as_list)):
        as_list[i] = as_list[i][0].upper() + as_list[i][1:]
    # convert list of words back into string
    result = " ".join(as_list)
    print(result)

if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        cap_first(row)
    # close file
    file.close()