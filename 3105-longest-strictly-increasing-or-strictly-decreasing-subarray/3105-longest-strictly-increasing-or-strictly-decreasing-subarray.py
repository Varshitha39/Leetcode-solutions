class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length=0
        for i in range(len(nums)):
            curr=1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[j-1]:
                    curr+=1
                else:
                    break
            max_length=max(max_length,curr)
        for i in range(len(nums)):
            curr=1
            for j in range(i+1,len(nums)):
                if nums[j]<nums[j-1]:
                    curr+=1
                else:
                    break
            max_length=max(max_length,curr)
        return max_length
        