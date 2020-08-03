def find_even_index(arr):
    counter = 0
    for element in arr:
        left_array = arr[:counter]
        right_array = arr[counter+1:]
        
        left_sum, right_sum = sum(left_array), sum(right_array)

        if left_sum == right_sum:
            return counter
        counter += 1
        
    return -1



find_even_index([1,2,3,4,3,2,1])
