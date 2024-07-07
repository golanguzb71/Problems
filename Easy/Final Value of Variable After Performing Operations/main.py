class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0
        for operation in operations:
            if operation == "X++" or operation == "++X":
                result += 1
            else:
                result -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    sol.finalValueAfterOperations(["--X", "X++", "X++"])
