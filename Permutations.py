from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = permutations(nums)
        ans = []
        for i in nums:
            ans.append(i)
        return ans
