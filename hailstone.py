def hailstone(integer):




    for index in range(integer, 0, -1):

        if integer % 2 == 0: #even case
            value = interger / 2
            integer = value

        if integer % 2 == 1: #odd case
            value = integer * 3 + 1
            integer = value

    return value
print(hailstone(3))