"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


from collections import deque
class Solution(object):
    def calculate(self, s):
        vals = deque()
        ops = deque()
        OPERATOR = set("+-*/")
        PRIORITY = set("*/")
        i = 0
        while i < len(s):
            if s[i] in OPERATOR:
                ops.append(s[i])
                i += 1
            if s[i] == ' ':
                i += 1
            else:
                curr_val = s[i]
                i+=1
                while (i < len(s)) and (s[i] not in OPERATOR) and (s[i] != ' '):
                    curr_val += s[i]
                    i += 1
                if len(ops) > 0 and ops[-1] in PRIORITY:
                    op = ops.pop()
                    val = vals.pop()
                    val = val*int(curr_val) if op == "*" else val/int(curr_val)
                    vals.append(val)
                else:
                    vals.append(int(curr_val))
        
        result = vals.popleft()
        while len(vals) > 0:
            val = vals.popleft()
            op = ops.popleft()
            result = result + val if op == "+" else result - val
        
        return result
            
