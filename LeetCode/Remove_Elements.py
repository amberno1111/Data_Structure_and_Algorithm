# Given an array and a value, remove all instances of that value in place and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example:
# Given input array nums = [3,2,2,3], val = 3
# Your function should return length = 2, with the first two elements of nums being 2.
# 思路: 从数组中去除某个值，返回新数组的长度；注意在去除完毕后数组中的元素应该变化了，即出现value的位置都被替换掉了，最后一句的意思是 新长度后面的元素值任意，也就是说，新数组的总长度可以保持不变，但是新长度之前的元素要正确，后面的无所谓。设置双指针,从前往后扫描一遍即可.


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        first, last = 0, 0
        while last < len(nums):
            if nums[last] != val:
                nums[first], nums[last] = nums[last], nums[first]
                first += 1
            last += 1
        return first
