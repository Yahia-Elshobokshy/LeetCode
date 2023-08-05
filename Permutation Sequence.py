from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        for i in range(1,n+1):
            res.append(i)
        perm = permutations(res)
        counter = 0
        for i in list(perm):
            counter += 1
            if counter == k:
                w = i
                break
        ans = ''.join(map(str,w))
        return ans
