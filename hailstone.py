def hailstone(integer):
    if integer == 1:
        return 0
    else:
        count = 0

    if integer > 1:

        if integer % 2 == 0: #even case
            count += (integer / 2)

        else: #odd case
            count += ((integer * 2) + 1)


    return count
print(int(hailstone(3)))