# print the longest word in a sentence
# if more than one, print the left-most one

import sys

def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# funtion to print in title case
def longest_word(instring):
    # convert string into list by splitting words into elements
    as_list = instring.split()
    word = ""
    length = 0
    for each in as_list:
        if len(each) > length:
            length = len(each)
            word = each
    print(word)

if __name__ == "__main__":
    file = file_open()
    for row in file:
        longest_word(row)
    file.close()
