"""
 167. Two Sum II - Input array is sorted
 https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
 """

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointer: if bigger right left-shift/if smaller left right-shift
        # NOTE: ^ in py is bitwise ops
        left = 0
        right = len(numbers) - 1
        while(left < right):
            sum = numbers[left] + numbers[right]
            if(sum == target):
                return [left+1, right+1]
            elif(sum < target):
                left = left + 1
            else:
                right = right -1
        return (null)