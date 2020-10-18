学习笔记
题目 不同路径II 的状态转移方程
dp[i, j] = dp[i-1, j] + dp[i, j-1] if (i, j)没有障碍物
dp[i, j] = 0                       if (i, j上有障碍物