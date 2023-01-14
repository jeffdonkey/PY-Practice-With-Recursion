# Write code for algorithm 2 below


def natural_numbers(lowerNum, higherNum):
    if lowerNum > higherNum:
        return
    else:
        print(lowerNum)
        natural_numbers(lowerNum + 1, higherNum)

n=10
natural_numbers(1,n)

# Line 11 sets "n" equal to "10"
# Line 12 calls function 'natural_numbers' sending '1' and 'n' as arguments
# Lines 5-6 are the base case.  
# Lines 7-9 are the recursion case.
# Line 8 will print the value of 'lowerNum'.
# Line 9 calls the function "natural_numbers" again; sending 'lowerNum + 1' and the original value for 'higherNum'
# function repeats until 'lowerNum' value is greater than 10