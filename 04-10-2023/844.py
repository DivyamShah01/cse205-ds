class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.x=[]
        self.y=[]

        for a in s:
            self.x.append(a)
            #print(self.x)
            if a=="#":
                self.x.pop()
                if self.x!=[]:
                    self.x.pop()
        for b in t:
            self.y.append(b)
            #print(self.y)
            if b=="#":
                self.y.pop()
                if self.y!=[]:
                    self.y.pop()
        #print(str(self.x),str(self.y))
        return self.x==self.y
