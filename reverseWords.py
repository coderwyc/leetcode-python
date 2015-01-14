##Given an input string, reverse the string word by word.
##
##For example,
##Given s = "the sky is blue",
##return "blue is sky the". 


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s_split = s.split() # split the string into words
        s_split.reverse()   # put them in reverse order
        ret = ''
        for elem in s_split:
            ret += elem     # string concatenation
            ret += " "      # add space
        return ret[:-1]     # leave out the trailing space
        
