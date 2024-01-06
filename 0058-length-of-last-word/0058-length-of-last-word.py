class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = -1
        while (1):
            if len(s.split(' ')[idx]) != 0:
                return len(s.split(' ')[idx])
            else:
                idx -= 1
         