def countBits(n: int) -> list:
    result = [0, 1]
    for i in range(2, n + 1):
        bit_count = result[i >> 1] + (i & 1)
        result.append(bit_count)

    return result
