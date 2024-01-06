class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic={}
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count+=1
            dic[i]=count
        new_dic=sorted(dic.items(),key=lambda x:x[1],reverse=False)
        new_list=[]
        for d in new_dic:
            new_list.append(d[0])
        return new_list[:k]
   
            
                