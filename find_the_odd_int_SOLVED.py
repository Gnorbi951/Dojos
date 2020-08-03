def find_it(seq):
    comparison_dict = {}
    for i in seq:
        if str(i) not in comparison_dict.keys():
            comparison_dict[str(i)] = 1
        else:
            comparison_dict[str(i)] += 1
    
    for key, value in comparison_dict.items():
        if value % 2 == 1:
            return int(key)



find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])



