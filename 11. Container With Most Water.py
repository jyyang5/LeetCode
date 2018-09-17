class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        in each move get the largest (two nodes)
        """
        max = 0
        left = 0
        right = len(height) - 1
        # Greedy each step move one container
        while (left < right):
            h = min(height[left], height[right])
            w = (right - left)
            if (max < h * w):
                max = h * w
            if (height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
        return max


