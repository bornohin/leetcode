class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = max_sum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            max_sum = max(max_sum, currSum)

        return max_sum
