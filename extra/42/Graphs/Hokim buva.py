def findJudge(n: int, trust: list) -> int:
    for massiv in trust:
        if massiv[0] == n or massiv[1] != n:
            return -1

    return n


print(findJudge(5, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]))
