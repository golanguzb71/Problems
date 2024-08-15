def missingNumber(lst):
    n = len(lst)
    sum_n = n * (n + 1) // 2
    sum_lst = sum(lst)
    return sum_n - sum_lst
