class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=(list(set(nums)))
        nums[:]=reversed(sorted(nums))
        L=len(nums)
        if L>=3:
            return nums[2]
        else:
            return max(nums)
                
        