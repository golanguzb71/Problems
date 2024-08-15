def numberToWords(num: int) -> str:
    ones = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
    tens = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
    thousands = ["", "ming", "million", "milliard"]
    if num == 0:
        return ""
    def three_digits_to_words(n):
        word = ""
        if n >= 100:
            word += ones[n // 100] + " yuz "
            n %= 100
        if n >= 10:
            word += tens[n // 10] + " "
            n %= 10
        if n > 0:
            word += ones[n]
        return word.strip()

    result = ""
    group = 0

    while num > 0:
        n = num % 1000
        if n != 0:
            result = three_digits_to_words(n) + " " + thousands[group] + " " + result
        num //= 1000
        group += 1

    return result.strip()
