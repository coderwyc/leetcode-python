#Implement atoi to convert a string to an integer.
class Solution:
    # @return an integer
    def atoi(self, str):
        i = 0;
        while i < len(str) and str[i].isspace(): # ignore leading space
            i += 1        
        sign = 1
        if i < len(str) and str[i] == '+':
            i += 1
        elif i < len(str) and str[i] == '-':
            sign = -1
            i += 1
        num = 0
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            num = num * 10 + digit
            if num > 2147483647 and sign > 0:
                return 2147483647
            if num > 2147483648 and sign < 0:
                return -2147483648
            i += 1
        return sign * num
