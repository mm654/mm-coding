#coding=utf-8
#思路：两次循环判断两者想加是否等于taregt

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2:
            return
        list1=[]
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]+nums[j]==target:
                    list1.append(i)
                    list1.append(j)
                    break
                    return list1                   
                j+=1
            i+=1
        return
                    
            
        
        