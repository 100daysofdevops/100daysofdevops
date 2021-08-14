# Leet Code Problem: https://leetcode.com/problems/palindrome-number/submissions/
# Negative number can't be palindrome -123 reverse is 321-
# Some other way to solve the problem is to convert integer to string and then reverse it
# Time complexity O(n) and Space Complexity 0(1)

def ispalindrome(x):
    if x < 0:
        return True
    b = 0
    c = x
    while c:
        b = b * 10 + c % 10
        c = int(c/10)
    return x == b

print(ispalindrome(121))
