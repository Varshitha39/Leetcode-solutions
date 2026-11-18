class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*(n+1)
        return self.calculate(nums,dp,n-1)
    def calculate(self,nums,dp,n):
        if n<0:
            return 0
        if n==0:
            return nums[0]
        if dp[n]!=-1:
            return dp[n]
        dp[n]=max(self.calculate(nums,dp,n-1),(nums[n]+self.calculate(nums,dp,n-2)))
        return dp[n]