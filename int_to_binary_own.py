def int_to_binary(n):
    base_counter = 0
    current_binary_bit = 1

    while n > current_binary_bit:
        base_counter += 1
        current_binary_bit = 2 ** base_counter

    print(current_binary_bit, base_counter)


int_to_binary(16)
