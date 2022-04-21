# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/20/2022
# Description: Counts the steps of a hailstone sequence from an integer back to 1.
#


def hailstone(integer):
    """Counts the steps of a hailstone sequence from an integer back to 1."""
    if integer == 1:
        return 0
    else:
        steps = 0

    if integer > 1:

        if integer % 2 == 0:
            steps += (integer / 2)

        else:
            steps += ((integer * 2) + 1)


    return steps
