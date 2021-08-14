def duplicate(x):
    dict = {}
    for val in x:
        if val in dict:
            return True
        else:
            dict[val] = 1
    return False



print(duplicate([1,2,3,1]))
