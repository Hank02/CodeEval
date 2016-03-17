# Print to stdout the largest sum of all the possible contiguous subarrays for a given array

import sys

# open file with comma-separated list of integers
def file_open():
    # get inout file name as command line argument
    in_file = sys.argv[1]
    # open input file
    test_cases = open(in_file, "r")
    return test_cases

# sum all subarrays of each list
def larget_sum(instring):
    # convert string of comma-separated str into list of ints
    inlist = [int(k) for k in instring.split(",")]
    # determine length of list
    list_length = len(inlist)
    
    # store sum of each subarray
    list_of_sums = []
    
    # iterate over subarrays of different sizes
    for i in range(1, list_length + 1):
        # if subarrays each have 1 element...
        if i == 1:
            # ...simply append each element to "list_of_sums"
            for element in inlist:
                list_of_sums.append(element)
        else:
            # determine number of subarrays with size "i"
            subarrays = list_length - i + 1
            # iterate over input list...
            for each in range(subarrays + 1):
                # ...and construct intermediate list with proper size "i"
                temp = inlist[each:each + i]
                # add elements of "temp" list and append to "list_of_sums"
                list_of_sums.append(sum(temp))
    
    # find largest element in "list_of_sums" and print
    print(max(list_of_sums))

if __name__ == "__main__":
    # open file
    file = file_open()
    #iterate over each line of file and run function
    for row in file:
        larget_sum(row)
    # close file
    file.close()
