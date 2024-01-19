class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 이분탐색을 이용해서 만약 mid와 오른쪽 합이 target 보다 크면 left를 mid-1로 정하기 만약 크면 right=mid+1
        left=0
        right = len(numbers)-1
        result=[]
        while left<right:
            output=numbers[left]+numbers[right]
            if output==target:
                result.append(left+1)
                result.append(right+1)
                break
            elif output>target:
                right-=1
            else:
                left+=1
        return result
                    
        