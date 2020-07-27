from math import sqrt, floor

# This solves it but server times out, there's a more optimised mathematical way


def solve(n):

    def is_perfect_square(number):
        if number == 2 or number == 3:
            return True
        root = sqrt(number)
        return int(root + 0.5) ** 2 == number

    if is_perfect_square(n):
        return -1

    increased_number = n
    add_counter = 0
    while True:
        if is_perfect_square(increased_number) and is_perfect_square(add_counter):
            break
        else:
            increased_number += 1
            add_counter += 1

    return add_counter


print(solve(429235524))
