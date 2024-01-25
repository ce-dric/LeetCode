class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp={}
        def helper(i,j):
            if i==n or j==m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            elif text1[i]==text2[j]:
                temp=1+helper(i+1,j+1)
                dp[(i,j)]=temp
            else:
                temp=max(helper(i,j+1),helper(i+1,j))
                dp[(i,j)]=temp
            return dp[(i,j)]
        return helper(0,0)