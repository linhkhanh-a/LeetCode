class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        memoir = []
        for i in range(n):
            memoir.append([False] * n)
        ans = ""
 
        for dist in range(0, n):
            for i in range(n - dist):
                if dist == 0:
                    memoir[i][i + dist] = True
                    ans = s[i : i+dist + 1]

                if dist > 1 and s[i] == s[i + dist] and memoir[i+1][i + dist - 1] == True:
                    memoir[i][i + dist] = True
                    ans = s[i : i+dist + 1]

                if dist == 1 and s[i] == s[i + dist]:
                    memoir[i][i + dist] = True
                    ans = s[i : i+dist + 1]

        return ans