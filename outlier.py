def find_outlier(integers):
    odd = True
    odd_counter = 0
    even_counter = 0
    for i in integers:
        if i % 2 == 1:
            odd_counter += 1
        if i % 2 == 0:
            even_counter += 1
        if odd_counter > 1:
            break
        if even_counter > 1:
            odd = False
            break
    # This dividant looks for the outlier, so if our list is odd it looks for an even number
    dividant = 1
    if odd:
        dividant = 0
    
    for i in integers:
        if i % 2 == dividant:
            return i

find_outlier([2, 4, 6, 8, 10, 3])