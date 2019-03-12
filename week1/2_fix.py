'''
快速选择、堆排序（题号：215）：
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''
from collections import deque
from math import log
L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
L.appendleft(0)

L2 = deque([3,2,1,5,6,4])
L2.appendleft(0)

def swap(L,i,j):
    L[i], L[j] = L[j],L[i]
    return L

#输入要调整的节点的index
#将此节点与其子节点按堆的规则排序
#node为节点的序号
def node_adjust(L,node):
    #先判断node的子节点，将值更大的调到左边

    if node*2>len(L)-1:
        return L
    #只有左子节点
    elif node*2+1>len(L)-1:
        if L[node]<L[node*2]:
            L[node], L[node*2] = L[node*2], L[node]
            return L
    else:
        if L[node*2]<L[node*2+1]:
            swap(L,node*2,node*2+1)
        #比较node与左子节点的值
        if L[node]<L[node*2]:
            L[node], L[node*2] = L[node*2], L[node]
    return L

def heap_struct(L):

    mid = int((len(L)-1)/2)
    for i in range(mid):
        node_adjust(L,mid-i)

    for i in range(mid):
        node_adjust(L,i+1)
    return L


def findKthLargest(L, k):
    if len(L) == 2:
        return L[1]
    if len(L) == 3:
        node_adjust(L, 1)
        return L[k]
    else:
        heap_struct(L)
        for i in range(k - 1):
            if len(L) == 2:
                return L[1]
            L[1], L[len(L) - 1] = L[len(L) - 1], L[1]
            L.pop()
            heap_struct(L)
        tmp = L[1]
    return tmp

print(findKthLargest(L2,2))
