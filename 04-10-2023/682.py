class Solution:
    def calPoints(self, operations: List[str]) -> int:

        self.x=[]

        for a in operations:
            self.x.append(a)

            if a=="+":
                self.x.pop()
                #y=int(("".join(self.x))[-1])+int(("".join(self.x))[-2])
                #y="".join(self.x)
                y1=self.x[-1]
                y2=int(y1)
                #print(y2)
                #y3="".join(self.x)
                y4=self.x[-2]
                y5=int(y4)
                #print(y5)
                y6=y2+y5
                y7=str(y6)
                self.x.append(y7)
                #print(self.x)
            elif a=="D":
                self.x.pop()
                #z="".join(self.x)
                z1=self.x[-1]
                print(z1)
                z2=int(z1)*2
                z3=str(z2)
                self.x.append(z3)
                #print(self.x)
            elif a=="C":
                self.x.pop()
                if self.x!=[]:
                    self.x.pop()
        sum=0
        for i in range(len(self.x)):
            sum+=int(self.x[i])
        return sum