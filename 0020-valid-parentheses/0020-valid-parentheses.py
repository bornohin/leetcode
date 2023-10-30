class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for bracket in s:
            if bracket in pairs.keys():
                stack.append(bracket)
            else:
                if not stack and bracket in pairs.values():
                    return False
                elif stack and pairs[stack[-1]] != bracket:
                    return False
                else:
                    stack.pop()
        return not stack
