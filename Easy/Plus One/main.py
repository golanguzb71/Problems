# https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs=""
        for i in range(len(digits)):
            strs+=str(digits[i])
        strs=int(strs)+1
        strs=str(strs)
        list1=[]
        for i in range(len(strs)):
            list1.append(int(strs[i]))
        return list1




Solution().plusOne([9])