class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import numpy as np
        left = 0
        right = int(np.sqrt(c))
        # two pointer: if bigger right left-shift/if smaller left right-shift
        # NOTE: ^ in py is bitwise ops
        while(left <= right):
            sum = left*left + right*right
            if(sum==c):
                return True
            elif(sum<c):
                left=left+1
            else:
                right=right-1
        return False
