#Suppose a sorted array is rotated at some pivot unknown to you beforehand.

#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

#You are given a target value to search. If found in the array return its index, otherwise return -1.

#You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def find_pivot(self, A):
        if len(A) <= 1:
            return 0
        index = 1
        while index < len(A):
            if A[index] < A[index-1]:
                return index
            index += 1
        return 0
    def binary_search(self, L, target):
        low = 0
        high = len(L) - 1
        while low <= high:
            mid = (low + high) // 2
            if L[mid] == target:
                return mid
            elif L[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1 # indicate no found 
    def search(self, A, target):
        pivot = self.find_pivot(A)
        ret = self.binary_search(A[:pivot], target)
        if ret != -1:
            return ret
        else:
            ret = self.binary_search(A[pivot:], target)
            if ret != -1:
                return pivot + ret
            else:
                return -1
        
        
