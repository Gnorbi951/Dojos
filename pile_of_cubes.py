def find_nb(m):
    # m is total volume
    current_layer = 0
    while m > 0:
        current_layer += 1
        m -= current_layer**3
        print(current_layer)

    if m == 0:
        return current_layer
    else:
        return -1
  



find_nb(4183059834009)