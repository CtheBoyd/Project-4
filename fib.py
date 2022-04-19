def fib(term):
    num_1 = 1
    num_2 = 1
    result = num_1 + num_2

    for index in range(1, term-2):
        num_1 = num_2 #num_2 from before
        num_2 = result #result from before
        result = num_1 + num_2

    return result

print(fib(1))