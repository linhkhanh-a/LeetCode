class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sSquares=[]
        for num in nums:
            snum=num*num
            sSquares.append(snum)
        return sorted(sSquares)
