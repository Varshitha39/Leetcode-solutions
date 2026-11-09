class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr=sorted(nums1+nums2)
        n = len(arr)
        mid=n//2
        if n % 2 != 0:
            return arr[mid]
        else:
            return (arr[mid - 1] + arr[mid]) / 2.0
