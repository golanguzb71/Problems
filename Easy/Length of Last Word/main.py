#https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s: str):
        res = s.split()
        return len(res[len(res) - 1])


print(Solution().lengthOfLastWord("salom dunyo nima gap   mono"))
