def countBits(n):
    binary_value = bin(n)
    bit_counter = 0
    for letter in binary_value:
        if letter == '1':
            bit_counter += 1

    return bit_counter


print(countBits(3))
