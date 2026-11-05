class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ct=0
        arr2.sort()
        for num in arr1:
            low=0
            high=len(arr2)-1
            valid=False
            while low<=high:
                mid=(low+high)//2
                if abs(num-arr2[mid])<=d:
                    valid=True
                    break
                elif arr2[mid]<num:
                    low=mid+1
                else:
                    high=mid-1
            if not valid:
                ct+=1
        return ct
                