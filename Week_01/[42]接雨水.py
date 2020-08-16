# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1550 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        i, j = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]
        ans = 0
        while i < j:
            max_left = max(height[i], max_left)
            max_right = max(height[j], max_right)
            if max_left < max_right:
                ans += max_left - height[i]
                i += 1
            else:
                ans += max_right - height[j]
                j -= 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
