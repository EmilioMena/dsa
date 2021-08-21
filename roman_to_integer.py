"""
Given a roman numeral, convert it to an integer.
"""

class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        edge_case = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"],
        }
        
        integer = 0
        idx = 0
        while idx < len(s):
            if s[idx] in edge_case:
                if idx+1 < len(s) and s[idx+1] in edge_case[s[idx]]:
                    integer += (roman_map[s[idx+1]] - roman_map[s[idx]])
                    idx += 2
                    continue
            
            integer += roman_map[s[idx]]
            idx+=1
                
        return integer
