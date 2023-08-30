class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            x=[[1],[1,1]]
            return x
        x=[[1],[1,1]]

        for i in range(3,numRows+1):
            y=x[i-2].copy()
            z=1
            y.append(z)
            a=y.copy()
            for j in range(len(y)-2):
                y[j+1]=a[j]+a[j+1]
                
            x.append(y)

        return x
        