学习笔记

广度优先遍历的应用总结

广度优先遍历：
主要思想：使用队结构，先访问根节点，再将对应的左子树、右子树分别入队

二叉树的最大深度：
主要思想：层序遍历，每遍历一层，深度加一，用队存储每一层的节点

二叉树的最小深度：
主要思想：使用队列层序遍历将对应的节点和深度如堆，找到队中第一个没有左右子树的节点，即二叉树最小深度

二叉树的最大宽度：
主要思路：层序遍历，每次将节点和对应下表索引入队，树的宽度=每层的最右节点索引-最左边节点索引+1

翻转二叉树：
主要思路：层序遍历思想，节点入队，交换对应节点的左右子树，再将左右子树（存在）分别入队

对称二叉树：（给定二叉树判断是否镜像对称）
主要思路：层序遍历，用队存储每一层的节点，判断每一层正反输出是否一样
