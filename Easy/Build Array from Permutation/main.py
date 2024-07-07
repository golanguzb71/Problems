# https://leetcode.com/problems/build-array-from-permutation/description/


class Solution(object):
    def buildArray(self, nums):
        ans = list(nums)
        for i in range(len(ans)):
            ans[i] = nums[nums[i]]
        return ans
