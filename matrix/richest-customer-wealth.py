class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        curr_richest = 0
        for row in accounts:
            s = sum(row)
            curr_richest = max(curr_richest, s)

        return(curr_richest)