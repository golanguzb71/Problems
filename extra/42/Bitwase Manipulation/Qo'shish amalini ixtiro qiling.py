def getSum(a: int, b: int) -> int:
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


getSum(100, 20)
