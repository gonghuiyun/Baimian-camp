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
            swap(L,node,node*2)
            return L
    else:
        if L[node*2]<L[node*2+1]:
            swap(L,node*2,node*2+1)
        #比较node与左子节点的值
        if L[node]<L[node*2]:
            swap(L,node,node*2)
    return L

# def node_adjust_rev(L, node):
#     if node / 2 < 1:
#         return L
#     if node % 2 == 0:
#         if L[int(node / 2)] < L[int(node)]:
#             swap(L, int(node), int(node / 2))
#         node_adjust_rev(L, int(node / 2))
#     else:
#         if L[int((node-1) / 2)] < L[int(node)]:
#             swap(L, int(node), int((node-1) / 2))
#         node_adjust_rev(L, int((node-1) / 2))


def heap_struct(L):

    mid = int((len(L)-1)/2)
    for i in range(mid):
        node_adjust(L,mid-i)

    for i in range(1,mid+1):
        print(i)
        node_adjust(L,i)
    return L

def top_to_botton(L,node):
    if node*2+1 >len(L)-1:
        return L
    if L[node]<L[node*2+1]:
        swap(L,node,node*2+1)
        top_to_botton(L,node*2+1)


print(L2)
heap_struct(L2)
print(L2)


