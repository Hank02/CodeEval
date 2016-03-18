# swap each letter's case

import sys

def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# funtion that reverses the order of words in a string
def swap_case(sentence):
    swaped = ""
    for each in sentence:
        if each.isalpha():
            if each.islower():
                swaped += each.upper()
            else:
                swaped += each.lower()
        else:
            swaped += each
    print(swaped)

if __name__ == "__main__":
    # open file
    file = file_open()
    # iterate over each line of file
    for line in file:
        swap_case(line)
    file.close()