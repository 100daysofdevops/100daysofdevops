def reverseString(s):
    length = len(s)
    l = 0
    r = length -1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l +=1
        r -=1


print(reverseString(["h","e","l","l","o"]))
