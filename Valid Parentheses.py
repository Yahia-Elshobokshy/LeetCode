class Solution(object):
    def isValid(self, s):
        define = dict(('()', '[]', '{}'))
        stack = []
        for idx in s:
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx != define[stack.pop()]:
                return False
        return len(stack) == 0
