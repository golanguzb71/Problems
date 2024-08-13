def hammingDistance(x: int, y: int) -> int:
    res = 0
    while x != 0 or y != 0:
        maskx = x & 1
        masky = y & 1
        res += maskx ^ masky
        x = x >> 1
        y = y >> 1

    return res


print(hammingDistance(1, 4))
