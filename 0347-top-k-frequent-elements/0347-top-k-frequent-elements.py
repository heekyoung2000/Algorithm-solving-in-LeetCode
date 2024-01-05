import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        count=0
        main=sorted(collections.Counter(nums).items(),key = lambda x:x[1],reverse=True)
        for key,value in main:
            count+=1
            result.append(key)
            if count==k:
                break
            else:
                continue
        return result
        