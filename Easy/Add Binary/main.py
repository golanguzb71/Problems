def convert_to_decimal(a: str) -> int:
    return int(a, 2)


def convert_to_binary(a: int) -> str:
    return bin(a)[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = convert_to_decimal(a)
        decimal_b = convert_to_decimal(b)

        sum_decimal = decimal_a + decimal_b

        return convert_to_binary(sum_decimal)
