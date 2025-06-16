'''题意：给定两个数组，编写一个函数来计算它们的交集。'''

# 直接使用集合
class Solution:
    def intersection(self, nums1: list[int], 
                     nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

# 用字典和集合
class Solution:
    def intersection(self, nums1: List[int], 
                     nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)