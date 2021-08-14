"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = map(lambda x: ''.join(sorted(x)), strs)
        anagram_map = {}

        for i, s in enumerate(sorted_strs):
            if s in anagram_map:
                anagram_map[s].append(strs[i])
            else:
                anagram_map[s] = [strs[i]]

        result = []
        for s in anagram_map:
            result.append(anagram_map[s])

        return result
