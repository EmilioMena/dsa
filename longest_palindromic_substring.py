"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

# find a palindrome, (s[i] = s[i+1] and/or s[i] = s[i+2])
# continue expanding it until it's no longer a palindrome and set longest
# O(n^2) time and O(1) space
class Solution(object):
    def longestPalindrome(self, s):

        if len(s) == 1:
            return s[0]

        if len(s) == 2:
            return s[0:2] if s[0] == s[1] else s[0]

        longest = [0,0]

        fast = 2
        for slow in range(len(s) -1):
            if s[slow] == s[slow+1]:
                start, end = find_palindromes(slow, slow+1, s)

                if end - start > longest[1] - longest[0]:
                    longest[0] = start
                    longest[1] = end

            if s[slow] == s[fast]:
                start, end = find_palindromes(slow, fast, s)

                if end - start > longest[1] - longest[0]:
                    longest[0] = start
                    longest[1] = end

            fast = fast + 1 if (fast < len(s) - 1) else fast

        return s[longest[0]: longest[1]+1]

def find_palindromes(start, end, s):
    while start -1 >= 0 and end+1 <= len(s) -1 and s[start-1] == s[end+1] :
        start = start -1
        end = end + 1

    return start, end
