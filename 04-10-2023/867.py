class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp=[]
        s=[]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                s.append(matrix[j][i])
            temp.append(s)
            s=[]
        return temp