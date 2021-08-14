def twoSum(nums, target):
    if len(nums) < 2:
        return
    hash = {}
    for i , n in enumerate(nums):
        if n in hash:
            return [hash[n],i]
        hash[target -n] = i
    return []
