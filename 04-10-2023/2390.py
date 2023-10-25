class Solution:
    def removeStars(self, s: str) -> str:
        self.x=[]

        for a in s:
            self.x.append(a)
            if a =="*":
                self.x.pop()
                if self.x!=[]:
                    self.x.pop()
        q="".join(self.x)
        #print(q)

        return q