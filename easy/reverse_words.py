# reverse the order of a sentence

import sys

def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# funtion that reverses the order of words in a string
def reverse_sentence(string_input):
    as_list = []
    # convert string into list by splitting words into elements
    as_list = string_input.split()
    # reverse the order of the list
    as_list.reverse()
    # convert reversed list into a string
    rev_string = " ".join(as_list)
    print(rev_string)

if __name__ == "__main__":
    # open file
    file = file_open()
    # iterate over each line of file
    for line in file:
        # if line is empty, skip
        if not line.strip():
            continue
        # otherwise, run function
        else:
            reverse_sentence(line)
    file.close()
