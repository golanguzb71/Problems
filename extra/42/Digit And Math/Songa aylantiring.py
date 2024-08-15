def myAtoi(s):
    s = s.strip()

    sign = 1
    if s and s[0] == '+':
        s = s[1:]
    elif s and s[0] == '-':
        sign = -1
        s = s[1:]

    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            break

    if num_str:
        result = sign * int(num_str)
    else:
        result = 0

    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result
