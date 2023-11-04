
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        def subsequence(s1, s2, m, n, dp):
            if m == 0 or n == 0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            if s1[m-1] == s2[n-1]:
                dp[m][n] = 1 + subsequence(s1, s2, m-1, n-1, dp)
            else:
                dp[m][n] = max(subsequence(s1, s2, m-1, n, dp), subsequence(s1, s2, m, n-1, dp))
            return dp[m][n]
        
        dp = [[-1] * (n+1) for i in range(m+1)]
        length =  subsequence(text1, text2, m, n, dp)

        return max(m-length,n-length)