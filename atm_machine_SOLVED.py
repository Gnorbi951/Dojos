def solve(n):
    if n % 5 == 0 and n % 10 != 0:
        return -1

    bill_number = 0

    while n != 0:
        if n >= 500:
            n -= 500
            bill_number += 1
            continue
        if n >= 200:
            n -= 200
            bill_number += 1
            continue
        if n >= 100:
            n -= 100
            bill_number += 1
            continue
        if n >= 50:
            n -= 50
            bill_number += 1
            continue
        if n >= 20:
            n -= 20
            bill_number += 1
            continue
        if n >= 10:
            n -= 10
            bill_number += 1
            continue

    return bill_number


print(solve(1010))
