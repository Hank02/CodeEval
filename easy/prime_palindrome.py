# find largest prime palindrome less than 1,000
# no input

from math import sqrt

# test if number is prime
def is_prime(num):
    # quick check to eliminate all even numbers larger than 2
    if num < 2 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    
    # no need to check every number from 2 to "num", just from 3 to sqrt of "num"
    max_test = int(sqrt(num))
    if max_test % 2 == 0:
        max_test += 1
    # # iterate from 3 to max_test, skipping even numbers, max_test+2 to include it
    for i in range(3, max_test + 2, 2):
        # if any is evenly divisible, not prime
        if num % i == 0:
            return False
    # if you finish iteration, then it must be prime
    return True

def is_pal(num):
    # turn num into a string
    str_num = str(num)
    # reverse string
    reverse = str_num[::-1]
    # compare strings
    if str_num == reverse:
        return True
    else:
        return False
        

if __name__ == "__main__":
# since we are looking for the largest number, count backward from 999
    for each in range(999, 0, -1):
        if is_prime(each) == True:
            if is_pal(each) == True:
                print(each)
                break

    
