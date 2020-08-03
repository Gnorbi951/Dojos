def dig_pow(n, p):
    digits = []
    for d in str(n):
        digits.append(int(d))

    elements_sum = 0
    for element in digits:
        elements_sum += element ** p
        p += 1
    for i in range(1, 15000):
        if n * i == elements_sum:
            return i

dig_pow(46288, 3)