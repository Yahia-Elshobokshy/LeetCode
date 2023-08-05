class Solution:
    def maxArea(self, height: List[int]) -> int:
        def maxArea(lo,hi,maxi):
            if lo >= hi: return maxi
            if height[lo] < height[hi]:
                return maxArea(lo+1, hi, max(maxi, height[lo] * (hi-lo)))
            return maxArea(lo, hi-1, max(maxi, height[hi] * (hi-lo)))
        return maxArea(0, len(height)-1, 0)
