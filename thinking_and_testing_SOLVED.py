def test_it(a, b):
    def split_number(num):
        return_array = []
        for i in str(num):
            return_array.append(int(i))
        return return_array

    a_sum = sum(split_number(a))
    b_sum = sum(split_number(b))

    return a_sum * b_sum
