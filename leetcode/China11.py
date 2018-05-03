#coding=utf-8
#注意：求最大区间面积不是梯形！其次要返回的是面积不是【ai,aj】
#之前思路是两重循环，用max_area始终装最大的面积得到结果，但是超时！
#转换思路：二分法，想到实际上就是对不同的ai值，要求跨度（j-i）最大，于是设置low和high两个指针
#在首尾，计算出的面积就是在当前ai下最大的面积，然后移动low或high去寻找其他面积。
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=area=0
        if len(height)<2:
            return
        low=0
        high=len(height)-1
        while low<high:
            if height[low]<height[high]:
                area=height[low]*(high-low)
                low+=1
            else:
                area=height[high]*(high-low)
                high-=1
            max_area=max(area,max_area)
        return max_area
        