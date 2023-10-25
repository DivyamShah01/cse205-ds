class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left=0
        right=len(matrix[0])-1    #row
        top=0
        bottom=len(matrix)-1    #column
        res=[]

        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            if left>right or top>bottom:
                break
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1

        return res
