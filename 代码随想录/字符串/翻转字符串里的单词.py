'''给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。'''

# 关键词：
# 1.python中的字符串处理
# split()：拆分字符串，能够自动忽略多余的空白字符
# 注意：因为字符串是不可变类型，所以反转单词的时候，需要将其转换成列表，
# 然后通过join函数再将其转换成字符串，所以空间复杂度不是O(1)
# 2.另一个思路：先反转整个字符串，再反转单词，单词用空字符间隔

class Solution:
    def reverseWords(self, s):
        words = s.split() #type(words) --- list
        words = words[::-1] # 反转单词
        return ' '.join(words) #列表转换成字符串