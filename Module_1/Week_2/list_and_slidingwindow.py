num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3


def finding_max_inlist (num_list, k):
    result = []
    slice_lst = []
    num_start = 0
    while num_start != len(num_list) - 2:
        slice_lst = num_list[num_start : num_start + k]
        result.append(max(slice_lst))
        num_start += 1
    return result

print (finding_max_inlist(num_list, k))
    
