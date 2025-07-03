'''给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"'''

# 关键词：
# 1. python语法：字符串末尾如果超过最大长度，则会返回至字符串最后一个值。
# 这个特性可以避免一些边界条件的处理。
# 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。
# 2. str和list互相转化：
# chars = list(s)
# s = ''.join(chars)

# 直接作为字符串处理
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p = 0
        while p < len(s):
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p + k][::-1] + s[p + k:]
            p = p + 2 * k
        return s

# 转化为列表处理
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = list(s)
        
        while i < len(chars):
            chars[i:i + k] = chars[i:i + k][::-1] # 反转后，更改原值为反转后值
            i += k * 2

        return ''.join(chars)