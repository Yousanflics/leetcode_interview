# decode str: 例如 3[a2[c]] => accacccaccc
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # 构建数字（可能是多位数）
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 遇到左括号，将当前的数字和字符串压入栈
                stack.append((current_num, current_str))
                # 重置当前数字和字符串
                current_num = 0
                current_str = ""
            elif char == ']':
                # 遇到右括号，从栈中弹出数字和之前的字符串
                num, prev_str = stack.pop()
                # 将当前字符串重复num次，并与之前的字符串拼接
                current_str = prev_str + current_str * num
            else:
                # 普通字符，直接添加到当前字符串
                current_str += char
        
        return current_str
