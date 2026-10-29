class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res={}
        total=0
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        for i in res:
            if res[i]==1:
                total+=i
        return total

        
            