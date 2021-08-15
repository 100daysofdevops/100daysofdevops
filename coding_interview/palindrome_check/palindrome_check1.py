def isPalindrome(s):
    res = ""

    for val in s:
        if val.isalnum():
            res = res + val.lower()

    length = len(res)
    l = 0
    r = length -1

    while l < r:
        if res[l] != res[r]:
            return False
        l +=1
        r -=1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
