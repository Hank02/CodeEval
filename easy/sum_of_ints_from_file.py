# sum integers read from a file, one per line

import sys

# open file with comma-separated list of integers
def sum_file_ints():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    total = 0
    # itarete over each line of file
    for row in test_cases:
        # convert to int and add
        total += int(row)
    # close file and return sum
    test_cases.close()
    return total

if __name__ == "__main__":
    answer = sum_file_ints()
    print(answer)