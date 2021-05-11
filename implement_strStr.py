"""
LC 28
Runtime beats 99.69%
Memory beats 64.03%

Naive solution O(n*m) where n = len(haystack), m = len(needle)
Can be optimized with KMP search algorithm to get O(n)
"""

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        
        return -1

    

## KMP ALgorithm

def strStr(self, haystack, needle):
	prefixes = [0] * len(needle) 
	i, j = 0, 1
	while j < len(needle):
		if needle[i] == needle[j]:
			prefixes[j] = i+1
			i += 1
			j += 1
		else:
			i = 0 if i == 0 else prefixes[i-1]
			if needle[i] != needle[j]:
				prefixes[j] = 0
				j += 1

	h, n = 0, 0
	while h < len(haystack) and n < len(needle):
		if haystack[h] == needle[n]:
			h += 1
			n += 1
		else:
			if n == 0:
				h += 1
			else:
				n = prefixes[n-1]

	return h - len(needle) if n == len(needle) else -1