class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        n = len(nums1)
        if n % 2 == 1:
            return nums1[n//2]
        else:
            x= (nums1[n//2 - 1] + nums1[n//2])/2
            return x
