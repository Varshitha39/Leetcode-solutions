class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        d={}
        for i in nums2:
            while stack and stack[-1] < i:
                d[stack.pop()]=i
            stack.append(i)
        ans = []
        for i in nums1:
            ans.append(d.get(i, -1))
        return ans