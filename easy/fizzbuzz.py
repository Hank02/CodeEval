# play FizzBuzz with user-defined fizz and buzz numbers

import sys

def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# function that plays fizz buzz according to inputs
def fb_game(test_cases):
    # for each row in input file...
    for row in test_cases:
        # variable to store fizz buzz sequence
        sequence = ""
        # split line into its three elements
        current_test = row.split()
        # first element is first divisor
        num1 = int(current_test[0])
        # second element is second divisor
        num2 = int(current_test[1])
        #third element is length of sequence to count
        count_upto = int(current_test[2])
        # play fizz buzz...
        for i in range(1, count_upto + 1):
            if i % num1 == 0 and i % num2 == 0:
                sequence += "FB "
            elif i % num1 == 0:
                sequence += "F "
            elif i % num2 == 0:
                sequence += "B "
            else:
                sequence += str(i) + " "

        print(sequence[0:-1])

if __name__ == "__main__":
    # open file
    file = file_open()
    # play fizz buzz
    fb_game(file)
    # close file
    file.close()
    
