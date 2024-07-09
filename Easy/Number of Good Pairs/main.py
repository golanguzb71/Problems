# https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1

        return counter

