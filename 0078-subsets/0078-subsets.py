from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        new_nums=[]
        def dfs(start,visited):
            new_nums.append(visited)
            for i in range(start,len(nums)):
                dfs(i+1,visited+[nums[i]])
    
        dfs(0,[])
        return new_nums
            
            
                
        