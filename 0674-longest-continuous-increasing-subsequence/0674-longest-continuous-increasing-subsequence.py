class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=0
        ans=0
        for i in range(len(nums)):
            if nums[i]>nums[i-1]:
                current+=1
            else:
                current=1
            if current>ans:
                ans=current
        return ans

        