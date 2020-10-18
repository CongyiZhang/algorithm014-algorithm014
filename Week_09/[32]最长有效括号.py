# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 1025 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif s[i-1] == ")" and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
                res = max(dp[i], res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
