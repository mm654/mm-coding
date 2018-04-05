#coding=utf-8
#广度优先搜索算法寻找是否存在到目的地的路径以及哪条路径最短
#先在一度关系中搜索，确定没有结果之后再在第二度关系中搜索，以此类推。。
#运用队列，先进先出

def isMango(person):
    if person[-1]=='y':
        return True
from collections import deque
def breadth_first_search():
    graph={}
    graph['you']=['Alice','Bob','Claire']
    graph['Alice']=['peggy']
    graph['Bob']=['anuj','peggy']
    graph['Claire']=['thom','jonny']
    graph['anuj']=[]
    graph['peggy']=[]
    graph['thom']=[]
    graph['jonny']=[]
    search=deque()
    search+=graph['you']
    while search:
        value=search.popleft()
        if isMango(value):
            print value +' is the mango seller!'
            return True
        else:
            search+=graph[value]
    return False
search_m=breadth_first_search()
print search_m
