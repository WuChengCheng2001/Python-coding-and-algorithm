'''给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0'''

# 关键词：
# 二分查找，拓展题

class Solution:
    def searchInsert(self, nums:list[int], target:int):
        left = 0
        right = len(nums)-1

        if target < nums[left]:
            return 0
        if target > nums[right]:
            return right+1
        
        while left <= right:
            mid = left+(right-left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
        return left
    
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#         while left <= right:
#             middle = (left + right) // 2

#             if nums[middle] < target:
#                 left = middle + 1
#             elif nums[middle] > target:
#                 right = middle - 1
#             else:
#                 return middle
#         return right + 1