class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        flag=0
        if nums==[] or k==0:
            return False
        if len(nums)==len(set(nums)):
            return False
        for i in range(len(nums)-1):
            j=i+1
            while j<len(nums) and j<i+k+1:
                if nums[j]==nums[i]:
                    return True
                    flag=1
                    break
                else:
                    j+=1
            if flag==1:
                break
        return False