class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # str==1이거나 str가 0일 때 return
        result = {}
        for word in strs:
            
            test = "".join(sorted(word))
          
            if test not in result:
                result[test]=[]
                result[test].append(word)
            else:
                result[test].append(word)
            result[test].sort()
            
        return list(sorted(result.values()))
        
        