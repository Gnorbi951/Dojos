def solution(number):

    number_list = []

    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            number_list.append(i)

    sum_value = sum(number_list)

    return sum_value


print(solution(93))
