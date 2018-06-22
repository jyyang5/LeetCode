"""
Source: https://leetcode.com/problems/k-th-symbol-in-grammar/description/
779. K-th Symbol in Grammar
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).


Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # basecase
        if(N==1):
            return 0
        parent = self.kthGrammar(N-1,(int)((K+1)/2))
        # parent value = 0 -> left child value  0 right child value 1                
        if parent == 0:
            return (K+1)%2
        # parent value = 1 -> left chid value 1 right child value 0 
        else:
            return (K)%2
