class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        result=0
        if len(s)==0:
            return True
        elif len(t)==0:
            return False
        
        while 1:
            if i>len(s)-1:
                result=1
                break
            elif j>len(t)-1:
                break
            elif s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if result==1:
            return True
        else:
            return False
            
            