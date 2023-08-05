class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dictj={}
        for i in jewels:
            if i in dictj:
                dictj[i]+=1
            else:
                dictj[i]=1
        sum=0
        for j in stones:
            if j in dictj:
                sum+=dictj[j]
                
        return(sum)
