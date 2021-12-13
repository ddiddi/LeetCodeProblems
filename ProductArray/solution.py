# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

 class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [0]*length
        right = [0]*length
        sol = [0]*length
        
        left[0] = 1
        right[length - 1] = 1
        
        for i in range(1, length):  
            left[i] = nums[i - 1] * left[i - 1]
            right[i] = nums[length-i + 1] * right[length-i + 1]
            sol[i] = left[i]*right[i]
        return sol