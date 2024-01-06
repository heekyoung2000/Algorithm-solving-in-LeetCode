
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_s=sorted(nums,reverse=True)
        return new_s[k-1]