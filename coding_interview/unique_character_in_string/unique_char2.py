def unique_char(s):
    chars = set()

    for val in s:
        if val in chars:
            return False
        else:
            chars.add(val)

    return True
