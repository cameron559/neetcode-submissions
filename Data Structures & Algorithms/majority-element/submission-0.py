class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        for i, n in enumerate(nums):
            numCount[n] = 1 + numCount.get(n, 0)
        return max(numCount, key=numCount.get)


        