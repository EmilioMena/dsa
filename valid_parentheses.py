"""
LC 20

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        BRACKET_LOOKUP = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        
        stack = []
        
        for bracket in s:
            if bracket in BRACKET_LOOKUP.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                open_bracket = stack.pop()
                if BRACKET_LOOKUP[open_bracket] != bracket:
                    return False
        
        return len(stack) == 0
