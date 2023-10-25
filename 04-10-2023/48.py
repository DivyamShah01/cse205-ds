class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        for i in range(len(matrix)):
            for j in range(len(matrix)-1,-1,-1):
                matrix[i].append(matrix[j].pop(0))