# Valid Parentheses
class Soluton:
    def isValide(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in mapping:
                top_ele = stack.pop() if stack else '#'
                if mapping[char] != top_ele:
                    return False
            else:
                stack.append(char)
        
        return not stack
