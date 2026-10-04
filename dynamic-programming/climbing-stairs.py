class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
            
        memoir = [0] * n
        memoir[0] = 1
        memoir[1] = 2

        for i in range(2, n):
            memoir[i] = memoir[i-1] + memoir[i-2]

        return memoir[-1]