userInput = int(input('enter a number to fibonacci up to    '))+1
fibonacci_cache = {}

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    # fibonacci 1, 1, 2, -the next part of the sequence is handled below
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
        # function calls itself to add the last two items in the sequence
        # this forms the next part of the sequence, 3, 5, 8 ,13 ...
        # this continues until n reaches the end of the loop found below 

for n in range(1, userInput):
    # loop from 1 to user input

    # prints the result of the fibonacci function
    print(n, ":", fibonacci(n))