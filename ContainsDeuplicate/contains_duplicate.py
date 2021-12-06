class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # put nums in set and compare with original input 
        len_set_nums = len(set(nums)
        len_nums = len(nums)
        duplicate_exists = len(set(nums) < len(nums)
        return duplicate_exists