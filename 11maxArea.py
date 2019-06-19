class Solution(object):
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        l = 0
        r = len(height) - 1
        maxarea = (l - r) * min(height[l], height[r])
        while l < r:
            h = 0
            if height[l] > height[r]:
                h = height[r]
                r -= 1
            else:
                h = height[l]
                l += 1
            maxarea = max(maxarea, (l - r) * h)
        return maxarea

if __name__ == "__main__":
    s = Solution()
    s.height([1,8,6,2,5,4,8,3,7])
