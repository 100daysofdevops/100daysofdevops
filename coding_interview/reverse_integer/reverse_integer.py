# Leet Code Problem: https://leetcode.com/problems/reverse-integer/
# Modulus and division of negative number shows some unexpected result int(divider/number) and number % -divisor
# Time Complexity 0(n) and Space Complexity 0(1)

def divide(number, divider):
    return int(number/divider)

def mod(number,divisor):
    if number < 0:
        return number % -divisor
    return number % divisor

MAX_INT = 2 ** 31 -1
MIN_INT = -2 ** 31

def reverse(x):
    res = 0
    while x:
        pop = mod(x,10)
        x = divide(x,10)
        if res > divide(MAX_INT, 10) or (res == divide(MAX_INT,10) and pop > 7):
            return 0
        if res < divide(MIN_INT, 10) or (res == divide(MIN_INT,10) and pop < -8):
            return 0
        res = res * 10 + pop
    return res


print(reverse(123))
