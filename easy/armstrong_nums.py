
import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

def armstrong(instring):
    # remember input
    original = int(instring)
    # remove \n from instring
    instring = instring[:-1]
    # determine number of digits
    power = len(instring)
    # elevate eacg digit to power and sum
    add = 0
    for each in instring:
        add += int(each) ** power
    # compare to original number
    if original == add:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    file = file_open()
    for line in file:
        armstrong(line)
    file.close()
    
    