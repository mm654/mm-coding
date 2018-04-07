#coding=utf-8
#这种解法 Time Limit Exceeded
'''class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag=0
        count=0
        if n<=2 and n>=0:
            return 0
        if n>2:
            k=2
            while k<n:
                if k**0.5 < 2:
                    count+=1
                else:
                    for i in range(2,int(k**0.5)+1):
                        if k%i==0:
                            flag=1
                            break
                        else:
                            flag=0
                    if flag==0:
                        count+=1
                k+=1
        return count'''
#第二种解法：用一个初始值为0的列表表示每个数的状态（被处理过/未处理过）
#如果找到一个素数i那么1*i,2*i,...j*i<n为止的数均不考虑（标记为1）
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        list_tag=[0]*n
        count=0
        for i in range(2,n):
            if list_tag[i]==0:
                count+=1
                j=2
                while j*i<n:
                    list_tag[i*j]=1
                    j+=1
        return count
                
                
        
        
                        
                            
            
        