def reversed_num(n: int) -> int:
    result = 0
    while n != 0:
        digit = n % 10
        result = result * 10 + digit
        n //= 10
    return result


reversed_num(11223439)