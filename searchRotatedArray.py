# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index,
# otherwise return -1.
# You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        first = 0
        last = len(A)
        cnt = 0
        while first != last:
            cnt += 1        
            mid = (first + last) / 2
            if A[mid] == target:
                return mid            
            if A[first] <= A[mid]:
                if A[first] <= target and target < A[mid]:
                    last = mid
                else:
                    first = mid + 1
            else:
                if A[mid] < target and target <= A[last-1]:
                    first = mid + 1
                else:
                    last = mid    
        return -1
