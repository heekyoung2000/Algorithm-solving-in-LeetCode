class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp=-1
        for i in range(len(arr)-1,-1,-1):
            n=arr[i]
            if temp<n:
                arr[i]=temp
                temp=n
            else:
                arr[i]=temp
        return arr
            