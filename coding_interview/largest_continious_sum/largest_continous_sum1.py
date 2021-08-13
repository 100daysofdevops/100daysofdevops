def largest_sum(arr):
    if len(arr) == 0:
        return False
    max_sum = cur_sum = arr[0]

    for val in arr[1:]:
        cur_sum = max(cur_sum+val, val)
        max_sum = max(cur_sum,max_sum)
    return max_sum
