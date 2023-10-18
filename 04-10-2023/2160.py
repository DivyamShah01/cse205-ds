class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        num=list(num)
        #print(num)
        num=sorted(num)
        #print(num)

        return (int(num[0]+num[-1]))+int((num[1]+num[-2]))
        