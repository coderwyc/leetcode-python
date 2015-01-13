# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 14:54:01 2015

@author: Administrator
"""

 
# Returns the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack. 

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]: # postion may be to return
                index = i
                match = self.compare(haystack[i:], needle) # compare two string
                if match:
                    return index                  
        return -1
    def compare(self, substring, needle):
        """check to see if two string are equal"""
        if len(substring) < len(needle):
            return False
        for i in range(len(needle)):           
            if substring[i] != needle[i]:
                return False                  
        return True

haystack = "mississippi"
needle = "ipp"
s = Solution()
print s.strStr(haystack, needle)        