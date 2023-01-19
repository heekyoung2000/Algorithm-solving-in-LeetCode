class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for i in nums:
            if i>=10 and i<100 or i>=1000 and i<10000 or i==100000:
                cnt+=1
        return cnt