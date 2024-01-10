from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        new_list=[i for i in range(1,n+1)]
        return combinations(new_list,k)