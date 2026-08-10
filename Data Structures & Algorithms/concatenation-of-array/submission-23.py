class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] * len(2 * nums)

        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        