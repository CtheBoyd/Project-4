# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/20/2022
# Description:  Takes a positive integer and returns that number's position in the Fibonacci sequence.
#


def fib(user):
    """Takes a positive integer and returns that number's position in the Fibonacci sequence."""
    if user == 1:
        return 1
    else:
        num_1 = 1
        num_2 = 1
        result = num_1 + num_2

    for index in range(1, user-2):
        num_1 = num_2
        num_2 = result
        result = num_1 + num_2

    return result

