__author__ = 'Administrator'
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        exist = [False] * 256
        max_length = 0
        j = 0
        for i in range(len(s)):
            while exist[ord(s[i])]:
                exist[ord(s[j])] = False
                j += 1
            exist[ord(s[i])] = True
            max_length = max(i - j + 1, max_length)
        return max_length

def lengthOfLongestSubstring(s):
    map_of_index = {}
    maxLen = 0
    j = 0 # point the beginning of substring
    for i in range(len(s)):
        if s[i] in map_of_index.keys() and j < map_of_index[s[i]] + 1: # found a repeated character
            j = map_of_index[s[i]] + 1
        map_of_index[s[i]] = i
        maxLen = max(i - j + 1, maxLen) # if i - j + 1 > maxLen, update it
    return maxLen

s = Solution()
# print  s.lengthOfLongestSubstring("abcabcbb")
# print lengthOfLongestSubstring("abcabcbb")
print  s.lengthOfLongestSubstring("abab")
print lengthOfLongestSubstring("abba")