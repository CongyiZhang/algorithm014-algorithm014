# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。 
# 
#  注意：本题相对原题做了扩展 
# 
#  示例: 
# 
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
#  Related Topics 回溯算法 
#  👍 39 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p+q not in xy_sum and p-q not in xy_diff:
                    dfs(queens+[q], xy_diff+[p-q], xy_sum+[p+q])

        result = []
        dfs([], [], [])

        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result ]

# leetcode submit region end(Prohibit modification and deletion)
