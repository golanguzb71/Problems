class Solution(object):
    def removeDuplicates(self, nums):
        result = []
        for num in nums:
            if num not in result:
                result.append(num)

        nums[:] = result
        return len(result)
