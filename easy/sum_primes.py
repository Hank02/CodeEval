# sum first 1,000 prime numbers

from math import sqrt

# test if number is prime
def is_prime(num):
    # hard-code first prime numbers
    if num == 2 or num == 3 or num == 5:
        return True
    
    # quick check to eliminate nums divisible by 2, 3 and 5
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
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

if __name__ == "__main__":
    total = 0
    count = 0
    num = 2
    # test each number for prime, sum and count it true
    while(count < 1000):
        prime_test = is_prime(num)
        if prime_test == True:
            total += num
            count += 1
        num += 1
    print(total)
