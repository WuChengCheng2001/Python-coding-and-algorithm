'''给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致
（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。'''

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
                if table[num] == 1:
                    del table[num]
                else:
                    table[num] -= 1

'''进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？

如果 nums1 的大小比 nums2 小，哪种方法更优？

如果 nums2 的元素存储在磁盘上，内存是有限的，
并且你不能一次加载所有的元素到内存中，你该怎么办？
'''

'''解法一：排序双指针
将两个数组进行排序，随后用双指针顺序查找相同的元素
时间复杂度：O(max(nlogn,mlogm,n+m))
空间复杂度：O(1)
(n,m 分别为两个数组的长度)

如果是进阶问题一中已排序的数组，则只需 O(n) 的时间复杂度
'''

class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort()
        nums2.sort()
        r = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                r.append(nums1[left])
                left += 1
                right += 1    
            else:
                right += 1
        return r

'''解法二: 哈希计数
将较小的数组哈希计数，随后在另一个数组中根据哈希来寻找。
时间复杂度：O(max(n,m))
空间复杂度：O(min(n,m))

适用于进阶问题二
'''

'''解法三：通过归并外排将两个数组排序后再使用排序双指针查找
对应进阶问题三，如果内存十分小，不足以将数组全部载入内存，
那么必然也不能使用哈希这类费空间的算法，只能选用空间复杂度最小的算法，
即解法一。

但是解法一中需要改造，一般说排序算法都是针对于内部排序，
一旦涉及到跟磁盘打交道（外部排序），则需要特殊的考虑。
归并排序是天然适合外部排序的算法，可以将分割后的子数组写到单个文件中，
归并时将小文件合并为更大的文件。当两个数组均排序完成生成两个大文件后，
即可使用双指针遍历两个文件，如此可以使空间复杂度最低。
'''