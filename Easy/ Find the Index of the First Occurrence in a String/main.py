class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1


s = Solution()
print(s.strStr("sadbutsad", "sad"))
