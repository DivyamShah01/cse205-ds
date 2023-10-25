class Solution:
    def isValid(self, s: str) -> bool:
        pair={
            "(":")",
            "[":"]",
            "{":"}"
        }
        self.x=[]

        for bracket in s:
            if bracket in pair:
                self.x.append(bracket)
            elif len(self.x)==0 or pair[self.x.pop()]!=bracket:
                return False
        return len(self.x)==0