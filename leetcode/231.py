class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        re=0
        while n>1 and re!=1:
            re=n%2
            n/=2
        if n==1 and re==0:
            return True
        return False
            
# solu=Solution()
# print solu.isPowerOfTwo(17)