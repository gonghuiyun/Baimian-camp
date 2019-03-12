'''
https://leetcode.com/problems/top-k-frequent-elements/description/
题目理解错了
这里是找到l中最大的数，但题目要求的是最大频率的数
'''
l = [1, 1, 1, 2, 2, 3]
l2 = [-1, -1]


class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def new_list(self, l, min_num):

        new_list = []
        for i in range(len(l)):
            if not l[i] == 0:
                if min_num >= 0:
                    for j in range(l[i]):
                        new_list.append(i )
                else:
                    for j in range(l[i]):
                        new_list.append(i + min_num)
        return new_list

    def topKFrequent(self):
        min_num = min(self.nums)
        max_num = max(self.nums)
        if len(self.nums) == 1:
            return self.nums
        if min_num >= 0:
            barrel = [0 for i in range(max_num + 1)]
            for i in self.nums:
                barrel[i] += 1
        else:
            barrel = [0 for i in range(max_num - min_num + 1)]
            for i in self.nums:
                barrel[i - min_num] += 1


        barrel_new = self.new_list(barrel, min_num)
        l_most_k = [barrel_new[len(barrel_new)-1-i] for i in range(self.k)]

        return l_most_k


a = Solution(l2, 1)
f_list = a.topKFrequent()
print(f_list)
