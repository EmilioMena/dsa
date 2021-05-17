"""
LC 38

runtime beats 84.60%
memory beats 43.19%

I basically coded itertools.groupBy from scratch, could've saved time by just importing it 
"""

class Solution(object):
    def countAndSay(self, n):         
        result = "1"
        
        for _ in range(n-1): 
            temp = ""
            
            i=0
            while i < len(result):
                count = 1
                current_n = result[i]
                while i+1 < len(result) and current_n == result[i+1]:
                    count+=1
                    i+=1
                temp += str(count)+result[i]
                i+=1
            result = temp
        
        return result
