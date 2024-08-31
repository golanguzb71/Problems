class Solution(object):
    def strStr(self, haystack, needle):
        hl = len(haystack) - 1
        nl = len(needle) - 1
        if hl < nl:
            return -1
        