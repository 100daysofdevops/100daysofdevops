def threesum(arr, target):
    res = []
    arr.sort()

    length = len(arr)

    for i in range(length -2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l = i +1
        r = length -1

        while l < r:
            total = arr[i] + arr[l] + arr[r]

            if total < target:
                l += 1
            elif total > target:
                r -=1
            else:
                res.append([arr[i],arr[l],arr[r]])
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while l < r and arr[r] == arr[r-1]:
                    r -= 1

                l +=1
                r -=1
    return res

print(threesum([-1,0,1,2,-1,-4],0))





