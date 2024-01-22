class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current_sum=0
        if len(nums)==1:
            return nums[0]
        else:
            for num in nums:
                current_sum = current_sum+num
                max_value = max(max_value,current_sum)
                if current_sum < 0:
                    current_sum = 0
            return max_value
