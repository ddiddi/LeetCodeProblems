# Prompt:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create list from nums - target 
        target_map = {}
        index_1 = None
        index_2 = None
        for i, m in enumerate(nums):
            if m-target in target_map.keys():
                index_1 = target_map[m-target]
                index_2 = i
                return index_1, index_2
            target_map[m] = i  
        return -1, -1