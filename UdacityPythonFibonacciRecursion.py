"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    # if position == 0:
    #     return 0
    # elif position == 1:
    #     return 1
    # counter = 2
    # value = get_fib_rec(position, counter, 0, 1)
    # return value

    # Better solution from Udacity
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

def get_fib_rec(position, counter, first, second):
    next = first + second
    if counter == position:
        return next
    else:
        first = second
        second = next
        counter += 1
        return get_fib_rec(position, counter, first, second)


# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
