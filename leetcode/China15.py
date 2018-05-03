#coding=utf-8
#思路：先对序列排序，每次遍历固定一个数，然后根据三者的和调整其他两个数的位置
#注意：总是出现时间超时，是因为遍历过程中要跳过重复的数字，相应的在加入到列表中时就不用判断列表中是否已存在
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums)<3:
            return []
        nums.sort()    
        list2=[]
        i=0
        e=len(nums)-1
        while i<e:
            a=nums[i]
            k=i+1
            j=e
            while k<j:
                b=nums[k]
                c=nums[j]
                if a+b+c==0:
                    list2.append([a,b,c]) 
                if a+b+c<=0:
                    while b==nums[k] and k<j:
                        k+=1
                if a+b+c>=0:
                    while c==nums[j] and k<j:
                        j-=1
            while a==nums[i] and i<e:
                i+=1
        return list2