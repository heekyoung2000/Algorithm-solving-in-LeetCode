class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k=sorted(heights)
        cnt=0
        for i in range(len(k)):
            if k[i]!=heights[i]:
                cnt+=1
        return cnt