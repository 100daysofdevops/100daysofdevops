def twosum(arr,target):
    if len(arr) < 2:
        return False

    dict = {}

    for i in range(len(arr)):
        diff = target - arr[i]

        if arr[i] in dict:
            return dict[arr[i]],i
        else:
            dict[diff] = i


print(twosum([1,3,2,2],4))
