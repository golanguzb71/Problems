# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/


class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(x % 3 > 0 for x in nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumOperations([8]))
