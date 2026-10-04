class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans1 = []
        ans2 = []
        for num1 in set(nums1):
            if num1 not in set(nums2):
                ans1.append(num1)
        for num2 in set(nums2):
            if num2 not in set(nums1):
                ans2.append(num2)
        return [ans1,ans2]