# reverse words in a string

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    

# str.split() 按照空格分开，默认首尾的空格也会去除，分割为每个单词的list [],然后对 list 取反用 “ ” join 起来
