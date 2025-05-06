# 稀疏矩阵乘法
# 重点跳过 0

class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        if not mat1 or not mat2:
            return [[]]
            
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:  # 只处理非零元素
                    for l in range(n):
                        if mat2[j][l] != 0:  # 只处理非零元素
                            result[i][l] += mat1[i][j] * mat2[j][l]
                            
        return result
