class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        L=len(nums)
        nums=set(nums)
        result=[]
        for i in range(1,L+1):
            if i not in nums:
                result.append(i)
        return result

            
        
            
            
        