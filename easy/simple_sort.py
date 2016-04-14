# take a string of floats and print sorted and with 3-digit precision in one line

import sys

def open_file():
    in_file = sys.argv[1]
    data = open(in_file, "r")
    return data

def sorter(instring):
    # remove \n from end string
    if instring[-1] == "\n":
        instring = instring[:-1]
    # convert string into list
    as_list = instring.split(" ")
    # convert strings into floats
    float_list = []
    for each in as_list:
        float_list.append(float(each))
    # sort
    float_list = sorted(float_list)
    # print formated floats into same line
    for i in float_list:
        sys.stdout.write("%.3f " % i)
    print("")


if __name__ == "__main__":
    file = open_file()
    for row in file:
        sorter(row)
    file.close()