def comp(array1, array2):
    
    if array1 == None or array2 == None:
        return False
    if len(array1) == 0 and len(array2) == 0:
        return True
    if len(array1) > len(array2) or len(array2) > len(array1):
        return False

    array1 = sort_by_abs(array1)
    array2 = sort_by_abs(array2)
    print(array1, array2)

    for a1, a2 in zip(array1, array2):
        if a1**2 != a2:
            return False
    return True

def sort_by_abs(numbers_array):

    return sorted(tuple(numbers_array), key=abs)


comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])