def romanToInt(s):
    lookup = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }

    curr = prev = total = 0
    for i in range(len(s)):
        curr = lookup[s[i]]

        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total = total + curr

        prev = curr
    return total



print(romanToInt("IV"))
