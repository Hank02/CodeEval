# print next-to-last word of each input string
# each string has more than one word

import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

def find_penultimate(instring):
    # convert string into list for easier access to individual words
    inlist = instring.split(" ")
    # access and print penultimate word
    print(inlist[-2])



if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        find_penultimate(row)
    # close file
    file.close()